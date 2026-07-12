# Cohort Analysis: Monthly SaaS Retention

**Product:** CloudDocs -- document collaboration SaaS (Melbourne-based)
**Data Source:** Supabase `auth.users` + `public.user_activity` tables
**Cohort Definition:** Month of first sign-up (AEST)
**Retention Event:** At least one document edit in the calendar month
**Analysis Period:** August 2025 -- January 2026

---

## Step 1: Cohort Assignment

Assign each user to a cohort based on the month they signed up.

```sql
CREATE OR REPLACE VIEW cohort_users AS
SELECT
  id AS user_id,
  date_trunc('month', created_at AT TIME ZONE 'Australia/Sydney') AS cohort_month
FROM auth.users
WHERE created_at >= '2025-08-01'
  AND created_at < '2026-02-01';
```

---

## Step 2: Monthly Activity Flags

Determine which months each user was active (performed at least one document edit).

```sql
CREATE OR REPLACE VIEW monthly_activity AS
SELECT DISTINCT
  user_id,
  date_trunc('month', activity_at AT TIME ZONE 'Australia/Sydney') AS activity_month
FROM public.user_activity
WHERE event_type = 'document_edit'
  AND activity_at >= '2025-08-01'
  AND activity_at < '2026-02-01';
```

---

## Step 3: Retention Matrix Query

Join cohorts to activity and calculate the percentage of each cohort retained at month N.

```sql
WITH cohort_activity AS (
  SELECT
    c.cohort_month,
    a.activity_month,
    EXTRACT(YEAR FROM age(a.activity_month, c.cohort_month)) * 12
      + EXTRACT(MONTH FROM age(a.activity_month, c.cohort_month)) AS months_since_signup,
    COUNT(DISTINCT c.user_id) FILTER (WHERE a.activity_month IS NOT NULL) AS active_users
  FROM cohort_users c
  LEFT JOIN monthly_activity a
    ON a.user_id = c.user_id
    AND a.activity_month >= c.cohort_month
  GROUP BY c.cohort_month, a.activity_month
),
cohort_sizes AS (
  SELECT cohort_month, COUNT(*) AS cohort_size
  FROM cohort_users
  GROUP BY cohort_month
)
SELECT
  TO_CHAR(cs.cohort_month, 'Mon YYYY') AS cohort,
  cs.cohort_size,
  ca.months_since_signup AS month_n,
  ca.active_users,
  ROUND(ca.active_users::numeric / cs.cohort_size * 100, 1) AS retention_pct
FROM cohort_activity ca
JOIN cohort_sizes cs ON cs.cohort_month = ca.cohort_month
WHERE ca.months_since_signup BETWEEN 0 AND 5
ORDER BY cs.cohort_month, ca.months_since_signup;
```

---

## Retention Heatmap

Percentage of each cohort active at month N. Higher is better.

```
Cohort      Size   M0      M1      M2      M3      M4      M5
─────────── ────── ─────── ─────── ─────── ─────── ─────── ───────
Aug 2025     312   100.0%  64.7%   51.3%   44.2%   40.1%   38.5%
Sep 2025     287   100.0%  68.3%   55.1%   47.0%   42.9%     --
Oct 2025     345   100.0%  71.2%   58.6%   49.3%     --      --
Nov 2025     298   100.0%  69.8%   56.2%     --      --      --
Dec 2025     264   100.0%  62.1%     --      --      --      --
Jan 2026     331   100.0%    --      --      --      --      --

Legend:  >=60% [====]   40-59% [===]   20-39% [==]   <20% [=]
```

Visual retention curve (Aug 2025 cohort):

```
100% |====================================================
 90% |
 80% |
 70% |
 64% |  ========================
 60% |
 51% |          ================
 50% |
 44% |                  ========
 40% |  . . . . . . . . . . . .=====. . . . .=====
 38% |                                        =====
     +--------+--------+--------+--------+--------+--------
      M0       M1       M2       M3       M4       M5
```

---

## Interpretation

### Key Findings

1. **Month-1 retention is improving.** The Oct 2025 cohort retained 71.2% at M1, up from 64.7% for Aug 2025. This aligns with the onboarding flow redesign shipped in late September.

2. **The critical drop-off is M0 to M1.** Across all cohorts, roughly 30-35% of users never return after sign-up month. This is the highest-leverage point for improvement.

3. **Retention stabilises around M3-M4.** The Aug cohort shows only a 2 percentage point drop from M3 (44.2%) to M5 (38.5%), suggesting users who survive 3 months become long-term.

4. **December cohort shows weaker M1 retention (62.1%).** Likely seasonal -- holiday sign-ups with lower intent. Worth excluding from trend analysis or flagging separately.

### Recommended Actions

| Priority | Action | Expected Impact |
|----------|--------|----------------|
| High | Implement a "Day 2-7" email drip targeting users who signed up but have not edited a document | Improve M1 retention by 5-8 ppt |
| High | Add in-app prompt to create first document during onboarding | Reduce M0->M1 drop-off |
| Medium | Introduce "workspace invites" nudge at Day 14 to drive collaborative use | Improve M2+ retention |
| Low | Segment December cohort separately in future reporting to avoid distorting trends | Cleaner analysis |

### Benchmarks

For B2B SaaS collaboration tools in the Australian market:
- **Good** M1 retention: 65-75%
- **Good** M6 retention: 35-45%
- CloudDocs is tracking within the "good" range, with an upward trend in early retention.
