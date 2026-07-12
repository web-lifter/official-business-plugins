---
title: VPC — AU/NZ mid-market in-house counsel v2
slug: vpc-au-midmarket-inhouse-counsel-v2
type: vpc
status: draft
owner: contractiq
created: 2026-06-04
updated: 2026-06-04
---

# Value Proposition Canvas — AU/NZ mid-market in-house counsel v2

Successor of [`vpc-au-midmarket-inhouse-counsel-v1`](vpc-au-midmarket-inhouse-counsel-v1.md) (now `status: superseded`).

Source segment: [`au-midmarket-inhouse-counsel`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/README.md)
Source profile: [`profile.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/profile.md) (v3 — refreshed 2026-06-02 after Aubergine Health design-partner kickoff)

## Customer profile (right half)

Imported from the segment profile. See [`profile.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/profile.md).

## Value map (left half)

### Products & services

| Product / service | Type |
|-------------------|------|
| AU/NZ-trained clause classifier (14 risky-clause categories) | digital |
| Tracked-changes redline export (`.docx`) | digital |
| One-page negotiation brief (PDF) for the business owner | digital |
| Obligation extractor (every "buyer shall…" → calendar + dependency graph) | digital |
| AU IRAP-equivalent data-handling story (private bucket, AU residency) | service |
| Paid 2-week pilot scope (concierge onboarding by Priya) | service |
| **NEW — MS Word add-in (parity feature set)** | digital |
| **NEW — "Run it on your last 6 MSAs" onboarding flow** | service |

### Pain relievers

| Reliever | Mechanism | Maps to pain |
|----------|-----------|--------------|
| 20-minute redline on a 40-page MSA | Classifier returns flagged clauses in < 60s | P-01 |
| Auto-renewal sentinel | Critical-finding flag + plain-English impact | P-02 |
| Obligation tracker auto-populated post-signature | NLP extraction + calendar + finance notification | P-03 |
| Private-tenant LLM with AU data residency | Anthropic API via Cloudflare Workers AU region; AU Postgres + Storage | P-04 |
| AU/NZ corpus | Classifier trained specifically on AU/NZ commercial MSAs | P-05 |
| "Second pair of eyes" framing + audit log defence | Findings + brief + decision log usable as audit defence | P-06, **P-07 (new mapping)** |
| **NEW — Word-native review** | Add-in shows findings as Word comments alongside the document | P-01, P-06 (for Word-native counsel) |

### Gain creators

| Creator | Mechanism | Maps to gain |
|---------|-----------|--------------|
| 20-min redline target | Median session time displayed in-product | G-01 |
| Plain-English clause explanations | Business-language explanation per flag | G-02 |
| AU/NZ-trained corpus | (See reliever) | G-03 |
| One-click obligation tracker | NLP extraction → Google/Outlook calendar → Slack reminders | G-04 |
| Audit-defensible decision log | Timestamped accept/reject decisions with rationale; exportable PDF | G-05 |
| Precedent lookup within the tenant | Filterable past-decision search | G-06 |
| Junior-friendly first-pass review mode | Critical + high findings only, with explainer text | G-07 |
| **NEW — "Run it on your last 6 MSAs" onboarding** | Customer uploads back-catalogue; tool produces a side-by-side ("caught what you caught, plus these you didn't") for compressed evaluation | **G-08 — trust threshold met within one session** (new gain from interview-analyse) |

## Diff from v1

### Added

- **MS Word add-in.** Form-factor candidate from `six-ways-to-innovate` (lens 3); confirmed by Aubergine Health design-partner P5 in week-1 feedback ("our team lives in Word; the web app is a context switch").
- **"Run it on your last 6 MSAs" onboarding.** Onboarding-experience candidate (lens 4); P3's explicitly stated trust threshold. Maps to a new gain `G-08 — trust threshold met within one session`.

### Removed

- None.

### Changed

- **"Second pair of eyes" reliever** now also maps to P-07 (embarrassment when finance discovers a missed clause). The audit-log mechanism that creates G-05 also defensively relieves P-07; the v1 fit-check flagged this as a gap.
- **Mechanism text on the obligation tracker** sharpened from "calendar export" to "Google/Outlook calendar + Slack reminders" — based on Aubergine Health design-partner stack.

## Trigger

- Rationale: Aubergine Health design-partner week-1 feedback + customer-profile v3 refresh.
- Linked entry: [`07-validation/pivot-refine-log.md#2026-06-04`](../07-validation/pivot-refine-log.md) (refine — narrow v2 around Aubergine Health observations).

## Notes

- Created from week-1 design-partner feedback (P5 / Aubergine Health) and the candidates surfaced in [`six-ways-au-midmarket-inhouse-counsel-2026-05-21.md`](six-ways-au-midmarket-inhouse-counsel-2026-05-21.md).
- v1 marked `status: superseded` with forward link to this file.
- `vpc-fit-check au-midmarket-inhouse-counsel` runs next automatically.
