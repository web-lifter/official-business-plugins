# Causal Impact Analysis — Sydney CBD congestion levy increase, 2024

**Intervention date:** 01/07/2024
**Outcome of interest:** Daily PT (public transport) trips into Sydney CBD
**Owner:** Data team — Transport Policy

---

## Intervention Summary

- **What happened:** NSW Government increased CBD parking levy by 25% (from $X to $X) on 1 July 2024
- **Who was affected:** All paid parking inside the Sydney CBD ring; ~32,000 affected spaces
- **When:** Effective 01/07/2024; announced 4 weeks prior
- **Why not RCT:** Policy change — can't randomise

---

## Method Chosen

**Method:** Diff-in-Diff
**Why:** We have daily PT trip data for both treated area (Sydney CBD) and natural control (Melbourne CBD — comparable but unaffected by NSW levy change). 24 months of pre-treatment + 6 months post is sufficient. Synthetic control would also be defensible; DiD is more interpretable for stakeholders.

---

## Identifying Assumption (Explicit + Falsifiable)

> **Parallel-trends assumption:** Absent the levy change, daily PT trips into Sydney CBD and Melbourne CBD would have moved in parallel.

How to test: visual + statistical pre-trends test on 24 months of pre-treatment data. Plot daily trips for both cities; run a regression of trip-difference on time over the pre-period and test whether the time coefficient is statistically zero.

---

## Estimating Equation / Spec

```
Y_{c,t} = α + β · post_t + γ · treated_c + δ · (post_t × treated_c) + θ · X_{c,t} + ε_{c,t}
```

Where:
- `Y_{c,t}` = log daily PT trips into city c CBD on day t
- `post_t` = 1 if t ≥ 01/07/2024, else 0
- `treated_c` = 1 if c = Sydney, else 0 (Melbourne)
- `X_{c,t}` = controls (day-of-week, public holidays, school holidays, rainfall, weather extremes)
- `δ` = the causal effect of the levy change

- **Standard errors:** Cluster-robust at city level (small clusters — flag wild bootstrap as alternative)
- **Pre-treatment covariates:** rainfall, day-of-week, holiday flags

---

## Validity Diagnostics

| Test | Result | Pass? |
|------|--------|-------|
| Pre-trends parallel (24-month pre-period regression) | Coef on time-difference = 0.0008, p = 0.61 | ✓ Pass |
| Placebo (apply DiD to pretend intervention 6 months before actual) | Effect = +0.4% (not significant) | ✓ Pass |
| Covariate balance | Mean rainfall, holiday pct comparable | ✓ Pass |

---

## Robustness Checks

| Check | Result | Direction |
|-------|--------|----------|
| Drop weather controls | Estimate +6.8% (CI [4.1, 9.5]) | Stable |
| Use SEIFA-weighted trip data | Estimate +7.2% (CI [4.3, 10.1]) | Stable |
| 30-day window post-treatment only | Estimate +6.9% (CI [3.8, 10.0]) | Stable |
| Synthetic-control alternative | Estimate +7.5% (CI [4.0, 11.0]) | Stable |

All four robustness checks point to ~+7% effect, increasing confidence.

---

## Effect Estimate

- **Point estimate:** +7.1% increase in daily PT trips into Sydney CBD relative to Melbourne CBD
- **95% CI:** [+4.3%, +9.9%]
- **Interpretation in plain English:** The CBD parking-levy increase is associated with a ~7% increase in PT trips into the Sydney CBD, compared to what we'd have seen without the change. Given pre-intervention baseline of ~480k trips/day, this is roughly 34k additional PT trips/day.

---

## Stats Reviewer — Independent Review

### Verdict: Approve-with-caveats

### Critical issues

None on the analysis itself. The pre-trends, placebo, and four robustness checks are all consistent. The DiD specification is correct.

### Important caveats

1. **Two-unit comparison is fragile.** Sydney vs Melbourne is N=2 at the city level. Cluster-robust SEs with two clusters are not well-behaved; the t-statistic distribution is non-standard. **Recommend wild bootstrap to validate inference.** If the wild bootstrap CI is dramatically wider, treat the CI here as too narrow.
2. **Concurrent changes.** Check whether anything else happened in Sydney CBD on/near 01/07/2024 (new train line, road closure, fuel price spike specific to NSW). If yes, the effect is confounded.
3. **Substitution vs new trips.** The +7% PT could be people who would have driven, OR additional CBD visits, OR substitution from cycling. Distinguishing these requires individual-level data, not this aggregate analysis.

### Optional improvements

1. Add Brisbane CBD as a third control (where data exists) to strengthen the comparison.
2. Run event-study version showing dynamic effects week-by-week post-intervention.
3. Examine heterogeneity: is the effect larger on weekdays (commute-driven) vs weekends (discretionary)?

### What I checked

- Identifying assumption stated + tested ✓
- Pre-trends parallel ✓
- Placebo ✓
- ≥ 2 robustness checks (✓ — four)
- Cluster-robust SEs (✓ — but small N caveat)
- External validity discussed (see limitations)
- Effect plausible given intervention size (yes — moderate elasticity)

---

## Limitations & External Validity

- Two-city comparison; small-N inference caveat (wild-bootstrap recommended)
- Cannot distinguish substitution from new demand without individual-level data
- Effect may attenuate over time as users adjust; check at 12-month follow-up
- External validity: Sydney's PT and CBD economy are atypical; effect may not transfer to other AU cities or to international comparisons
- Magnitude is plausible given parking demand elasticity estimates in the literature (~-0.3 to -0.5), but a 25% price increase producing a 7% PT shift is on the upper end — would benefit from confirmation by a follow-up analysis at 12 months
