---
name: tech-stack-recommender
description: Compare viable technology stacks for a startup MVP using the hypothesis, existing system, team, budget and data constraints; recommend the simplest justified option.
argument-hint: "[optional: --override=<stack-keyword>]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

## Runtime preflight

Read [the runtime guide](../../RUNTIME.md) before this workflow.


# tech-stack-recommender

Idempotency: side-effect-free planner; rewrites `09-mvp/tech-stack.md` in place. Stack changes should be paired with a fresh ADR via `/adr-writer`.

Delegation chain: called by `/mvp-tech-plan`; precedes `/architecture-design` and `/adr-writer`.

## Stack selection boundary

The stack described below is a candidate reference architecture, not a default requirement. First inspect the actual product needs, existing system, team skills, traffic, budget and data-residency constraints. Compare a simpler alternative. Pin a currently supported framework/runtime version only after checking its official support policy; do not assume a historical `Next.js 15` example is current. Vercel and Cloudflare are alternatives unless their distinct roles are justified. Available planning skills do not justify choosing a provider.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Resolve the venture workspace as specified in `../../RUNTIME.md`.
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

## Phase 3: Compare the smallest viable options

Compare at least two candidates that fit the requirements. Include a static site,
manual or no-code experiment when testing demand does not require a product.
For an interactive web product, an existing team-supported framework plus a
managed database is a candidate, not an automatic winner. For mobile-specific
needs, compare a native/mobile option separately.

Score delivery effort, total operating cost, data handling, maintainability and
team fit. State weights and evidence; unknowns stay unknown rather than becoming
invented scores. An available connector is not a business requirement. Do not
bundle two hosting platforms unless their separate roles are justified.

Verify current official support and pricing documentation before recommending
specific versions or quoting costs. Without browsing, mark these unverified.

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

**<stack name and version-verification status>**

### Rationale

- <why this stack for this hypothesis class>
- <operating and data constraints>
- <team fit>

## Alternatives considered

| Stack | Delivery effort | Cost evidence | Data/operations | Team fit | Decision |

## Decision

Adopting <stack>. Rationale above. ADR to follow via `/adr-writer`.

## Connector consequences

- Supabase MCP available → schema work via
  `supabase-schema-design`, migrations via `migration-plan`
- Cloudflare MCP available → deploy plan via `cloudflare-deploy-plan`
- Vercel selected → provider-neutral planning via `mvp-deploy-plan`; use actual available tooling only
- Figma MCP available → design handoff via `figma-design-handoff`
```

## Phase 5: Cascade

Recommend `/adr-writer "tech stack decision"` to formalise as an ADR
under `09-mvp/architecture/`.

## Phase 6: Log

Append: `## [<today>] tech-stack | <stack> recommended`.

## Important principles

- Do not claim a stack fits an arbitrary percentage of MVPs.
- Planning is not deployment. Only the plan and its explicit index/log entries
  change; no provider resources are created by this skill.
- Preserve an existing decision unless evidence justifies a replacement.
- Standalone chat without a mounted workspace returns the plan, not a claimed file write.
