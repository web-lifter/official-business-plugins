# Competitive Dynamics — AU SMB Accounting Software (cloud, < $500/mo plans)

**Date:** 20/05/2026
**Time horizon:** 24 months
**Our position:** Challenger (~2% market share, 4 years old)

---

## Market Definition

- **Narrow scope:** Cloud-based accounting SaaS for AU SMBs (< 100 employees) at < $500/mo per business
- **Excluded:** Mid-market & enterprise (Workday, NetSuite); accounting-firm-facing tools (CAS360, Karbon); single-purpose tools (invoicing-only, payroll-only)
- **Buyers:** Sole-trader (60% of count, 15% of revenue), micro (10 FTE) (30%, 45%), small (10–100 FTE) (10%, 40%)
- **Substitutes:** Spreadsheets; bookkeeping outsourcing; QuickBooks Self-Employed (lower-end); accounting firms with their own portals

---

## 5 Forces

| Force | Score (1–5) | Evidence |
|-------|------------|----------|
| Rivalry among existing | 5 | Xero (~60% AU share), MYOB (~25%), Reckon (~7%), QuickBooks Online (~3%), others (~5%). Aggressive feature competition + bundled banking/payments. Price-war episodes 2023, 2025. |
| Threat of new entrants | 2 | High switching cost + accounting-firm certification ecosystem makes entry hard. Wave + Sage tried AU; both pulled back. |
| Bargaining power of buyers | 3 | Sole-traders have low individual power but high churn elasticity. Small biz (3–100 FTE) heavily influenced by their accountant — accountant has significant indirect buyer power. |
| Bargaining power of suppliers | 3 | Bank-feed APIs (Yodlee, ASIC Open Banking) commoditising; ATO STP requirements set by gov; payroll-tax rules state-set. AWS/cloud is commodity. Suppliers limited but key. |
| Threat of substitutes | 3 | Spreadsheets persistent at sole-trader end (free, familiar). Bookkeeping-outsourcing growing as a hybrid model. AI bookkeeping startups emerging but immature. |
| **Sum** | **16/25** | Tough — heavy rivalry + accountant gatekeeper |

---

## Equilibrium Prediction (24 months)

- **Predicted dynamic:** Dominant-firm with fringe — Xero remains dominant, MYOB defends mid-market with feature parity, Reckon + QBO + smaller players compete for the 10% remaining
- **Players consolidating:** QuickBooks Online may acquire a smaller AU player to accelerate share; one of the smaller players will exit or be acquired in the 24-month window
- **Players exiting:** At least 1 of the bottom 3 ranked by funding will exit AU market
- **Our trajectory:** Without category re-definition (e.g. accounting + something else), our 2% share grows to 3–4% — surviving but not winning
- **Confidence:** Medium-high; the dominant-firm pattern is stable

---

## Response-Game Tree

### If we move first — cut price 25% to attack the bottom tier

| Our move | Likely competitor response | Our counter | Equilibrium |
|----------|---------------------------|-------------|-------------|
| Cut Starter price by 25% | Xero matches within 6 weeks (they have deep pockets); MYOB doesn't match (worse margins) | We hold price; ride out the 6 months of pain | New floor; both Xero and us at lower margin; long-term loss |

### If a competitor moves first — Xero adds embedded payroll free

| Their move | Our response | Their counter | Equilibrium |
|-----------|-------------|--------------|-------------|
| Xero embeds payroll free | We can't match (payroll is 35% of revenue) | Xero waits 6 months, then drops core SaaS price | We squeezed; partnership/integrate-with-Xero strategy becomes more attractive |

**Nash equilibrium:** Neither side can profitably move first without significant strategic positioning. The stable game is feature competition + bundling, not pure price.

---

## Exit / Consolidation Scenarios

| Player | Likelihood of exit | M&A target? | Effect on us |
|--------|-------------------|-------------|--------------|
| Xero | Very low | No (acquirer) | Continues dominance; pressure on margin remains |
| MYOB | Low | Possible (PE-owned, may flip) | If acquired by international, scale advantage shifts |
| Reckon | Medium | Yes (long-tail; may be acquired by QBO or smaller player) | Their exit consolidates share to Xero |
| QBO | Medium (could pull AU) | No | If they exit AU, ~3% share redistributes — small bump for us |
| Us | Medium-low | Possible exit target | Pressure to find category-defining angle within 24 months or be acquired |

---

## Red Team — Where this analysis is wrong

### Too optimistic

1. **"Our trajectory: 3-4% share growth without category re-definition"** — this assumes our current product trajectory continues with no major disruption. But Xero has signaled embedded AI bookkeeping at their 2026 AGM. If they ship it H2 2026, the value-prop for AI-bookkeeping startups (and us if we're not on it) collapses. Realistic downside: flat 2% or decline.

2. **"Sum of 5 Forces = 16/25"** — this number is unhelpful; the *composition* matters. Rivalry of 5 + supplier power 3 means the bottom-line squeeze is structural, not cyclical.

### Counter-moves the analysis doesn't account for

1. **Open Banking maturation** — by 2027, AU CDR (Consumer Data Right) accounting reads/writes become standard. A startup with a strong CDR-native architecture could leapfrog Xero's legacy bank-feed approach. Our analysis doesn't model this.
2. **Accountant-owned product** — large accounting firms (Big 4) building their own SMB portal. Direct disintermediation risk.
3. **AI bookkeeping startups (Receipt-Bank-style)** — if one (e.g. Dext, Hubdoc) shifts upstream to full-stack accounting, their data-density advantage on receipts could be a wedge.

### Disconfirmers — if we observed any of these in 12 months, the analysis is wrong

1. Xero growth rate drops below 8% — equilibrium not as stable as claimed
2. A new entrant raises > $30M USD specifically for AU SMB accounting — entry barriers lower than scored
3. Two or more accounting firms launch their own product — buyer-power score should jump
4. AI bookkeeping captures > 5% of net-new SMB starts — substitute threat under-scored

### Time-horizon risks

- **Year 1:** Dominant-firm equilibrium holds; we navigate steady state
- **Year 3:** AI bookkeeping is real or rejected — pivotal evidence
- **Year 5:** Either category re-defines (AI-native) or we're an acquisition target

### The base case I'd hold the operator to

"We are a sub-scale challenger in a structurally tough market. Without a category-defining move in 12–18 months (AI-bookkeeping wedge, vertical specialisation, or accountant-channel partnership), our most likely 36-month outcome is a financial-exit acquisition (low multiple) or slow decline. The 5 Forces sum of 16 understates the structural squeeze from Xero's dominant-firm position. Two-thirds of analysts should bet on continued share concentration, not fragmentation."

---

## Strategic Implications

1. **Pure price/feature competition is unwinnable.** Don't fight Xero on their game.
2. **Wedge opportunities exist** — vertical SaaS (trades + accounting), accountant-channel partnership (B2B2C via firms), or AI-bookkeeping integration. Pick one within 12 months.
3. **Acquisition is a realistic exit** in 24–36 months at modest multiples; if that's not desired, the wedge must work.
4. **Watch the AI-bookkeeping space monthly** — the equilibrium prediction is most vulnerable here.
5. **Open Banking / CDR architecture should be a strategic priority** regardless of wedge choice.
