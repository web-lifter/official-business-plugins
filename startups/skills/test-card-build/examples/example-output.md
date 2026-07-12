---
title: Test card TC-001 — H-001
slug: TC-001
type: test-card
status: open
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# TC-001 — Mid-market AU/NZ in-house counsel will pay AU$300/seat/month

Tests: [H-001](../../01-hypotheses/hypothesis-register.md)

## We believe

Mid-market in-house counsel (Head of Legal / GC at AU/NZ companies of
50–500 staff, AU$10M–AU$200M revenue) will pay AU$300 per seat per
month for a clause-classification + obligation-extraction tool that
redlines a 40-page MSA in ≤ 20 minutes and surfaces AU/NZ-specific
risks (PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018).

## To verify, we will

Run **20 customer-development interviews** with Heads of Legal at
target-segment companies, recruited via Priya's GC network and a
warm-intro chain from two AU corporate law firms.

- Audience: 20 Heads of Legal / GCs at AU/NZ companies, 50–500 staff
- Sample target: 20 (interview-to-completion; partial interviews
  excluded)
- Structure: 45-minute Zoom; problem interview script (no demo); price
  question asked using the **van Westendorp Price Sensitivity Meter**
  to avoid anchoring ("at what price would this be a bargain / at what
  price would you start to question quality / at what price would it
  be too expensive / at what price would it be so cheap you'd doubt
  it"). Self-reported willingness-to-pay buckets recorded.

## Measure

- Data: structured interview notes (one Notion page per interview); a
  Postgres table `interview_wtp` capturing each interviewee's
  van-Westendorp four-point answers in AUD
- Instrument: Notion + Postgres; manual entry by Priya within 24h of
  each interview
- Channel: Zoom recording + transcript (consent obtained at start)

## We are right if

≥ 30% of 20 completed interviews (so ≥ 6 interviewees) place the
"acceptable price" point at ≥ AU$250/seat/month (matching or above
AU$300 minus a 17% sensitivity buffer).

## Threshold

- Pass: ≥ 6 of 20 interviewees with acceptable-price ≥ AU$250
- Fail: < 6 of 20 — H-001 is refuted; the segment will not bear the
  price band; the BMC's Revenue Streams cell needs rework

## Cost / time

- Time: 6 weeks (recruitment + 20 interviews + analysis)
- Cost: AU$0 incremental (Priya's time, existing Zoom and Notion
  subscriptions); ~AU$150 for two coffee meet-ups in person

## Risk to mitigate

- **Anchoring bias**: leading the price question undermines the
  signal. Mitigation: van Westendorp PSM specifically.
- **Network bias**: Priya's GC network is friendly. Mitigation: at
  least 6 of 20 interviews must come from outside her direct first-
  degree network (warm intros through the two corporate firms count
  as outside).
- **Confidentiality risk in conversation**: interviewees often share
  vendor info that is sensitive. Mitigation: explicit "we won't quote
  you" note at interview start; transcripts encrypted at rest.

## Linked

- Hypothesis: [H-001](../../01-hypotheses/hypothesis-register.md)
- Segment: [in-house-counsel](../segments/in-house-counsel/README.md)
- Predecessor test card: none (H-001 is the demand hypothesis)
- Related: TC-002 (H-002, usability) is queued for once H-001 passes
  the 12-interview interim check
