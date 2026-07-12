# Break-Even Scenario Modeller — Reference Material

## CVP (Cost-Volume-Profit) Formulas

### Basic break-even (units)

```
BE_units = Fixed_costs / Contribution_margin_per_unit
```

Where Contribution_margin_per_unit = Price − Variable_cost_per_unit.

### Break-even in AUD

```
BE_revenue = BE_units × Price
```

Or equivalently:

```
BE_revenue = Fixed_costs / Contribution_margin_ratio
```

Where CM_ratio = CM_per_unit / Price.

### Target-profit volume

```
Target_units = (Fixed_costs + Target_profit) / Contribution_margin_per_unit
```

### Margin of safety

```
MoS = (Actual_revenue − BE_revenue) / Actual_revenue
```

A MoS < 20% is fragile; > 30% is comfortable.

---

## Scenario-Bundle Library

### Best / Base / Worst / Black-Swan

| Scenario | Typical assumptions |
|----------|--------------------|
| **Best** | All known opportunities realised — better COGS, +10% pricing, no churn shock |
| **Base** | Current trajectory continues; modest improvements at known levers |
| **Worst** | Two adverse shocks compounding — competitor entry + cost increase + churn rise |
| **Black swan** | Existential shock — supplier collapse, regulatory ban, market evaporation |

Don't model only "best vs worst" — base case is what investors and operators actually plan from.

### Multi-product scenarios

For multi-product businesses, model:
- **Mix-shift** scenarios (current → 70% premium product → 50%)
- Weighted contribution margin
- Per-product break-even (lowest-margin product = priority to fix)

### Subscription / SaaS scenarios

- **Steady-state** (no growth) — what does monthly profit look like?
- **Growth + investment** — burn rate vs ARR growth
- **Churn shock** — what if monthly churn goes from 2% to 4%?

---

## Cost-Structure Linkages

This skill consumes outputs from `[[cost-structure-builder]]`:

- Fixed cost per month
- Variable cost per unit
- Step-fixed thresholds + magnitudes
- Volume at which step costs trigger

Always check that the modelled break-even volume sits in the right step-fixed bucket. If it crosses a threshold, the answer is **non-monotonic** — break-even can occur on either side of a step.

---

## Common Pitfalls

1. **Single-point break-even** — useless without sensitivity
2. **Ignoring step-fixed costs** — break-even can be 20% off if you treat them as fully variable
3. **No connection to runway** — break-even at month 24 with 6 months of runway is not a plan
4. **Including unattainable scenarios in headline** — "we break even at 50,000 units" when current is 2,800 is not motivating
5. **Cost-of-goods static assumption** — at higher volume, you get rebates; model this
6. **Pricing fixed in sensitivity** — if pricing power is the answer, surface it
7. **Marketing as fixed when it's variable** — most performance marketing scales with growth ambition

---

## When to Reach for Other Skills

- Break-even shows pricing is the lever → `[[pricing-architecture-designer]]`
- Break-even shows cost is the issue → `[[cost-structure-builder]]` deep-dive
- Break-even shows you need more volume → `[[revenue-channel-mapper]]` (smb/business-operations)
- Break-even shows unit economics are upside-down → `[[unit-economics-calculator]]`
- Break-even tied to a single experiment → `[[ab-test-designer]]`
