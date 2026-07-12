---
title: AU/NZ mid-market in-house counsel
slug: au-midmarket-inhouse-counsel
type: segment
status: active
owner: contractiq
created: 2026-04-09
updated: 2026-05-19
---

# Segment — AU/NZ mid-market in-house counsel

## Who they are

Sole or small (1–5 person) in-house legal team at AU/NZ companies with 50–500 staff and AU$10M–AU$200M revenue. Titles: General Counsel, Head of Legal, Senior Legal Counsel. Often the *only* lawyer in the business. Reports either to the CFO, COO, or directly to the CEO. Reviews 8–25 commercial contracts a week — supplier MSAs, reseller agreements, NDAs, employment contracts (rarely), data-processing agreements.

## Where they are

- **Geography:** Australia and New Zealand. ~70% Sydney/Melbourne/Brisbane; ~15% Auckland/Wellington; the balance scattered (Perth, Adelaide, Canberra, regional).
- **Channel:** primarily LinkedIn (the AU/NZ corporate-counsel community is tight); secondarily the Association of Corporate Counsel (Australia) member network; tertiarily peer referrals.

## What they're trying to do

The single dominant job-to-be-done: get a commercial MSA from "received" to "ready for the business to sign" without becoming the company's bottleneck.

## What's currently in their way

1. Reading 40-page contracts at 9pm on a Thursday because the business needs sign-off Friday morning.
2. Missing auto-renewal or uncapped-liability clauses that surface as expensive surprises 12–18 months later.
3. No system to track obligations created by a contract once it's signed — every counsel maintains a personal spreadsheet.

## User vs paying customer

- **User:** the in-house counsel themselves (1–5 per company). They evaluate the tool and recommend it.
- **Paying customer:** procurement or finance holds the budget for legal-tech tools. The buyer-user split is real and is the reason `au-midmarket-procurement` exists as a secondary segment (see [`02-customer-discovery/segments/au-midmarket-procurement/README.md`](../au-midmarket-procurement/README.md)).

We do *not* create separate `<slug>-user` and `<slug>-buyer` sub-folders here because the buyer is a different role (procurement), modelled as its own segment. The convention applies when both roles sit inside the same function.

## Sub-segments

- `au-midmarket-inhouse-counsel-sole` — single-lawyer companies (≥ 60% of the segment by Priya Natarajan's network estimate).
- `au-midmarket-inhouse-counsel-team` — 2–5 person teams.

Not yet split into folders; pain priorities differ subtly (the team-of-five has handoff coordination as a top-3 pain that the sole-counsel does not).

## Optional persona

Not delegated to brand-manager yet. Priya's first-person knowledge as a former GC at a mid-market AU SaaS is the working persona until the segment is 🟢 on `customer-discovery-status`.

## Next steps

- `/customer-profile-build au-midmarket-inhouse-counsel` — fill in jobs/pains/gains.
- `/early-adopter-profile au-midmarket-inhouse-counsel` — identify earlyvangelists.
- `/interview-guide-build au-midmarket-inhouse-counsel` — generate an interview guide.
