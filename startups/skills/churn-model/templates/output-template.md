# Churn model

Inputs and evidence: {{rate, period, source, measured or assumed}}
Definitions: r = retention; c = 1-r. Survival = r**n; mean paid periods = 1/c.

| Monthly retention | Monthly churn | Annual retention | Mean lifetime (months) |
|---|---|---|---|
| {{r}} | {{c}} | {{r**12}} | {{1/c or unbounded}} |

## Cohort and sensitivity

{{Shares after 1, 3, 6, 12 and 24 months; valid anchor +/-5pp cases.}}

## Economics, where inputs exist

Gross profit/month = ARPU * gross-margin fraction.
Contribution LTV = gross profit/month / churn.
Payback months = CAC / gross profit/month.
LTV:CAC = contribution LTV / CAC, where CAC > 0.

## Limitations and next evidence

{{Constant-rate assumptions, data gaps, uncertainty and finite horizon.}}
