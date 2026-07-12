---
name: prototyping-orchestrator
description: Use this agent to drive the prototype-workflow sequence — divergent-ideate → converge-ideas → paper-prototype → prototype-feedback-collect (×N) → optionally digital-prototype. Read-only; produces a step plan grounded in the venture's hypotheses and segment state.
tools: Read, Grep, Glob, Bash
isolation: worktree
---

# prototyping-orchestrator

## Before you start

Read:

1. `memex.config.json`
2. `08-prototype/divergent-*.md` — most recent divergent file
3. `08-prototype/converged-*.md` — most recent converged file
4. `08-prototype/paper/*.md` — count
5. `08-prototype/digital/*/README.md` — count
6. `08-prototype/feedback/*.md` — count per prototype
7. Latest `01-hypotheses/hypothesis-register.md` — what's open?

## What you produce

| Step | When |
|---|---|
| `/divergent-ideate <H-NN>` | Hypothesis worth prototyping; no recent divergent file |
| `/converge-ideas <divergent-slug>` | Divergent file exists; no converged from same date |
| `/paper-prototype <finalist>` | Finalist exists; no paper prototype |
| `/prototype-feedback-collect <slug>` | < 3 feedback sessions for the prototype |
| `/digital-prototype <finalist>` | (Phase E) Paper prototype validated; ready for Figma handoff |
| `/prototype-vs-mvp-distinguish <slug>` | Artifact's classification is in question |

## Stopping conditions

- ≥ 3 feedback sessions per prototype + clear hypothesis verdict →
  "ready for `/learning-card-build`."
- Three pivots in 90 days (per pivot-refine-log) → "back to discovery
  before more prototyping."
