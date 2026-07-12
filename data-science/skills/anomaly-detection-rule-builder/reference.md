# Anomaly Detection Rule Builder -- Reference

Supplementary reference material for the anomaly-detection-rule-builder skill.
Contains SQL templates, threshold guidance, seasonality patterns, severity
classification, investigation playbooks, and false-positive reduction strategies.

---

## Table of Contents

- [1. SQL Templates for Common Anomaly Detection Queries](#1-sql-templates-for-common-anomaly-detection-queries)
- [2. Threshold Guidance Table](#2-threshold-guidance-table)
- [3. Common Business Metric Seasonality Patterns](#3-common-business-metric-seasonality-patterns)
- [4. Alert Severity Classification](#4-alert-severity-classification)
- [5. Investigation Playbook Template](#5-investigation-playbook-template)
- [6. False Positive Reduction Strategies](#6-false-positive-reduction-strategies)

---

## 1. SQL Templates for Common Anomaly Detection Queries

### 1A. Z-Score Detection (Parametric)

Flags values more than N standard deviations from a rolling mean.
Best for metrics with roughly normal distribution and stable variance.

```sql
-- =============================================================
-- Z-Score Anomaly Detection
-- Configuration: change metric_name, lookback, threshold below
-- =============================================================
WITH params AS (
  SELECT
    'daily_revenue'::text   AS metric_name,
    14                      AS lookback_days,
    2.5                     AS z_threshold   -- 2.0=~5% FP, 2.5=~1%, 3.0=~0.3%
),
stats AS (
  SELECT
    m.date,
    m.value,
    AVG(m.value) OVER w   AS rolling_mean,
    STDDEV(m.value) OVER w AS rolling_stddev
  FROM daily_metrics m, params p
  WHERE m.metric_name = p.metric_name
  WINDOW w AS (
    ORDER BY m.date
    ROWS BETWEEN (p.lookback_days - 1) PRECEDING AND CURRENT ROW
  )
)
SELECT
  s.date,
  s.value,
  ROUND(s.rolling_mean::numeric, 2)   AS rolling_mean,
  ROUND(s.rolling_stddev::numeric, 2) AS rolling_stddev,
  ROUND(((s.value - s.rolling_mean) / NULLIF(s.rolling_stddev, 0))::numeric, 2) AS z_score,
  CASE
    WHEN (s.value - s.rolling_mean) / NULLIF(s.rolling_stddev, 0) > p.z_threshold  THEN 'spike'
    WHEN (s.value - s.rolling_mean) / NULLIF(s.rolling_stddev, 0) < -p.z_threshold THEN 'drop'
    ELSE 'normal'
  END AS anomaly_type
FROM stats s, params p
WHERE ABS((s.value - s.rolling_mean) / NULLIF(s.rolling_stddev, 0)) > p.z_threshold
ORDER BY s.date DESC;
```

### 1B. Percentage Deviation from Rolling Average

Simpler than Z-score. Works for any distribution shape.

```sql
-- =============================================================
-- Percentage Deviation Detection
-- =============================================================
WITH params AS (
  SELECT
    'conversion_rate'::text AS metric_name,
    14                      AS lookback_days,
    25.0                    AS pct_threshold  -- % deviation to flag
),
baseline AS (
  SELECT
    m.date,
    m.value,
    AVG(m.value) OVER (
      ORDER BY m.date
      ROWS BETWEEN (p.lookback_days - 1) PRECEDING AND CURRENT ROW
    ) AS rolling_avg
  FROM daily_metrics m, params p
  WHERE m.metric_name = p.metric_name
)
SELECT
  b.date,
  ROUND(b.value::numeric, 2)       AS actual,
  ROUND(b.rolling_avg::numeric, 2) AS expected,
  ROUND((100.0 * (b.value - b.rolling_avg) / NULLIF(b.rolling_avg, 0))::numeric, 1) AS pct_deviation,
  CASE
    WHEN 100.0 * (b.value - b.rolling_avg) / NULLIF(b.rolling_avg, 0) > p.pct_threshold  THEN 'above'
    WHEN 100.0 * (b.value - b.rolling_avg) / NULLIF(b.rolling_avg, 0) < -p.pct_threshold THEN 'below'
    ELSE 'normal'
  END AS direction
FROM baseline b, params p
WHERE ABS(100.0 * (b.value - b.rolling_avg) / NULLIF(b.rolling_avg, 0)) > p.pct_threshold
ORDER BY b.date DESC;
```

### 1C. Moving Average Crossover (Trend Detection)

Detects when a short-term average crosses below a long-term average --
classic trend-change signal.

```sql
-- =============================================================
-- Moving Average Crossover
-- Detects when short MA crosses below long MA (bearish crossover)
-- =============================================================
WITH moving_avgs AS (
  SELECT
    date,
    value,
    AVG(value) OVER (ORDER BY date ROWS BETWEEN 6  PRECEDING AND CURRENT ROW) AS ma_7,
    AVG(value) OVER (ORDER BY date ROWS BETWEEN 27 PRECEDING AND CURRENT ROW) AS ma_28
  FROM daily_metrics
  WHERE metric_name = 'daily_revenue'
),
crossovers AS (
  SELECT
    date,
    value,
    ROUND(ma_7::numeric, 2)  AS short_ma,
    ROUND(ma_28::numeric, 2) AS long_ma,
    CASE WHEN ma_7 < ma_28 THEN true ELSE false END AS short_below_long,
    LAG(CASE WHEN ma_7 < ma_28 THEN true ELSE false END) OVER (ORDER BY date) AS prev_short_below_long
  FROM moving_avgs
)
SELECT date, value, short_ma, long_ma, 'bearish_crossover' AS signal
FROM crossovers
WHERE short_below_long = true AND prev_short_below_long = false
ORDER BY date DESC;
```

### 1D. Day-of-Week Baseline Comparison

Compares today's value against the same weekday average over the past N weeks.
Essential for metrics with strong weekly seasonality.

```sql
-- =============================================================
-- Day-of-Week Baseline Comparison
-- Compares current value to same-weekday average (past 4 weeks)
-- =============================================================
WITH weekday_history AS (
  SELECT
    date,
    value,
    EXTRACT(DOW FROM date) AS dow
  FROM daily_metrics
  WHERE metric_name = 'website_sessions'
),
baseline AS (
  SELECT
    h.date,
    h.value,
    AVG(h2.value) AS dow_avg,
    STDDEV(h2.value) AS dow_stddev,
    COUNT(h2.value) AS sample_size
  FROM weekday_history h
  JOIN weekday_history h2
    ON h2.dow = h.dow
    AND h2.date >= h.date - INTERVAL '28 days'
    AND h2.date <  h.date  -- exclude current day
  GROUP BY h.date, h.value
)
SELECT
  date,
  ROUND(value::numeric, 0)    AS actual,
  ROUND(dow_avg::numeric, 0)  AS weekday_avg,
  sample_size,
  ROUND((100.0 * (value - dow_avg) / NULLIF(dow_avg, 0))::numeric, 1) AS pct_vs_baseline,
  ROUND(((value - dow_avg) / NULLIF(dow_stddev, 0))::numeric, 2)      AS z_vs_weekday
FROM baseline
WHERE date = CURRENT_DATE
  AND ABS(100.0 * (value - dow_avg) / NULLIF(dow_avg, 0)) > 30;
```

### 1E. Event-Aware Detection (Suppress Known Events)

Wraps any detection query with known-event suppression.

```sql
-- =============================================================
-- Event-Aware Wrapper
-- Suppresses alerts during known events
-- =============================================================
WITH anomalies AS (
  -- ... insert any detection query here that returns: date, metric_name, ...
  SELECT
    date,
    'daily_revenue' AS metric_name,
    value,
    z_score
  FROM your_detection_query
),
suppressed AS (
  SELECT a.*,
    CASE
      WHEN EXISTS (
        SELECT 1 FROM expected_anomaly_events e
        WHERE a.date BETWEEN e.start_date AND e.end_date
          AND a.metric_name = ANY(e.affected_metrics)
          AND e.suppress_alerts = true
      ) THEN true
      ELSE false
    END AS is_suppressed
  FROM anomalies a
)
SELECT * FROM suppressed
WHERE is_suppressed = false;
```

### 1F. Anomaly Logging Table

```sql
-- =============================================================
-- Anomaly Log Table
-- Records every detected anomaly for tuning and audit
-- =============================================================
CREATE TABLE IF NOT EXISTS anomaly_log (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  detected_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  metric_name   TEXT NOT NULL,
  metric_date   DATE NOT NULL,
  actual_value  NUMERIC,
  expected_value NUMERIC,
  deviation_pct NUMERIC,
  z_score       NUMERIC,
  rule_name     TEXT NOT NULL,
  severity      TEXT NOT NULL CHECK (severity IN ('critical','warning','info')),
  anomaly_type  TEXT CHECK (anomaly_type IN ('spike','drop','trend','missing')),
  is_suppressed BOOLEAN DEFAULT false,
  suppression_reason TEXT,
  -- Post-investigation fields (filled later)
  classification TEXT CHECK (classification IN (
    'true_positive', 'false_positive', 'expected', 'under_review'
  )),
  classified_by TEXT,
  classified_at TIMESTAMPTZ,
  notes         TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_anomaly_log_metric_date ON anomaly_log(metric_name, metric_date);
CREATE INDEX idx_anomaly_log_severity    ON anomaly_log(severity) WHERE classification IS NULL;
```

---

## 2. Threshold Guidance Table

| Metric Type | Example Metrics | Suggested Static Threshold | Suggested Dynamic Method | Lookback |
|---|---|---|---|---|
| **Revenue (daily)** | Daily revenue, MRR | Min $1 (non-zero check) | Z-score (2.5 SD) on 14-day window | 14 days |
| **Revenue (monthly)** | MRR, ARR | MoM decline > 5% | Pct deviation (15%) from 3-month avg | 3 months |
| **Traffic** | Sessions, page views | > 0 (outage check) | Day-of-week baseline (30% deviation) | 4 weeks same-weekday |
| **Conversion rate** | Signup rate, checkout rate | > 0% (funnel broken check) | Z-score (2.0 SD) on 14-day window | 14 days |
| **Churn rate** | Monthly churn % | > 10% absolute | Pct deviation (50%) from 3-month avg | 3 months |
| **Error rate** | HTTP 5xx %, API errors | > 1% of requests | Z-score (2.0 SD) on 7-day window | 7 days |
| **Support volume** | Tickets/day | (none -- too variable) | Day-of-week baseline (100% spike) | 4 weeks same-weekday |
| **Ad spend** | Daily campaign spend | > 120% of daily budget cap | Pct deviation (20%) from 7-day avg | 7 days |
| **Utilisation** | Billable hours % | < 50% (below breakeven) | Consecutive decline (3+ weeks) | 3 weeks |
| **Refund rate** | Refunds / transactions | > 2% of transactions | Z-score (2.0 SD) on 30-day window | 30 days |

### Choosing Between Static and Dynamic

- **Use static thresholds** when a hard business rule exists (revenue must not be $0, error rate must stay below 1%). Static thresholds are Layer 1 -- they catch catastrophic failures.
- **Use dynamic (statistical) thresholds** when "normal" varies over time. Dynamic thresholds are Layer 2 -- they catch unusual-but-not-catastrophic deviations.
- **Use both** for critical metrics. Static catches total failures; dynamic catches subtle shifts.

---

## 3. Common Business Metric Seasonality Patterns

| Pattern | Affected Metrics | Shape | How to Handle |
|---|---|---|---|
| **Weekly cycle** | Traffic, signups, support tickets, e-commerce revenue | Dip on weekends, peak Tue-Thu | Day-of-week baseline comparison |
| **Monthly cycle** | B2B revenue, invoice payments, SaaS signups | Spike at month-start and month-end | Compare to same-day-of-month or use 4-week rolling |
| **Payday cycle** | Consumer e-commerce, subscription renewals | Spikes around 1st and 15th of month | Same-day-of-month comparison |
| **Holiday depression** | All metrics | Drop during Christmas/NY, Easter, national holidays | Known-events calendar with suppression |
| **Holiday spike** | E-commerce revenue, traffic | Surge during Black Friday, Christmas shopping | Known-events calendar; separate thresholds |
| **EOFY / EOCY** | B2B revenue, pipeline, professional services | Spike in last 2 weeks of fiscal year | Known-events calendar |
| **Back-to-school** | Education, family products | August-September surge | Monthly baseline with YoY comparison |
| **Summer lull** | B2B SaaS, professional services | Gradual dip June-August | Wider thresholds for summer months, or YoY baseline |
| **Launch effect** | All product metrics | Spike post-launch, then normalisation | Suppress for 2 weeks post-launch; reset baselines after |

### Handling Multi-Layer Seasonality

Most business metrics have overlapping seasonal patterns (weekly + monthly + annual).
Layer detection approaches:

1. **Daily checks** -- use day-of-week baselines (handles weekly cycle)
2. **Weekly checks** -- use 4-week rolling average (handles monthly cycle)
3. **Monthly checks** -- use year-over-year comparison (handles annual cycle)
4. **All checks** -- consult known-events calendar (handles holidays, launches, campaigns)

---

## 4. Alert Severity Classification

### P1 -- Critical

| Attribute | Value |
|---|---|
| **Response time** | Within 1 hour (immediate for revenue/outage) |
| **Notification** | Slack DM + SMS/phone to on-call |
| **Criteria** | Revenue = $0 when expected > $0; payment processing failure; website/app down; data pipeline broken |
| **Escalation** | If not acknowledged in 15 min, escalate to founder/CTO |
| **Examples** | Stripe webhook stopped; zero orders for 4+ hours during business hours; database unreachable |

### P2 -- Warning

| Attribute | Value |
|---|---|
| **Response time** | Within 4 hours (same business day) |
| **Notification** | Slack channel alert + daily digest email |
| **Criteria** | Revenue >30% below baseline; conversion rate halved; churn rate doubled; error rate >5x normal |
| **Escalation** | If not investigated by end of business day, escalate |
| **Examples** | Revenue dropped 40% vs same day last week; signup conversion from 5% to 2%; 3 enterprise clients churned in one week |

### P3 -- Attention

| Attribute | Value |
|---|---|
| **Response time** | Within 24 hours (next business day OK) |
| **Notification** | Daily digest email + weekly review dashboard |
| **Criteria** | Revenue 15-30% below baseline; gradual trend decline (3+ consecutive periods); traffic source mix shift |
| **Escalation** | Include in weekly review meeting |
| **Examples** | Organic traffic declining for 3 consecutive weeks; average deal size dropped 20%; utilisation trending down |

### P4 -- Informational

| Attribute | Value |
|---|---|
| **Response time** | Next weekly review cycle |
| **Notification** | Weekly digest only |
| **Criteria** | Minor deviations within normal variance; new trends not yet confirmed; data quality notes |
| **Escalation** | None -- review at leisure |
| **Examples** | Slight uptick in support tickets; one referral source dropped slightly; minor data pipeline delay |

---

## 5. Investigation Playbook Template

Use this template for every detection rule. Copy and fill in per rule.

```markdown
## Investigation Playbook: [Rule Name]

**Trigger condition:** [Plain-language description of what fires this alert]
**Severity:** [P1/P2/P3/P4]
**Typical root causes:** [Ranked list of most common reasons]

### Step 1: Confirm the anomaly is real (2 min)
- [ ] Check the raw data source -- is the metric actually at the reported value?
- [ ] Verify the data pipeline ran successfully (no stale data, no ETL failure)
- [ ] Check for known events: is this date in the expected_anomaly_events calendar?
- [ ] Check if other related metrics are also anomalous (correlated signals)

### Step 2: Identify the scope (5 min)
- [ ] Is this affecting all segments or a specific one? (region, product, channel)
- [ ] When did the anomaly start? (narrow the window)
- [ ] Is the anomaly still ongoing or has the metric recovered?

### Step 3: Diagnose root cause (10 min)
- [ ] Check recent deployments or configuration changes
- [ ] Check third-party service status (payment provider, ad platform, CDN)
- [ ] Check for external factors (competitor action, market event, press coverage)
- [ ] Review application logs and error rates for the same time window
- [ ] Query related tables for pattern changes:
  ```sql
  -- Segment breakdown to isolate the anomaly
  SELECT
    [segment_column],
    SUM(value) AS segment_total,
    COUNT(*) AS record_count
  FROM [source_table]
  WHERE date = '[anomaly_date]'
  GROUP BY [segment_column]
  ORDER BY segment_total DESC;
  ```

### Step 4: Decide on action
- [ ] **If P1 (revenue/outage):** Engage incident response; fix or roll back immediately
- [ ] **If P2 (significant deviation):** Investigate today; report findings to stakeholders
- [ ] **If P3 (trend):** Document finding; add to weekly review agenda
- [ ] **If false positive:** Log as false_positive in anomaly_log; adjust threshold if recurring

### Step 5: Close the loop
- [ ] Update anomaly_log with classification (true_positive / false_positive / expected)
- [ ] If threshold needs tuning, create a ticket or adjust config
- [ ] If a new known event was discovered, add to expected_anomaly_events
- [ ] If a new detection rule is needed, document the gap
```

### Quick Investigation Queries

```sql
-- What changed on the anomaly date vs the day before?
SELECT
  date,
  SUM(value) AS total,
  COUNT(*) AS record_count,
  AVG(value) AS avg_value
FROM daily_metrics
WHERE metric_name = '[metric]'
  AND date IN ('[anomaly_date]', '[anomaly_date]'::date - 1)
GROUP BY date
ORDER BY date;

-- Segment-level breakdown for the anomalous period
SELECT
  segment,
  SUM(CASE WHEN date = '[anomaly_date]' THEN value ELSE 0 END) AS anomaly_day,
  SUM(CASE WHEN date = '[anomaly_date]'::date - 7 THEN value ELSE 0 END) AS same_day_last_week,
  ROUND(100.0 * (
    SUM(CASE WHEN date = '[anomaly_date]' THEN value ELSE 0 END) -
    SUM(CASE WHEN date = '[anomaly_date]'::date - 7 THEN value ELSE 0 END)
  ) / NULLIF(SUM(CASE WHEN date = '[anomaly_date]'::date - 7 THEN value ELSE 0 END), 0), 1) AS pct_change
FROM daily_metrics_by_segment
WHERE metric_name = '[metric]'
GROUP BY segment
ORDER BY pct_change ASC;  -- worst-performing segments first

-- Check for data pipeline freshness
SELECT
  metric_name,
  MAX(date) AS latest_date,
  MAX(created_at) AS latest_load_time,
  NOW() - MAX(created_at) AS data_age
FROM daily_metrics
GROUP BY metric_name
ORDER BY latest_date DESC;
```

---

## 6. False Positive Reduction Strategies

### Strategy 1: Day-of-Week Adjustment

**Problem:** Monday traffic is always lower than Thursday traffic. A flat rolling
average flags every Monday as anomalous.

**Solution:** Compare to same-weekday history instead of a flat rolling window.
Use the day-of-week baseline query (Section 1D above).

### Strategy 2: Known-Events Calendar

**Problem:** Christmas, Black Friday, product launches, and marketing campaigns
create expected anomalies that trigger alerts.

**Solution:** Maintain the `expected_anomaly_events` table. Check it before
dispatching any alert. Log suppressed anomalies for audit.

```sql
-- Check before alerting
SELECT EXISTS (
  SELECT 1 FROM expected_anomaly_events
  WHERE CURRENT_DATE BETWEEN start_date AND end_date
    AND '[metric_name]' = ANY(affected_metrics)
    AND suppress_alerts = true
) AS should_suppress;
```

### Strategy 3: Minimum Data Requirement

**Problem:** Detection rules produce meaningless results when the lookback window
has insufficient data (e.g., a new metric with 3 days of history).

**Solution:** Require minimum sample size before applying statistical rules.

```sql
-- Add to any detection query
HAVING COUNT(*) >= 14  -- require at least 14 data points for 14-day lookback
```

### Strategy 4: Consecutive Confirmation

**Problem:** A single outlier triggers an alert, but the metric returns to normal
the next period.

**Solution:** Require the anomaly to persist for 2+ consecutive periods before
alerting (for non-critical metrics).

```sql
-- Consecutive anomaly confirmation
WITH daily_check AS (
  SELECT
    date,
    value,
    rolling_avg,
    CASE WHEN ABS(pct_deviation) > 25 THEN 1 ELSE 0 END AS is_anomalous
  FROM your_detection_query
),
consecutive AS (
  SELECT
    date,
    is_anomalous,
    is_anomalous + COALESCE(LAG(is_anomalous) OVER (ORDER BY date), 0) AS consecutive_count
  FROM daily_check
)
SELECT * FROM consecutive
WHERE consecutive_count >= 2;  -- only alert after 2 consecutive anomalous days
```

### Strategy 5: Graduated Thresholds by Volatility

**Problem:** Applying the same Z-score threshold to both stable and volatile
metrics produces too many false positives on volatile metrics.

**Solution:** Classify metrics by coefficient of variation (CV) and apply
appropriate thresholds.

| CV Range | Volatility Class | Z-Score Threshold | % Deviation Threshold |
|---|---|---|---|
| < 0.10 | Very stable | 2.0 | 15% |
| 0.10 -- 0.25 | Stable | 2.5 | 25% |
| 0.25 -- 0.50 | Moderate | 3.0 | 40% |
| > 0.50 | Highly variable | 3.5 or use % deviation only | 60% |

```sql
-- Calculate CV for each metric to auto-classify
SELECT
  metric_name,
  ROUND(AVG(value)::numeric, 2) AS mean_value,
  ROUND(STDDEV(value)::numeric, 2) AS std_dev,
  ROUND((STDDEV(value) / NULLIF(AVG(value), 0))::numeric, 3) AS cv,
  CASE
    WHEN STDDEV(value) / NULLIF(AVG(value), 0) < 0.10 THEN 'very_stable'
    WHEN STDDEV(value) / NULLIF(AVG(value), 0) < 0.25 THEN 'stable'
    WHEN STDDEV(value) / NULLIF(AVG(value), 0) < 0.50 THEN 'moderate'
    ELSE 'volatile'
  END AS volatility_class
FROM daily_metrics
WHERE date >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY metric_name;
```

### Strategy 6: Cooldown Periods

**Problem:** The same anomaly triggers repeated alerts on consecutive checks.

**Solution:** After an alert fires, suppress the same rule + metric combination
for a cooldown period.

```sql
-- Check cooldown before alerting
SELECT NOT EXISTS (
  SELECT 1 FROM anomaly_log
  WHERE metric_name = '[metric]'
    AND rule_name = '[rule]'
    AND detected_at > NOW() - INTERVAL '4 hours'  -- cooldown period
    AND classification IS DISTINCT FROM 'false_positive'
) AS should_alert;
```

### Strategy 7: Composite Scoring

**Problem:** Individual rules produce marginal alerts. Confidence is low for any
single signal.

**Solution:** Score each anomaly across multiple methods and only alert when the
composite score exceeds a threshold.

```sql
-- Composite anomaly score
SELECT
  date,
  metric_name,
  -- Each method contributes 0 or 1
  (CASE WHEN ABS(z_score) > 2.0 THEN 1 ELSE 0 END) +
  (CASE WHEN ABS(pct_deviation) > 25 THEN 1 ELSE 0 END) +
  (CASE WHEN ABS(dow_z_score) > 2.0 THEN 1 ELSE 0 END) AS composite_score
FROM combined_detection_results
WHERE
  (CASE WHEN ABS(z_score) > 2.0 THEN 1 ELSE 0 END) +
  (CASE WHEN ABS(pct_deviation) > 25 THEN 1 ELSE 0 END) +
  (CASE WHEN ABS(dow_z_score) > 2.0 THEN 1 ELSE 0 END) >= 2;  -- require 2+ methods to agree
```
