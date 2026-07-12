---
title: Funnel model
slug: funnel-model
type: funnel
status: active
owner: {{venture_name}}
created: {{date}}
updated: {{date}}
---

# Funnel model

| Stage | Definition (event) | Volume | Rate from prior | Source | Hypothesis |
|-------|--------------------|--------|-----------------|--------|------------|
| Awareness | {{event}} | {{n}} | — | — | — |
| Sign-up | {{event}} | {{n}} | {{rate}} | {{source}} | {{H-NN}} |
| Activation | {{event}} | {{n}} | {{rate}} | {{source}} | {{H-NN}} |
| Conversion | {{event}} | {{n}} | {{rate}} | {{source}} | {{H-NN}} |
| Retention (W4) | {{event}} | {{n}} | {{rate}} | {{source}} | {{H-NN}} |

End-to-end yield: {{pct}}%

## Reality check

- Industry benchmark for primary channel: {{benchmark}}
- Our model is {{better_worse_par}} by {{factor}}
- Risk: {{risk_note}}

## Hand-off

Run `mvp-planning/funnel-instrumentation-spec` to translate these stages into events.
