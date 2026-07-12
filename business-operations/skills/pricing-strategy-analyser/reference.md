# Pricing Strategy Analyser — Reference Material

## Van Westendorp Price Sensitivity Meter (PSM)

PSM is a market research technique for identifying the acceptable price range and optimal price point from customer survey responses.

### The Four Survey Questions

Ask each target customer:

1. **Too cheap**: "At what price would this product be so cheap that you'd question its quality?"
2. **Cheap**: "At what price would this product seem like a bargain — cheap but worth considering?"
3. **Expensive**: "At what price would this start to feel expensive, though you'd still consider it?"
4. **Too expensive**: "At what price would this be so expensive you would definitely not buy it?"

### Plotting the Curves

Plot cumulative frequency distributions for each question:

- **Too cheap** (TC): % of respondents saying "too cheap" at or above each price — descending
- **Not cheap** (NC): % of respondents NOT saying "cheap" — ascending (inverse of "cheap")
- **Not expensive** (NE): % of respondents NOT saying "expensive" — descending (inverse of "expensive")
- **Too expensive** (TE): % of respondents saying "too expensive" at or above each price — ascending

### Key Intersection Points

| Intersection | Name | Meaning |
|-------------|------|---------|
| TC × TE | Optimal Price Point (OPP) | Maximum revenue — fewest people say "too cheap" or "too expensive" |
| NC × NE | Indifference Price Point (IDP) | Where equal numbers find it cheap vs expensive — market middle |
| TC × NE | Point of Marginal Cheapness (PMC) | Lower bound of acceptable range |
| NC × TE | Point of Marginal Expensiveness (PME) | Upper bound of acceptable range |

**Acceptable Price Range** = PMC to PME

### Without Survey Data: Estimation Method

Ask stakeholders or the user to estimate for each target segment:
- Floor: "The price at which customers would question quality" = PMC estimate
- Target: "The price that feels right for the value delivered" = OPP estimate
- Ceiling: "The price at which meaningful churn begins" = PME estimate

Document these as `[est]` and note the assumption basis.

---

## Hermann Simon Value-Based Pricing

Value-based pricing sets price equal to the economic value delivered to the customer, not the cost of production.

### Value-Based Pricing Formula

```
Price = Economic Value to Customer (EVC)
EVC  = Reference Value + Differentiation Value
     = (Competitor price or next-best alternative cost)
     + (Quantified benefit of your product over the alternative)
```

### Steps to Quantify EVC

1. Identify the customer's next-best alternative (competitor product, doing it themselves, doing without)
2. Quantify the reference value (what they pay for the alternative)
3. Quantify each differentiated benefit:
   - Time saved × customer's hourly cost
   - Revenue enabled × expected realisation rate
   - Risk avoided × probability × cost of risk event
   - Quality improvements × customer's willingness-to-pay for quality
4. EVC = Reference + Sum of differentiated benefits
5. Price = EVC × Value share % (typically 50–80% of EVC; you share value with the customer)

---

## Anchoring and Decoy Effects

### Anchoring
The first price a customer sees becomes the reference point for all subsequent price comparisons. The anchor shapes perception of value.

- **High anchor → middle tiers feel reasonable**: a $499/month Enterprise plan makes a $149/month Professional plan feel like a bargain.
- **Annual pricing anchor**: showing annual price first (e.g. $1,788/year) makes monthly equivalent ($149/month) feel cheaper.

### Decoy Effect (Asymmetric Dominance)
A third option that is clearly inferior to one option on most dimensions causes customers to favour that option.

**Classic decoy structure:**
- Option A (small): $9/month, 5 projects
- Option B (large): $49/month, unlimited projects ← **intended hero**
- Option C (decoy): $39/month, 10 projects ← similar price to B, much less value
When C is present, Option B appears obviously superior. Without C, customers anchor on Option A.

### Recommendations for Tier Design
1. Always have 3 tiers minimum for B2B SaaS.
2. Position your "hero" tier as the middle option.
3. Use the top tier as an anchor (even if few customers choose it).
4. Ensure each tier step-up feels like ≥ 2× the value for ≤ 2× the price.

---

## Monroe Pricing Pyramid

The Monroe Pricing Pyramid frames pricing as a hierarchy of customer perceptions:

```
Level 5: Price is irrelevant — product is unique/irreplaceable
Level 4: Price is secondary — strong preference for this product
Level 3: Price matters but value justifies it — deliberate choice
Level 2: Price is primary decision factor — commodity comparison
Level 1: Price must be lowest — pure commodity
```

Most differentiated SMB products should aim to position at Level 3–4 with their primary segment. Level 1–2 requires scale and operational efficiency that most SMBs cannot sustain profitably.

**Application**: map each customer segment to a pyramid level to determine whether value-based or competitor-indexed pricing is appropriate for that segment.

---

## Pricing Model Selection Criteria

| Model | Use when | Avoid when |
|-------|---------|-----------|
| **Cost-plus** | Cost structure is known; margins are regulated or thin; commodity product | Value delivered significantly exceeds cost (leaving money on the table) |
| **Value-based** | Product delivers quantifiable ROI; high differentiation; B2B | Value is intangible or hard to quantify; customer won't share financial data |
| **Competitor-indexed** | Price-transparent market; customers actively compare | You have strong differentiation that justifies premium (you'd be underpricing) |
| **Dynamic** | Demand varies by time, location, or customer type; perishable capacity | B2B relationships where price instability destroys trust |
| **Freemium** | Viral/PLG motion; low marginal cost per user; land-and-expand model | High support cost per user; low free-to-paid conversion potential |
| **Tiered** | Multiple distinct segments with different willingness-to-pay | Product is genuinely one-size-fits-all; artificial segmentation creates confusion |
| **Usage-based** | Value scales with usage; customers resist upfront commitment; metered infrastructure | Unpredictable billing creates customer anxiety; high churn at low usage cohorts |

---

## Pricing Elasticity Benchmarks

### B2B SaaS

| Price increase | Expected churn impact | Net revenue impact |
|--------------|----------------------|-------------------|
| +10% | 0–3% churn increase | Positive if churn < 9% |
| +20% | 2–8% churn increase | Positive if churn < 17% |
| +30% | 5–15% churn increase | Depends on base churn rate |

**Break-even churn rate** for a price increase: Δ Revenue / (ARPU × Number of customers)

### B2C SaaS / Consumer Subscription

Typically 2–3× more price-sensitive than B2B. A 20% price increase in B2C can produce 10–25% churn increase depending on brand strength and switching cost.

---

## Annual Discount Strategy

Standard annual discount tiers for SaaS:

| Discount | Signal |
|----------|--------|
| 10–15% | Minimal incentive — customers may not switch |
| 17–20% | "2 months free" framing — proven conversion trigger |
| 25–33% | Strong incentive — use when cash flow timing matters more than margin |
| > 33% | Value-destructive — signals that monthly pricing is inflated |

Recommended default: 17% annual discount (equivalent to 2 months free on annual plan).

---

## GST Considerations (Australia)

- GST is 10% on most goods and services in Australia.
- B2B prices are typically quoted ex-GST; B2C prices are typically quoted inc-GST.
- For SaaS sold to overseas customers, GST may not apply (consult ATO guidance on digital services).
- If pricing is displayed inc-GST, show the ex-GST breakdown on invoices for business customers registered for GST.
