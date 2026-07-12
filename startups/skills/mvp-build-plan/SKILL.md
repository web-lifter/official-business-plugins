---
name: mvp-build-plan
description: Translate mvp-spec.md into a sprint plan — features → tickets → estimates, paired to hypotheses. Delegates to software-development/plan-orchestrator (upstream) for the parallel multi-agent coverage check when an audit-grade plan is needed.
argument-hint: [optional: --use-orchestrator]
allowed-tools: Read Write Edit Glob Grep Agent
effort: high
---

# mvp-build-plan

Idempotency: safe to re-run; rewrites `09-mvp/build-plan.md` in place. Re-runs after material scope changes are expected.

Delegation chain: optionally hands the ticket list to upstream `software-development/plan-orchestrator` via the Agent tool when `--use-orchestrator` is passed.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `09-mvp/mvp-spec.md` (must exist, status `active`).
3. Read `09-mvp/mvp-metrics.md`, `09-mvp/tech-stack.md` (if exists),
   `09-mvp/architecture/ADR-*.md` (if exist), `09-mvp/schema/*` (if
   exist).
4. If `tech-stack.md` is missing, refuse and route to `/mvp-tech-plan`
   first — without a tech stack, sprint estimates are noise.

## Phase 2: Decompose features into tickets

For each `keep` feature in `mvp-spec.md`:

- Decompose into 1-5 tickets (sized small enough to ship in ≤ 2 days)
- Each ticket has:
  - Title
  - Acceptance criteria (3-5 bullet points)
  - Dependencies (other tickets / external)
  - Estimate (XS / S / M / L; rough day-equivalents)
  - Hypothesis link (which hypothesis does this ticket help test)

## Phase 3: Sequence

Order tickets:

1. **Foundations** — env / repo / CI / auth (if needed); blocking
   everything else
2. **Core value flow** — the path that actually tests the primary
   hypothesis
3. **Instrumentation** — events from `mvp-metrics.md`
4. **Polish** — only what the demo needs; no gold-plating
5. **Launch** — landing page / marketing copy / payment / support
   channel

## Phase 4: Optional — invoke plan-orchestrator

If `--use-orchestrator` is passed, hand off the ticket list to
`software-development/plan-orchestrator` (upstream) for a parallel
multi-agent coverage check across the codebase. Use the Agent tool to
invoke the appropriate sub-agents.

## Phase 5: Write

Write `09-mvp/build-plan.md`:

```markdown
---
title: MVP build plan
slug: mvp-build-plan
type: mvp-spec
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# MVP build plan

Source: [mvp-spec](mvp-spec.md)
Tech stack: [tech-stack](tech-stack.md)

## Foundations

| Ticket | AC | Deps | Estimate |

## Core value flow

| Ticket | AC | Deps | Estimate | Hypothesis |

## Instrumentation

| Ticket | AC | Deps | Estimate | Metric |

## Polish

| Ticket | AC | Deps | Estimate |

## Launch

| Ticket | AC | Deps | Estimate |

## Total estimate

- Days: <rough sum>
- Calendar: <accounting for review / blockers / 60% productive ratio>

## Risks

- <ticket>: <risk> — <mitigation>
```

## Phase 6: Log

Append: `## [<today>] mvp-build-plan | <ticket-count> tickets`.

## Important principles

- **Tickets ≤ 2 days each.** Bigger tickets always slip.
- **Every ticket links to a hypothesis or a foundation.** No vanity
  tickets.
- **Polish is bounded.** The demo-quality bar, not production
  finish.
- **Calendar > sum of estimates.** Apply the 60% productive ratio.
- **Plan-orchestrator is optional.** For solo dogfood ventures it's
  overkill; for multi-engineer ventures it's worth the parallel check.
