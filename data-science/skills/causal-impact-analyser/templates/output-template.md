# Causal Impact Analysis — {{intervention_name}}

**Intervention date:** {{date}}
**Outcome of interest:** {{metric}}
**Owner:** {{name}}

---

## Intervention Summary

- **What happened:** {{describe}}
- **Who was affected:** {{units}}
- **When:** {{period}}
- **Why not RCT:** {{reason}}

---

## Method Chosen

**Method:** {{DiD/SC/ITS/RDD/IV}}
**Why:** {{rationale}}

---

## Identifying Assumption (Explicit + Falsifiable)

> {{assumption}}

How to test: {{test}}

---

## Estimating Equation / Spec

```
{{equation_or_spec}}
```

- **Standard errors:** {{cluster-robust at level X}}
- **Pre-treatment covariates:** {{list}}

---

## Validity Diagnostics

| Test | Result | Pass? |
|------|--------|-------|
| Pre-trends parallel (DiD) / Pre-RMSPE (SC) / Density at cutoff (RDD) | {{val}} | {{y/n}} |
| Placebo | {{val}} | {{y/n}} |
| Covariate balance | {{val}} | {{y/n}} |

---

## Robustness Checks

| Check | Result | Direction |
|-------|--------|----------|
| Leave-one-out / bandwidth × 0.5 / placebo year | {{val}} | {{stable/changes}} |

---

## Effect Estimate

- **Point estimate:** {{val}}
- **95% CI:** [{{lower}}, {{upper}}]
- **Interpretation in plain English:** {{sentence}}

---

## Stats Reviewer — Independent Review

_[Inserted by stats-reviewer agent]_

---

## Limitations & External Validity

- {{limitation_1}}
- {{limitation_2}}
- {{external_validity_caveat}}
