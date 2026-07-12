---
title: MVP metrics
slug: mvp-metrics
type: mvp-spec
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# MVP metrics

**MVP type:** Partial product (a narrow but real end-to-end slice — upload → classify → review → redline).
**MVP spec:** [mvp-spec](mvp-spec.md)

## Hypothesis-driven metrics

| Hypothesis | Metric | Threshold | Timeframe | Source |
|-----------|--------|-----------|-----------|--------|
| H-001 — Demand | Willingness-to-pay (≥ AU$300/seat/month) in cohort interviews | ≥ 30% of 20 interviewees express willingness | 2026-05-26 → 2026-07-04 (6 weeks) | Interview notes (`02-customer-discovery/interviews/`) coded into PostHog `wtp_response` event |
| H-002 — Usability | Median time-to-redline across the 12-counsel cohort | < 25 minutes | 2026-05-26 → 2026-06-13 | Supabase SQL: `percentile_cont(0.5)` over `findings.reviewed_at - classifier_runs.finished_at` |
| H-003 — Scale (classifier precision) | Precision across the 14 risky-clause categories on held-out AU MSA set | ≥ 85% precision (refute < 70%) | 2026-06-01 → 2026-06-22 | Manual labelling pass on 30-document held-out set; reviewer = Priya |

## MVP-type-standard metrics (partial product)

| Metric | Threshold | Timeframe | Source |
|--------|-----------|-----------|--------|
| Activation rate: signed-up → contract uploaded | ≥ 70% within 7 days | rolling 30-day | PostHog funnel `user_signed_up → contract_uploaded` |
| Week-2 retention (paid cohort) | ≥ 50% | weeks 1-4 post-`checkout_completed` | PostHog retention insight, cohort = checkout_completed |
| NPS / qualitative score from the 12-counsel cohort | NPS ≥ +20 OR ≥ 8/12 say "would use weekly" | exit interview at week 6 | Survey (Tally) + interview notes |

## Decision rules

At end of each metric's timeframe:

- **All H-001/H-002/H-003 metrics meet threshold** → MVP succeeded on demand + usability + scale. Proceed to: H-001 expansion (paid waitlist conversion via Stripe), H-002 widen cohort (12 → 40 counsel), H-003 hold and monitor.
- **H-001 < threshold and H-002 ≥ threshold** → product works but pricing is off; build learning card LC-001 covering pricing tier exploration; refine pricing.
- **H-002 < 25 min but ≥ 45 min** → refine UX (likely findings UI density); rerun TC-007 with same cohort.
- **H-002 ≥ 45 min OR H-003 < 70%** → MVP refuted on usability or core technical bet. Build learning card; decide pivot vs refine. Pivot options: structured wizard UI (more guidance) OR narrower clause taxonomy (more precision, fewer categories).
- **Activation < 70%** is a secondary indicator — only acts as a tie-breaker; it doesn't carry the decision alone.

## Hand-off

Next: `/mvp-analytics-plan` translates these metrics into events to instrument, then `/funnel-instrumentation-spec` wires the funnel thresholds, then `/experiment-data-collection-plan` per test card for the H-002 cohort study.
