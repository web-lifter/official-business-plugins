# Pricing Strategy — ClearLedger: Cloud Accounting for Australian Trades Businesses

**Date:** 15/05/2026
**Product type:** SaaS
**Goal:** Transition from flat $50/month pricing to a three-tier model; validate before rollout
**Prepared by:** Pricing Strategy Analyser skill

---

## Strategy Memo

**Recommended pricing model:** Value-based tiered pricing (primary) with annual discount incentive (secondary)

**Rationale:** ClearLedger's current flat $50/month pricing leaves significant revenue on the table: the business serves sole traders (who use 2–3 features) and growing trades businesses with 3–5 staff (who use invoicing, job costing, payroll integration, and BAS lodgement). A single price either overcharges the sole trader (causing churn) or undercharges the multi-staff business (destroying margin opportunity). A three-tier model allows ClearLedger to capture higher willingness-to-pay from established businesses while maintaining an accessible entry point that serves as a top-of-funnel growth engine.

Van Westendorp PSM interviews with 31 customers (April 2026) confirm that sole traders have an Optimal Price Point of $39/month, while multi-staff businesses have an OPP of $89/month — a 2.3× spread that a single price cannot bridge. The competitive context supports this: Xero starts at $32/month for sole traders and $85/month for mid-tier; MYOB ranges from $27–$99/month. ClearLedger's job-costing and BAS automation differentiates it from both at the professional tier.

**Key assumptions:**
- Annual plan uptake of 35% of new subscribers (consistent with industry averages at 17–20% discount).
- Churn impact of new pricing ≤ 4% on existing flat-rate customers (grandfathered for 6 months).
- Average gross margin at COGS = $8/month/account (hosting, support allocation).

---

## Van Westendorp Ranges (by segment)

| Segment | Too Cheap (PMC) | Optimal (OPP) | Upper Bound (PME) | Current Price | Gap |
|---------|----------------|--------------|------------------|--------------|-----|
| Sole trader (1 person) | $19 | $39 | $55 | $50 | Overpriced by ~$11/month for this segment |
| Small trades (2–5 staff) | $45 | $89 | $129 | $50 | Underpriced by ~$39/month for this segment |
| Growing trades (6–15 staff) | $79 [est] | $149 [est] | $219 [est] | $50 | Underpriced by ~$99/month |

> Values for "Growing trades" are `[est]` — this segment was under-represented in April 2026 interviews (n=4). Recommend a follow-up survey of 15 customers in this band before launching the Professional Plus tier.

---

## Pricing Tiers

| Tier | Price (AUD/mo) | Annual (AUD/yr) | Target Persona | Key Value Drivers | Boundary Conditions | Gross Margin |
|------|--------------|----------------|---------------|------------------|--------------------|-|
| **Starter** | $39 | $389 | Sole trader / contractor — one-person operation, minimal complexity | Invoicing, expense tracking, BAS lodgement, mobile app | Upgrade when adding first employee or needing job costing | 79% |
| **Professional** | $89 | $889 | Small trades business — 2–5 staff, recurring jobs, payroll | Starter + job costing, payroll integration (Xero Payroll or Employment Hero), client portal, priority support | Upgrade when staff > 5 or needing multi-site | 91% |
| **Professional Plus** | $179 | $1,790 | Growing trades — 6–15 staff, multiple project types, complex reporting | Professional + multi-site dashboard, custom reporting, dedicated account manager, API access | Enterprise quote when staff > 15 | 96% |

**Hero tier:** Professional ($89/month) — designed as the obvious default for any business with staff
**Anchor tier:** Professional Plus ($179/month) — makes Professional feel very reasonable
**Annual discount:** 17% ("2 months free" framing — $889/year vs $1,068/year for Starter; $889 vs $1,068 → actually use $889 = ~17% off)

---

## Sensitivity Analysis

