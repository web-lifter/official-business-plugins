---
title: Shadow BMC — Spellbook v1
slug: shadow-spellbook-v1
type: bmc
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Shadow BMC — Spellbook v1

Tags: every cell entry is `inferred` unless backed by a verifiable
public source.

Source SWOT: [spellbook](../04-competitors/swot/spellbook/README.md)
Source competitor row: [competitor-table.md](../04-competitors/competitor-table.md)

## Customer Segments

- Transactional lawyers at small-to-mid US law firms (5–50 lawyers) `[inferred]`
- In-house legal at US mid-market technology companies `[inferred]` — secondary
- UK and Canadian transactional teams `[inferred]` — overflow from US base

## Value Propositions

- Faster clause review and redlining inside Word `[inferred]`
- US clause library and precedent search `[inferred]`
- "AI that thinks like a deal lawyer" — positioning per their public site `[inferred]`

## Channels

- Direct web (spellbook.legal, content marketing, demo-request flow) `[inferred]`
- Microsoft AppSource listing for the Word add-in `[fact]` — publicly verifiable
- Legaltech conferences and partner-firm referrals `[inferred]`

## Customer Relationships

- Self-serve trial → sales-assisted close `[inferred]`
- Customer success for the firm-tier accounts `[inferred]`

## Revenue Streams

- Subscription, per-seat per-month, ~US$199 entry tier (Lite); enterprise on request `[inferred]` — public pricing page snapshot
- Annual contracts with discount `[inferred]`

## Key Resources

- US-commercial-contract training corpus `[inferred]` — depth is the moat
- Word add-in engineering (Office.js + their LLM orchestration) `[inferred]`
- Funding: Series A/B raised (publicly reported); cash runway `[inferred]`
- Brand and content library `[inferred]`

## Key Activities

- LLM prompt-engineering and clause-classifier training `[inferred]`
- Word add-in maintenance and Office API tracking `[inferred]`
- Sales and content marketing into US transactional law `[inferred]`
- Compliance with US bar guidance on AI in legal services `[inferred]`

## Key Partnerships

- Microsoft (AppSource distribution) `[fact]` — publicly verifiable
- LLM provider (OpenAI / Anthropic / both; not publicly broken out) `[inferred]`
- Legaltech distributors and resellers `[inferred]`

## Cost Structure

- Engineering team (estimated 25–50 staff at funded scale) — fixed `[inferred]`
- LLM inference per review — variable `[inferred]`
- Sales & marketing — likely the largest single line at this funded stage `[inferred]`
- Bar / compliance review of marketing claims — fixed `[inferred]`

## What it suggests for our BMC

- **Cells where their model differs sharply from ours:**
  - *Customer Segments:* they target law firms first; we target in-house
    counsel first. Different decision-maker, different sales motion.
  - *Channels:* they invest heavily in conferences and content; we have
    a warm-intro / referral edge from Priya's GC network — cheaper and
    faster to convert in AU/NZ.
  - *Revenue Streams:* their AU-dollar-equivalent ~AU$300+ tier is
    *exactly* our H-001 willingness-to-pay band, but on a US corpus.
    We can price the same or slightly under and out-specialise.

- **Cells where their model is similar:**
  - Key Partnerships (Microsoft Word distribution) — we will compete
    on the same shelf.
  - Variable-cost shape (LLM inference per contract reviewed).

- **Implications for our hypotheses:**
  - **H-001 (demand)** band of AU$300/seat/month is defensible — it
    aligns with Spellbook's inferred AU-equivalent.
  - **H-008 (proposed in swot-spellbook):** AU/NZ specialisation is
    the wedge. Their shadow BMC has no AU/NZ-specific cell entries.
  - **H-009 (proposed in swot-spellbook):** Microsoft AppSource is a
    shared channel; first-mover advantage in the AU region is small
    but real.

Cross-ref: this shadow BMC feeds `04-competitors/insights.md` together
with shadow BMCs for LawGeex and LinkSquares.
