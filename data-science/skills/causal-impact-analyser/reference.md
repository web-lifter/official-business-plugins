# Causal Impact Analyser — Reference Material

## Method Selection Flowchart

```
Can you randomise?
├── Yes → Use [[ab-test-designer]] instead.
└── No → Quasi-experimental:
    ├── Have a comparable untreated group + pre-post data? → DiD
    ├── One treated unit + many candidate controls? → Synthetic Control
    ├── One unit + rich pre-treatment time-series? → ITS
    ├── Treatment determined by a cutoff (age, score, distance)? → RDD
    ├── Treatment encouraged but not mandatory; have an instrument? → IV / LATE
    └── None of the above? → Use a structural model or admit causal claim is weak
```

---

## Validity Tests by Method

### Diff-in-Diff

- **Parallel-trends test:** Regress outcome difference on time pre-treatment; coefficient should be zero
- **Placebo test:** Apply same method to a "pretend" intervention before actual
- **Event study:** Plot effect by period — looking for flat pre and sharp post
- **Anticipation effect:** Check 1–2 periods immediately before intervention for early movement
- **Triple-difference:** If you have a third dimension (e.g. age × city × time), use it

### Synthetic Control

- **Pre-treatment RMSPE:** Should be small (good fit)
- **Donor pool definition:** Must be defensible; document what was included/excluded
- **Weight interpretability:** Top weights should be intuitive comparators
- **Leave-one-out:** Re-estimate dropping each donor; result should be stable
- **In-time placebo:** Pretend treatment happened earlier; effect should be near zero
- **In-space placebo:** Apply method to untreated units; treated should be in tails

### Interrupted Time-Series

- **Autocorrelation handling:** Newey-West SEs or AR(p) model
- **Structural-break test:** Bai-Perron or supF
- **Pre-period length:** Need ≥ 24 obs for monthly; ≥ 100 for daily
- **Concurrent-intervention check:** Any other change in same window?

### Regression Discontinuity (RDD)

- **McCrary density test:** No bunching around cutoff (subjects can't manipulate score)
- **Covariate-balance test:** Smooth across cutoff
- **Bandwidth choice:** Use Calonico-Cattaneo-Titiunik (CCT) optimal bandwidth
- **Polynomial order:** Local linear is recommended default; cubic+ is fishy
- **Sharp vs fuzzy:** If treatment isn't deterministic, use fuzzy RDD (instrument)

### Instrumental Variables (IV)

- **Relevance:** First-stage F > 10 (rule of thumb; Andrews-Stock more recent)
- **Exclusion restriction:** Instrument affects outcome only through the treatment (untestable; argue based on context)
- **Monotonicity:** No defiers (relevant for LATE interpretation)
- **Over-identification (if multiple instruments):** Hansen J-test

---

## Common Pitfalls

1. **Selection on the dependent variable** — choosing treated/control units based on the outcome you're measuring
2. **Confounded interventions** — multiple changes at the same time make the effect unidentifiable
3. **Pre-trend violations ignored** — DiD with diverging pre-trends has no identifying assumption
4. **Bandwidth selection driven by the desired effect** — RDD with manual bandwidth chosen to maximise significance
5. **Synthetic control with poor pre-fit** — if pre-RMSPE is large, the counterfactual is bad and so is the effect
6. **ITS without correcting for autocorrelation** — standard errors are dramatically understated
7. **Post-hoc subgroup analysis** — finding "the segment where the policy worked" after the fact
8. **External-validity overreach** — extrapolating from one specific context to "policy in general"

---

## Sensitivity-Analysis Menu

For any causal claim, ask:
- **Functional form:** Linear vs log; spline vs polynomial — does the effect survive?
- **Sample definition:** Drop pre-X years; restrict to comparable region — stable?
- **Specification:** With/without controls; alternative SE clusters — stable?
- **Placebo:** Same method on a known no-effect period
- **External corroboration:** Does a different data source / instrument confirm?
- **Plausibility:** Is the effect size in the range of prior literature? If not, why?

If ≥ 3 of these sensitivity checks fail, the causal claim is weak.
