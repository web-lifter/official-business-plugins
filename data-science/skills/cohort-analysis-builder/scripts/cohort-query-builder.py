#!/usr/bin/env python3
"""Generate PostgreSQL cohort SQL; never execute queries or connect to a database.

Assumes events(created_at, user_id, event_type, amount). Times use the database
session timezone; set it explicitly for reproducible boundaries. Retention and
count report active users, not a retention percentage. Behaviour groups classify
users by whether the event occurs anywhere in the supplied table: descriptive,
not a causal comparison or a point-in-time prediction feature.
"""
import argparse
import re


def identifier(value: str, *, qualified: bool = False) -> str:
    parts = value.split(".") if qualified else [value]
    if not parts or any(not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", p) for p in parts):
        raise ValueError("SQL identifiers must contain only letters, digits and underscores")
    return ".".join('"' + p + '"' for p in parts)


def _arguments(period: str, metric: str, table: str, user: str) -> tuple[str, str, str, str]:
    if period not in ("week", "month", "quarter"):
        raise ValueError("period must be week, month or quarter")
    if metric not in ("retention", "revenue", "count"):
        raise ValueError("metric must be retention, revenue or count")
    table, user = identifier(table, qualified=True), identifier(user)
    value = "COALESCE(SUM(amount), 0)" if metric == "revenue" else f"COUNT(DISTINCT {user})"
    label = "total_revenue" if metric == "revenue" else "active_users" if metric == "retention" else "user_count"
    return table, user, value, label


def _offset(period: str) -> str:
    if period == "week":
        return "((activity_period::date - cohort_period::date) / 7)"
    months = "((EXTRACT(YEAR FROM activity_period) - EXTRACT(YEAR FROM cohort_period)) * 12 + EXTRACT(MONTH FROM activity_period) - EXTRACT(MONTH FROM cohort_period))"
    return months + (" / 3" if period == "quarter" else "")


def build_time_cohort_query(period: str, metric: str, events_table: str, user_col: str) -> str:
    table, user, value, label = _arguments(period, metric, events_table, user_col)
    amount = ", e.amount" if metric == "revenue" else ""
    return f"""-- PostgreSQL: calendar {period} cohorts; {metric}.
-- Set the session timezone explicitly. Missing periods are absent, not zeros.
WITH cohort_base AS (
    SELECT {user}, MIN(created_at) AS first_event
    FROM {table}
    WHERE {user} IS NOT NULL AND created_at IS NOT NULL
    GROUP BY {user}
), activity AS (
    SELECT e.{user}, date_trunc('{period}', cb.first_event) AS cohort_period,
           date_trunc('{period}', e.created_at) AS activity_period{amount}
    FROM {table} e
    JOIN cohort_base cb ON e.{user} = cb.{user}
    WHERE e.created_at IS NOT NULL
)
SELECT cohort_period AS cohort_{period},
       ({_offset(period)})::int AS periods_since_start,
       {value} AS {label}
FROM activity
GROUP BY cohort_period, activity_period
ORDER BY cohort_period, activity_period;"""


def build_behavior_cohort_query(period: str, metric: str, event: str,
                                events_table: str, user_col: str) -> str:
    table, user, value, label = _arguments(period, metric, events_table, user_col)
    if not isinstance(event, str) or not event.strip() or any(ord(c) < 32 for c in event):
        raise ValueError("event must be non-empty text without control characters")
    # SQL standard strings with single quotes escaped. Require standard strings
    # (PostgreSQL default); double backslashes in an explicit E string instead.
    literal = "E'" + event.replace(chr(92), chr(92) * 2).replace("'", "''") + "'"
    amount = ", e.amount" if metric == "revenue" else ""
    return f"""-- Descriptive ever-event groups; future events affect membership.
-- This is not causal attribution or point-in-time classification.
WITH behavior_cohort AS (
    SELECT DISTINCT {user} FROM {table}
    WHERE event_type = {literal} AND {user} IS NOT NULL
), activity AS (
    SELECT e.{user}, date_trunc('{period}', e.created_at) AS activity_{period},
           CASE WHEN bc.{user} IS NOT NULL THEN 'performed_event' ELSE 'other_users' END AS cohort{amount}
    FROM {table} e
    LEFT JOIN behavior_cohort bc ON bc.{user} = e.{user}
    WHERE e.{user} IS NOT NULL AND e.created_at IS NOT NULL
)
SELECT cohort, activity_{period}, {value} AS {label}
FROM activity
GROUP BY cohort, activity_{period}
ORDER BY cohort, activity_{period};"""


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--type", choices=("time", "behavior"), required=True)
    p.add_argument("--period", choices=("week", "month", "quarter"), required=True)
    p.add_argument("--metric", choices=("retention", "revenue", "count"), default="retention")
    p.add_argument("--event", default="signup")
    p.add_argument("--table", default="events")
    p.add_argument("--user-col", default="user_id")
    a = p.parse_args()
    try:
        query = build_time_cohort_query(a.period, a.metric, a.table, a.user_col) if a.type == "time" else build_behavior_cohort_query(a.period, a.metric, a.event, a.table, a.user_col)
    except ValueError as exc:
        p.error(str(exc))
    print(query)


if __name__ == "__main__":
    main()
