# Elasticity Method Spec — AU B2B SaaS (project mgmt for trades) — Crew tier

**Date:** 20/05/2026

---

## Recommended Method

**Method:** A/B price test on new signups (gold standard)
**Why:** Product has > 100 new signups/wk into the Crew tier — sufficient traffic for power. Pricing is publicly listed but server-controlled — easy to vary by experiment cell. No regulatory constraint on differential pricing of new customers (existing customers grandfathered separately). Historical regression won't work — only one price change in the past 24 months. Survey methods would suffer from hypothetical bias and don't capture renewal behaviour.

---

## Implementation

| Parameter | Value |
|-----------|-------|
| Required N | 3 cells × 1,200 new signups = 3,600 (over ~12 weeks at 100/wk per cell after randomisation) |
| Time to deliver | 12 weeks experiment + 12 weeks post-conversion observation (to measure 90-day retention impact) = 24 weeks |
| Cost estimate (AUD) | Mostly internal — 1 wk analyst time for design + 1 wk for readout. ~$5,000 internal. Plus opportunity cost of running price experiments. |
| Statistical power | 0.8 to detect 10% relative change in conversion-to-paid at $89 baseline (4.5% baseline; MDE 0.45pp) |

---

## Identification Assumption

> Cell assignment is genuinely random (not influenced by user characteristics); each cell sees only its assigned price during the experiment; no price leakage via referrals or external review sites.

How to validate:
- SRM check on cell assignment + on geo/source/device split (chi-square; expect p > 0.01)
- Cookie check: same user lands in same cell on revisit
- Monitor review sites + community boards for any user posting "X told me $79 but my friend got $99"

---

## Implementation Plan

| Week | Activity |
|------|---------|
| 1 | Design experiment (use `[[ab-test-designer]]`); pre-register decision matrix |
| 2 | Engineering: implement 3-cell server-side price routing with cookie pinning |
| 3 | Pre-launch QA: SRM monitor, cell-pinning test, billing-system reconciliation |
| 4–15 | Experiment runs (12 wk); weekly SRM check; weekly guardrail check |
| 16 | Primary read: conversion-to-paid at each price; estimate elasticity from {pageviews, signups, conversions} per cell |
| 17–24 | Post-conversion observation: 90-day retention by cell; check for selection effects |
| 25 | Final readout via `[[experiment-readout-builder]]`; recommend pricing action via `[[pricing-architecture-designer]]` |

---

## Expected Output Format

| Output | Description |
|--------|-------------|
| Point elasticity for Crew tier | Expected ε ≈ -0.8 to -1.5 (B2B SaaS typical range) |
| Confidence interval | 95% CI on ε |
| Price-response curve | Conversion-to-paid % at each of 3 price points + 95% CI |
| 90-day retention by cell | Are price-sensitive cohorts also churn-prone? |
| Annual upgrade rate by cell | Does the $79 cell upgrade to Annual at a different rate? |

---

## Caveats

| Caveat | Severity | Mitigation |
|--------|----------|------------|
| Price-leakage (user finds out about lower price) | M | Monitor public channels weekly; pause if leak detected; size of effect at AU SMB scale should be small |
| Selection by cell (random assignment but cell sees different value-cue) | M | Cell-pinning; verify SRM; verify covariates balanced |
| 12-week duration captures only short-run elasticity | M | The 90-day post-observation helps; long-run renewal-elasticity is different — flag in readout |
| Existing customer fairness (the elephant in the room) | M-H | Be transparent in policy: "new pricing experiments occasionally happen for new signups; existing customers always pay or less than what they signed up at" |
| 3 cells dilutes per-cell power | L | At 100/wk × 12 wk = 1,200 per cell, we're appropriately powered for 0.45pp MDE on 4.5% baseline |

---

## What to Do With the Result

- If |ε| < 0.5 → Crew tier is highly inelastic; raise price toward $99 (`[[pricing-architecture-designer]]`)
- If 0.5 < |ε| < 1.0 → moderate; consider $94 micro-test or hold
- If |ε| > 1.0 → elastic; current $89 may even be high; test $79
- Whatever the result, route to `[[pricing-architecture-designer]]` for the action plan and `[[break-even-scenario-modeller]]` for the runway-impact analysis
