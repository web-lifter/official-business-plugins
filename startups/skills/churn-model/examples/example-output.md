# Illustrative churn model: ContractIQ

Assumed monthly retention: 94%; churn: 6%. These are hypothetical scenario inputs, not observed Australian SaaS benchmarks or validated venture results.

| Monthly retention | Monthly churn | Annual retention | Mean paid periods (months) |
|---|---|---|---|
| 50% | 50% | 0.0% | 2.0 |
| 60% | 40% | 0.2% | 2.5 |
| 70% | 30% | 1.4% | 3.3 |
| 80% | 20% | 6.9% | 5.0 |
| 85% | 15% | 14.2% | 6.7 |
| 90% | 10% | 28.2% | 10.0 |
| 92% | 8% | 36.8% | 12.5 |
| 94% | 6% | 47.6% | 16.7 |
| 95% | 5% | 54.0% | 20.0 |
| 97% | 3% | 69.4% | 33.3 |
| 99% | 1% | 88.6% | 100.0 |

## Anchor cohort

Using r = 0.94 and survival r**n:

| Month | Cohort still active |
|---|---|
| 0 | 100.0% |
| 1 | 94.0% |
| 3 | 83.1% |
| 6 | 69.0% |
| 12 | 47.6% |
| 24 | 22.7% |

Average lifetime is 16.6667 months before rounding. At 89% retention it is 9.0909 months; at 99% it is 100 months. This sensitivity makes the high-retention forecast fragile.

## Contribution economics

Assumed ARPU AU$300/month, gross margin 85%, CAC AU$1,800:

Gross profit/month = AU$255. Contribution LTV = 255 / 0.06 = **AU$4,250**. LTV:CAC = **2.36x**. CAC payback = 1,800 / 255 = **7.06 months**. Revenue LTV before costs is AU$5,000, not the value used in the contribution ratio. No generic benchmark establishes that these economics are viable for this venture.

This flat-rate model ignores changing retention, expansion, discounting and censoring. Replace assumptions with observed cohort data; the model is not necessarily conservative.