| Scenario | Monthly Price (avg blended) | Expected Monthly Volume | Expected MRR | Gross Margin | Notes |
|----------|-------------|------------------------|-------------|-------------|-------|
| Current (flat $50) | $50 | 1,240 accounts | $62,000 | 84% | Baseline — no tier differentiation |
| Proposed — base case | $74 blended | 1,240 accounts (flat assumption) | $91,760 | 89% | 35% on Starter, 50% Professional, 15% Prof Plus |
| Proposed — downside (2× churn on existing) | $74 blended | 1,140 accounts (-8% from churn) | $84,360 | 89% | If existing flat-rate customers churn at 8% |
| PSM floor (Starter only) | $39 | High conversion | Below cost-efficient | 79% | Loss-leader if all customers choose Starter |
| PSM ceiling (Pro Plus push) | $179 | Low conversion from current base | Uncertain | 96% | Requires segment to be proven first |

**Break-even additional churn:** 32% — at this rate, the blended price increase is revenue-neutral. This is far beyond any realistic scenario (2× downside case is 8%).
**Recommended guard-rail:** Revert Starter pricing to $45 (split-test fallback) if net MRR growth is flat or negative in the first 60 days post-launch.

---

## Test Plan

| # | Test type | Hypothesis | Success metric | Sample / Duration | Kill criterion |
|---|-----------|-----------|---------------|------------------|----------------|
| 1 | Soft launch (new customers only) | If new customers are offered the three-tier model from 01/06/2026, blended ARPU will increase from $50 to ≥ $68 within 60 days with ≤ 5% conversion rate reduction | Blended ARPU ≥ $68, conversion rate ≥ 90% of baseline | All new signups from 01/06/2026 — expect ~120 in 60 days | If ARPU < $60 or conversion drops > 15%, revert to two-tier model |
| 2 | Customer survey (existing accounts) | If we conduct a Van Westendorp survey with the 6–15 staff segment (n ≥ 30), the OPP will fall within $120–$180/month, validating the Professional Plus price point | OPP within $120–$180 for ≥ 60% of this segment | 30 existing accounts with 6–15 staff; 4-week survey window | If OPP < $100, reprice Professional Plus to $139 before existing-customer rollout |

**Grandfathering strategy:** All 1,240 existing flat-rate customers ($50/month) are grandfathered for 6 months (to 01/12/2026). At 01/11/2026 they receive notification of migration to the closest new tier with a 15% loyalty discount for the first 12 months on annual plan. No customer moves to a higher price without an explicit upgrade trigger (e.g. adding an employee).

**Customer communication timeline:**
- 01/06/2026: New pricing live for new customers (no announcement to existing)
- 01/11/2026: Email to existing customers — "We're updating our plans. Here's what changes for you."
- 01/12/2026: Existing customers migrate to new tiers. Loyalty discount applied automatically in Stripe.

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Sole traders churn when Starter increases from $50 to $39 (price perception) | Low — $39 is actually lower, but perception risk if current customers feel "repackaged" | Medium | Communicate $39 as a price reduction for sole traders; frame as "a plan designed for you" |
| Competitors respond by cutting price to undercut new Starter tier | Medium — Xero and MYOB have responded to price changes before | Medium | Professional tier is differentiated by job-costing + BAS automation — features Xero Basic does not include; maintain this moat |
| Professional Plus segment is too small to validate within 60 days | Medium — n=4 in initial PSM | Low — does not block Starter or Professional launch | Proceed with Starter and Professional; treat Professional Plus as a Q3 2026 launch after follow-up survey completes |

---

## Next Steps

| # | Action | Owner | By |
|---|--------|-------|-----|
| 1 | Configure three-tier pricing in Stripe (Starter $39, Professional $89, Professional Plus $179) with annual plan SKUs | Head of Engineering | 28/05/2026 |
| 2 | Update public pricing page and in-app upgrade flow for new customers | Head of Product | 28/05/2026 |
| 3 | Recruit 30 existing 6–15 staff accounts for Van Westendorp follow-up survey (Typeform + $30 gift card incentive) | Head of CX | 01/06/2026 |
| 4 | Draft existing-customer migration email (legal review required for terms-of-service update) | Head of Marketing + Legal | 01/11/2026 |
