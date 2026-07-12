---
title: Digital prototype — ContractIQ clause-review pane
slug: digital-contractiq-clause-review
type: prototype
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Digital prototype — ContractIQ clause-review pane

Tests: H-002 (usability — median redline time ≤ 25 minutes vs. > 90 minutes manual).
Source paper prototype: [paper/contractiq-clause-review](../paper/contractiq-clause-review.md)
Source Figma: `ContractIQ-MVP` (placeholder file ID — to be created at `figma.com/file/ABC123/ContractIQ-MVP`)

## Fidelity

**Click-through Figma**. Justification: H-002 is a usability hypothesis answerable by clicks alone; a coded prototype is premature until we know the right interaction shape. We will revisit fidelity after three feedback sessions.

## Figma handoff

Pending — the Figma file does not yet exist. Once created, run `/figma-design-handoff <file-id>` and this section will be auto-populated with the component inventory, design tokens, and screen captures.

Until then, the sketch lives as ASCII layouts in the paper prototype. Six screens, mirroring the paper flow:

1. Upload
2. Processing (loading state)
3. Findings list + clause detail (the value-revealing screen)
4. Annotation modal
5. Export
6. Confirmation

## Feedback collection plan

- **Sessions:** 5 target. Pilot user "Aubergine Health" GC committed to 2; recruit 3 more via the founder's LinkedIn network of mid-market AU GCs.
- **Task:** "Walk me through reviewing this 38-page Aubergine supplier MSA using ContractIQ." Use the same sample contract across all sessions for cross-session comparability.
- **Probes:**
  - "What did you expect when you dropped the file?"
  - "Would you trust the AI's reasoning on clause 14.3, or re-read the original text?"
  - "Where would you reach for Word instead of this tool?"
  - "What would have to be true for you to use this on a 9pm-Thursday-deadline contract?"
- **Hypothesis touch-points:**
  - H-002 (primary) — measure median time-to-export across the 5 sessions.
  - H-001 (secondary) — at session close, surface willingness-to-pay probe at AU$300/seat/month.

## Open design questions

- Should the "Approve / Reject / Annotate" buttons be in the right pane or sticky at the bottom of the viewport? (Defer to first session.)
- Should the obligation-timeline view be a separate tab or appear inline below the findings list? (Out of scope for the click-through; flag for the next iteration.)

## Next actions

1. Priya creates the Figma file at `figma.com/file/ABC123/ContractIQ-MVP` (placeholder URL — actual ID will be assigned by Figma on creation).
2. Run `/figma-design-handoff <file-id>` once the file exists.
3. Run `/prototype-feedback-collect digital-contractiq-clause-review` for each of the 5 sessions.
