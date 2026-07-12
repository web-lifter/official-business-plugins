## Cohort Analysis Framework — [Business Name]

### 1. Cohort Framework

- **Cohort Definition:** {{how users are grouped — e.g. month of first purchase}}
- **Activity Metric:** {{what counts as "active" — e.g. completed a purchase}}
- **Analysis Type:** Retention / Revenue / Custom
- **Granularity:** Weekly / Monthly / Quarterly
- **Observation Window:** {{e.g. 12 months from cohort start}}
- **Rationale:** {{why this cohort definition and metric were chosen}}

<!-- Be explicit about what "active" means. Ambiguous activity definitions are the most common cohort analysis mistake. -->

---

### 2. Cohort Assignment SQL

```sql
-- ============================================================
-- Configuration: update these values for your schema
-- ============================================================
-- Table: {{schema.table_name}}
-- User ID column: {{user_id_column}}
-- Activity date column: {{activity_date_column}}
-- Revenue column (if applicable): {{revenue_column}}
-- ============================================================

-- Assign each user to their cohort (first activity period)
WITH cohort_assignment AS (
  SELECT
    {{user_id_column}},
    DATE_TRUNC('{{granularity}}', MIN({{activity_date_column}})) AS cohort_period
  FROM {{table_name}}
  GROUP BY {{user_id_column}}
)
SELECT * FROM cohort_assignment;
```

<!-- Cohort assignment derives from the first observed activity. -->
<!-- If signup date is available, prefer it over first activity date. -->

---

### 3. Retention/Revenue Analysis SQL

```sql
-- ============================================================
-- Cohort Retention Analysis
-- ============================================================

WITH cohort_assignment AS (
  -- {{cohort assignment CTE from above}}
),
activity_periods AS (
  SELECT
    {{user_id_column}},
    DATE_TRUNC('{{granularity}}', {{activity_date_column}}) AS activity_period
  FROM {{table_name}}
  GROUP BY 1, 2
),
cohort_retention AS (
  SELECT
    ca.cohort_period,
    (EXTRACT(YEAR FROM ap.activity_period) - EXTRACT(YEAR FROM ca.cohort_period)) * 12
      + EXTRACT(MONTH FROM ap.activity_period) - EXTRACT(MONTH FROM ca.cohort_period)
      AS period_offset,
    COUNT(DISTINCT ca.{{user_id_column}}) AS active_users
  FROM cohort_assignment ca
  JOIN activity_periods ap USING ({{user_id_column}})
  GROUP BY 1, 2
  HAVING COUNT(DISTINCT ca.{{user_id_column}}) >= 30  -- Minimum cohort size
)
SELECT
  cohort_period,
  period_offset,
  active_users,
  ROUND(100.0 * active_users / FIRST_VALUE(active_users)
    OVER (PARTITION BY cohort_period ORDER BY period_offset), 1) AS retention_pct
FROM cohort_retention
ORDER BY cohort_period, period_offset;
```

<!-- Flag cohorts with fewer than 30 members as statistically unreliable. -->
<!-- Period 0 is always 100% by definition. State whether it is included or excluded. -->

---

### 4. Visualisation Specification

**Cohort Retention Grid (Heatmap):**

| Cohort | M0 | M1 | M2 | M3 | ... |
|--------|-----|-----|-----|-----|-----|
| {{period}} | 100% | {{%}} | {{%}} | {{%}} | ... |

- **Colour scale:** Green (>benchmark) to Red (<benchmark)
- **Tool recommendation:** {{spreadsheet / Metabase / Looker / custom}}

**Retention Curve (Line Chart):**
- X-axis: Period offset (months since cohort start)
- Y-axis: Retention percentage (0-100%)
- One line per cohort, with legend
- Overlay: benchmark line at {{industry benchmark %}}

<!-- Include both grid and curve views. The grid shows individual cohort performance; the curve shows trends. -->

---

### 5. Interpretation Guide

**What to look for:**
- **Flattening curves:** Retention that levels off indicates a stable retained base. The higher the plateau, the healthier the business.
- **Improving cohorts over time:** Later cohorts retaining better than earlier ones indicates product/market improvements are working.
- **Degrading cohorts:** Later cohorts retaining worse suggests market saturation, quality issues, or audience drift.
- **Steep early drop:** High M0-to-M1 drop suggests onboarding problems or mismatched expectations.

**Benchmarks:**
- {{Industry}}: M1 retention ~{{%}}, M6 retention ~{{%}}, M12 retention ~{{%}}
- Source: {{benchmark source}}

**Decision Framework:**
- If M1 retention < {{threshold}}: Focus on onboarding and activation
- If M6 retention < {{threshold}}: Focus on engagement and habit formation
- If cohorts are degrading: Investigate acquisition channel quality

---

### 6. Assumptions & Limitations

- **Data completeness:** {{note any gaps in historical data}}
- **Cohort start point:** {{signup date vs first activity — which is used and why}}
- **Activity definition:** {{exactly what events qualify as "active"}}
- **Small cohort warning:** Cohorts with fewer than 30 members are flagged; interpret with caution.
- **Survivorship bias:** {{note if only active users are in the dataset}}
- **Recommended refresh cadence:** {{weekly / monthly}} with tracking of how same-period retention evolves over time.
