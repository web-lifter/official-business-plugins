---
title: Converged finalists — ContractIQ MVP shape
slug: converged-2026-05-21
type: prototype
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Converged finalists — ContractIQ MVP shape

Source: [divergent](divergent-2026-05-21.md)

## Filter scores (top 5)

| # | Idea | Segment fit | Hypothesis value | Build cost (inv) | Novelty | Total |
|---|------|-------------|------------------|------------------|---------|-------|
| 18 | Radiology-style approve/reject-per-finding UI | 5 | 5 | 3 | 5 | 18 |
| 9 | Cross-portfolio pattern detection | 4 | 4 | 2 | 5 | 15 |
| 14 | Wizard-of-Oz manual review email | 5 | 5 | 5 | 5 | 20 |
| 2 | Microsoft Word add-in | 5 | 4 | 2 | 3 | 14 |
| 11 | Email-in / report-out zero-frontend | 5 | 4 | 4 | 4 | 17 |

## Finalists (top 3)

### F1: Wizard-of-Oz manual review email
- Concept: GC emails a `.docx` to `review@contractiq.com.au`; Priya (founder, ex-GC) reviews it overnight, runs the prototype classifier, and emails back a one-page findings report + tracked-changes redline within 24 hours. Customer-facing experience is "the tool works"; back-end is a human in the loop.
- Tests: **H-001 (demand)** — will mid-market GCs actually use a third-party for clause review at AU$300/seat/month? — and **H-002 (usability)** — can the report cut redline time from 90 to ≤25 minutes?
- Segment: Primary — in-house counsel at AU/NZ mid-market companies (50–500 staff). Aubergine Health pilot is the first target.
- Build cost: ~AU$200 of infra (Mailgun inbound + Vercel landing page) + Priya's nights. No engineering required beyond the existing Python+Streamlit prototype Tom built.
- Risks: doesn't scale past ~5 contracts/week; founder burnout; doesn't prove the *automated* classifier hypothesis (H-003). Acceptable for this pass — H-003 is the third hypothesis, not the first.
- Success signal: 3 of 5 pilot users send a *second* contract within 14 days; ≥2 are willing to pay a deposit for a follow-on month.

### F2: Radiology-style approve/reject-per-finding UI
- Concept: Streamlit upload + a clause-review pane where each finding (risky-clause / missing-protection / obligation) appears as a card with Approve / Reject / Annotate. Visually inspired by radiology second-opinion AI tools.
- Tests: **H-002 (usability)** mainly; partially H-003 (precision) by counting reject rate per finding category.
- Segment: Same as F1.
- Build cost: ~3 weeks of Tom's time; existing classifier code carries over.
- Risks: GCs may reject the AI's findings systematically (precision <70% kills H-003); UI may not collapse review time enough.
- Success signal: median time-to-redline ≤25 minutes across 5 sessions; ≥70% of AI findings approved without modification.

### F3: Email-in / report-out (zero-frontend)
- Concept: Inbound email → automated classifier → outbound report PDF + tracked-changes `.docx`. No login, no UI, no accounts. Defaults to manual review (F1) if the classifier confidence falls below threshold.
- Tests: H-001 + H-002 in a workflow that's deliberately low-friction.
- Segment: Same.
- Build cost: ~1 week. Builds on the Streamlit prototype's classifier; Mailgun handles email; Vercel hosts a marketing splash.
- Risks: email round-trip too slow for the "9pm Thursday" use case; PDF report less actionable than an in-app review.
- Success signal: ≥3 GCs send a second contract within 14 days.

## Recommended next action

- F1 (Wizard-of-Oz) is the fastest hypothesis test and the strongest dual-hypothesis cover. Run `/paper-prototype F1` next.
- F2 is the right second move once F1 has 3+ feedback sessions in the bag.
- F3 is the fallback if the founder bandwidth for F1 doesn't hold past week 2.

## Notes

- Score table is conjunctive on *total*, not majority — F1's perfect score across all four filters is the tie-breaker.
- All three finalists test H-001 and H-002; only F2 partially tests H-003. We accept this — H-003 is a scale hypothesis worth deferring.
