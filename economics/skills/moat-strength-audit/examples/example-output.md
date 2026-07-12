# Moat Strength Audit — Stylised AU vertical SaaS (project mgmt for trades)

**Date:** 20/05/2026
**Stated moat thesis:** "Network effects from trade-to-client invitations + switching costs from job history."

---

## Business Snapshot

| Field | Value |
|-------|-------|
| Age | 4 years |
| Scale | ~$2.1M ARR, ~1,650 active customers |
| Market position | 4th in AU vertical SaaS for trades (after Tradify, ServiceM8, AroFlo); ~2% segment share |
| Industry growth | ~15% per year |

---

## 7 Powers Scoring

| Moat | Score (0–10) | Evidence | Comparable |
|------|--------------|----------|-----------|
| **Scale economies** | 2 | Cloud SaaS — most cost categories are roughly fixed at our scale; little cost advantage from being 4×–10× our size in our segment. Marginal cost to serve scales with seats. | Stripe (10) — true scale on payments infra; Xero (7) — meaningful but not dominant per-customer cost advantage |
| **Network effects** | 3 | Trade-to-client invitations create *some* lock-in (clients see "this trade uses ProductX"). But clients aren't users; they don't pay; they don't multiply. The "network" is one-sided. Tradies don't depend on each other on the platform. | Etsy / DoorDash (8) — two-sided proper; Quickbooks Online (5) — accountant-firm channel is a partial network |
| **Counter-positioning** | 2 | Established competitors could match our feature set in 6–9 months. No structural reason they can't. | Costco vs Walmart — Walmart can't replicate Costco's no-marketing model |
| **Switching costs** | 5 | Job history, quotes, customer database all live in-system. Migration tools don't exist between AU vertical-trades SaaS. Average customer has 18+ months of data after year 1. | Slack (8) — high cost; SaaS HR products (4) — moderate; raw spreadsheet (1) — none |
| **Branding** | 2 | Tradies recognise us; brand sentiment positive but not premium-pricing-strong. Customers wouldn't pay 20%+ for our name. | Apple (10); Bunnings (7 in AU); xero (6 — strong AU brand) |
| **Cornered resource** | 1 | Team is good but not unreplicable; no exclusive contracts; no proprietary IP that competitors can't reverse engineer. | Disney (10 — IP); LVMH (9 — brand portfolio) |
| **Process power** | 3 | Customer-support quality is genuinely better than ServiceM8 at our scale, but this is replicable by a competent operator with 18 months and the right hires. | Toyota Production System (10); In-N-Out (8) |
| **Total** | **18/70** | | |

---

## Decay-Rate Forecast

| Moat | Today | Year 1 | Year 3 | Year 5 | Decay driver |
|------|-------|--------|--------|--------|--------------|
| Switching costs | 5 | 5 | 4 | 3 | Industry standards + CDR-style data portability mandates; migration tools commoditise |
| Network effects | 3 | 3 | 3 | 2 | Single-sided network is fragile; doesn't compound with use |
| Process power | 3 | 3 | 2 | 2 | A competent competitor with 18 months hires + product investment can match |
| Branding | 2 | 2 | 3 | 3 | Could strengthen if we invest; weak today |
| Counter-positioning | 2 | 2 | 2 | 2 | Static; no structural change to counter-position |
| Scale economies | 2 | 2 | 3 | 3 | Slowly improves with growth, but capped by SaaS economics |
| Cornered resource | 1 | 1 | 2 | 2 | If we accumulate trade-specific data + workflows nobody else has, could rise |

Total: 18 → 18 → 19 → 17. Roughly flat with a slight decline.

---

## Erosion Threats (per moat with score ≥ 5)

| Moat | Specific erosion event | Likelihood (5y) | Severity |
|------|----------------------|----------------|----------|
| Switching costs | Government mandates data portability for SMB SaaS (CDR-style); migration tools become commodity | Medium | High — would compress switching costs to 2/10 |
| Switching costs | A migration tool startup raises serious VC + builds importer for top 3 competitors | Medium-high | High |

