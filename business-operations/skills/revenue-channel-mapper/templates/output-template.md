# Revenue Channel Map — {{business_name}}

**Date:** {{date_dd_mm_yyyy}}
**Business Stage:** {{business_stage}}
**Model:** {{b2b_b2c_hybrid}} | {{product_service_marketplace}}
**Prepared by:** Revenue Channel Mapper skill

---

## Executive Summary

- {{key_insight_1}}
- {{key_insight_2}}
- {{key_insight_3}}

---

## Channel Canvas

| Channel | Type | Monthly Volume | CAC (AUD) | LTV (AUD) | LTV:CAC | Contribution % | Friction (0–5) | Status |
|---------|------|---------------|-----------|-----------|---------|----------------|----------------|--------|
| {{channel_1}} | {{type}} | {{volume}} | ${{cac}} | ${{ltv}} | {{ratio}} | {{pct}}% | {{friction}} | {{status}} |
| {{channel_2}} | {{type}} | {{volume}} | ${{cac}} | ${{ltv}} | {{ratio}} | {{pct}}% | {{friction}} | {{status}} |
| {{channel_3}} | {{type}} | {{volume}} | ${{cac}} | ${{ltv}} | {{ratio}} | {{pct}}% | {{friction}} | {{status}} |
| _Add rows as needed_ | | | | | | | | |

> Cells marked `[est]` are estimates — see Assumptions section.

---

## Revenue Flow Map

```mermaid
flowchart LR
  {{customer_node}}[Prospect / Customer]
  {{channel_node_1}}[{{channel_name_1}}]
  {{channel_node_2}}[{{channel_name_2}}]
  {{revenue_node}}[Revenue — {{revenue_type}}]

  {{customer_node}} --> {{channel_node_1}}
  {{customer_node}} --> {{channel_node_2}}
  {{channel_node_1}} --> {{revenue_node}}
  {{channel_node_2}} --> {{revenue_node}}
```

---

## RICE Prioritisation

| Channel | Reach (1–10) | Impact (1–3) | Confidence | Effort (wks) | RICE Score | Recommendation |
|---------|-------------|-------------|-----------|-------------|-----------|----------------|
| {{channel_1}} | {{reach}} | {{impact}} | {{confidence}}% | {{effort}} | {{score}} | {{invest_hold_cut}} |
| {{channel_2}} | {{reach}} | {{impact}} | {{confidence}}% | {{effort}} | {{score}} | {{invest_hold_cut}} |
| {{channel_3}} | {{reach}} | {{impact}} | {{confidence}}% | {{effort}} | {{score}} | {{invest_hold_cut}} |

**Top 3 to invest:** {{top_channels}}
**Deprioritise:** {{cut_channels}}

---

## 90-Day Experiment Plan

| # | Channel | Hypothesis | Success Metric | Budget (AUD) | Effort | Owner | Start | Kill Criterion |
|---|---------|-----------|---------------|-------------|--------|-------|-------|----------------|
| 1 | {{channel}} | If we {{action}}, {{metric}} will {{change}} by {{pct}}% in {{days}} days | {{kpi}} = {{target}} | ${{budget}} | {{days}}d | {{role}} | Wk {{n}} | < {{threshold}} by day {{d}} |
| 2 | {{channel}} | If we {{action}}, {{metric}} will {{change}} by {{pct}}% in {{days}} days | {{kpi}} = {{target}} | ${{budget}} | {{days}}d | {{role}} | Wk {{n}} | < {{threshold}} by day {{d}} |
| 3 | {{channel}} | If we {{action}}, {{metric}} will {{change}} by {{pct}}% in {{days}} days | {{kpi}} = {{target}} | ${{budget}} | {{days}}d | {{role}} | Wk {{n}} | < {{threshold}} by day {{d}} |

---

## Assumptions & Data Gaps

| Channel | Field | Assumption | Data Needed to Sharpen |
|---------|-------|-----------|----------------------|
| {{channel}} | {{field}} | {{assumption}} | {{data_source}} |

---

## Next Steps

1. {{next_step_1}}
2. {{next_step_2}}
3. {{next_step_3}}
