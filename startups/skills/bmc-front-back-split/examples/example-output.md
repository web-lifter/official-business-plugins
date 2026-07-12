---
title: BMC v1 front/back-stage view
slug: bmc-v1-front-back
type: bmc
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# BMC v1 — front/back-stage

Source: [bmc-v1](bmc-v1.md)

## Front-stage (customer-facing)

### Customer Segments

- Head of Legal / General Counsel at AU/NZ mid-market companies, 50–500 staff, AU$10M–AU$200M revenue `[hypothesis]` — see H-001
- Procurement managers at the same companies `[hypothesis]` — secondary; see H-004

### Value Propositions

- Redline a 40-page MSA in ≤ 20 minutes, vs. 3 hours manual `[hypothesis]` — see H-002
- AU/NZ-specific risk flagging (PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018) `[hypothesis]`
- Obligation-deadline extraction into calendar + dependency graph `[hypothesis]`

### Channels

- Direct outbound to Head of Legal via LinkedIn `[hypothesis]`
- Referrals from AU corporate law firms `[hypothesis]`
- Content / SEO on AU/NZ contract-law pain `[hypothesis]`

### Customer Relationships

- Concierge onboarding for first 10 pilots `[hypothesis]`
- Self-serve from customer 11 onward, quarterly check-in `[hypothesis]`

### Revenue Streams

- AU$300 per seat per month, 1–5 seats per company `[hypothesis]` — see H-001 falsifier

## Back-stage (business-facing)

### Key Activities

- Build and ship the redline tool (`.docx` → tracked-changes output) `[hypothesis]`
- AU/NZ clause-classifier training, evaluation, and refresh `[hypothesis]`
- Pilot acquisition and concierge onboarding `[hypothesis]`

### Key Resources

- AU/NZ MSA training corpus `[hypothesis]`
- LLM clause-classifier model + the prompts / rubrics `[hypothesis]` — see H-003
- Priya's GC network `[fact]` — 11 warm-intro conversations booked

### Key Partnerships

- Microsoft Word / Office add-in distribution `[hypothesis]`
- Anthropic API (LLM inference) `[fact]`
- Supabase (auth + RLS-scoped contract storage) `[hypothesis]`

### Cost Structure

- Engineering (Tom full-time, contractor on the add-in) `[hypothesis]` — fixed, ~AU$22k/month
- LLM inference per contract reviewed `[hypothesis]` — variable, AU$0.40–AU$1.20 per 40-page MSA
- AU/NZ legal review of the classifier rubric `[hypothesis]` — fixed, ~AU$4k/quarter
- Hosting (Vercel + Cloudflare + Supabase) `[hypothesis]` — ~AU$800/month at 20 customers

## Sequencing recommendation

- Front-stage hypotheses are typically cheaper to test (interviews,
  landing pages, fake doors). For ContractIQ, the priority test order is
  H-001 (demand — 20 customer-development interviews, ~3 weeks) then
  H-002 (usability — 5 concierge pilots, ~6 weeks).
- Back-stage hypotheses (Anthropic cost, Word add-in distribution
  partnership, AU/NZ corpus completeness) require vendor conversations
  and the unit-economics sketch from `revenue-cost-sketch-v1.md`.
  Schedule once H-001 has signal.
