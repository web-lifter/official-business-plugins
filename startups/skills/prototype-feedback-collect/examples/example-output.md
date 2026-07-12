---
title: Feedback — contractiq-clause-review session 001
slug: feedback-contractiq-clause-review-001
type: feedback
status: active
owner: ContractIQ
created: 2026-05-22
updated: 2026-05-22
---

# Feedback — contractiq-clause-review session 001

Prototype: [contractiq-clause-review](../paper/contractiq-clause-review.md)
Tests: H-002 (usability — median redline time ≤ 25 minutes)

- Date: 2026-05-22
- Duration: 38 minutes (including post-session debrief)
- Participant: **P3** — Head of Legal, ~120-staff edtech in Brisbane. Strong segment fit (1-lawyer team, reviews 12–15 contracts/week).
- Setup: paper

## Task

"Imagine you've just been asked by the procurement team to sign off on this 38-page Aubergine supplier MSA by tomorrow morning. Walk me through how you'd use ContractIQ to do the review."

## Walkthrough

### Step-by-step observations

- Drop-zone screen: P3 hesitated for ~5 seconds — looked for a "select contract type" picker. Said: "I'd normally tell the tool this is a SaaS MSA vs a services agreement; that changes what I'm looking for." Useful signal.
- Processing screen: accepted instantly. "Twenty seconds is fine; I'm getting coffee."
- Findings screen: P3 went straight to the indemnity clause (14.3) — the highest-priority finding. Took ~90 seconds to read the rationale, then 30 seconds to compose a reject reason. Approved 7 of 12 findings without modification.
- Annotation modal: P3 used the free-text field for 4 of 5 rejections. The preset options ("Already negotiated favourably", "Not relevant") were used once.
- Export: chose `Email both to me`. Confirmed: "Yes, I want it in my inbox; I'll forward the negotiation brief to the business owner."

### Where they got stuck

- The "missing protections" findings were less actionable than the risky-clauses ones. P3: "I know I want a termination-for-convenience clause. What I want from the tool is the *draft language* I could paste in." That's a feature gap, not a flow problem.
- After approving the obligation-deadlines, P3 asked: "Where does this end up — does it sync to my calendar?" That's H-002-adjacent — we'd assumed export was sufficient; calendar integration is a stronger signal.

### Surprises

- P3 trusted the AI's rationale on 11 of 12 findings without going back to the original clause text. We'd expected ~50% trust at this stage.
- P3 estimated the review took "about 20 minutes" — actual elapsed was 22 minutes. Well inside H-002's 25-minute threshold.

## Quotes

> "If this saved me even 30 minutes per contract, at 12 contracts a week, that's 6 hours back. I'd find AU$300/seat in the budget tomorrow."

> "The reason I trust this is it doesn't make me re-read the clause. It quotes the clause, tells me what's wrong with it, and gives me the cap I should ask for. That's the same conversation I have with a colleague."

> "The 'missing protections' thing — I want the drafted language. Without that, I'm doing the work twice."

## Hypothesis touch-points

| Hypothesis | Outcome | Evidence |
|------------|---------|----------|
| H-001 (demand) | confirm | P3 willingness-to-pay quote at AU$300/seat. n=1; not yet validating. |
| H-002 (usability) | confirm | 22-minute end-to-end review, inside the 25-minute threshold. n=1. |
| H-003 (precision) | ambiguous | P3 rejected 5 of 12 findings. Reject rate 42% — too high to call precision, too small a sample to call low. Need 14-category breakdown across ≥3 sessions. |

## Follow-ups

- Schedule session 002 with Aubergine Health GC (already committed) for 2026-05-29.
- Draft a feature note: "draft language for missing-protection clauses" — add to the H-002 follow-on backlog, not the MVP.
- Investigate calendar integration as a Keep-stage feature (out of scope for the H-002 prototype).
- P3 offered to introduce us to the Head of Legal at a 200-staff manufacturer in their network — schedule warm intro.
