---
title: Competitor insights
slug: competitor-insights
type: competitor
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Competitor insights

Generated from 6 competitors (Spellbook, LawGeex, LinkSquares,
general-purpose ChatGPT, manual Word redlining, do-nothing), 3 full
SWOTs (Spellbook, LawGeex, LinkSquares), and 2 shadow BMCs (Spellbook,
LawGeex).

## White space

- **AU/NZ jurisdictional specialisation.** None of the three direct
  competitors flag PPSA, Privacy Act 1988 schedule 1, Modern Slavery
  Act 2018, or FOS / AFCA-specific risks. This is the strongest
  white-space finding and validates the H-008 differentiation
  hypothesis surfaced in `swot-spellbook`.
- **The single in-house counsel persona.** LawGeex and LinkSquares
  assume a multi-stakeholder approval chain. Spellbook assumes a
  firm-with-multiple-lawyers workflow. **Nobody is product-led for the
  solo in-house counsel** — which is exactly the 50–500 staff
  AU mid-market segment.

## Crowded space

- US enterprise CLM + AI review. LinkSquares, Ironclad, ContractPodAi,
  and Spellbook's enterprise tier are all competing for the Fortune
  500 buyer. We should not engage here.
- General-purpose LLM "first-pass" usage. Confidentiality concerns
  block formal adoption but the substitute pressure is real
  (4 of 6 interviewees admit informal use).

## Common weaknesses

- US-centric corpus across all three direct competitors. None train on
  AU/NZ commercial MSAs.
- Heavy implementation footprint (LawGeex playbook authoring,
  LinkSquares CLM onboarding). Mid-market in-house teams cannot
  budget the implementation time.
- No local time-zone support presence in AU/NZ.

## Common strengths

- Mature Word integration (Spellbook especially). We cannot beat them
  on add-in polish in year 1; we must match-and-specialise.
- Funded marketing engines for the US mid-market. We cannot match
  brand spend; we must rely on warm-intro / referral via Priya's
  network.

## Pricing patterns

- Public anchor: Spellbook ~US$199/seat/month for the entry tier
  (≈ AU$300+).
- Enterprise tier opaque (LawGeex, LinkSquares, Spellbook enterprise).
- **AU$300/seat/month for ContractIQ (H-001) sits at the lower edge
  of the visible band** — defensible without being a discount play.

## Channel patterns

- All direct competitors invest in the Microsoft AppSource listing for
  the Word add-in. **First-mover advantage in the AU region of
  AppSource is small but achievable** (Spellbook's AU traction is
  thin per interview signal).
- Spellbook leans on conferences (Legaltech NYC, ILTACON). None of the
  three has visible AU corporate-counsel-event presence.
  ContractIQ-specific opportunity: AusCC, Corporate Counsel Forum.

## Shared risks

- General-purpose LLM commoditisation. Applies to every specialised
  legal LLM. Our defence is the jurisdictional moat plus
  Word-native UX plus the audit trail.
- AU regulatory ambiguity on AI in legal services. Applies to all
  vendors selling into AU; faster guidance favours whichever vendor
  is already present and known when the rules clarify.

## Proposed hypothesis updates

(User approves each before applying via `/hypothesis-register`.)

- [ ] **New H-008** (already drafted in swot-spellbook): AU/NZ
  specialisation produces ≥ 1.5x usefulness uplift over a US-centric
  reviewer in head-to-head MSA review.
- [ ] **New H-009** (already drafted in swot-spellbook): Microsoft
  AppSource AU/NZ listing produces ≥ 8 qualified leads/month at day 90.
- [ ] **New H-010**: Solo in-house counsel at AU mid-market is a
  meaningfully distinct user from the multi-lawyer firm seat — they
  value time-saved and audit-trail more than precedent depth.
  Falsifier: feature-rank exercise with 12 in-house counsel does not
  put time-saved + audit-trail in the top 3.
- [ ] **Update H-004**: refute via [LC-002](../02-customer-discovery/learning-cards/LC-002.md);
  procurement is not a separate buying segment.

Next: run `/hypothesis-register add` for H-008, H-009, H-010 if
approved. Run `/bmc-update` afterwards to bump the BMC if any of those
flip.
