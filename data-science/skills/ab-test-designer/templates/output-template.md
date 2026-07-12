# A/B Test Design — {{test_name}}

**Date:** {{date_dd_mm_yyyy}}
**Owner:** {{role_or_name}}

---

## Hypothesis

**H1:** If we {{change}}, {{primary_metric}} will {{direction}} by ≥ {{mde}} (vs control).
**H0:** No effect.

---

## Design Specification

| Field | Value |
|-------|-------|
| Primary metric | {{metric}} |
| Definition | {{def}} |
| Secondary metrics (pre-registered) | {{list}} |
| Guardrail metrics | {{list}} |
| Randomisation unit | {{unit}} |
| Variants | A (control 50%) / B (50%) |
| Sample size per arm | {{n}} |
| Total sample | {{total}} |
| Duration at expected traffic | {{n}} weeks |
| Pre-launch | A/A check + SRM monitor day 1 |
| Stopping rule | Fixed horizon, no peeking |

---

## Power Analysis

| Parameter | Value |
|-----------|-------|
| Baseline | {{p}} |
| MDE (absolute) | {{mde}} |
| Alpha | 0.05 |
| Power | 0.80 |
| Sample/arm | {{n}} |

### Sensitivity

| MDE × | Sample/arm | Duration |
|-------|-----------|----------|
| 0.5× | {{n}} | {{wks}} |
| 1.0× | {{n}} | {{wks}} |
| 2.0× | {{n}} | {{wks}} |

---

## Pre-Registered Decision Matrix

| Outcome | Action |
|---------|--------|
| Significant + ≥ MDE + no guardrail breach | Ship to 100% |
| Significant but below MDE | Discuss; usually don't ship |
| Not significant | Don't ship; consider follow-up |
| Guardrails breached | Don't ship; investigate |
| Inconclusive (CI too wide) | Rerun with more traffic |

---

## Launch & Monitoring Plan

- **Day 1:** SRM check (chi-square p > 0.01 expected); A/A residual sanity check
- **Day 3:** First peek for harm only (guardrail breach check, no primary read)
- **End of duration:** Primary read + secondary + guardrail summary
- **Post-launch:** Document outcome in experiment ledger

---

## Stats Reviewer — Independent Review

_[Inserted by stats-reviewer agent]_
