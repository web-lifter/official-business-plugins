---
title: Revenue / cost sketch for BMC v1
slug: revenue-cost-sketch-v1
type: bmc
status: draft
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Revenue / cost sketch — BMC v1

This is a sketch, not a financial model. Pre-revenue, pre-MVP. Brackets
only. Run `business-economics/unit-economics` once we have a paid
pilot, a month of Anthropic billing, and a real go-to-market plan.

## Revenue

### Per segment

| Segment | Archetype | Price range | Willingness-to-pay | Confidence |
|---|---|---|---|---|
| In-house counsel (primary) | Subscription, per seat | AU$200–AU$450 / seat / month | High (per interview-001 with P3) | Medium — n=4 interviews so far |
| Procurement managers (secondary) | Subscription, per seat (lower tier) | AU$80–AU$150 / seat / month | Medium | Low — no interviews yet |

H-001 anchors the in-house counsel band at AU$300/seat/month. Spellbook's
public pricing (when contacted, "starts ~US$199/lawyer/month for
transactional teams") and LawGeex's enterprise-only pricing (no public
number; estimated from G2 reviews at US$10k–$30k annual minimum) bracket
the market.

### Per-contract surcharge (alternative archetype to test)

- AU$10–AU$25 per contract reviewed beyond an included monthly volume.
  Mirrors Spellbook's add-on model. Not in BMC v1 — surfaced here for
  H-005 (proposed).

## Costs

### Fixed (per month)

- Engineering — Tom full-time + part-time Word add-in contractor: AU$18k–AU$26k
- AU/NZ legal review of classifier rubric (external counsel quarterly): AU$1k–AU$1.5k amortised monthly
- SaaS tooling (Linear, GitHub, PostHog Cloud EU, Sentry): AU$300–AU$500
- Founder salary (Priya, deferred): AU$0 currently, AU$8k–AU$12k from month 7

### Variable (per customer / per unit)

- LLM inference (Anthropic) per 40-page MSA reviewed: AU$0.40–AU$1.20 at current Claude pricing
- Supabase storage + Cloudflare bandwidth per active org: AU$2–AU$8 / month
- Concierge onboarding labour for first 10 pilots: AU$300–AU$600 per pilot one-off

### One-time

- Word add-in store registration + Microsoft Partner Network: AU$500–AU$1.5k
- Pilot agreement legal templates (own counsel): AU$2k–AU$3k
- AU/NZ corpus build (anonymised contract collection + tagging): AU$4k–AU$8k
- Brand and domain (already secured: `contractiq.com.au`): AU$200 one-off, AU$80/year renewal

## Hypotheses surfaced

- **H-001** (already registered, demand): AU$300/seat/month is acceptable to ≥ 30% of 20 interviewees. Drives the revenue archetype choice.
- **H-005** (proposed, pricing structure): Per-contract surcharge above an included volume captures more revenue than flat seat pricing. Falsifier: < 20% of pilots in round 2 exceed their included volume.
- **H-006** (proposed, COGS): Anthropic inference cost remains ≤ AU$1.50 per 40-page MSA at production prompt depth. Falsifier: median cost > AU$2.50 across the first 100 reviewed contracts.
- **H-007** (proposed, fixed costs): External counsel rubric review can be quarterly (not monthly) without classifier drift. Falsifier: precision drops > 5% between quarterly reviews on the held-out test set.

When ≥ 1 paid pilot is live and Anthropic billing is real, hand off to
`business-economics/unit-economics` for the modelled view; this sketch
should be linked from there.
