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

These are illustrative, pre-specified decision rules, not observed results. First check usable sample, event completeness and the declared cohort for each metric.

- H-001: willingness-to-pay at or above 30% supports an interview-based demand signal only; it is not a paid conversion or proof of market demand. Investigate alternatives when below the threshold, not pricing alone.
- H-002: median below 25 minutes meets the usability threshold; 25 to under 45 minutes triggers UX refinement; 45 minutes or more fails the target. These ranges do not overlap.
- H-003: precision at least 85% meets the technical target; 70% to under 85% requires refinement; below 70% fails. None proves scalability without load and cost evidence.
- Missing data, insufficient samples or conflicting guardrails are inconclusive. Passing all three supports a controlled follow-on pilot, not immediate scale.

## Hand-off

Next: `/mvp-analytics-plan` translates these metrics into events to instrument, then `/funnel-instrumentation-spec` wires the funnel thresholds, then `/experiment-data-collection-plan` per test card for the H-002 cohort study.
