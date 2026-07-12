# Anomaly Detection Rules: E-Commerce Revenue Monitoring

**Store:** Koala & Co. Online (Australian homewares e-commerce)
**Data Source:** Supabase `orders`, `sessions`, `carts` tables
**Monitoring Window:** Rolling 7-day baseline, evaluated daily at 06:00 AEST

---

## Rule 1: Daily Revenue Drop

**Metric:** Total gross revenue (AUD) per calendar day
**Sensitivity:** Alert when daily revenue falls below 2 standard deviations from the 7-day rolling average.

```sql
WITH daily_revenue AS (
  SELECT
    date_trunc('day', completed_at AT TIME ZONE 'Australia/Sydney') AS revenue_date,
    SUM(total_amount_cents) / 100.0 AS revenue_aud
  FROM orders
  WHERE status = 'completed'
    AND completed_at >= NOW() - INTERVAL '8 days'
  GROUP BY 1
),
baseline AS (
  SELECT
    AVG(revenue_aud) AS mean_revenue,
    STDDEV(revenue_aud) AS stddev_revenue
  FROM daily_revenue
  WHERE revenue_date < CURRENT_DATE
)
SELECT
  dr.revenue_date,
  dr.revenue_aud,
  b.mean_revenue,
  b.mean_revenue - (2 * b.stddev_revenue) AS lower_threshold
FROM daily_revenue dr
CROSS JOIN baseline b
WHERE dr.revenue_date = CURRENT_DATE
  AND dr.revenue_aud < b.mean_revenue - (2 * b.stddev_revenue);
```

**Threshold:** Dynamic -- `mean - 2 * stddev` (approx. $4,200 based on recent $6,800 avg)
**Severity:** Critical
**Notification:** Slack #ops-alerts + email to finance@koalaandco.com.au

---

## Rule 2: Conversion Rate Decline

**Metric:** Sessions with a completed order / total sessions (daily)
**Sensitivity:** Alert when conversion rate drops more than 40% relative to the 7-day average.

```sql
WITH daily_conversion AS (
  SELECT
    date_trunc('day', s.started_at AT TIME ZONE 'Australia/Sydney') AS session_date,
    COUNT(DISTINCT s.id) AS total_sessions,
    COUNT(DISTINCT o.session_id) AS converting_sessions,
    COUNT(DISTINCT o.session_id)::numeric / NULLIF(COUNT(DISTINCT s.id), 0) AS conversion_rate
  FROM sessions s
  LEFT JOIN orders o ON o.session_id = s.id AND o.status = 'completed'
  WHERE s.started_at >= NOW() - INTERVAL '8 days'
  GROUP BY 1
),
baseline AS (
  SELECT AVG(conversion_rate) AS avg_conversion
  FROM daily_conversion
  WHERE session_date < CURRENT_DATE
)
SELECT
  dc.session_date,
  ROUND(dc.conversion_rate * 100, 2) AS conversion_pct,
  ROUND(b.avg_conversion * 100, 2) AS avg_conversion_pct,
  ROUND((1 - dc.conversion_rate / NULLIF(b.avg_conversion, 0)) * 100, 1) AS pct_decline
FROM daily_conversion dc
CROSS JOIN baseline b
WHERE dc.session_date = CURRENT_DATE
  AND dc.conversion_rate < b.avg_conversion * 0.6;
```

**Threshold:** 40% relative decline (e.g., baseline 3.2% -> alert below 1.92%)
**Severity:** High
**Notification:** Slack #ops-alerts

---

## Rule 3: Cart Abandonment Spike

**Metric:** Carts created but not converted within 24 hours
**Sensitivity:** Alert when abandonment rate exceeds 80% (absolute threshold).

```sql
WITH daily_carts AS (
  SELECT
    date_trunc('day', created_at AT TIME ZONE 'Australia/Sydney') AS cart_date,
    COUNT(*) AS total_carts,
    COUNT(*) FILTER (
      WHERE id NOT IN (SELECT cart_id FROM orders WHERE status = 'completed')
        AND created_at < NOW() - INTERVAL '24 hours'
    ) AS abandoned_carts
  FROM carts
  WHERE created_at >= NOW() - INTERVAL '2 days'
    AND created_at < CURRENT_DATE
  GROUP BY 1
)
SELECT
  cart_date,
  total_carts,
  abandoned_carts,
  ROUND(abandoned_carts::numeric / NULLIF(total_carts, 0) * 100, 1) AS abandonment_pct
FROM daily_carts
WHERE abandoned_carts::numeric / NULLIF(total_carts, 0) > 0.80;
```

**Threshold:** 80% absolute abandonment rate
**Severity:** Medium
**Notification:** Slack #marketing-alerts

---

## Rule 4: Average Order Value Anomaly

**Metric:** Mean order value (AUD) per day
**Sensitivity:** Alert on both unusually high (>2.5 stddev) and low (<2 stddev) values.

```sql
WITH daily_aov AS (
  SELECT
    date_trunc('day', completed_at AT TIME ZONE 'Australia/Sydney') AS order_date,
    AVG(total_amount_cents) / 100.0 AS avg_order_value,
    COUNT(*) AS order_count
  FROM orders
  WHERE status = 'completed'
    AND completed_at >= NOW() - INTERVAL '31 days'
  GROUP BY 1
),
baseline AS (
  SELECT
    AVG(avg_order_value) AS mean_aov,
    STDDEV(avg_order_value) AS stddev_aov
  FROM daily_aov
  WHERE order_date < CURRENT_DATE
)
SELECT
  d.order_date,
  ROUND(d.avg_order_value, 2) AS aov_aud,
  ROUND(b.mean_aov, 2) AS baseline_aov,
  CASE
    WHEN d.avg_order_value > b.mean_aov + (2.5 * b.stddev_aov) THEN 'SPIKE'
    WHEN d.avg_order_value < b.mean_aov - (2.0 * b.stddev_aov) THEN 'DROP'
  END AS anomaly_type
FROM daily_aov d
CROSS JOIN baseline b
WHERE d.order_date = CURRENT_DATE
  AND (d.avg_order_value > b.mean_aov + (2.5 * b.stddev_aov)
       OR d.avg_order_value < b.mean_aov - (2.0 * b.stddev_aov));
```

**Threshold:** Upper: `mean + 2.5 * stddev` (~$185) / Lower: `mean - 2 * stddev` (~$78)
**Severity:** Medium (DROP) / Low (SPIKE -- may indicate bulk order, investigate)
**Notification:** Slack #ops-alerts

---

## Investigation Playbook

When an alert fires, follow this triage sequence:

| Step | Action | Tool |
|------|--------|------|
| 1 | Confirm the alert is not a data lag issue -- check `orders` table max timestamp | SQL query |
| 2 | Segment by traffic source -- is the drop isolated to paid, organic, or direct? | GA4 / UTM breakdown |
| 3 | Check for site errors -- 5xx spike in the last 24h | Cloudflare analytics or server logs |
| 4 | Review payment gateway status -- failed transaction rate | Stripe dashboard |
| 5 | Check promotional calendar -- did a sale end or a competitor launch a campaign? | Marketing team via Slack |
| 6 | Verify inventory -- are bestsellers out of stock? | Inventory management system |

**Escalation path:**
- Critical alerts with no clear root cause within 30 minutes -> page on-call engineer
- Revenue drop confirmed as real and >25% -> notify Head of Commercial immediately
- Cart abandonment spike + payment errors -> escalate to Stripe support
