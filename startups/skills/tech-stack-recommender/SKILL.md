---
name: tech-stack-recommender
description: Score candidate stacks against the venture's hypothesis class (demand / usability / scale) and recommend a default. Defaults to Next.js 15 + Supabase + Cloudflare Workers + Vercel + Figma; accepts override. Outputs a comparison matrix and rationale.
argument-hint: [optional: --override=<stack-keyword>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# tech-stack-recommender

Idempotency: side-effect-free planner; rewrites `09-mvp/tech-stack.md` in place. Stack changes should be paired with a fresh ADR via `/adr-writer`.

Delegation chain: called by `/mvp-tech-plan`; precedes `/architecture-design` and `/adr-writer`.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `09-mvp/mvp-spec.md`, `mvp-metrics.md`, primary segment
   profile, latest BMC. The hypothesis class drives the
   recommendation.
3. Read `09-mvp/tech-stack.md` if it exists — for upgrades / pivots.

## Phase 2: Classify the hypothesis class

What is the MVP testing first?

- **Demand** — pre-order / audience / show-and-tell types. The stack
  needs to ship a marketing site fast and instrument funnel events.
- **Usability** — partial product type. The stack needs sign-up,
  auth, the core value flow, and instrumentation.
- **Scale** — uncommon at MVP stage. Only relevant when the
  hypothesis is "the system handles X load."

## Phase 3: Score candidate stacks

Default candidate set (override if `--override`):

1. **Next.js 15 + Supabase + Vercel + Cloudflare** — the Web Lifter
   default. Wins on speed-to-MVP for SaaS / consumer web.
2. **Astro + Supabase + Cloudflare Pages** — wins for content-heavy
   landing-page MVPs.
3. **Remix + PostgreSQL + Fly.io** — alt; less integrated.
4. **SvelteKit + Supabase + Vercel** — alt for teams that prefer
   Svelte.
5. **Mobile-only (Expo + Supabase)** — when the segment uses mobile
   exclusively.

Score each on:

- Speed to MVP (days)
- Cost at MVP scale (per month)
- Connector ecosystem (does the rest of this marketplace's plugins
  work with it?)
- Team fit (familiarity)

The Web Lifter default is recommended by default. Other stacks need a
deliberate reason.

## Phase 4: Write

Write `09-mvp/tech-stack.md`:

```markdown
---
title: Tech stack
slug: tech-stack
type: adr
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Tech stack

Hypothesis class: demand | usability | scale
MVP type: <type>

## Recommended

**<stack name>** — Next.js 15 + Supabase + Vercel + Cloudflare
Workers + Figma (default).

### Rationale

- <why this stack for this hypothesis class>
- <connector ecosystem fit>
- <team fit>

## Alternatives considered

| Stack | Speed | Cost | Connectors | Team fit | Total |

## Decision

Adopting <stack>. Rationale above. ADR to follow via `/adr-writer`.

## Connector consequences

- Supabase MCP available → schema work via
  `supabase-schema-design`, migrations via `migration-plan`
- Cloudflare MCP available → deploy plan via `cloudflare-deploy-plan`
- Vercel CLI → deploy plan via `vercel-deploy-plan` (no MCP, plan
  only)
- Figma MCP available → design handoff via `figma-design-handoff`
```

## Phase 5: Cascade

Recommend `/adr-writer "tech stack decision"` to formalise as an ADR
under `09-mvp/architecture/`.

## Phase 6: Log

Append: `## [<today>] tech-stack | <stack> recommended`.

## Important principles

- **Default is opinionated.** The Web Lifter default works for ~80% of
  MVPs. Override when there's a real reason.
- **Connector ecosystem is a tie-breaker.** Skills downstream depend
  on the stack choice.
- **Read-only on the venture.** Writes only `tech-stack.md`.
- **No connector calls.** This skill is local-only.
