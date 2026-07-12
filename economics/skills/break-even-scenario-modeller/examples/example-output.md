# Break-Even Analysis — Boutique Skincare (DTC, Melbourne)

**Date:** 20/05/2026

---

## Inputs Snapshot

| Field | Base | Best | Worst |
|-------|------|------|-------|
| Price per unit (AUD) | $45 | $49 (+9%) | $42 (-7%) |
| Variable cost per unit | $36 | $32 (volume + COGS) | $38 (shipping squeeze) |
| Contribution margin per unit | $9 | $17 | $4 |
| Contribution margin ratio | 20% | 34.7% | 9.5% |
| Fixed cost monthly | $34,500 | $34,500 | $36,000 (rent uplift) |
| Step-fixed thresholds | 6,000 / 8,500 / 12,000 units/mo | (same) | (same) |

---

## Break-Even per Scenario

| Scenario | Break-even units/mo | Break-even AUD/mo | Months to BE at current growth (+8% MoM) |
|----------|---------------------|--------------------|--------------------------------------|
| Best | 3,500 | $171,500 | 3 months |
| Base | 6,556 (crosses step at 6,000 → effective ~7,150) | $321,750 | 12 months |
| Worst | 14,500 (multiple step-jumps; in practice infeasible at current model) | $609,000 | >24 months — not achievable |
| Black swan (no marketing efficiency, 2× shipping) | infinite (CM ≤ 0) | — | never |

**The base-case shift over the step-fixed threshold at 6,000 is critical** — the moment you need a 4th ops FTE, you jump from CM $9 covering $34,500 to covering $42,700, pushing break-even from 3,833 units to 7,150 units.

---

## Sensitivity (Break-Even Units per Month, Base scenario)

| Price × Cost | Cost -10% | Cost 0% | Cost +10% |
|-------------|-----------|---------|-----------|
| Price -10% | 4,600 | 6,900 | 13,800 |
| Price 0% | 3,833 | 6,556 | 11,500 |
| Price +10% | 3,290 | 5,176 | 8,625 |

Key insight: a **+10% price** with **-10% cost** breaks even at 3,290 units (well below current 2,800; ~17% volume growth away from profitability) — vs the base case of 6,556 units which requires 134% growth. Pricing power is the highest-leverage lever.

---

## Runway Impact

| Scenario | Months to BE | Cash on hand | Monthly burn | Runway months | Bridge needed? |
|----------|--------------|--------------|--------------|--------------|----------------|
| Best | 3 | $180,000 | $20,000 (improving) | 9 | No |
| Base | 12 | $180,000 | $33,800 → declining | 5–9 months | **Yes — bridge likely needed at month 6** |
| Worst | >24 | $180,000 | $50,000+ | 4 | **Critical — need plan now** |

**Critical:** Base-case break-even at month 12 exceeds runway. Bridge financing or operational change required.

---

## CVP Graph Spec

For the BI tool / spreadsheet:

- X-axis: monthly volume (units), range 0 → 12,000
- Y-axis: AUD per month, range 0 → $600,000
- Line 1: Revenue = $45 × volume
- Line 2: Total cost = $34,500 + ($36 × volume) + step-fixed jumps:
  - Jump +$8,200 at volume = 6,000 (adds 4th ops FTE)
  - Jump +$8,200 at volume = 8,500 (adds 5th)
  - Jump +$11,500 at volume = 12,000 (warehouse + rent uplift)
- Mark: Break-even intersection (at base scenario ~6,556 units / ~$295,000 revenue)
- Mark: Step-fixed jump points (vertical step lines on Line 2)

---

## Recommendations

1. **Pricing review is the single highest-leverage action.** Sensitivity shows a 10% price increase moves break-even from 6,556 to 5,176 units — that's 21% closer at zero operational change. Couple with `[[pricing-architecture-designer]]` to design the change properly.
2. **Bridge financing conversation now, not at month 4.** Base-case runway exhausts before break-even. A modest bridge ($100–150k) buys 3 months at base burn; pair with milestone-based release (e.g. half on signing, half on hitting volume KPI).
3. **Worst-case is unsurvivable as currently structured.** If worst-case probability > 25%, fix the cost structure now — reduce 3PL pick-pack dependency, renegotiate COGS, or accept lower marketing intensity (sacrifice growth for margin).
4. **Bring break-even forward of step-jump at 6,000 units.** Reach 5,000 units/mo with operational headcount unchanged — the step-jump at 6,000 is what pushes base-case break-even from 3,833 → 6,556 units. Holding ops headcount at 3 until 6,500 buys 80% of break-even progress at minimum cost.
