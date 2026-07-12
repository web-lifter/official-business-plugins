---
title: Business Model Canvas v1
slug: bmc-v1
type: bmc
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Business Model Canvas v1

> v1 is honest: pre-revenue, pre-MVP, all cells default to `hypothesis`
> unless backed by a concluded learning card. Founder Priya Natarajan
> spent 14 years as a GC at AU mid-market SaaS; tech co-founder Tom
> Whitaker has shipped the Streamlit prototype. Only two facts so far,
> both back-stage.

## Customer Segments

- Head of Legal / General Counsel at AU/NZ mid-market companies, 50–500 staff, AU$10M–AU$200M revenue `[hypothesis]` — see H-001 (demand, open)
- Procurement managers at the same companies who own supplier-onboarding flow `[hypothesis]` — secondary; see H-004 (proposed)

## Value Propositions

- Redline a 40-page MSA in ≤ 20 minutes, vs. 3 hours manual `[hypothesis]` — see H-002 (usability, open)
- AU/NZ-specific risk flagging (PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018) `[hypothesis]` — differentiates from Spellbook (US-centric); see `04-competitors/uvp.md`
- Obligation-deadline extraction into calendar + dependency graph `[hypothesis]` — surfaced by interview-001 (anonymised, P3) but not yet a fact

## Channels

- Direct outbound to Head of Legal via LinkedIn `[hypothesis]`
- Referrals from AU corporate law firms (warm-intro path) `[hypothesis]`
- Content / SEO on AU/NZ contract-law pain (PPSA risk, auto-renewal traps) `[hypothesis]`

## Customer Relationships

- Concierge onboarding for first 10 pilots (Priya runs the kick-off herself) `[hypothesis]`
- Self-serve from customer 11 onward, with quarterly check-in `[hypothesis]`

## Revenue Streams

- AU$300 per seat per month, 1–5 seats per company `[hypothesis]` — see H-001 falsifier (≥ 30% willingness-to-pay across 20 interviewees)

## Key Resources

- AU/NZ MSA training corpus (founder's anonymised archive + public AustLII) `[hypothesis]`
- LLM clause-classifier model + the prompts / rubrics `[hypothesis]` — see H-003 (scale, open)
- Priya's GC network (privileged access to the buyer's decision loop) `[fact]` — verified by 11 warm-intro conversations already booked

## Key Activities

- Build and ship the redline tool (`.docx` → tracked-changes output) `[hypothesis]`
- AU/NZ clause-classifier training, evaluation, and refresh `[hypothesis]`
- Pilot acquisition and concierge onboarding `[hypothesis]`

## Key Partnerships

- Microsoft Word / Office add-in distribution `[hypothesis]` — required to meet legal teams where they already work
- Anthropic API (LLM inference) `[fact]` — committed; pricing modelled in `revenue-cost-sketch-v1.md`
- Supabase (auth + RLS-scoped storage of confidential contracts) `[hypothesis]` — committed pending security review by pilot customer

## Cost Structure

- Engineering (Tom full-time, contractor on the add-in) `[hypothesis]` — fixed, ~AU$22k/month
- LLM inference per contract reviewed `[hypothesis]` — variable, estimated AU$0.40–AU$1.20 per 40-page MSA at current Anthropic pricing
- AU/NZ legal review of the classifier rubric (external counsel quarterly) `[hypothesis]` — fixed, ~AU$4k/quarter
- Hosting (Vercel + Cloudflare + Supabase) `[hypothesis]` — fixed/variable mix, ~AU$800/month at 20 customers

## Notes

- Hypotheses driving this version: H-001 (demand), H-002 (usability), H-003 (scale precision)
- Predecessor: none (v1)
- Front/back-stage view: see [bmc-v1-front-back.md](bmc-v1-front-back.md)
- Linked VPC: [vpc-in-house-counsel-v1](../03-value-proposition/vpc-in-house-counsel-v1.md)
- Competitor shadow BMCs to build next: Spellbook, LawGeex
