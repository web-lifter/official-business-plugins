---
title: Hypothesis register
slug: hypothesis-register
type: hypothesis
status: active
owner: contractiq
created: 2026-04-02
updated: 2026-05-19
---

# Hypothesis register — ContractIQ

Append-only. Status flips require evidence (interview link, learning card, or external citation).

## Register

| ID | Cell | Statement | Status | Falsifier | Measurement | Threshold | Timeframe | Evidence | Updated |
|----|------|-----------|--------|-----------|-------------|-----------|-----------|----------|---------|
| H-001 | Revenue Streams | AU/NZ mid-market in-house counsel will pay AU$300/seat/month for clause-classification + obligation-extraction | open | < 30% of 20 interviewees express willingness to pay AU$300/seat/month at end of interview | Discovery interviews + pre-order test card | ≥ 30% verbal willingness; ≥ 3 paid pre-orders in TC-001 | 60 days | [interview-003](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/interview-003.md); [interview-005](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/interview-005.md) | 2026-05-19 |
| H-002 | Value Propositions | A senior in-house counsel produces a redline of a 40-page MSA in < 25 min median using the tool, vs. > 90 min manual | open | Median time ≥ 60 min in prototype-feedback sample (n ≥ 5) | Side-by-side timed sessions on identical contracts | Median ≤ 25 min; manual baseline ≥ 90 min | 90 days post-prototype-v1 | — | 2026-05-10 |
| H-003 | Key Resources | An LLM-backed clause classifier reaches ≥ 85% precision on the 14 risky-clause categories most common in AU commercial MSAs | open | < 70% precision on held-out test set | Held-out test of 50 annotated AU MSAs across the 14 categories | ≥ 85% precision aggregate; ≥ 70% per category | 30 days post-classifier-v1 | [feasibility note](../09-mvp/feasibility.md) | 2026-05-10 |
| H-004 | Customer Segments | Procurement managers at the same companies hold the budget and will sponsor pilots even when legal is the user | open | < 25% of procurement interviewees agree to sponsor a paid pilot | 5 paired procurement interviews referred by primary-segment contacts | ≥ 25% sponsor + budget identified | 60 days | — | 2026-05-08 |
| H-005 | Channels | Inbound via the AU/NZ corporate-counsel LinkedIn community outperforms outbound to GC titles on Apollo | open | Inbound conversion < 50% of outbound conversion at the same CAC | UTM on landing page; LinkedIn DM A/B | Inbound CPA < AU$300 vs outbound | 90 days | — | 2026-05-08 |

## Notes

- IDs use 3-digit zero-padding from the start; the team chose this on day one anticipating > 100 entries over the venture's life.
- H-001 statement was reworded on 2026-05-19 to match the segment refinement logged in [`07-validation/pivot-refine-log.md`](../07-validation/pivot-refine-log.md). The change is a sharpening, not a flip — status stays `open`.
- See [`references.md`](../references.md) for the underlying Blank / Maurya conventions.
