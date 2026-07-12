# Experiment Readout — Checkout button colour: green vs amber

**Period:** 19/05/2026 → 01/06/2026 (14 days)
**Owner:** Growth PM — Aisha
**Pre-registered design:** `ab-test-design.md` (see ab-test-designer example)

---

## Pre-Registration Recap

- **Primary metric:** Checkout conversion rate
- **MDE:** 0.5 percentage points (4.2% → 4.7%)
- **Decision matrix:** Ship if ≥ 0.5pp + no guardrail breach; discuss if 0.2–0.5pp; don't ship if < 0.2pp or guardrail red

---

## SRM Check

| Arm | Observed | Expected | % deviation |
|-----|----------|----------|------------|
| A (green) | 11,792 | 11,820 | -0.24% |
| B (amber) | 11,848 | 11,820 | +0.24% |

**Chi-square p-value:** 0.71
**Verdict:** Passed (no SRM)

---

## Primary Read

| Arm | Sample | Checkout CR | 95% CI |
|-----|--------|------------|--------|
| A (green) | 11,792 | 4.21% | [3.85%, 4.57%] |
| B (amber) | 11,848 | 4.43% | [4.06%, 4.80%] |

- **Absolute effect:** +0.22 pp
- **Relative effect:** +5.2%
- **95% CI on absolute effect:** [-0.30 pp, +0.74 pp]
- **p-value:** 0.41
- **Practically significant?** No — well below the 0.5pp MDE

---

## Secondary + Segment + Novelty

### Secondary metrics

| Metric | A | B | Effect | CI | Notes |
|--------|---|---|--------|----|-------|
| Cart-abandon rate | 31.4% | 30.8% | -0.6pp | [-1.4, +0.2] | Directional, not significant |
| AOV (AUD) | $87.20 | $86.40 | -$0.80 | [-$4.10, +$2.50] | Noise |
| Time-on-checkout | 122s | 119s | -3s | [-8s, +2s] | Noise |

### Pre-registered segments

| Segment | A | B | Effect | CI | Notes |
|---------|---|---|--------|----|-------|
| Mobile | 3.91% | 4.18% | +0.27pp | [-0.30, +0.84] | Directional |
| Desktop | 4.62% | 4.78% | +0.16pp | [-0.40, +0.72] | Noise |
| Returning | 5.30% | 5.41% | +0.11pp | [-0.50, +0.72] | Noise |
| New | 3.18% | 3.45% | +0.27pp | [-0.30, +0.84] | Directional |

### Novelty / primacy

Days 1–7 effect: +0.31pp
Days 8–14 effect: +0.13pp
**Pattern:** Declining — consistent with novelty effect on UI colour change

---

## Guardrails

| Metric | A | B | Status |
|--------|---|---|--------|
| 7-day refund rate | 1.8% | 1.8% | 🟢 |
| CS ticket volume / 1k orders | 14 | 13 | 🟢 |
| Page-load p95 (ms) | 1,820 | 1,825 | 🟢 |

---

## Decision (Matrix Applied)

**Outcome:** Effect = +0.22pp (below 0.5pp MDE; CI includes zero)
**Matrix says:** Don't ship; consider follow-up experiment.

**Recommended action:** Hold green colour. Direction suggests amber may be slightly better, but effect is not detectable at our traffic level + 14 days. Don't ship a 5% relative improvement that we can't measure with confidence — we'd be running an effectively-random change.

---

## Stats Reviewer — Independent Review

### Verdict: Approve (analysis is correct)

### Critical issues

None. SRM passes, CI is reported, decision matrix applied as pre-registered.

### Important caveats

1. **Novelty effect is visible** (Days 1–7 vs 8–14 split shows decline). This is the most informative finding — UI colour changes typically wash out. Don't rerun the same test.
2. **Mobile vs desktop split is interesting** — mobile shows directional lift, desktop is noise. Worth probing in a follow-up that isolates mobile.
3. **Power was set for 0.5pp MDE** — we couldn't have detected anything smaller anyway. This is a "test concluded" not a "treatment doesn't work" outcome.

### Optional improvements

For the follow-up: consider testing button copy ("Place order" vs "Pay $X now" vs "Confirm and pay"). Copy changes often have larger and longer-lived effects than colour.

### What I checked

SRM ✓; CI > p-value reporting ✓; pre-registration adherence ✓; novelty surfaced ✓; segment effects reported ✓; decision matrix applied verbatim ✓.

---

## Follow-Up Experiments

1. **Mobile-only button copy test:** "Place order" vs "Pay $X now" vs "Confirm and pay" — segments show mobile may be most sensitive
2. **Checkout flow audit before next colour test** — likely larger gains come from reducing form fields or adding express-pay options than from colour
3. **Mid-funnel attribution check** — drop-off from cart → checkout is 31.4%; that's where the bigger opportunity is than the green-button conversion
