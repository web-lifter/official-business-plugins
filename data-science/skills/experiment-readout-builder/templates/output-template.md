# Experiment Readout — {{test_name}}

**Period:** {{start}} → {{end}}
**Owner:** {{name}}
**Pre-registered design:** {{link_or_path}}

---

## Pre-Registration Recap

- **Primary metric:** {{metric}}
- **MDE:** {{mde}}
- **Decision matrix:** {{summary}}

---

## SRM Check

| Arm | Observed | Expected | % deviation |
|-----|----------|----------|------------|
| A | {{n}} | {{n}} | {{n}}% |
| B | {{n}} | {{n}} | {{n}}% |

**Chi-square p-value:** {{p}}
**Verdict:** {{passed_or_failed}}

If failed → STOP. Do not interpret primary metric. Investigate instrumentation.

---

## Primary Read

| Arm | Sample | Primary metric | 95% CI |
|-----|--------|---------------|--------|
| A (control) | {{n}} | {{value}} | — |
| B | {{n}} | {{value}} | — |

- **Absolute effect:** {{val}}
- **Relative effect:** {{pct}}
- **95% CI on effect:** [{{lower}}, {{upper}}]
- **p-value:** {{p}}
- **Practically significant?** {{yes_no}} (compared to MDE)

---

## Secondary + Segment + Novelty

### Secondary metrics

| Metric | A | B | Effect | CI | Notes |
|--------|---|---|--------|----|-------|

### Pre-registered segments

| Segment | A | B | Effect | CI | Notes |
|---------|---|---|--------|----|-------|

### Novelty / primacy

Week 1 effect: {{val}}
Week 2 effect: {{val}}
**Pattern:** stable / declining / strengthening

---

## Guardrails

| Metric | A | B | Status |
|--------|---|---|--------|
| {{metric}} | | | 🟢 / 🟡 / 🔴 |

---

## Decision (Matrix Applied)

**Outcome:** {{primary_outcome}}
**Matrix says:** {{action}}

**Recommended action:** {{action}}

---

## Stats Reviewer — Independent Review

_[Inserted by stats-reviewer agent]_

---

## Follow-Up Experiments

1. {{follow_up_1}}
2. {{follow_up_2}}
3. {{follow_up_3}}
