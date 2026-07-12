# Elasticity Method Spec — {{product_name}}

**Date:** {{date_dd_mm_yyyy}}

---

## Recommended Method

**Method:** {{Historical regression / Van Westendorp / Gabor-Granger / Conjoint / A/B price test / Quasi-experimental}}
**Why:** {{rationale based on data + capability}}

---

## Implementation

| Parameter | Value |
|-----------|-------|
| Required N | {{n}} |
| Time to deliver | {{weeks}} |
| Cost estimate (AUD) | ${{n}} |
| Statistical power | {{0.8 default}} |

---

## Identification Assumption

> {{assumption_explicit_and_falsifiable}}

How to validate: {{test}}

---

## Implementation Plan

| Week | Activity |
|------|---------|
| 1 | {{activity}} |
| 2 | {{activity}} |
| ... | ... |

---

## Expected Output Format

| Output | Description |
|--------|-------------|
| Point elasticity | Single number ε = (% ΔQ) / (% ΔP); typically -0.5 to -2.0 for normal goods |
| Confidence interval | 95% CI on ε |
| Validation result | Identification check passed / failed |
| Price-response curve | Q at each tested P with CIs |

---

## Caveats

| Caveat | Severity | Mitigation |
|--------|----------|------------|
| {{caveat}} | {{H/M/L}} | {{action}} |

---

## What to Do With the Result

- If |ε| < 0.5 → highly inelastic; consider raising price
- If 0.5 < |ε| < 1.0 → moderate; small careful price moves
- If |ε| > 1.0 → elastic; price cuts may increase revenue (or vice versa)
- Always route to `[[pricing-architecture-designer]]` for the action plan
