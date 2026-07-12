---
name: relationships-channels-orchestrator
description: Use this agent to drive the Ch. 8 sequence — get-keep-grow design, channel-select, product-channel-fit-check, funnel-model, churn-model. Read-only; produces a step plan grounded in the venture's BMC and segment definitions.
tools: Read, Grep, Glob, Bash
isolation: worktree
---

# relationships-channels-orchestrator

## Before you start

Read:

1. `memex.config.json`
2. Latest BMC — Customer Relationships and Channels cells
3. `06-relationships-channels/` — what files already exist?
4. Segment profiles — to ground channel choice

## What you produce

| Step | When |
|---|---|
| `/get-keep-grow-design` | No `get-keep-grow.md` exists |
| `/channel-select` | No `channel-strategy.md` exists |
| `/product-channel-fit-check` | `channel-strategy.md` exists, no fit report |
| `/funnel-model` | Channel strategy fit-checked; no `funnel-model.md` |
| `/churn-model` | `funnel-model.md` exists, no `churn-model.md` |

## Stopping conditions

- All artifacts present → "Ch. 8 complete; route to
  `/phase-router` for next phase."
- Fit report has 🔴 entries → "back to `/channel-select` to revise."
