---
title: Competitor discovery — in-house counsel
slug: competitor-discovery-2026-05-21
type: competitor
status: draft
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Competitor candidates — in-house counsel (primary segment)

Sources used: vendor trade publications (Legaltech News, Artificial
Lawyer), G2 / Capterra category listings, AU corporate law conference
speaker rosters (Corporate Counsel Forum 2025), peer recommendations
from 6 customer-development interviewees ("who else have you looked
at?"), and job-to-be-done search queries.

## Direct

| Name | URL | Why it competes |
|---|---|---|
| Spellbook | spellbook.legal | Office add-in for clause review by transactional lawyers. Closest competitor. US-centric corpus. Premium pricing (~US$199/seat/month entry tier per public site). |
| LawGeex | lawgeex.com | Pre-execution contract review for procurement. Workflow-heavy. Enterprise customers (Fortune 500). No published AU/NZ presence. |
| LinkSquares | linksquares.com | CLM-first; review is one feature among many. Enterprise sales motion. |
| Ironclad AI | ironcladapp.com | CLM with AI review module. Crowded space for the buyer's attention even when not the chosen tool. |

## Indirect

| Name | URL | Why it competes |
|---|---|---|
| Harvey | harvey.ai | General-purpose legal LLM; not yet AU-focused but cited by 2 interviewees as "the one we keep getting demoed." |
| Lexis+ AI | lexisnexis.com.au | Research tool with AI Q&A; legal teams have it via firm subscription and use it for ad-hoc clause questions. |
| ContractPodAi | contractpodai.com | Contract lifecycle with negotiation support; enterprise-only. |

## Substitutes

| Name | URL | Why it competes |
|---|---|---|
| General-purpose ChatGPT | chat.openai.com | Free, accessible, *but* raises confidentiality concerns (legal teams cannot upload client contracts without an enterprise plan and DPA). Cited by 4 of 6 peer-recommend interviewees as "what I used the first three times." |
| Microsoft Word "Track Changes" | (built-in) | The actual interface every lawyer lives in. Not a "competitor" in the vendor sense, but is the surface this product must integrate with — see Key Partnerships in BMC v1. |
| Outsourcing to AU corporate law firm | (varies) | Hourly external counsel (AU$450–AU$900/hr) for high-stakes MSAs. Slow, expensive, but the trusted default. |

## Current workaround

- **Manual Word redlining**: ~5 of 6 interviewees do this today.
  Average time: 2.5–3 hours for a 40-page MSA. Cost (loaded) at a
  ~AU$180/hr internal-counsel rate ≈ AU$540 per contract.
- **Lawyer-on-call from a corporate firm**: 3 of 6 interviewees
  escalate ~10–20% of contracts (anything high-value or unusual) to a
  panel firm. Cost: AU$1k–AU$4k per escalation.
- **ChatGPT (consumer or workspace)**: 4 of 6 interviewees have used it
  for "first-pass smell test" on a clause, despite the confidentiality
  concern. Reveals a real latent demand for AU-context AI review.

## Do-nothing

The segment pays a heavy do-nothing cost. From interview-001 (P3, Head
of Legal at a ~120-staff Brisbane edtech):

> "I had a supplier auto-renew us last year. AU$80k. I missed the
> 90-day window because I was reading another contract that Friday
> night. We absorbed it."

Quantified: at least 3 of 6 interviewees can name a specific
auto-renewal, indemnity, or termination clause they missed in the last
24 months. **Estimated do-nothing severity:** AU$30k–AU$120k per missed
clause; ~1–2 misses per year per legal team. This is the strongest
"competitor" for ContractIQ to dislodge — the cost of changing nothing
is high but invisible until it bites.

## Next step

Run `/competitor-table-build` to canonicalise the top six (Spellbook,
LawGeex, LinkSquares, ChatGPT, manual Word redlining, do-nothing) into
the table. Run `/swot-build` for Spellbook, LawGeex, LinkSquares —
those three are the direct competitive set for the BMC's Value
Propositions cell.
