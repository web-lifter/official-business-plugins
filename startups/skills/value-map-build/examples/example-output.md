---
title: VPC — AU/NZ mid-market in-house counsel v1
slug: vpc-au-midmarket-inhouse-counsel-v1
type: vpc
status: draft
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Value Proposition Canvas — AU/NZ mid-market in-house counsel v1

Source segment: [`au-midmarket-inhouse-counsel`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/README.md)
Source profile: [`profile.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/profile.md)

## Customer profile (right half)

Imported from the segment profile; not duplicated here. See [`profile.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/profile.md).

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

### Pain relievers

| Reliever | Mechanism | Maps to pain |
|----------|-----------|--------------|
| 20-minute redline on a 40-page MSA | Classifier returns flagged clauses in < 60s; counsel walks the flags + accepts/rejects in a structured UI | P-01 (3+ hour late-night reviews) |
| Auto-renewal sentinel | Every auto-renewal clause is surfaced as a critical finding with plain-English impact ("auto-bills $X in N months unless cancelled by D") | P-02 (missed auto-renewal incidents) |
| Obligation tracker auto-populated post-signature | NLP extraction of every "buyer shall…" clause into a calendar + dependency graph + finance-team notification 60 days before each obligation fires | P-03 (no system for post-signature obligations) |
| Private-tenant LLM with AU data residency | Anthropic API via Cloudflare Workers in AU region; Supabase Postgres + Storage in AU; row-level security keyed on `org_id`; no contract content leaves the tenant boundary | P-04 (generic-AI confidentiality concerns) |
| AU/NZ corpus (PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018) | Classifier trained specifically on AU/NZ commercial MSAs with a held-out test set across the 14 risky-clause categories | P-05 (US-corpus tools miss AU-specific issues) |
| "Second pair of eyes" framing | Findings + brief + audit log structurally reduce single-point-of-failure risk; counsel can show the audit log to the business when a clause decision is questioned | P-06 (single-point-of-failure anxiety) |

### Gain creators

| Creator | Mechanism | Maps to gain |
|---------|-----------|--------------|
| 20-min redline target | Median session time displayed in-product; sessions exceeding 25 min logged for product-team review | G-01 (redline in ≤ 20 minutes) |
| Plain-English clause explanations | Every flag includes a 1–2 sentence business-language explanation suitable for forwarding to a non-lawyer | G-02 (plain-English brief for business owner) |
| AU/NZ-trained corpus | (See pain reliever above) | G-03 (AU/NZ-trained corpus) |
| One-click obligation tracker | NLP extraction → calendar export to Google/Outlook → Slack reminders | G-04 (post-signature obligation tracker) |
| Audit-defensible decision log | Every accept/reject decision is timestamped with the user, the clause, and the rationale; exportable as PDF for audit/board review | G-05 (audit-defensible record) |
| Precedent lookup within the tenant | "Show me every NDA we've signed in the last 12 months where we accepted a 5-year survival clause" | G-06 (precedent lookup) |
| Junior-friendly first-pass review mode | A toggle that surfaces only critical + high findings, with explainer text, suitable for a paralegal or junior to walk through first | G-07 (delegate first-pass review) |

## Notes

- Created from the segment profile v2 (post-2026-05-12 refresh).
- No prior VPC version exists; this is v1.
- Fit check (`/vpc-fit-check au-midmarket-inhouse-counsel`) is the next action; expect full fit on `high` priorities, partial on `medium`.
- The precedent-lookup gain creator (G-06) intentionally scopes to the tenant — the cross-company precedent feature raised by 2/7 interviewees in [`interview-summary.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/interview-summary.md) conflicts with the confidentiality positioning and is deferred to a future VPC version.