---

## Investment Leverage

| Moat | Action to strengthen | Approximate cost (AUD) | Expected score lift |
|------|--------------------|-----------------------|-----------------------|
| Network effects | Build client-paying side (clients pay $X for premium account; tradies invite them) → two-sided | $400k + 12 months | 3 → 5 |
| Switching costs | Deep workflow integrations + AI features that require historical data → leave = lose AI | $250k + 6 months | 5 → 6 |
| Cornered resource | Exclusive data partnership with a trade-supply distributor (e.g. Reece, Bunnings Trade) | $500k + 18 months | 1 → 4 |
| Process power | Build trades-specific support + product-led growth motion no one else has | $300k/yr ongoing | 3 → 5 over 24 months |

Best single bet: **Network effects → two-sided** (cheapest leverage; transforms the structural moat).

---

## Red Team — Where this analysis is wrong

### Too optimistic

1. **"Switching costs at 5/10"** — overstates. AU SMB trades are 9% of customers per year leaving for any reason (death, sale, retirement). Half of those won't bother migrating data because they're closing the business. The "real" switching cost is for the 4% who actively migrate to a competitor — and ServiceM8 already imports our CSV exports manually within 4 hours. Score should be 3.
2. **"Cornered resource at 1/10"** — barely defensible; nothing we have is exclusive. Even if you accept "team is good", another VC-funded startup could pay 2× and rebuild in 12 months.
3. **"18/70 = moderate"** — score is meaningless as a sum. 18/70 is **weak** in absolute terms; market-leading SaaS in defensible categories scores 35–45. Comparable Xero scores ~38.

### Counter-moves the analysis doesn't account for

1. **ServiceM8 + AroFlo merge** → 3rd-and-4th player consolidate; we become a footnote with no moat
2. **Tradify (US-owned, well-funded) doubles AU investment** → outspends us on feature parity within 18 months; brand follows
3. **A general accounting product (Xero, MYOB) adds trade-specific workflows** → trades default to existing accounting tool; our 18 months of data becomes irrelevant if the new entrant ports it for free

### Disconfirmers — if we observed any of these in 12 months, the analysis is wrong

1. Three competitors release CSV import from our format in same quarter (probability ~30%) → switching costs effectively zero
2. ServiceM8 announces AU-specific TLC for their AU customer base + drops price 20% → our brand 2 → 1
3. Government CDR consultation includes SMB SaaS specifically (probability ~25% in 24 months) → switching cost cliff in 36–48 months

### Time-horizon risks

- **Year 1:** Flat moat score; small attrition possible
- **Year 3:** Either we've invested in network-effects pivot (and it's working) or we're absorbed
- **Year 5:** Probable outcomes: (a) acquired at modest multiple (b) flat in niche (c) closed; the "we win on moats" story has fragile evidence today

### The base case I'd hold the operator to

"We are a 4th-place player in a market dominated by Xero (60% in adjacent category) and three trade-specific competitors of our scale. Our actual moat score is ~14/70 (after pricing-in the switching-cost overstatement), which is in the bottom quartile of B2B SaaS. Without a category-defining investment (network effects via two-sided product, or cornered resource via exclusive partnership), our 5-year outcome is either a modest acquisition or slow decline. Calling our current position a 'moat' is generous. Calling it 'flat' is honest."

---

## Overall Moat Score + Recommendation

**Overall:** 18/70 (or 14/70 after red-team adjustment) = **Weak**

**Recommendation:** Treat the current position as undefensible. Pick one of three strategic bets in the next 12 months: (a) two-sided network effects via paying-client tier, (b) exclusive trade-supply partnership for a cornered-resource moat, or (c) accept that the company is most likely an acquisition target and optimise the financial story for that outcome. Maintaining the status quo predicts a slow-decline 5-year outcome with ~70% confidence.
