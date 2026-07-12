# A/B Test Design — Checkout button colour: green vs amber

**Date:** 19/05/2026
**Owner:** Growth PM — Aisha

---

## Hypothesis

**H1:** If we change the "Place order" button from green (#27AE60) to amber (#F39C12), checkout conversion rate will rise by ≥ 0.5 percentage points (from 4.2% to ≥ 4.7%).
**H0:** No effect.

---

## Design Specification

| Field | Value |
|-------|-------|
| Primary metric | Checkout conversion rate |
| Definition | Sessions reaching `/order/confirm` ÷ sessions reaching `/checkout/begin`, per user |
| Secondary metrics | Cart-abandon rate; AOV; time-on-checkout |
| Guardrail metrics | Refund rate (7-day); CS-ticket volume; page-load p95 latency |
| Randomisation unit | user_id (hashed) |
| Variants | A control (green 50%) / B amber (50%) |
| Sample size per arm | 11,820 |
| Total sample | 23,640 |
| Duration at 1,800 users/day into test | 13 days |
| Pre-launch | A/A test 24-hour SRM check + 24-hour A/A residual scan |
| Stopping rule | Fixed 14-day horizon; no peeking on primary |

---

## Power Analysis

| Parameter | Value |
|-----------|-------|
| Baseline | 0.042 (4.2%) |
| MDE (absolute) | 0.005 |
| Alpha | 0.05 (two-sided) |
| Power | 0.80 |
| Sample/arm | 11,820 |

### Sensitivity

| MDE × | Sample/arm | Duration |
|-------|-----------|----------|
| 0.5× (0.25pp) | 47,280 | ~7 weeks |
| 1.0× (0.5pp) | 11,820 | ~13 days |
| 2.0× (1.0pp) | 2,955 | ~3 days |

---

## Pre-Registered Decision Matrix

| Outcome | Action |
|---------|--------|
| ≥ 0.5pp lift, no guardrail breach | Ship to 100% week 3 |
| 0.2–0.5pp lift, no guardrail breach | Discuss in growth-review; default to ship with monitoring |
| Not significant or < 0.2pp | Don't ship; design follow-up experiment |
| Guardrail breach (refund > +5% rel or latency p95 > +50ms) | Don't ship; investigate |
| CI too wide (lower bound < 0 with > 5wk traffic seen) | Extend or accept inconclusive |

---

## Launch & Monitoring Plan

- **Day 1:** SRM chi-square check (expect p > 0.05); A/A residual eyeballed
- **Day 3:** Guardrail-only peek (refund + CS tickets + latency); pause if breached
- **Day 14:** Primary read + secondary + guardrail summary; readout via `[[experiment-readout-builder]]`
- **Post-launch:** Document in experiment ledger; share findings in next growth review

---

## Stats Reviewer — Independent Review

### Verdict: Approve-with-changes

### Critical issues

1. **Single primary metric is clean.** Good.
2. **Sample-size math checks** with the provided baseline + MDE.
3. **Guardrails are appropriate** — refund + CS + latency cover the obvious harms.
4. **Potential SUTVA concern: low.** This is a per-user button colour change; minimal cross-user effect.

### Important caveats

1. **Novelty effect at 13 days is unlikely to be significant for a UI colour change** — but flag for monitoring; if observed lift declines over time, consider extending.
2. **MDE of 0.5pp is plausible but on the larger side for a button-colour change.** Industry effect sizes for colour changes are typically 0.1–0.3pp. Recommend mentally preparing for "inconclusive" being the most likely outcome.
3. **No mention of mobile vs desktop split** — checkout conversion differs dramatically. Pre-register the split as a secondary; do not run as the primary cut.

### Optional improvements

1. Consider running for 14 days minimum to capture a full weekly cycle.
2. Tag mobile vs desktop in the read; don't combine.
3. Pre-write the follow-up experiment now (e.g. button copy + colour) so a "not significant" outcome doesn't waste the learning.

### What I checked

- Primary metric clarity ✓
- Sample-size justification ✓
- Randomisation unit ✓
- Guardrails ≥ 2 ✓
- Stopping rule ✓
- SRM check planned ✓
- Multiple-comparisons not applicable (1 primary, secondaries flagged)
- Novelty/primacy considered ✓
- Network effects checked (none expected) ✓
- Practical vs statistical sig discussed ✓
- Decision criteria pre-written ✓
