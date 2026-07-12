# Cohort Analysis Builder -- Reference

Supplementary reference material for the cohort-analysis-builder skill.
Contains SQL patterns for cohort assignment, retention matrices, revenue
cohorts, timezone handling, sparse cohort strategies, visualisation specs,
and common pitfalls.

---

## Table of Contents

- [1. SQL Patterns for Time-Based Cohort Assignment](#1-sql-patterns-for-time-based-cohort-assignment)
- [2. Retention Matrix SQL Template (PostgreSQL)](#2-retention-matrix-sql-template-postgresql)
- [3. Revenue Cohort SQL Template with Cumulative LTV](#3-revenue-cohort-sql-template-with-cumulative-ltv)
- [4. Timezone Handling Strategies for Cohort Boundaries](#4-timezone-handling-strategies-for-cohort-boundaries)
- [5. Sparse Cohort Handling](#5-sparse-cohort-handling)
- [6. Visualisation Specification Templates](#6-visualisation-specification-templates)
- [7. Common Cohort Analysis Pitfalls and Solutions](#7-common-cohort-analysis-pitfalls-and-solutions)

---

## 1. SQL Patterns for Time-Based Cohort Assignment

### 1A. Signup Month Cohort

The most common cohort definition: group users by the month they signed up.

```sql
-- Cohort assignment: signup month
SELECT
  user_id,
  DATE_TRUNC('month', created_at AT TIME ZONE 'UTC') AS cohort_month
FROM users
WHERE created_at IS NOT NULL;
```

### 1B. First Purchase Week Cohort

For e-commerce or marketplace businesses where signup date is less meaningful
than first transaction date.

```sql
-- Cohort assignment: first purchase week
SELECT
  customer_id AS user_id,
  DATE_TRUNC('week', MIN(order_date)) AS cohort_week
FROM orders
WHERE order_status NOT IN ('cancelled', 'refunded')
GROUP BY customer_id;
```

### 1C. First Activity Cohort (Generic)

When there is no explicit signup date, derive the cohort from first observed
activity.

```sql
-- Cohort assignment: first observed activity
SELECT
  user_id,
  DATE_TRUNC('month', MIN(event_timestamp)) AS cohort_month
FROM events
WHERE event_type IN ('page_view', 'login', 'api_call')  -- define "activity"
GROUP BY user_id;
```

### 1D. Behaviour-Based Cohort

Group users by the first feature they used or the plan they started on.

```sql
-- Cohort assignment: first plan tier
WITH first_plan AS (
  SELECT
    user_id,
    plan_tier,
    started_at,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY started_at) AS rn
  FROM subscriptions
)
SELECT
  user_id,
  plan_tier AS cohort_segment,
  DATE_TRUNC('month', started_at) AS cohort_month
FROM first_plan
WHERE rn = 1;
```

### 1E. Acquisition Channel Cohort

Group users by how they were acquired.

```sql
-- Cohort assignment: acquisition channel + signup month
SELECT
  u.id AS user_id,
  COALESCE(u.acquisition_source, 'unknown') AS cohort_channel,
  DATE_TRUNC('month', u.created_at) AS cohort_month
FROM users u;
```

---

## 2. Retention Matrix SQL Template (PostgreSQL)

Complete, copy-paste-ready retention matrix query. Produces the standard
rows = cohort, columns = period_number, values = retention %.

```sql
-- =============================================================
-- Retention Matrix
-- =============================================================
-- Configuration: update these CTEs for your schema
-- =============================================================

WITH config AS (
  SELECT
    'month'::text AS granularity,       -- 'week', 'month', 'quarter'
    12            AS max_periods,        -- how many periods to show
    30            AS min_cohort_size     -- minimum users per cohort
),

-- Step 1: Assign each user to a cohort
cohort_assignment AS (
  SELECT
    u.id AS user_id,
    DATE_TRUNC((SELECT granularity FROM config), u.created_at) AS cohort_date
  FROM users u
  WHERE u.created_at IS NOT NULL
),

-- Step 2: Map user activity to periods
user_activity AS (
  SELECT DISTINCT
    e.user_id,
    ca.cohort_date,
    DATE_TRUNC((SELECT granularity FROM config), e.event_timestamp) AS activity_period
  FROM events e
  INNER JOIN cohort_assignment ca ON ca.user_id = e.user_id
  WHERE e.event_timestamp >= ca.cohort_date
),

-- Step 3: Calculate period numbers
activity_periods AS (
  SELECT
    user_id,
    cohort_date,
    activity_period,
    -- Period calculation varies by granularity
    CASE (SELECT granularity FROM config)
      WHEN 'week'    THEN EXTRACT(EPOCH FROM (activity_period - cohort_date)) / (7 * 86400)
      WHEN 'month'   THEN (EXTRACT(YEAR FROM activity_period) - EXTRACT(YEAR FROM cohort_date)) * 12
                         + (EXTRACT(MONTH FROM activity_period) - EXTRACT(MONTH FROM cohort_date))
      WHEN 'quarter' THEN (EXTRACT(YEAR FROM activity_period) - EXTRACT(YEAR FROM cohort_date)) * 4
                         + (EXTRACT(QUARTER FROM activity_period) - EXTRACT(QUARTER FROM cohort_date))
    END::int AS period_number
  FROM user_activity
),

-- Step 4: Cohort sizes
cohort_sizes AS (
  SELECT
    cohort_date,
    COUNT(DISTINCT user_id) AS cohort_size
  FROM cohort_assignment
  GROUP BY cohort_date
  HAVING COUNT(DISTINCT user_id) >= (SELECT min_cohort_size FROM config)
),

-- Step 5: Retention counts per cohort per period
retention_counts AS (
  SELECT
    ap.cohort_date,
    ap.period_number,
    COUNT(DISTINCT ap.user_id) AS active_users
  FROM activity_periods ap
  INNER JOIN cohort_sizes cs ON cs.cohort_date = ap.cohort_date
  WHERE ap.period_number BETWEEN 0 AND (SELECT max_periods FROM config)
  GROUP BY ap.cohort_date, ap.period_number
)

-- Step 6: Final output
SELECT
  TO_CHAR(rc.cohort_date, 'YYYY-MM') AS cohort,
  cs.cohort_size,
  rc.period_number,
  rc.active_users,
  ROUND(100.0 * rc.active_users / cs.cohort_size, 1) AS retention_pct
FROM retention_counts rc
INNER JOIN cohort_sizes cs ON cs.cohort_date = rc.cohort_date
ORDER BY rc.cohort_date, rc.period_number;
```

### Pivoted Retention Matrix

To produce a spreadsheet-friendly pivoted matrix (cohort rows, period columns):

```sql
-- Pivoted retention matrix (up to 12 periods)
-- Uses the retention_counts and cohort_sizes CTEs from above
SELECT
  TO_CHAR(cs.cohort_date, 'YYYY-MM') AS cohort,
  cs.cohort_size,
  MAX(CASE WHEN rc.period_number = 0  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M0",
  MAX(CASE WHEN rc.period_number = 1  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M1",
  MAX(CASE WHEN rc.period_number = 2  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M2",
  MAX(CASE WHEN rc.period_number = 3  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M3",
  MAX(CASE WHEN rc.period_number = 4  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M4",
  MAX(CASE WHEN rc.period_number = 5  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M5",
  MAX(CASE WHEN rc.period_number = 6  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M6",
  MAX(CASE WHEN rc.period_number = 7  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M7",
  MAX(CASE WHEN rc.period_number = 8  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M8",
  MAX(CASE WHEN rc.period_number = 9  THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M9",
  MAX(CASE WHEN rc.period_number = 10 THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M10",
  MAX(CASE WHEN rc.period_number = 11 THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M11",
  MAX(CASE WHEN rc.period_number = 12 THEN ROUND(100.0 * rc.active_users / cs.cohort_size, 1) END) AS "M12"
FROM cohort_sizes cs
LEFT JOIN retention_counts rc ON rc.cohort_date = cs.cohort_date
GROUP BY cs.cohort_date, cs.cohort_size
ORDER BY cs.cohort_date;
```

---

## 3. Revenue Cohort SQL Template with Cumulative LTV

### Revenue Retention (% of Period-0 Revenue Retained)

```sql
-- =============================================================
-- Revenue Retention Cohort
-- Shows what % of a cohort's initial revenue is retained each period
-- =============================================================
WITH cohort_assignment AS (
  SELECT
    customer_id AS user_id,
    DATE_TRUNC('month', MIN(order_date)) AS cohort_date
  FROM orders
  WHERE order_status = 'completed'
  GROUP BY customer_id
),

revenue_by_period AS (
  SELECT
    ca.cohort_date,
    (EXTRACT(YEAR FROM DATE_TRUNC('month', o.order_date)) - EXTRACT(YEAR FROM ca.cohort_date)) * 12
      + (EXTRACT(MONTH FROM DATE_TRUNC('month', o.order_date)) - EXTRACT(MONTH FROM ca.cohort_date))
    AS period_number,
    COUNT(DISTINCT o.customer_id) AS paying_users,
    SUM(o.total_amount) AS period_revenue
  FROM orders o
  INNER JOIN cohort_assignment ca ON ca.user_id = o.customer_id
  WHERE o.order_status = 'completed'
    AND DATE_TRUNC('month', o.order_date) >= ca.cohort_date
  GROUP BY ca.cohort_date, period_number
),

cohort_sizes AS (
  SELECT cohort_date, COUNT(DISTINCT user_id) AS cohort_size
  FROM cohort_assignment
  GROUP BY cohort_date
  HAVING COUNT(DISTINCT user_id) >= 30
),

period_zero_revenue AS (
  SELECT cohort_date, period_revenue AS p0_revenue
  FROM revenue_by_period
  WHERE period_number = 0
)

SELECT
  TO_CHAR(r.cohort_date, 'YYYY-MM') AS cohort,
  cs.cohort_size,
  r.period_number,
  r.paying_users,
  ROUND(r.period_revenue::numeric, 2) AS period_revenue,
  ROUND(100.0 * r.period_revenue / NULLIF(p0.p0_revenue, 0), 1) AS revenue_retention_pct,
  -- Cumulative revenue per user (LTV proxy)
  ROUND(
    SUM(r.period_revenue) OVER (
      PARTITION BY r.cohort_date ORDER BY r.period_number
    )::numeric / cs.cohort_size, 2
  ) AS cumulative_ltv_per_user
FROM revenue_by_period r
INNER JOIN cohort_sizes cs ON cs.cohort_date = r.cohort_date
LEFT JOIN period_zero_revenue p0 ON p0.cohort_date = r.cohort_date
WHERE r.period_number BETWEEN 0 AND 12
ORDER BY r.cohort_date, r.period_number;
```

### LTV Projection from Cohort Data

```sql
-- =============================================================
-- Cumulative LTV Curve
-- Shows how much revenue a typical user in each cohort generates
-- over time, useful for payback period and LTV:CAC calculations
-- =============================================================
WITH cohort_ltv AS (
  -- Use the cumulative_ltv_per_user from the query above
  SELECT
    cohort_date,
    period_number,
    cumulative_ltv_per_user
  FROM revenue_cohort_output  -- reference the revenue cohort query
)
SELECT
  TO_CHAR(cohort_date, 'YYYY-MM') AS cohort,
  MAX(CASE WHEN period_number = 0  THEN cumulative_ltv_per_user END) AS "LTV_M0",
  MAX(CASE WHEN period_number = 1  THEN cumulative_ltv_per_user END) AS "LTV_M1",
  MAX(CASE WHEN period_number = 3  THEN cumulative_ltv_per_user END) AS "LTV_M3",
  MAX(CASE WHEN period_number = 6  THEN cumulative_ltv_per_user END) AS "LTV_M6",
  MAX(CASE WHEN period_number = 12 THEN cumulative_ltv_per_user END) AS "LTV_M12"
FROM cohort_ltv
GROUP BY cohort_date
ORDER BY cohort_date;
```

---

## 4. Timezone Handling Strategies for Cohort Boundaries

### The Problem

A user signs up at 11:30 PM on January 31st in Sydney (AEST, UTC+11).
In UTC, that is 12:30 PM on January 31st. No issue here.

But a user who signs up at 11:30 PM on January 31st in Los Angeles (PST, UTC-8)
is actually February 1st in UTC. If you cohort by UTC month, this user lands in
the February cohort despite experiencing January 31st locally.

### Strategy 1: Convert to Business Timezone (Recommended)

If the business operates primarily in one timezone, convert all timestamps
before truncating.

```sql
-- Cohort assignment in business timezone
SELECT
  user_id,
  DATE_TRUNC('month',
    created_at AT TIME ZONE 'Australia/Sydney'  -- business timezone
  ) AS cohort_month
FROM users;
```

### Strategy 2: Store User Timezone, Convert Per User

For global businesses where each user's local date matters.

```sql
-- Cohort assignment respecting each user's timezone
SELECT
  u.id AS user_id,
  DATE_TRUNC('month',
    u.created_at AT TIME ZONE COALESCE(u.timezone, 'UTC')
  ) AS cohort_month
FROM users u;
```

### Strategy 3: Use UTC Consistently

For businesses where timezone precision is less critical than consistency.
Simplest approach; avoids ambiguity.

```sql
-- Cohort assignment in UTC (simplest, most portable)
SELECT
  user_id,
  DATE_TRUNC('month', created_at AT TIME ZONE 'UTC') AS cohort_month
FROM users;
```

### Strategy 4: Weekly Cohorts with ISO Weeks

ISO weeks start on Monday. Use `DATE_TRUNC('week', ...)` in PostgreSQL which
aligns to Monday boundaries.

```sql
-- Weekly cohort assignment (ISO week, Monday start)
SELECT
  user_id,
  DATE_TRUNC('week', created_at AT TIME ZONE 'Australia/Sydney') AS cohort_week
FROM users;
-- Result: 2025-01-06 for any date in the week of Jan 6-12
```

### Key Rules

1. **Pick one strategy and document it.** Mixing timezone approaches within
   the same analysis produces incorrect results.
2. **Apply the same timezone conversion to both cohort assignment AND activity
   mapping.** If you cohort in AEST, measure activity in AEST.
3. **`AT TIME ZONE` in PostgreSQL converts TIMESTAMPTZ to a local TIMESTAMP.**
   `DATE_TRUNC` then operates on the local value. This is the correct sequence.
4. **Test boundary cases.** Manually check users who signed up near midnight in
   different timezones to verify correct cohort assignment.

---

## 5. Sparse Cohort Handling

### The Problem

Small cohorts (e.g., 5 users who signed up in December) produce wildly
unreliable percentages. One user returning makes it 20% retention; the
true retention rate for a similar-sized group could be anywhere from 0-80%.

### Minimum Cohort Size Thresholds

| Analysis Type | Minimum Cohort Size | Reasoning |
|---|---|---|
| Retention % (directional) | 30 users | Basic statistical stability |
| Retention % (actionable decisions) | 100 users | Confidence intervals narrow enough |
| Revenue retention | 50 users | Revenue variance is higher than activity variance |
| A/B cohort comparison | 200+ per group | Needed for statistical significance |

### SQL Filter for Minimum Size

```sql
-- Add to any cohort query's cohort_sizes CTE
cohort_sizes AS (
  SELECT
    cohort_date,
    COUNT(DISTINCT user_id) AS cohort_size
  FROM cohort_assignment
  GROUP BY cohort_date
  HAVING COUNT(DISTINCT user_id) >= 30  -- minimum threshold
)
```

### Strategies for Sparse Data

**1. Aggregate to larger time periods**

```sql
-- Instead of monthly cohorts, use quarterly
DATE_TRUNC('quarter', created_at) AS cohort_quarter
```

**2. Combine adjacent small cohorts**

```sql
-- Roll small months into the previous month's cohort
WITH raw_cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('month', created_at) AS cohort_month
  FROM users
),
cohort_sizes AS (
  SELECT cohort_month, COUNT(*) AS size
  FROM raw_cohorts
  GROUP BY cohort_month
),
adjusted_cohorts AS (
  SELECT
    rc.user_id,
    CASE
      WHEN cs.size < 30 THEN
        -- Merge with previous month
        (rc.cohort_month - INTERVAL '1 month')::date
      ELSE rc.cohort_month
    END AS cohort_month
  FROM raw_cohorts rc
  JOIN cohort_sizes cs ON cs.cohort_month = rc.cohort_month
)
SELECT * FROM adjusted_cohorts;
```

**3. Flag unreliable cohorts in the output**

```sql
-- Add a reliability column to the final output
SELECT
  cohort,
  cohort_size,
  period_number,
  retention_pct,
  CASE
    WHEN cohort_size < 30  THEN 'unreliable'
    WHEN cohort_size < 100 THEN 'directional'
    ELSE 'reliable'
  END AS confidence_level
FROM retention_matrix;
```

---

## 6. Visualisation Specification Templates

### 6A. Heatmap (Cohort Grid)

The standard cohort visualisation. Rows are cohorts, columns are periods,
cells are colour-coded by metric value.

```json
{
  "type": "heatmap",
  "title": "User Retention by Signup Month",
  "data": {
    "source": "retention_matrix_query",
    "rows": "cohort_date",
    "columns": "period_number",
    "values": "retention_pct"
  },
  "layout": {
    "row_header": "{cohort_date} (n={cohort_size})",
    "column_header": "M{period_number}",
    "cell_format": "{value}%",
    "empty_cell": "-"
  },
  "colour_scale": {
    "type": "diverging",
    "low": "#dc2626",
    "mid": "#facc15",
    "high": "#16a34a",
    "domain": [0, 50, 100],
    "na_colour": "#f3f4f6"
  },
  "annotations": {
    "show_values": true,
    "font_size": 11,
    "highlight_diagonal": true,
    "flag_small_cohorts": true,
    "small_cohort_threshold": 30
  },
  "tool_recommendations": [
    "Looker Studio: use pivot table with conditional formatting",
    "Metabase: use pivot table visualisation",
    "Excel/Sheets: pivot table with conditional formatting rules",
    "React: use recharts or nivo heatmap component",
    "Python: seaborn.heatmap() or plotly"
  ]
}
```

### 6B. Retention Curves (Line Chart)

Overlay retention curves for multiple cohorts to compare performance over time.

```json
{
  "type": "line_chart",
  "title": "Retention Curves by Cohort",
  "data": {
    "source": "retention_matrix_query",
    "x": "period_number",
    "y": "retention_pct",
    "series": "cohort_date"
  },
  "axes": {
    "x": {
      "label": "Months Since Signup",
      "min": 0,
      "tick_format": "M{value}"
    },
    "y": {
      "label": "Retention %",
      "min": 0,
      "max": 100,
      "tick_format": "{value}%"
    }
  },
  "series_options": {
    "highlight": ["most_recent", "largest_cohort"],
    "dim_older_cohorts": true,
    "max_series": 12,
    "show_average_line": true
  },
  "reference_lines": [
    {
      "y": 50,
      "label": "50% retention benchmark",
      "style": "dashed",
      "colour": "#9ca3af"
    }
  ],
  "tool_recommendations": [
    "Looker Studio: time series chart with cohort dimension",
    "Metabase: line chart with breakout by cohort",
    "React: recharts LineChart with multiple Line components",
    "Python: matplotlib or plotly with one trace per cohort"
  ]
}
```

### 6C. LTV Curves (Cumulative Revenue per User)

```json
{
  "type": "line_chart",
  "title": "Cumulative LTV by Cohort",
  "data": {
    "source": "revenue_cohort_query",
    "x": "period_number",
    "y": "cumulative_ltv_per_user",
    "series": "cohort_date"
  },
  "axes": {
    "x": {
      "label": "Months Since First Purchase",
      "min": 0
    },
    "y": {
      "label": "Cumulative Revenue per User ($)",
      "min": 0,
      "tick_format": "${value}"
    }
  },
  "annotations": {
    "show_cac_breakeven_line": true,
    "cac_value": null,
    "payback_period_label": true
  },
  "tool_recommendations": [
    "Same tools as retention curves",
    "Add a horizontal CAC line to identify payback period"
  ]
}
```

### 6D. Cohort Size Over Time (Bar Chart)

Context chart showing how many users are in each cohort.

```json
{
  "type": "bar_chart",
  "title": "Cohort Sizes Over Time",
  "data": {
    "source": "cohort_sizes",
    "x": "cohort_date",
    "y": "cohort_size"
  },
  "axes": {
    "x": { "label": "Cohort", "tick_format": "MMM YYYY" },
    "y": { "label": "Users" }
  },
  "annotations": {
    "threshold_line": 30,
    "threshold_label": "Min reliable size"
  }
}
```

---

## 7. Common Cohort Analysis Pitfalls and Solutions

### Pitfall 1: Survivorship Bias in Activity Definition

**Problem:** Defining "active" as "has a paid subscription" excludes users who
cancelled and returned. The retention curve looks better than reality because
it only counts survivors.

**Solution:** Define activity broadly enough to capture re-engagement. For SaaS,
"logged in" is better than "has active subscription" for retention. Track
subscription status separately.

### Pitfall 2: Incomplete Cohorts at Edges

**Problem:** The most recent cohort always looks like it has worse retention
because not enough time has passed. The oldest cohort may be incomplete if
data collection started mid-cohort.

**Solution:** Exclude incomplete cohorts from the analysis. Only show period N
data for cohorts that have had N full periods to mature.

```sql
-- Filter out immature data points
WHERE ap.period_number <= (
  EXTRACT(EPOCH FROM (DATE_TRUNC('month', NOW()) - ap.cohort_date))
  / (30.44 * 86400)  -- approximate months elapsed
)::int
```

### Pitfall 3: Confusing User Retention with Revenue Retention

**Problem:** Reporting "85% retention" without specifying whether it is user
retention or revenue retention. These are very different numbers -- you can
retain 85% of users but only 60% of revenue (if high-value users churn more).

**Solution:** Always label the metric explicitly. Run both user and revenue
retention and compare them. If revenue retention is lower than user retention,
your highest-value customers are churning disproportionately.

### Pitfall 4: Period 0 = 100% Confusion

**Problem:** Period 0 retention is always 100% by definition (the user was
active in the period they were assigned to the cohort). Including it in the
chart wastes a column and can mislead stakeholders who see "100%" and think
things are great.

**Solution:** Choose one approach and document it:
- **Include Period 0:** Makes the retention curve start at 100%. Visually shows
  the full decay. Better for presentations.
- **Exclude Period 0:** Start from Period 1. Shows the real first-period
  retention rate. Better for operational analysis.

### Pitfall 5: Mixing Cohort Granularity with Activity Granularity

**Problem:** Monthly cohorts with daily activity data. A user active on day 1
and day 30 of month 1 counts the same as a user active every single day.
Monthly cohorts lose intra-month detail.

**Solution:** Match granularity to the decision cadence. If you review retention
monthly, use monthly cohorts. If you need to detect week-over-week changes,
use weekly cohorts. Do not mix (e.g., weekly cohorts with monthly periods).

### Pitfall 6: Not Accounting for Seasonality

**Problem:** Comparing the December cohort to the June cohort and concluding
that "winter signups retain better." The difference might be entirely seasonal
(e.g., holiday buyers vs regular buyers have different behaviour patterns).

**Solution:** Compare cohorts year-over-year (Dec 2024 vs Dec 2023) rather than
sequentially (Dec 2024 vs Nov 2024). Add acquisition channel as a secondary
dimension to isolate seasonal marketing effects.

### Pitfall 7: Ignoring Cohort Size When Making Decisions

**Problem:** A cohort of 8 users shows 50% Month-3 retention. Another cohort
of 800 users shows 35% Month-3 retention. Concluding the small cohort performed
better and trying to replicate whatever caused it.

**Solution:** Always display cohort size alongside retention percentages. Use
the minimum size thresholds from Section 5. Consider confidence intervals:

```sql
-- Approximate 95% confidence interval for retention %
-- Using Wilson score interval (better than naive for proportions)
SELECT
  cohort,
  retention_pct,
  cohort_size AS n,
  ROUND(
    (retention_pct/100.0 + 1.96*1.96/(2*cohort_size)
     - 1.96 * SQRT((retention_pct/100.0 * (1 - retention_pct/100.0)
     + 1.96*1.96/(4*cohort_size)) / cohort_size))
    / (1 + 1.96*1.96/cohort_size) * 100, 1
  ) AS ci_lower,
  ROUND(
    (retention_pct/100.0 + 1.96*1.96/(2*cohort_size)
     + 1.96 * SQRT((retention_pct/100.0 * (1 - retention_pct/100.0)
     + 1.96*1.96/(4*cohort_size)) / cohort_size))
    / (1 + 1.96*1.96/cohort_size) * 100, 1
  ) AS ci_upper
FROM retention_matrix;
```

### Pitfall 8: One-Time Purchasers Polluting E-Commerce Cohorts

**Problem:** In e-commerce, many customers only ever make one purchase. Including
them in retention analysis makes every cohort's M1+ retention look terrible
(often < 20%).

**Solution:** Either:
1. Accept this as reality and benchmark against e-commerce norms (20-30% M1).
2. Run a separate analysis on "repeat purchasers" (users with 2+ orders) to
   understand the behaviour of your core customer base.
3. Use "repeat purchase rate" as the metric instead of "retention rate" -- what
   % of the cohort has made a 2nd purchase by period N?

```sql
-- Repeat purchase rate by cohort
WITH orders_per_user AS (
  SELECT
    ca.cohort_date,
    o.customer_id,
    COUNT(*) AS order_count,
    MAX(o.order_date) AS last_order_date
  FROM orders o
  INNER JOIN cohort_assignment ca ON ca.user_id = o.customer_id
  GROUP BY ca.cohort_date, o.customer_id
)
SELECT
  TO_CHAR(cohort_date, 'YYYY-MM') AS cohort,
  COUNT(*) AS total_customers,
  SUM(CASE WHEN order_count >= 2 THEN 1 ELSE 0 END) AS repeat_buyers,
  ROUND(100.0 * SUM(CASE WHEN order_count >= 2 THEN 1 ELSE 0 END) / COUNT(*), 1) AS repeat_rate_pct,
  SUM(CASE WHEN order_count >= 3 THEN 1 ELSE 0 END) AS triple_buyers,
  ROUND(100.0 * SUM(CASE WHEN order_count >= 3 THEN 1 ELSE 0 END) / COUNT(*), 1) AS triple_rate_pct
FROM orders_per_user
GROUP BY cohort_date
HAVING COUNT(*) >= 30
ORDER BY cohort_date;
```

### Pitfall 9: Reactivated Users Inflating Retention

**Problem:** A user is inactive for 6 months, then returns. They appear as
"retained" in period 8, making it look like the cohort is recovering. In
reality, these are reactivation events, not continuous retention.

**Solution:** Distinguish between "ever active in period N" (standard retention)
and "continuously active through period N" (strict retention). Report both if
reactivation is common in the business.

```sql
-- Strict retention: user must have been active in EVERY period up to N
WITH continuous AS (
  SELECT
    user_id,
    cohort_date,
    period_number,
    -- Check for gaps: if there is any missing period before this one,
    -- the user is not continuously retained
    period_number - ROW_NUMBER() OVER (
      PARTITION BY user_id, cohort_date ORDER BY period_number
    ) AS gap_group
  FROM activity_periods
  WHERE period_number >= 0
)
SELECT
  cohort_date,
  period_number,
  COUNT(DISTINCT user_id) FILTER (WHERE gap_group = 0) AS continuously_active,
  COUNT(DISTINCT user_id) AS ever_active
FROM continuous
GROUP BY cohort_date, period_number;
```
