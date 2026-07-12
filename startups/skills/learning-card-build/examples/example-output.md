---
title: Learning card LC-001 — TC-001
slug: LC-001
type: learning-card
status: active
owner: contractiq
created: 2026-07-09
updated: 2026-07-09
---

# LC-001 — AU$300/seat/month is acceptable; H-001 confirmed

Resolves: [TC-001](../test-cards/TC-001.md)
Hypothesis: [H-001](../../01-hypotheses/hypothesis-register.md)

## We tested

Mid-market in-house counsel at AU/NZ companies of 50–500 staff will pay
AU$300/seat/month for a clause-classification + obligation-extraction
tool. Falsifier: < 30% of 20 interviewees express willingness to pay.
Method: 22 problem-interview-style conversations (2 over the
20-interview target — schedule overflow accepted because they were
already booked), van Westendorp PSM for the price question.

## Observed

- Sample: n = 22 completed interviews (2 partial discarded, not counted)
- Result: **14 of 22 (63.6%) placed acceptable price ≥ AU$250/seat/month**;
  of those, 9 placed it at AU$300 or above, and 3 went as high as
  AU$400+ (one explicitly said "$500 if it saved me one indemnity
  miss in the year")
- Threshold (from TC-001): ≥ 6 of 20 (30%) at ≥ AU$250
- Crossed threshold? **Yes** — by a wide margin (63.6% vs the 30% bar)
- Notable quotes / behaviours:
  - P3 (Brisbane edtech, ~120 staff): "I'd buy two seats today if
    you had something working. I missed an auto-renewal that cost us
    AU$80k. AU$300/seat is rounding error against that."
  - P11 (Sydney health-tech, ~180 staff — the future "Aubergine
    Health" pilot): "AU$300 is fair. AU$200 would feel like a
    consumer product and I'd worry about the corpus."
  - 4 of 22 raised confidentiality / data-residency concerns
    unprompted — AU data hosting is a buying criterion. This is a
    surfaced finding, not part of H-001 but feeds H-011.
  - 5 of 22 specifically called out PPSA, Privacy Act 1988, or Modern
    Slavery Act 2018 as a "what nobody else does" wedge — confirms
    H-008 is worth a dedicated test.

## Learned

H-001 is strongly supported. The AU$300 band is not just acceptable —
it is the floor for credibility. The 8 of 22 interviewees who priced
below AU$250 were a mix of: very-small in-house teams (1 lawyer,
< 5 contracts/week — outside our target segment volume bar), and
buyers who confused us with a CLM (price expectation set by CLM
vendors' published lower tiers, not by AI-review tools).

The data-residency finding (4 of 22) suggests **H-011 should be
registered**: "AU data hosting is required to close ≥ 75% of paid
pilots." Falsifier: < 50% of pilots close without an AU-data-residency
commitment. This was not in scope for TC-001 but is signal worth
elevating.

The AU/NZ-specific risk-flag wedge (5 of 22) confirms H-008
(specialisation differentiator) deserves its own test, queued as
TC-008 once TC-002 (usability) concludes.

## Will now

- [x] Confirm hypothesis (recommend `/hypothesis-register flip H-001 accepted`)

## Confidence

**High** — 14 of 22 above threshold, the threshold was set
pre-test, the price elicitation method (van Westendorp PSM) avoids
the most common anchoring bias, and 6 of 22 came from outside Priya's
direct first-degree network. The strongest residual concern is that
the segment is friendly to legal-tech *category framing* in a way that
may not translate to actual purchase — TC-002's concierge pilots will
test that conversion under real conditions.

## Evidence

- [TC-001](../test-cards/TC-001.md) (test card with run log)
- Interview transcripts: encrypted at `s3://contractiq-private/interviews/2026-05/`
  (private; not in repo)
- `interview_wtp` Postgres table — 22 rows, exported as
  `LC-001-wtp-export-2026-07-09.csv` (private)
- 6 interview write-ups elevated to anonymised case-study form:
  `interview-001` (P3, Brisbane), `interview-007`, `interview-011`
  (P11, the future Aubergine Health pilot), `interview-014`,
  `interview-019`, `interview-021`

## Cascade

Recommended next actions (user runs):

1. `/hypothesis-register flip H-001 accepted` — formal flip
2. `/bmc-update H-001` — bumps BMC v1 → v2; promotes Customer Segments
   and Revenue Streams cell entries to `[fact]`
3. `/hypothesis-register add H-011` — AU data residency as a new
   hypothesis surfaced during TC-001
4. Begin TC-002 recruitment (the 5 concierge pilots; H-011 informs
   pilot agreement language around data residency)
