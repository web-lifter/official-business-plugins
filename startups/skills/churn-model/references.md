# churn-model — references

See [`startups/SOURCES.md`](../../../../SOURCES.md) for the canonical citation list.

## Primary sources

- **Reichheld, Frederick.** *The Loyalty Effect.* Harvard Business Press, 1996.
  - Origin of compound-retention math: a 5pp swing in retention compounds dramatically over a customer lifetime.
  - Source of the `(1 − r)^n` cohort-decay formula and the average-lifetime identity `1/(1 − r)`.
- **Reichheld, Frederick.** *The Ultimate Question 2.0.* Harvard Business Review Press, 2011.
  - Extends *The Loyalty Effect* with the Net Promoter framework — relevant where Keep-stage NPS is the retention proxy.
- **Skok, David.** "SaaS Metrics 2.0" (For Entrepreneurs, 2013). <https://www.forentrepreneurs.com/saas-metrics-2/>
  - The standard SaaS-industry treatment of monthly vs annual churn and the LTV/CAC ratio.

## Why the formula

- **`(1 − r)^n`** assumes constant per-period churn — a Bernoulli-trial model on a cohort. Real cohorts deviate: typically more churn in months 1–3, then a plateau. The constant-rate model is the right first approximation pre-data; refine once empirical cohorts exist.
- **`1/(1 − r)`** is the closed-form expectation of a geometric distribution with success probability `(1 − r)` (where "success" = churn). It is the **average** lifetime — the median is usually shorter, the long tail is fat.

## Why ±5pp sensitivity

From Reichheld (1996): "a 5 percentage point increase in customer retention can increase the lifetime profit per customer by 25%–95%." The mechanism is that lifetime is `1/(1 − r)`, which is **hyperbolic** in `r`: small additive changes near `r = 1` produce huge multiplicative changes in lifetime. The skill surfaces ±5pp explicitly so the user sees this fragility.
