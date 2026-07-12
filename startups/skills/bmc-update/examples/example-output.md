---
title: Business Model Canvas v2
slug: bmc-v2
type: bmc
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-07-09
---

# Business Model Canvas v2

> v1 was honest (all-hypothesis). v2 lands H-001 (demand) as a fact
> after 22 customer-development interviews, and refutes the original
> H-004 (procurement as a buying centre). One cell change, no pivot.

## Customer Segments

- Head of Legal / General Counsel at AU/NZ mid-market companies, 50–500 staff, AU$10M–AU$200M revenue `[fact]` — see [LC-001](../02-customer-discovery/learning-cards/LC-001.md) (H-001 confirmed across 22 interviews; 14 of 22 expressed willingness to pay ≥ AU$300/seat/month)
- ~~Procurement managers at the same companies~~ `[refuted]` — see [LC-002](../02-customer-discovery/learning-cards/LC-002.md) (H-004 refuted: procurement evaluates only after legal recommends; they are influencers, not buyers)

## Value Propositions

- Redline a 40-page MSA in ≤ 20 minutes, vs. 3 hours manual `[hypothesis]` — see H-002 (usability, TC-002 running)
- AU/NZ-specific risk flagging (PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018) `[hypothesis]`
- Obligation-deadline extraction into calendar + dependency graph `[hypothesis]`

## Channels

- Direct outbound to Head of Legal via LinkedIn `[hypothesis]`
- Referrals from AU corporate law firms `[hypothesis]`
- Content / SEO on AU/NZ contract-law pain `[hypothesis]`

## Customer Relationships

- Concierge onboarding for first 10 pilots `[hypothesis]`
- Self-serve from customer 11 onward, quarterly check-in `[hypothesis]`

## Revenue Streams

- AU$300 per seat per month, 1–5 seats per company `[fact]` — see [LC-001](../02-customer-discovery/learning-cards/LC-001.md) (14 of 22 willing at this band; 3 willing above AU$400; 5 below AU$200 — workable range)

## Key Resources

- AU/NZ MSA training corpus `[hypothesis]`
- LLM clause-classifier model + the prompts / rubrics `[hypothesis]` — see H-003
- Priya's GC network `[fact]` — same as v1

## Key Activities

- Build and ship the redline tool `[hypothesis]`
- AU/NZ clause-classifier training, evaluation, and refresh `[hypothesis]`
- Pilot acquisition and concierge onboarding `[hypothesis]`

## Key Partnerships

- Microsoft Word / Office add-in distribution `[hypothesis]`
- Anthropic API (LLM inference) `[fact]` — same as v1
- Supabase (auth + RLS-scoped contract storage) `[hypothesis]`

## Cost Structure

(unchanged from v1; see [bmc-v1](bmc-v1.md))

## Changelog

### 2026-07-09 — v1 → v2

- **Customer Segments** — "Head of Legal / GC at AU/NZ mid-market"
  `[hypothesis]` → `[fact]` (evidence: [LC-001](../02-customer-discovery/learning-cards/LC-001.md), driven by H-001)
- **Customer Segments** — removed: "Procurement managers at the same
  companies" `[hypothesis]` (refuted by [LC-002](../02-customer-discovery/learning-cards/LC-002.md), H-004 refuted —
  procurement is an influencer, not a buyer; do not segment them
  separately)
- **Revenue Streams** — "AU$300 per seat per month"
  `[hypothesis]` → `[fact]` (same evidence as H-001; the demand
  hypothesis bundles the price band)

## Notes

- Predecessor: [bmc-v1](bmc-v1.md) (now `status: superseded`)
- Hypotheses driving this version: H-001 (now `accepted`), H-004 (now `refuted`)
- Pivot implied? **No** — only one substantive cell touched (Customer
  Segments). The procurement-as-segment removal is a refinement, not a
  pivot. Skip `/pivot-refine-log`.
- Cascading updates required: refresh `04-competitors/uvp.md` (the UVP
  template referenced the procurement secondary segment); refresh
  `vpc-in-house-counsel-v1.md` BMC linkage to v2.
