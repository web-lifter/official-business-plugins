# Pricing Architecture Designer — Reference Material

## Pricing Model Decision Matrix

| Model | Best when | Cautions |
|-------|-----------|----------|
| **Tiered (Good/Better/Best)** | Clear feature/seat segmentation; multiple personas | Sprawl risk; pick exactly 3 |
| **Usage-based** | Value scales linearly with use; unit is clear | Bill predictability concern; trust required |
| **Freemium** | Strong network effects; viral loop; bottoms-up adoption | Free-rider risk; conversion < 5% typical |
| **Value-based** | High-touch sales; quantifiable customer outcome | Pricing meeting per customer = slow |
| **Outcome-based** | Measurable outcomes (lead-gen, jobs closed) | Trust + attribution challenge; rare to do well |
| **Hybrid (tiered + usage)** | Most modern SaaS | Complexity — needs clear UX |

---

## Van Westendorp Price Sensitivity Meter (PSM)

Ask buyers 4 questions:

1. At what price is it so **cheap** you'd question quality?
2. At what price is it a **bargain**?
3. At what price is it starting to feel **expensive** but you'd still consider?
4. At what price is it **too expensive**?

Plot cumulative distributions; intersections:

- **Optimal Price Point (OPP)** = intersection of "Too cheap" + "Too expensive"
- **Range of Acceptable Prices (RAP)** = between PME (Point of Marginal Expensiveness) and PMC (Point of Marginal Cheapness)

Sample size: ≥ 200 respondents per segment for stable estimates.

---

## Fences (How to gate buyers between tiers)

1. **Functional fence** — feature in higher tier (best for B2B SaaS)
2. **Quantity fence** — users / jobs / contacts cap (best when usage varies by company size)
3. **Customer-type fence** — free for students / educators (segments by identity)
4. **Time-based fence** — first 6 months at lower price (best for new customers)
5. **Channel fence** — different pricing by partner channel (rarely good UX)
6. **Service-level fence** — support response time tied to tier (B2B Enterprise common)

Strong fences are:
- **Defensible** — buyer can't easily bypass
- **Customer-justifiable** — different value, not arbitrary
- **Operable** — your team can enforce

---

## Anchor & Decoy Patterns

### The "Asymmetric Dominance" decoy

Three tiers where the middle is dominantly better than the cheapest, but worse than the best on one dimension:

- Good: 1 user, 25 jobs, $39
- Better (target): 10 users, 100 jobs, $89 — dominates Good
- Best: unlimited, $189 — dominates Better

Buyers gravitate to "Better" because it dominates the comparison without paying for "Best" features they don't need.

### Centering

When 3 tiers are arranged, buyers prefer the middle by ~70% in many studies. Engineering the middle to be the most profitable per acquisition is the highest-leverage move.

### The "Decoy" tier

A tier nobody buys, that exists only to make others look better. E.g. a $999/mo tier when actual buyers fit $89 or $189 — the $999 makes $189 feel reasonable.

---

## Common Packaging Mistakes Table

| Mistake | Why it fails |
|---------|-------------|
| 5+ tiers | Paralysis; conversion drops 40%+ |
| Identical features, different seat caps only | Single-fence pricing; no differentiation |
| "Contact sales" for middle tier | Forces friction; only top tier should require contact |
| Annual-only pricing | Cuts off the trial-curious; recommend monthly + annual |
| Discount as the answer to "no" | Trains buyers to negotiate; price holds first |
| Pricing on the homepage (B2B Enterprise > $50k ACV) | Anchors below true value; "contact sales" for big tier |
| Pricing hidden (B2B SMB < $5k ACV) | Friction in self-serve flow; lose to competitors with transparent pricing |
| Per-feature pricing (90s telco style) | Cognitive load; bills feel unpredictable |

---

## Migration Patterns

| Pattern | Use when | Risk |
|---------|----------|------|
| **Grandfather** existing customers | Most price changes | Loyalty/fairness pressure preserved |
| **Sunset** on a date | Major model change | Churn spike at sunset date |
| **Opt-in upgrade** | Pricing change adds value | Low conversion to new tier |
| **Auto-migrate** | Equivalent tier exists | Need 8+ weeks notice; some churn |
| **Bespoke per account** | Top 50 customers | High-touch; only for enterprise |
