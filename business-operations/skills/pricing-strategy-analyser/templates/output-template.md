# Pricing Strategy — {{business_name}}: {{product_name}}

**Date:** {{date_dd_mm_yyyy}}
**Product type:** {{product_type}}
**Goal:** {{pricing_goal}}
**Prepared by:** Pricing Strategy Analyser skill

---

## Strategy Memo

**Recommended pricing model:** {{pricing_model}}

**Rationale:** {{rationale_paragraph}}

**Key assumptions:**
- {{assumption_1}}
- {{assumption_2}}
- {{assumption_3}}

---

## Van Westendorp Ranges (by segment)

| Segment | Too Cheap (PMC) | Optimal (OPP) | Upper Bound (PME) | Current Price | Gap |
|---------|----------------|--------------|------------------|--------------|-----|
| {{segment_1}} | ${{pmc}} | ${{opp}} | ${{pme}} | ${{current}} | {{gap}} |
| {{segment_2}} | ${{pmc}} | ${{opp}} | ${{pme}} | ${{current}} | {{gap}} |

> PSM values marked `[est]` are estimates from stakeholder interview — no customer survey data available.

---

## Pricing Tiers

| Tier | Price (AUD/mo) | Annual (AUD/yr) | Target Persona | Key Value Drivers | Boundary Conditions | Gross Margin |
|------|--------------|----------------|---------------|------------------|--------------------|-|
| {{tier_1_name}} | ${{mo_price}} | ${{yr_price}} | {{persona}} | {{value_drivers}} | {{boundary}} | {{margin}}% |
| {{tier_2_name}} | ${{mo_price}} | ${{yr_price}} | {{persona}} | {{value_drivers}} | {{boundary}} | {{margin}}% |
| {{tier_3_name}} | ${{mo_price}} | ${{yr_price}} | {{persona}} | {{value_drivers}} | {{boundary}} | {{margin}}% |

**Hero tier:** {{hero_tier_name}} (designed to be the obvious default choice)
**Anchor tier:** {{anchor_tier_name}} (sets price reference; few customers expected here)
**Annual discount:** {{annual_discount}}% ({{annual_discount_framing}})

---

## Sensitivity Analysis

| Scenario | Monthly Price | Expected Monthly Volume | Expected MRR | Gross Margin | Notes |
|----------|-------------|------------------------|-------------|-------------|-------|
| Current | ${{current_price}} | {{volume}} | ${{mrr}} | {{margin}}% | Baseline |
| Proposed (base) | ${{proposed_price}} | {{volume}} | ${{mrr}} | {{margin}}% | {{assumption}} |
| Proposed (downside: 2× churn) | ${{proposed_price}} | {{volume}} | ${{mrr}} | {{margin}}% | Conservative |
| PSM floor | ${{floor_price}} | {{volume}} | ${{mrr}} | {{margin}}% | Too-cheap boundary |
| PSM ceiling | ${{ceiling_price}} | {{volume}} | ${{mrr}} | {{margin}}% | Churn risk boundary |

**Break-even additional churn:** {{breakeven_churn}}% — at this churn rate, the price increase is revenue-neutral.
**Recommended guard-rail:** Revert pricing if net revenue declines in any 30-day window post-launch.

---

## Test Plan

| # | Test type | Hypothesis | Success metric | Sample / Duration | Kill criterion |
|---|-----------|-----------|---------------|------------------|----------------|
| 1 | {{test_type}} | If we {{action}}, then {{metric}} will {{change}} by {{pct}}% | {{kpi}} = {{target}} | {{sample_or_duration}} | {{kill}} |
| 2 | {{test_type}} | If we {{action}}, then {{metric}} will {{change}} by {{pct}}% | {{kpi}} = {{target}} | {{sample_or_duration}} | {{kill}} |

**Grandfathering strategy:** {{grandfathering_policy}}
**Customer communication timeline:** {{communication_timeline}}

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| {{risk_1}} | High / Med / Low | High / Med / Low | {{mitigation_1}} |
| {{risk_2}} | High / Med / Low | High / Med / Low | {{mitigation_2}} |
| {{risk_3}} | High / Med / Low | High / Med / Low | {{mitigation_3}} |

---

## Next Steps

| # | Action | Owner | By |
|---|--------|-------|-----|
| 1 | {{action_1}} | {{role_1}} | {{date_1}} |
| 2 | {{action_2}} | {{role_2}} | {{date_2}} |
| 3 | {{action_3}} | {{role_3}} | {{date_3}} |
