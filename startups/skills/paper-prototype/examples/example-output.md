---
title: Paper prototype — ContractIQ clause-review pane
slug: paper-contractiq-clause-review
type: prototype
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Paper prototype — ContractIQ clause-review pane

Tests: H-002 (usability) — "a senior in-house counsel can produce a redline in < 25 minutes (median) using the tool, vs. > 90 minutes manual."
Segment: in-house counsel at AU/NZ mid-market (50–500 staff).

## Screens / states

Six screens. Anything beyond seven is a digital prototype trying to escape.

### Screen 1: Upload (first-run)

```
+----------------------------------------------------+
| ContractIQ        [Priya N.]  [Help]               |
+----------------------------------------------------+
|                                                    |
|   Drop a .docx or .pdf MSA here                    |
|   (or click to choose)                             |
|                                                    |
|   [        Drop zone — 60% of screen          ]    |
|                                                    |
|   Last contract: Acme-MSA-v3.docx · 2 days ago     |
+----------------------------------------------------+
```

### Transition 1 → 2
Participant drops `Aubergine-supplier-MSA-v2.docx` (sample contract, 38 pages, prepared on a paper card).

### Screen 2: Processing

```
+----------------------------------------------------+
| Analysing Aubergine-supplier-MSA-v2.docx ...       |
|   [████████████░░░░] 14 of 22 clauses classified   |
|   3 risky · 2 missing protections · 7 obligations  |
+----------------------------------------------------+
```

Wizard-of-Oz note: facilitator counts to ~20 then turns the card.

### Transition 2 → 3
Auto-transition on completion.

### Screen 3: Findings list (left rail) + clause detail (right pane)

```
+--------------------+-------------------------------+
| Findings (12)      | Clause 14.3 — Indemnity       |
|                    |                               |
| [!] 3 Risky        | "Buyer shall indemnify and    |
|  • 14.3 Indemnity  |  hold harmless Seller from    |
|  • 22.1 Auto-renew |  any and all claims..."       |
|  • 8.2 Liability   |                               |
|                    | Why this is risky:            |
| [?] 2 Missing      | Uncapped indemnity with no    |
|  • Audit rights    | knowledge qualifier. Industry |
|  • TFC clause      | norm is capped at fees paid.  |
|                    |                               |
| [⏱] 7 Obligations  | [ Approve ] [ Reject ]        |
|  • 60-day notice   | [ Annotate ] [ Skip for now ] |
|  • Audit timing... |                               |
+--------------------+-------------------------------+
```

### Transition 3 → 4
Participant clicks `[ Reject ]` on clause 14.3.

### Screen 4: Annotation prompt (modal)

```
+----------------------------------------------------+
|  Reject clause 14.3 — why?                         |
|                                                    |
|  ( ) Already negotiated favourably                 |
|  ( ) Not relevant to this deal                     |
|  (•) Need to renegotiate — note for redline:       |
|      [ Cap indemnity at fees paid prior 12mo ]    |
|                                                    |
|  [ Save ]    [ Cancel ]                            |
+----------------------------------------------------+
```

### Transition 4 → 3
Modal closes, return to findings list. Counter updates: `1 of 12 reviewed`.

### Screen 5: Export

```
+----------------------------------------------------+
| All 12 findings reviewed.                          |
|                                                    |
| Export:                                            |
|  [⬇ Tracked-changes .docx]                         |
|  [⬇ Negotiation brief (1 page PDF)]                |
|  [✉ Email both to me]                              |
+----------------------------------------------------+
```

### Transition 5 → 6
Click `Email both to me`.

### Screen 6: Confirmation

```
Sent. Redline and brief in your inbox in 30 seconds.

[Review another contract]
```

## Run-through script

### Setup

"Thanks for trying this out, P3. This is a paper prototype — rough sketches on cards. I'll move the screens as you click. Don't worry about polish; tell me what you'd do at each step. I'd love it if you can think out loud — what you expect to see, what surprises you, where you'd reach for a real Word document instead."

### Task

"Imagine you've just been asked by the procurement team to sign off on this 38-page supplier MSA from a new vendor by tomorrow morning. Walk me through how you'd use ContractIQ to do the review."

### Probes (use as relevant)

- "What did you expect to happen when you dropped the file?"
- "When you saw the three risky-clause findings, what was your first reaction — relief, scepticism, frustration?"
- "On clause 14.3 — would you trust the tool's reasoning, or would you go back to the original text and re-read it yourself?"
- "If this were a real tool, what would have to be true for you to use it on a Friday-morning deadline contract?"
- "Where would you stop and pick up the phone to a colleague instead of the tool?"

### Close

- "Why does this kind of tool matter to you, if at all?"
- "Why wouldn't you use it?"
- "Who else at a similar-sized company should we show this to?"
- "Can we follow up in a fortnight after a few more sessions?"

## Recording

Use `/prototype-feedback-collect contractiq-clause-review` to log each session.
