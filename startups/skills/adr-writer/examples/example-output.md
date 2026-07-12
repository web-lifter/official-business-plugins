---
title: ADR-001 — Adopt Next.js 15 + Supabase + Cloudflare Workers for ContractIQ MVP
slug: ADR-001-tech-stack
type: adr
status: accepted
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# ADR-001 — Adopt Next.js 15 + Supabase + Cloudflare Workers for ContractIQ MVP

## Context

ContractIQ is pre-MVP. The primary hypothesis under test is H-002 (a senior in-house counsel can produce a redline in under 25 minutes using the tool). The MVP must let an authenticated user upload a `.docx` or `.pdf`, run an LLM-backed clause classifier, present findings, and export a tracked-changes redline.

The founding team is two people (Priya Natarajan, ex-GC; Tom Whitaker, CTO). Time-to-MVP matters more than long-run scale. The customer-facing surface is a logged-in web app — no mobile, no API. Document parsing and LLM orchestration are CPU/latency-heavy and must not block the page render.

Australian data-residency is not a strict requirement for the MVP (interview subjects accepted Cloudflare's APAC edge), but PII handling under the Privacy Act 1988 is in scope.

## Decision

Adopt **Next.js 15 (App Router) on Vercel** for the web front-end, **Supabase** for Postgres + Auth + Storage, and **Cloudflare Workers** for LLM orchestration and the document-parsing queue. Domain on `contractiq.com.au`.

## Consequences

### Positive
- Speed to MVP: estimated 6–8 weeks for the H-002 testable slice (vs. 12+ on a self-hosted stack).
- Built-in RLS in Supabase Postgres maps cleanly onto the org-scoped multi-tenant model required for in-house legal teams.
- Cloudflare Workers + Durable Objects support the streaming LLM responses the redline UX needs.

### Negative
- Two infra vendors to manage (Vercel + Cloudflare) plus Supabase — three control planes for a two-person team.
- Vercel Edge runtime does not support some Node-native libraries the document parser may need; this pushes parsing onto Workers, increasing latency.
- Cloudflare Workers' 30s CPU ceiling on the paid plan caps single-document processing.

### Neutral
- LLM calls go through Anthropic's API; vendor risk shifts to Anthropic for the classifier accuracy that underpins H-003.

## Alternatives considered

### Alternative 1: Remix + self-hosted Postgres on Fly.io
- **Summary:** Full-stack Remix, single-region Postgres on Fly.io, no Cloudflare.
- **Why we did not pick it:** Auth, storage, and RLS would need to be built — adds three to four weeks. Loses the Supabase MCP integration that the Web Lifter plugin family depends on.

### Alternative 2: SvelteKit + Supabase + Vercel
- **Summary:** Same data layer, SvelteKit front-end.
- **Why we did not pick it:** Tom's prior production experience is React; no team-fit advantage; shadcn/ui (the chosen component library) is React-only.

## Status

`accepted` as of 2026-05-21.

## Linked

- Tech stack: [tech-stack](../tech-stack.md)
- MVP spec: [mvp-spec](../mvp-spec.md)
- Architecture: [architecture-overview](architecture-overview.md)
- Related ADRs: ADR-002 (RLS tenancy model), ADR-003 (LLM orchestration on Workers)
