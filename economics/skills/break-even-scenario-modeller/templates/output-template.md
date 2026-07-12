# Break-Even Analysis — {{business_name}}

**Date:** {{date_dd_mm_yyyy}}

---

## Inputs Snapshot

| Field | Base | Best | Worst |
|-------|------|------|-------|
| Price per unit (AUD) | ${{n}} | ${{n}} | ${{n}} |
| Variable cost per unit | ${{n}} | ${{n}} | ${{n}} |
| Contribution margin per unit | ${{n}} | ${{n}} | ${{n}} |
| Contribution margin ratio | {{n}}% | {{n}}% | {{n}}% |
| Fixed cost monthly | ${{n}} | ${{n}} | ${{n}} |
| Step-fixed thresholds | {{list}} | | |

---

## Break-Even per Scenario

| Scenario | Break-even units/mo | Break-even AUD/mo | Months to BE at current growth |
|----------|---------------------|--------------------|-------------------------------|
| Best | {{n}} | ${{n}} | {{n}} |
| Base | {{n}} | ${{n}} | {{n}} |
| Worst | {{n}} | ${{n}} | {{n}} |
| Black swan | {{n}} | ${{n}} | {{n}} |

---

## Sensitivity (Break-Even Units per Month)

| Price × Cost | Cost -10% | Cost 0% | Cost +10% |
|-------------|-----------|---------|-----------|
| Price -10% | {{n}} | {{n}} | {{n}} |
| Price 0% | {{n}} | {{n}} | {{n}} |
| Price +10% | {{n}} | {{n}} | {{n}} |

---

## Runway Impact

| Scenario | Months to BE | Cash on hand (AUD) | Monthly burn | Runway months | Bridge needed? |
|----------|--------------|-------------------|--------------|--------------|----------------|
| Best | {{n}} | ${{n}} | ${{n}} | {{n}} | {{y/n}} |
| Base | {{n}} | ${{n}} | ${{n}} | {{n}} | {{y/n}} |
| Worst | {{n}} | ${{n}} | ${{n}} | {{n}} | {{y/n}} |

---

## CVP Graph Spec

For the BI tool / spreadsheet:

- X-axis: monthly volume (units), range 0 → {{2× current volume}}
- Y-axis: AUD per month
- Line 1: Revenue = Price × volume
- Line 2: Total cost = Fixed + (Variable × volume) + Step-fixed (with vertical jumps at thresholds)
- Mark: Break-even intersection
- Mark: Step-fixed jump points
- Optional: Target-profit horizontal line (revenue - target profit = total cost)

---

## Recommendations

1. {{rec_1}}
2. {{rec_2}}
3. {{rec_3}}
