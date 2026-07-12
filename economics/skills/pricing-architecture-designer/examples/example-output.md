# Pricing Architecture — AU B2B SaaS (project-management for trades)

**Date:** 20/05/2026

---

## Pricing Model Selected

**Model:** Tiered with usage-based add-ons (hybrid)
**Why:** SaaS product with clear seat-count + job-count differentiation. Customers segment naturally by team size (sole-trader → 2–5 → 5+ tradespeople). Pure usage-based was rejected because customers want predictable bills. Pure tiered without usage adds rigidity around high-volume teams.

---

## Tier Architecture

| Tier | Price (AUD/mo) | Target segment | Capture % (expected) | Fence (key restrictor) | Anchor |
|------|---------------|---------------|---------------------|----------------------|--------|
| Sole Trader | $39 | Single tradesperson | 30% | 1 user; 25 jobs/mo | — |
| Crew (target) | $89 | Team 2–10 | 55% | 10 users; 100 jobs/mo; custom forms | Centred between $39 and $189 — feels balanced; double user count and 4× job ceiling vs Sole Trader |
| Operator | $189 | Team 10+ / multi-site | 15% | Unlimited users + jobs; SSO; API; priority support | — |

**Usage add-ons:** Extra users at $9/user/mo (Crew), $7/user/mo (Operator). Extra jobs at $0.50/job (Sole Trader), $0.30/job (Crew). API calls at $0.001 over 10k/mo (Operator only).

---

## Revenue Projection (3 Scenarios)

| Scenario | Avg ARPU (AUD/mo) | Retention impact | New ARR | Δ vs current |
|----------|------------------|-----------------|---------|--------------|
| Conservative | $96 | +2pp churn | $1.96M | -8% (current $2.13M) |
| Base | $108 | ±0% | $2.39M | +12% |
| Aggressive | $124 | -1pp churn | $2.76M | +30% |

**Assumptions:**
- Current customers: ~1,650 active
- Current avg ARPU: $108 (mixed legacy + recent pricing)
- 12-month projection assumes 8% net new customer growth + price-driven ARPU change
- Conservative assumes 2pp churn increase on price change; Aggressive assumes Crew tier wins more upgrades than expected

---

## Migration Plan

| Cohort | Treatment | Communication | Discount |
|--------|-----------|--------------|----------|
| Existing customers (Sole Trader equivalent on old plan) | Grandfather 12 months | 8-week heads-up email + 2-week reminder | None |
| Existing customers (Crew equivalent on old plan) | Grandfather 6 months, then auto-migrate to new Crew | 12-week heads-up + sales call for top 50 accounts | 20% off Crew Year 1 if upgrade in heads-up window |
| At-risk accounts (NPS < 6 or >$2k MRR) | 1:1 call from founder/CSM | Personal | Bespoke (up to 25% Year 1) |
| New customers | New prices day 1 | New pricing page + onboarding | — |

---

## 90-Day Monitoring Plan

| Metric | Threshold | Action if breached |
|--------|-----------|--------------------|
| Churn (existing customers) | +2pp vs baseline (which is 3%) | Pause migrations; review messaging |
| New-customer conversion | -10% vs baseline (which is 8.5%) | A/B test middle-tier anchor; revisit Crew price |
| Sales cycle length (Operator tier) | +15% (now 14 days median) | Sales team coaching; review value-proof in deck |
| NPS post-change | Drop > 5 points | Targeted survey; surface qualitative themes |
| Tier mix (Crew %) | Falls below 40% | Anchor not working; adjust pricing of Good or Best |

---

## Suggested A/B Tests

1. **Anchor strength test:** Crew at $89 (current) vs $99 vs $79 — find the WTP-conversion sweet spot
2. **Annual discount strategy:** 10% vs 20% annual discount on all tiers — measure conversion lift to annual
3. **Free trial vs freemium for Sole Trader:** 14-day trial (current) vs limited-forever-free (50 jobs/lifetime) — measure paid conversion at 90 days

Run these via `[[ab-test-designer]]`; design first, peer-review with stats-reviewer agent.
