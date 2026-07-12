---
title: Churn model
slug: churn-model
type: funnel
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Churn model

Source funnel: [funnel-model.md](funnel-model.md)
**Anchor monthly retention rate: 94%** (i.e. 6% monthly churn — the working assumption for a pre-PMF AU mid-market B2B SaaS targeting in-house legal teams).

The 6%-monthly figure sits at the high end of SaaS gross-churn benchmarks for that segment; we will revalidate once 5+ paying logos have ≥ 3 months of data.

## Sensitivity table

| Monthly retention (r) | Monthly churn (1−r) | Annual retention r^12 | Avg lifetime 1/(1−r) (months) |
|-----------------------|---------------------|-----------------------|-------------------------------|
| 50%                   | 50%                 | 0.0%                  | 2.0                           |
| 70%                   | 30%                 | 1.4%                  | 3.3                           |
| 80%                   | 20%                 | 6.9%                  | 5.0                           |
| 85%                   | 15%                 | 14.2%                 | 6.7                           |
| 90%                   | 10%                 | 28.2%                 | 10.0                          |
| 92%                   | 8%                  | 36.8%                 | 12.5                          |
| **94% (anchor)**      | **6%**              | **47.7%**             | **16.7**                      |
| 95%                   | 5%                  | 54.0%                 | 20.0                          |
| 97%                   | 3%                  | 69.4%                 | 33.3                          |
| 99%                   | 1%                  | 88.6%                 | 100.0                         |

## Cohort decay at 94% monthly retention

Using `(1 − r)^n` where r = 0.06 (the churn rate):

| Month | Cohort still active | Calculation |
|-------|---------------------|-------------|
| 0     | 100.0%              | (0.94)^0    |
| 1     | 94.0%               | (0.94)^1    |
| 2     | 88.4%               | (0.94)^2    |
| 3     | 83.1%               | (0.94)^3    |
| 6     | 69.0%               | (0.94)^6    |
| 9     | 57.3%               | (0.94)^9    |
| 12    | 47.6%               | (0.94)^12   |
| 15    | 39.5%               | (0.94)^15   |
| 18    | 32.8%               | (0.94)^18   |
| 21    | 27.3%               | (0.94)^21   |
| 24    | 22.7%               | (0.94)^24   |

After 24 months, ~23% of a starting cohort remains at the 6% monthly churn assumption.

## Interpretation

- **Average customer lifetime:** 16.7 months (≈ 1.4 years).
- **Cohort still active at 12 months:** 47.6%.
- **±5pp sensitivity:**
  - Drop to 89% retention (11% churn) → lifetime falls to 9.1 months (−7.6 months).
  - Rise to 99% retention (1% churn) → lifetime rises to 100 months (+83.3 months).
  - The high-retention end of the curve is enormously sensitive; SaaS unit economics live or die in the 95%–99% band.

## Implications for unit economics

- **LTV at AU$300/seat/month, 16.7-month average lifetime:** ≈ AU$5,010 per seat (before gross-margin adjustment). Apply ~85% gross margin → contribution LTV ≈ AU$4,260.
- **CAC payback target:** under 6 months. At a target CAC of AU$1,800 per seat (≈ 6 months of revenue), the LTV/CAC ratio is ~2.8x — below the 3x SaaS rule of thumb, so we should either (a) get CAC under AU$1,500 via referrals, or (b) lift retention to 96%+ via Keep-stage investment.
- Hand off to `business-economics/unit-economics` for a rigorous LTV/CAC with gross-margin and CAC-payback breakdown.

## Notes

- The 6% baseline came from public commentary on AU SaaS mid-market churn (Skok benchmarks adapted to the local market); refine with our own data after Q2 2026.
- Annual retention `r^12` is conservative; real cohorts often see front-loaded churn in months 1–3, then a plateau. We will track this once we have ≥ 6 monthly cohorts.
