---
name: churn-model
description: Model customer survival and expected lifetime from a stated retention rate; distinguish assumptions from observed cohorts and compute gross-margin-adjusted economics.
argument-hint: "[monthly retention rate, optional ARPU, gross margin and CAC]"
allowed-tools: Read Write Edit Glob Grep Bash
effort: low
---

# churn-model

## Runtime preflight

Read [the runtime guide](../../RUNTIME.md) before this workflow.

## User Context

$ARGUMENTS

## Phase 1: Define inputs

Resolve the venture root. Read `06-relationships-channels/funnel-model.md` or the supplied cohort data. Confirm the time period and whether an input is retention or churn. `r` always denotes retention and `c = 1-r` denotes churn. Do not infer an industry benchmark or substitute an illustrative rate for measured data. Preserve the existing `--rate` interpretation as monthly retention.

## Phase 2: Calculate

Use `r**n` for cohort share remaining after `n` periods. Under constant churn and including the initial paid period, expected lifetime is `1/(1-r)`. See [derivation and limitations](references.md). Use the bundled helper when execution is available:

```bash
python3 <plugin-root>/scripts/retention_model.py --retention 0.94 --months 12
```

Compute sensitivity at relevant rates between 0 and 1, including the anchor and valid plus/minus five-percentage-point cases. Do not pass rates above 1. At `r=1`, lifetime is unbounded in this model; use a finite forecast horizon, not an infinite business valuation. Round only final displayed values.

## Phase 3: Interpret without overstating

Report monthly churn, annual retention, average lifetime and sensitivity. If ARPU and gross margin are provided, contribution LTV is `ARPU * gross_margin / churn`; CAC payback is `CAC / (ARPU * gross_margin)` when gross profit is positive. Do not compare revenue LTV against a contribution-LTV benchmark. Zero CAC gives an undefined/infinite ratio, not evidence of a scalable acquisition channel.

No observed cohorts means a scenario, not a validated forecast. Constant retention ignores changing hazards, expansion, discounting and censoring. Prefer observed cohort estimates when sufficient data is supplied. A flat-rate forecast is not necessarily conservative.

## Phase 4: Deliver

Write `06-relationships-channels/churn-model.md` using the [template](templates/output-template.md), preserving the funnel inputs. Include exact inputs, formulas, assumptions and source evidence. Update the venture log only when persisted content changes. The optional `economics:unit-economics-calculator` handoff provides more detailed economics; absence of that plugin does not prevent this analysis.
