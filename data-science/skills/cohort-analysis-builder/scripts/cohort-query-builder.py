#!/usr/bin/env python3
"""Generate cohort analysis SQL queries from parameters.

Builds PostgreSQL queries for time-based or behavior-based cohort analysis.

Usage:
    python cohort-query-builder.py --type time --period month --metric retention
    python cohort-query-builder.py --type time --period week --metric revenue
    python cohort-query-builder.py --type behavior --period month --metric retention --event signup
"""

import argparse
import sys


def build_time_cohort_query(period: str, metric: str, events_table: str, user_col: str) -> str:
    """Build a time-based cohort query."""
    trunc = f"date_trunc('{period}', first_event)"
    activity_trunc = f"date_trunc('{period}', e.created_at)"

    if metric == "retention":
        value_expr = f"COUNT(DISTINCT e.{user_col})"
        value_label = "active_users"
    elif metric == "revenue":
        value_expr = "COALESCE(SUM(e.amount), 0)"
        value_label = "total_revenue"
    else:
        value_expr = f"COUNT(DISTINCT e.{user_col})"
        value_label = "user_count"

    return f"""-- Cohort Analysis: {period}ly {metric}
-- Generated query for PostgreSQL

WITH cohort_base AS (
    SELECT
        {user_col},
        MIN(created_at) AS first_event
    FROM {events_table}
    GROUP BY {user_col}
),
cohort_labeled AS (
    SELECT
        cb.{user_col},
        {trunc} AS cohort_{period},
        {activity_trunc} AS activity_{period}
    FROM cohort_base cb
    JOIN {events_table} e ON e.{user_col} = cb.{user_col}
),
cohort_data AS (
    SELECT
        cohort_{period},
        activity_{period},
        EXTRACT(EPOCH FROM (activity_{period} - cohort_{period}))
            / EXTRACT(EPOCH FROM INTERVAL '1 {period}') AS period_offset,
        {value_expr} AS {value_label}
    FROM cohort_labeled cl
    JOIN {events_table} e ON e.{user_col} = cl.{user_col}
        AND {activity_trunc} = cl.activity_{period}
    GROUP BY cohort_{period}, activity_{period}
)
SELECT
    cohort_{period},
    period_offset::int AS periods_since_start,
    {value_label}
FROM cohort_data
ORDER BY cohort_{period}, period_offset;"""


def build_behavior_cohort_query(period: str, metric: str, event: str,
                                 events_table: str, user_col: str) -> str:
    """Build a behavior-based cohort query."""
    trunc = f"date_trunc('{period}', e.created_at)"

    return f"""-- Behavior Cohort Analysis: users who did '{event}', tracked by {period}
-- Generated query for PostgreSQL

WITH behavior_cohort AS (
    SELECT DISTINCT {user_col}
    FROM {events_table}
    WHERE event_type = '{event}'
),
non_behavior_cohort AS (
    SELECT DISTINCT {user_col}
    FROM {events_table}
    WHERE {user_col} NOT IN (SELECT {user_col} FROM behavior_cohort)
),
activity AS (
    SELECT
        e.{user_col},
        {trunc} AS activity_{period},
        CASE WHEN bc.{user_col} IS NOT NULL THEN 'did_{event}' ELSE 'did_not_{event}' END AS cohort
    FROM {events_table} e
    LEFT JOIN behavior_cohort bc ON bc.{user_col} = e.{user_col}
)
SELECT
    cohort,
    activity_{period},
    COUNT(DISTINCT {user_col}) AS active_users
FROM activity
GROUP BY cohort, activity_{period}
ORDER BY cohort, activity_{period};"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate cohort analysis SQL queries.")
    parser.add_argument("--type", choices=["time", "behavior"], required=True, help="Cohort type")
    parser.add_argument("--period", choices=["week", "month", "quarter"], required=True, help="Analysis period")
    parser.add_argument("--metric", choices=["retention", "revenue", "count"], default="retention", help="Metric")
    parser.add_argument("--event", default="signup", help="Event for behavior cohorts")
    parser.add_argument("--table", default="events", help="Events table name")
    parser.add_argument("--user-col", default="user_id", help="User ID column name")
    args = parser.parse_args()

    if args.type == "time":
        query = build_time_cohort_query(args.period, args.metric, args.table, args.user_col)
    else:
        query = build_behavior_cohort_query(args.period, args.metric, args.event, args.table, args.user_col)

    print(query)


if __name__ == "__main__":
    main()
