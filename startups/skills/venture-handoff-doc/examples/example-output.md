---
title: Handoff brief — ContractIQ
slug: handoff
type: vision
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Handoff brief — ContractIQ

A self-contained five-minute brief on ContractIQ for a new team member, investor, or future-you.

## At a glance

- **Phase:** Customer discovery (pre-MVP, pre-revenue).
- **Date:** 2026-05-21.
- **One-liner:** We help in-house counsel at AU/NZ mid-market companies redline a 40-page MSA in 20 minutes instead of 3 hours by flagging risky clauses, missing protections, and obligation deadlines.

## The problem

Sole in-house counsel at 50–500-staff AU/NZ companies review 8–25 contracts a week, often as the only lawyer in the business. 6 of 7 interviewees in [`02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/`](.memex/02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/) reported reading 40-page MSAs after 9pm to meet next-day business deadlines; 4 of 7 had been personally responsible for an auto-renewal clause that cost the company > AU$50k 12+ months later. The status quo is manual Word redlining; generic ChatGPT raises confidentiality concerns and has no AU/NZ context.

## The segment

- **Primary:** AU/NZ mid-market in-house counsel — sole or small (1–5) legal team at 50–500-staff, AU$10M–AU$200M-revenue companies.
- **Secondary:** Procurement managers at the same companies (own the supplier-onboarding flow; hold budget).
- **Top three pains (priority high):** late-night MSA reviews; missed auto-renewals that auto-billed the company; no system to track obligations once a contract is signed.
- **Early adopters:** 2 named (Priya Natarajan's network); target 3 to clear `customer-discovery-status` Q3.

## The unique value proposition

> For in-house counsel at mid-market companies who review 8+ contracts a week, **ContractIQ** is the contract-review co-pilot that finds risky clauses and missing protections in under 20 minutes — so you can get out of the bottleneck without sacrificing the quality of your review. Unlike generic legal AI tools, ContractIQ is trained on Australian and New Zealand commercial MSAs and flags AU/NZ-specific issues (e.g. PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018 reporting).

## What we've validated

*Not yet — no learning cards have been written.*

## What's still open

- **H-001 (demand).** Mid-market in-house counsel will pay AU$300/seat/month for clause-classification + obligation-extraction. Falsifier: < 30% of 20 interviewees express willingness to pay. Measurement: discovery interviews + pre-order test card.
- **H-002 (usability).** Senior in-house counsel produces a redline in < 25 min median using the tool vs. > 90 min manual. Falsifier: median ≥ 60 min in prototype-feedback sample.
- **H-003 (scale).** LLM-backed clause classifier reaches ≥ 85% precision on the 14 risky-clause categories most common in AU commercial MSAs. Falsifier: < 70% precision on held-out test set.

## What we've ruled out

*None yet.*

## MVP scope

*Not yet defined — `09-mvp/mvp-spec.md` not created. Blocked by `customer-discovery-status` 🟢 gate.*

## Recent pivots / refines

- **2026-05-19 (refine).** Narrowed primary segment from "any in-house counsel" to AU/NZ mid-market 50–500 staff. See [`pivot-refine-log.md`](.memex/07-validation/pivot-refine-log.md).
- **2026-04-02 (refine).** Added procurement-manager secondary segment.

## Open risks

1. **Confidentiality.** Interviewees flagged that uploading client contracts to an LLM is non-trivial; we need a clear data-handling story before any pilot.
2. **Spellbook expansion.** If Spellbook launches an AU-corpus product before we ship, our moat narrows to AU/NZ-specific clause categories.
3. **Procurement gate.** Procurement managers, not legal, often hold budget. We need at least one procurement-side interview before pricing tests.

## What to do next

1. `/interview-analyse au-midmarket-inhouse-counsel` — aggregate findings across 7 interviews.
2. `/value-map-build au-midmarket-inhouse-counsel` — build the left half of the VPC.
3. `/early-adopter-profile au-midmarket-inhouse-counsel` — recruit one more named earlyvangelist to clear Q3 of the gate.

## Where to dig in

- Index: [`.memex/index.md`](.memex/index.md)
- Founder: Priya Natarajan (former GC). CTO: Tom Whitaker (Python + Streamlit prototype).
- Domain: `contractiq.com.au`.
