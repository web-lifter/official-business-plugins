# Pricing Architecture — {{product_name}}

**Date:** {{date_dd_mm_yyyy}}

---

## Pricing Model Selected

**Model:** {{tiered / usage / freemium / value / outcome / hybrid}}
**Why:** {{rationale}}

---

## Tier Architecture

| Tier | Price (AUD/mo) | Target segment | Capture % | Fence (key restrictor) | Anchor |
|------|---------------|---------------|-----------|----------------------|--------|
| Good | ${{n}} | {{seg}} | {{n}}% | {{fence}} | — |
| Better (target) | ${{n}} | {{seg}} | {{n}}% | {{fence}} | Anchored between Good + Best |
| Best | ${{n}} | {{seg}} | {{n}}% | {{fence}} | — |

---

## Revenue Projection (3 Scenarios)

| Scenario | Avg ARPU | Retention impact | New ARR | Δ vs current |
|----------|----------|-----------------|---------|--------------|
| Conservative | ${{n}} | -{{n}}% churn ↑ | ${{n}} | {{Δ}} |
| Base | ${{n}} | ±0% | ${{n}}M | {{Δ}} |
| Aggressive | ${{n}} | +{{n}}% churn ↓ | ${{n}}M | {{Δ}} |

---

## Migration Plan

| Cohort | Treatment | Communication | Discount |
|--------|-----------|--------------|----------|
| Existing customers | Grandfather 12 months | 8-week heads-up email + in-app | None |
| At-risk accounts | Annual discount option | 1:1 outreach | 15% annual lock |
| New customers | New prices day 1 | New pricing page | — |

---

## 90-Day Monitoring Plan

| Metric | Threshold | Action if breached |
|--------|-----------|--------------------|
| Churn (existing) | +2pp vs baseline | Pause; review messaging |
| Conversion (new) | -10% vs baseline | Test middle-tier anchor |
| Sales cycle length | +15% | Coach sellers on framing |
| NPS post-change | Drop > 5 | Survey explicitly |

---

## Suggested A/B Tests

1. **Anchor test:** Better tier $X vs $X+20% vs $X+40% (3-arm) — find optimal anchor
2. **Discount strategy:** annual 10% vs 20% vs none — measure conversion lift
3. **Fence salience:** prominent vs subtle differences — does capture % shift?
