---
title: Divergent ideation — ContractIQ MVP shape
slug: divergent-2026-05-21
type: prototype
status: draft
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Divergent ideation — ContractIQ MVP shape

Source context: H-001 (demand) and H-002 (usability) — see `01-hypotheses/hypothesis-register.md`.

Goal of this pass: surface a wide range of possible MVP shapes for the clause-classification + obligation-extraction tool before convergence. No critique in this file.

## Ideas (24 total)

### Category: Direct
1. Web app where a Head of Legal uploads a `.docx` MSA and gets a colour-coded clause-classifier UI back. [novelty 2 / stretch 2]
2. Microsoft Word add-in that flags risky clauses in the open document. [novelty 3 / stretch 4]
3. Obligation timeline view — every "Buyer shall…" extracted to a Gantt-style chart with due dates. [novelty 3 / stretch 3]
4. Redline export — generate a `.docx` with tracked changes for the negotiation counterpart. [novelty 2 / stretch 3]

### Category: Inverse
5. Tool that flags *missing* clauses (audit rights, termination-for-convenience) rather than risky ones. [novelty 4 / stretch 2]
6. "Show me what I should have rejected" — post-execution review of contracts already signed. [novelty 4 / stretch 3]
7. Negotiation brief generated *for the business owner*, not the lawyer — counter-stakeholder framing. [novelty 4 / stretch 2]

### Category: Constraint-relaxing
8. Live LLM co-pilot pane that explains each clause in plain English as the GC scrolls. [novelty 3 / stretch 4]
9. Cross-portfolio pattern detection — "you accepted this auto-renewal clause 11 times last quarter." [novelty 5 / stretch 4]
10. Auto-generated negotiation-strategy memo with precedent from the company's own prior MSAs. [novelty 4 / stretch 5]

### Category: Constraint-tightening
11. Zero-frontend: GC emails a `.docx` to `review@contractiq.com.au`; gets a PDF report back in 3 minutes. [novelty 4 / stretch 1]
12. Single-page Streamlit app — upload, classify, download. No accounts, no DB. [novelty 2 / stretch 1]
13. Slackbot — `/contractiq <attachment>` returns inline findings. [novelty 3 / stretch 2]
14. Manual: founder Priya reviews the contract herself overnight and emails the report (Wizard of Oz). [novelty 5 / stretch 1]

### Category: Cross-domain
15. Borrow GitHub PR review UI — clauses as "diff hunks" with inline comments. [novelty 4 / stretch 3]
16. Borrow Grammarly's right-rail suggestion model. [novelty 3 / stretch 3]
17. Borrow tax-software wizard pattern — "answer 6 questions, we tell you the 3 clauses to renegotiate." [novelty 4 / stretch 3]
18. Borrow radiology second-opinion AI: GC submits, AI flags, GC approves/rejects per finding. [novelty 5 / stretch 3]

### Category: Strange
19. Audio: GC reads the contract aloud; we transcribe and flag in real time. [novelty 5 / stretch 5]
20. Gamify it — "you saved your company AU$42k this quarter from clauses you would have missed." [novelty 4 / stretch 2]
21. Make the contract negotiate itself — autonomous-agent redline against a known counter-party. [novelty 5 / stretch 5]
22. Physical: print contracts with QR-coded clauses that link to risk explanations. [novelty 5 / stretch 4]
23. Calendar-first: ContractIQ shows up as a Google Calendar with obligation deadlines, no contract UI at all. [novelty 5 / stretch 3]
24. The product is the negotiation brief; the classifier is hidden infrastructure. [novelty 4 / stretch 2]

## Top 5 by novelty (for converge-ideas)

1. (#9) Cross-portfolio pattern detection
2. (#18) Radiology-style approve/reject-per-finding UI
3. (#21) Autonomous-agent redline
4. (#22) QR-coded printed contracts
5. (#23) Calendar-first obligation view

## Meta-findings

- A strong theme emerged: separating the *classifier* (back-end ML) from the *workflow* (how the GC interacts) is where most of the novelty lives.
- The Wizard-of-Oz variant (#14) is cheap enough that we should pair it with whichever finalist wins convergence as a hypothesis-test fallback.
