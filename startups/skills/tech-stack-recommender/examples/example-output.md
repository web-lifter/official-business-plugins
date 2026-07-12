---
title: Tech stack
slug: tech-stack
type: adr
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Tech stack

**Hypothesis class:** Usability (H-002 is primary)
**MVP type:** Partial product

## Recommended

**Web Lifter default — Next.js 15 (App Router) + Supabase + Cloudflare Workers + Vercel + Figma**

### Rationale

- **Speed-to-MVP for the usability slice.** Auth, Postgres, Storage, RLS are first-class via Supabase; the team avoids ~3 weeks of boilerplate. Streaming LLM responses fit naturally on Cloudflare Workers with Durable Objects.
- **Connector ecosystem fit.** The MVP-planning skills downstream (`supabase-schema-design`, `migration-plan`, `cloudflare-deploy-plan`, `vercel-deploy-plan`) all depend on this stack; deviating from the default loses tooling leverage.
- **Team fit.** Tom's prior production experience is React + TypeScript; Priya can read and review the front-end. shadcn/ui — React-only — has the data-table primitives the findings UI needs.
- **AU data-residency story.** Cloudflare APAC edge plus PostHog EU region cover the relevant Privacy Act 1988 obligations without bespoke infra.

## Alternatives considered

Scores out of 5 (higher = better fit for H-002 usability MVP).

| Stack | Speed | Cost | Connectors | Team fit | Total |
|-------|-------|------|-----------|---------|-------|
| **Next.js 15 + Supabase + Vercel + Cloudflare** | 5 | 4 | 5 | 5 | **19** |
| Astro + Supabase + Cloudflare Pages | 3 | 5 | 4 | 3 | 15 |
| Remix + PostgreSQL on Fly.io | 3 | 3 | 2 | 3 | 11 |
| SvelteKit + Supabase + Vercel | 4 | 4 | 4 | 2 | 14 |
| Expo (mobile-only) + Supabase | 2 | 4 | 3 | 1 | 10 |

Astro is the closest second on cost (no Vercel Pro at zero traffic) but loses on the dynamic findings UI — most of the app is authenticated, not content; Astro's SSG-by-default advantage doesn't apply.

## Decision

Adopting the Web Lifter default. ADR-001 to follow via `/adr-writer`.

## Connector consequences

- **Supabase MCP** → schema via `/supabase-schema-design`, apply via `/migration-plan`. Active.
- **Cloudflare MCP** → deploy plan via `/cloudflare-deploy-plan`. Active.
- **Vercel CLI** → deploy plan via `/vercel-deploy-plan` (no MCP — plan only; Tom runs the CLI).
- **Figma MCP** → not in scope for MVP (Tom mocks in shadcn/ui directly; Figma handoff post-H-002).
- **PostHog** has no MCP in this marketplace — analytics planning via `/mvp-analytics-plan` is local-only.

## Risks tied to this choice

- Cloudflare Worker 30 s CPU ceiling vs long classifier runs — tracked as open question `wcfw-cpu-ceiling`.
- Three vendor control planes (Vercel + Cloudflare + Supabase) for a 1.5-FTE team — accepted as cost of speed.
- `@supabase/ssr` cookie handling on Next.js App Router still has rough edges — Tom has prior experience with the pattern.
