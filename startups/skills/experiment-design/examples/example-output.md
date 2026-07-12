---
title: Experiment recommendation — H-001
slug: experiment-recommendation-H-001
type: experiment-design
status: draft
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Experiment recommendation for H-001

Hypothesis: Mid-market in-house counsel at AU/NZ companies of 50–500
staff will pay AU$300/seat/month for a clause-classification +
obligation-extraction tool. Falsifier: < 30% of 20 interviewees
express willingness to pay.

## Top recommendation: Customer interview (problem-style, with van Westendorp Price Sensitivity Meter)

- **Why:** H-001 is a Customer Segments + Revenue Streams hypothesis,
  pre-MVP. The interview-class test is the cheapest way to falsify
  willingness-to-pay at this stage; concierge MVP or pre-order would
  be premature (no MVP to deliver, and pre-order risks burning warm-
  intro goodwill from Priya's GC network). The PSM method is
  specifically designed to elicit price ranges without anchoring,
  which is the single biggest risk of an interview-led price question.
- **Sample:** 20 completed interviews (target). The H-001 falsifier
  threshold of 30% across n=20 has reasonable power for a binary
  pass/fail at this stage; we accept that n=20 is under-powered for
  a precision price band — that's TC-002's job once the segment is
  confirmed.
- **Time:** 6 weeks (recruitment + execution + analysis).
- **Cost:** ~AU$0 incremental; AU$150 for in-person coffees.
- **Confidence the test produces a clear answer:** **High** — PSM
  produces structured numbers per interviewee, and the threshold is
  pre-set.
- **Risk:** network bias (Priya's GC network is friendly). Mitigation:
  at least 6 of 20 interviews must come from outside her direct
  first-degree network.

## Alternatives

- **Pre-order / letter of intent**: would test willingness-to-pay more
  rigorously (signed LOI is stronger evidence than interview-stated
  intent). Did not win because (a) we have no MVP to attach the LOI
  to, and (b) cold-asking warm-intro contacts for a signed commitment
  before they have seen anything is likely to burn the relationship.
  Re-consider for H-002 (usability) once we have a concierge pilot
  to attach to.

- **Survey of a wider AU mid-market in-house counsel panel**: would
  reach n=50–100 cheaply via a third-party legal panel and reduce the
  network-bias concern. Did not win because (a) the panel cost
  (~AU$3–5k) is real money for pre-revenue stage, and (b) surveys
  test stated preference, not price elasticity, less accurately than
  PSM in interview. Park for round 2 if interview signal is ambiguous.

## Next step

Run `/test-card-build H-001 customer-interview` to draft the test
card. The card should set the PSM thresholds explicitly and pre-commit
to the 30% / n=20 pass line.
