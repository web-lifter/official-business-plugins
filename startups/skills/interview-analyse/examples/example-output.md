---
title: Interview summary — AU/NZ mid-market in-house counsel
slug: interview-summary-au-midmarket-inhouse-counsel
type: profile
status: active
owner: contractiq
created: 2026-05-20
updated: 2026-05-20
---

# Interview summary — AU/NZ mid-market in-house counsel

Based on 7 logged interviews, dates 2026-04-23 – 2026-05-14.

## Hypothesis touch-points

| Hypothesis | Total | Confirms | Refutes | Ambiguous | Direction |
|------------|-------|----------|---------|-----------|-----------|
| H-001 (willingness to pay AU$300/seat/month) | 6 | 4 | 1 | 1 | inconclusive — close to threshold, needs a hard-commitment test card |
| H-002 (redline speed < 25 min) | 5 | 3 | 0 | 2 | inconclusive — only 5 interviews; redline-speed claim is forward-looking and needs prototype testing |
| H-003 (classifier ≥ 85% precision) | 0 | 0 | 0 | 0 | not testable via interview — feasibility test only |
| H-004 (procurement holds budget) | 7 | 6 | 0 | 1 | strongly supported (6/7 named procurement as the budget-holder; not yet 5+ procurement interviews) |
| H-005 (LinkedIn community outperforms outbound) | 4 | 2 | 1 | 1 | inconclusive |

## Emergent themes

- **Confidentiality is the first objection, not pricing.** 5/7 interviewees raised data-handling concerns before any price discussion. The current profile has P-04 (generic AI raises confidentiality concerns) but not as a *gating* objection. Recommend bumping P-04 from `medium` to `high`.
- **Obligation tracking is a higher-priority pain than initially modelled.** 4/7 spontaneously brought up personal Excel sheets for "buyer shall…" tracking. Currently P-03 priority `high` — confirmed.
- **Junior delegation is a "post-confidence" feature.** 3/7 named delegation to a paralegal as a gain only after the tool was trusted on the first dozen contracts. G-07 should be re-tagged from `desired` to `unexpected` (they didn't think to ask for it).

## Sub-segment candidates

- `au-midmarket-inhouse-counsel-sole` — 5/7 interviewees are sole counsel; this sub-segment is dominant and warrants splitting once we have 10+ interviews.
- `au-midmarket-inhouse-counsel-team` — 2/7 are 3–5 person teams; their pain priority differs (handoff coordination is a top-3 pain). Not yet a separate folder.

## Repeated outliers

- **2/7 interviewees wanted clause precedent across companies, not just within their own.** This is a network-effect feature that conflicts with the confidentiality positioning. Note as an open question.
- **2/7 expressed strong preference for an MS Word add-in over a web app** (Spellbook frame). Recommend a Word-add-in MVP variant be considered in `/mvp-type-select`.

## Proposed register updates

(User approves each before applying.)

- [ ] H-004: flip to `accepted` — confirmed in 6/7 interviews. Evidence: 6 named procurement contacts; AU$10k–AU$40k budget line referenced by 5/6.
- [ ] H-001: keep `open`, sharpen falsifier to "< 30% of 20 *primary-segment* interviewees AND < 1 paid pilot from TC-001 within 60 days". Move from interview evidence to hard-commitment evidence.
- [ ] New hypothesis: "Confidentiality is a gating concern; an SOC-2 or AU IRAP-equivalent claim is required before paid pilot conversion." Cell: Key Resources. Emerged in 5/7 interviews.

## Follow-ups required

- P7 (Auckland fin-services) — booked 2026-05-26 to verify criterion 3 for earlyvangelist status.
- 4 ACC Australia introductions outstanding from Priya's network.
- Confidentiality story: draft a one-pager (data-handling, on-prem option, AU residency) before the next 5 interviews.
- Procurement-side interviews: 0 logged. Recommend booking 3 procurement contacts referred by P3, P5, P6 before any pricing test card runs.
