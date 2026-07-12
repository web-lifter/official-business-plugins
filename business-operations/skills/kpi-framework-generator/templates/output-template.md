# KPI Framework — {{business_name}}

**Date:** {{date_dd_mm_yyyy}}
**Business Model:** {{business_model}}
**Reporting Cadence:** {{cadence}}
**Framework prepared by:** KPI Framework Generator skill

---

## North-Star Metric

| Field | Value |
|-------|-------|
| **Metric name** | {{north_star_name}} |
| **Definition** | {{north_star_definition}} |
| **Formula** | {{north_star_formula}} |
| **Current value** | {{current_value}} |
| **Target** | {{target_value}} by {{target_date}} |
| **Data source** | {{data_source}} |
| **Why this metric** | {{rationale}} |

---

## Input Metrics

| # | Metric | Definition | Causal Link to North-Star | Current | Target | Owner | Cadence |
|---|--------|-----------|--------------------------|---------|--------|-------|---------|
| 1 | {{metric_1}} | {{definition}} | {{causal_link}} | {{current}} | {{target}} | {{owner_role}} | {{cadence}} |
| 2 | {{metric_2}} | {{definition}} | {{causal_link}} | {{current}} | {{target}} | {{owner_role}} | {{cadence}} |
| 3 | {{metric_3}} | {{definition}} | {{causal_link}} | {{current}} | {{target}} | {{owner_role}} | {{cadence}} |

---

## KPI Tree

```
{{north_star_name}}
├── {{input_metric_1}}
│   ├── {{functional_kpi_1a}} ({{function}})
│   └── {{functional_kpi_1b}} ({{function}})
├── {{input_metric_2}}
│   ├── {{functional_kpi_2a}} ({{function}})
│   └── {{functional_kpi_2b}} ({{function}})
└── {{input_metric_3}}
    ├── {{functional_kpi_3a}} ({{function}})
    └── {{functional_kpi_3b}} ({{function}})
```

---

## KPI Framework Mindmap

```mermaid
mindmap
  root(({{north_star_name}}))
    {{input_metric_1}}
      {{kpi_1a}}
      {{kpi_1b}}
    {{input_metric_2}}
      {{kpi_2a}}
      {{kpi_2b}}
    {{input_metric_3}}
      {{kpi_3a}}
      {{kpi_3b}}
```

---

## KPI Cards — Full Reference

### {{function_1}} KPIs

| KPI | Definition | Formula | Owner | Baseline | Target | Cadence | Data Source |
|-----|-----------|---------|-------|---------|--------|---------|------------|
| {{kpi}} | {{definition}} | {{formula}} | {{role}} | {{baseline}} | {{target}} | {{cadence}} | {{source}} |

### {{function_2}} KPIs

| KPI | Definition | Formula | Owner | Baseline | Target | Cadence | Data Source |
|-----|-----------|---------|-------|---------|--------|---------|------------|
| {{kpi}} | {{definition}} | {{formula}} | {{role}} | {{baseline}} | {{target}} | {{cadence}} | {{source}} |

_(Add a section per function)_

---

## OKR Alignment

| Objective | Key Result | Primary KPI | Owner | Target |
|-----------|-----------|-------------|-------|--------|
| {{objective}} | {{key_result}} | {{kpi}} | {{role}} | {{target}} |

---

## KPI Health Dashboard Template

> Copy this table into your weekly/monthly review doc and update the Status column.

| KPI | Current | Target | Status | Owner | Notes |
|-----|---------|--------|--------|-------|-------|
| {{north_star_name}} | | {{target}} | On Track / At Risk / Off Track | {{owner}} | |
| {{kpi_1}} | | {{target}} | On Track / At Risk / Off Track | {{owner}} | |
| {{kpi_2}} | | {{target}} | On Track / At Risk / Off Track | {{owner}} | |

---

## Build-to List

KPIs marked `[build-to]` require tooling or process not yet in place.

| KPI | What's Needed | Recommended Tool | Effort | Priority |
|-----|--------------|-----------------|--------|---------|
| {{kpi}} | {{gap}} | {{tool}} | {{effort}} | {{high_medium_low}} |

---

## Next 30-Day Actions

1. {{action_1}}
2. {{action_2}}
3. {{action_3}}
