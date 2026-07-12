---
title: Falsifiability check — H-001
slug: falsifiability-check-H-001-2026-05-21
type: falsifiability-check
status: pass
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Falsifiability check — H-001

## Verdict

**PASS**

## JSON sidecar

```json
{
  "id": "H-001",
  "verdict": "pass",
  "issues": []
}
```

## Detailed findings

H-001 statement under review:

> "Mid-market in-house counsel at AU/NZ companies of 50–500 staff will
> pay AU$300/seat/month for a clause-classification + obligation-
> extraction tool. Falsifier: < 30% of 20 interviewees express
> willingness to pay."

### Falsifier

- **Present.** The hypothesis names an observable outcome ("< 30% of
  20 interviewees express willingness to pay"). The falsifier
  references a specific cohort (20 interviewees from the named
  segment) and a specific event (expressing willingness to pay during
  the interview).

### Measurement

- **Present.** Implicit measurement is the structured price-sensitivity
  meter response captured during a customer-development interview.
  Recommend the test card spell out the instrument explicitly (van
  Westendorp PSM → Postgres `interview_wtp` table) — see TC-001 for
  the elaborated version.

### Threshold

- **Present.** "30% of 20" = at least 6 interviewees expressing
  willingness to pay at AU$300/seat/month (or above the AU$250 PSM
  acceptable-price floor). Specific, pre-set, binary.

### Timeframe

- **Inherited from the experiment**, not the hypothesis itself.
  TC-001 sets the 6-week interview window, which is appropriate for
  this hypothesis class. **Recommendation:** when registering future
  hypotheses, include the timeframe explicitly in the hypothesis text
  ("…within 30 days of MVP launch", "…by end of Q3 2026"). H-001
  passes as registered because the experiment is paired with it
  immediately.

## Override

None — `pass` verdict.

## Comparison: an example that would FAIL

If H-001 had been stated as:

> "There's a viable price point for the tool."

…the check would have returned **FAIL** with these issues:

- `falsifier`: missing — "viable" is undefined and unobservable.
- `measurement`: missing — no data source named.
- `threshold`: missing — no specific number.
- `timeframe`: missing.

…and the calling skill (`/hypothesis-register add`) would refuse the
addition unless `--force` was passed. With `--force`, the override
would be logged to `.memex/log.md` as:

```
## [2026-05-21] gate-override | hypothesis-falsifiability-check
bypassed for H-001 (issues: falsifier, measurement, threshold,
timeframe — all missing)
```

…and the next reviewer to read the audit trail would see exactly
which gates were skipped and why.
