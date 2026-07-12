---
title: Churn model
slug: churn-model
type: funnel
status: active
owner: {{venture_name}}
created: {{date}}
updated: {{date}}
---

# Churn model

Source funnel: [funnel-model.md](funnel-model.md)
Anchor monthly retention rate: {{rate}}%
Implied monthly churn: {{churn}}%

## Sensitivity table

| Monthly retention | Monthly churn | Annual retention | Avg lifetime (mo) |
|-------------------|---------------|------------------|-------------------|
| {{r}}             | {{c}}         | {{annual}}       | {{lifetime}}      |

## Cohort decay (anchor rate)

| Month | Cohort still active |
|-------|---------------------|
| 1     | {{pct}}             |
| 3     | {{pct}}             |
| 6     | {{pct}}             |
| 12    | {{pct}}             |
| 24    | {{pct}}             |

## Interpretation

- Average customer lifetime: {{X}} months
- Cohort still here at 12 months: {{pct}}%
- ±5pp sensitivity: {{range}}

## Implications for unit economics

- LTV ≈ price × {{X}}
- CAC payback target: < {{months}}
- Hand off to `business-economics/unit-economics` for rigorous LTV/CAC.
