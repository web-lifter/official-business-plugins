# A/B Test Designer — Reference Material

## Sample-Size Formulas (Quick Reference)

### Two-proportion z-test (standard A/B on conversion)

Per group:
```
n = (z_{α/2}√(2p̄(1-p̄)) + z_β√(p1(1-p1) + p2(1-p2)))² / (p2 - p1)²
```
Where p̄ = (p1+p2)/2, p2 - p1 = MDE.

### Two-sample t-test (continuous metric)

Per group:
```
n = 2σ²(z_{α/2} + z_β)² / MDE²
```

### Ratio metrics (LTV, revenue per user)

Use Delta method or cluster bootstrap. Standard formulas underestimate sample size for high-variance metrics.

---

## Guardrail Metric Library

| Category | Metric examples |
|----------|----------------|
| Engagement | Sessions/user/week; DAU; time-on-site |
| Quality | Bounce rate; error rate; 404s |
| Revenue | Refund rate; chargeback rate; ARPU |
| Performance | p50/p95/p99 latency; TTFB; LCP |
| Customer experience | CS ticket volume; NPS post-test |
| Specific to checkout | Cart abandon; payment failure rate; address-validation rate |

Always include ≥ 2 guardrails; one engagement + one performance is a sensible minimum.

---

## Randomisation-Unit Decision Tree

1. **Logged-in product?** → user_id (hashed)
2. **Logged-out product, returning users?** → cookie + device fingerprint
3. **Single-page workflow?** → session
4. **Server-side rendering?** → session at SSR entry
5. **Network-effect-sensitive (marketplace, social, multi-user shared content)?** → cluster randomisation (cohort / region / org)
6. **Pricing or recommendation?** → user, with care for cross-user spillover

---

## Common Pitfalls (mapped to stats-reviewer checklist)

1. **Peeking** — checking results daily and stopping when significant. Inflates false-positive rate from 5% to ~20–30%.
2. **Multiple metrics, no correction** — running 10 metrics and the first to hit p<0.05 wins. Use Bonferroni or BH.
3. **SRM not checked** — imbalanced split (e.g. 49.2% / 50.8%) is a bug, not noise. Investigate.
4. **Novelty / primacy** — UI changes show early lift that fades; A/B too short captures only the novelty.
5. **Network effects (SUTVA violation)** — standard A/B assumes user A's behaviour doesn't affect user B. False in marketplaces.
6. **Effect heterogeneity** — average effect masks segments where treatment harms. Pre-register subgroups.
7. **Post-hoc decision criteria** — without pre-registered criteria, results are rationalised after the fact.
8. **MDE too small for traffic** — running underpowered tests guarantees "not significant" outcomes.
9. **Pricing test fairness** — differential pricing creates customer-trust and legal risk.
10. **One-way doors as A/B** — irreversible changes shouldn't be A/B'd; use staged rollout.
11. **Holiday confound** — Black Friday / EOFY / Christmas inside test window break the comparison.
12. **Self-selection** — testing only on users who opted into a flag biases the population.

---

## Bayesian Alternative

For low-traffic startups or where business stakeholders find frequentist hard to consume:

- Prior: weakly informative (e.g. Beta(α, β) close to noninformative)
- Update with observed data → posterior
- Report "probability that B > A" + 95% credible interval
- Decision rule: ship if P(B > A) > some threshold (e.g. 0.95)

Practical edge: easier to communicate, no peeking penalty, smaller sample size for "directionally confident" decisions. Trade-off: prior choice matters; less standardised across teams.
