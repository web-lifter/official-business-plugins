---
name: mvp-deploy-plan
description: Produce the deployment plan. Delegates to vercel-deploy-plan and cloudflare-deploy-plan. Thin orchestrator.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# mvp-deploy-plan

Idempotency: safe to re-run; thin orchestrator. Re-running re-invokes the sub-skills, each of which rewrites its own file.

Delegation chain: calls `/vercel-deploy-plan` then `/cloudflare-deploy-plan` based on what is in `tech-stack.md`, then cross-checks the two outputs.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `tech-stack.md`, `architecture-overview.md`. Halt if missing.

## Phase 2: Decide which sub-plans to run

Check the tech stack for which platforms apply:

- Vercel in stack → run `/vercel-deploy-plan`
- Cloudflare in stack → run `/cloudflare-deploy-plan`
- Both → run both in sequence

## Phase 3: Sequenced delegation

1. `/vercel-deploy-plan` (if applicable) → produces
   `09-mvp/deploy/vercel.md`.
2. `/cloudflare-deploy-plan` (if applicable) → produces
   `09-mvp/deploy/cloudflare.md`.

## Phase 4: Cross-check

- Env vars listed in Vercel match env vars referenced in Cloudflare
  bindings.
- DNS / domain plan is consistent across both.
- Observability hooks don't double-up.

## Phase 5: Cascade

Recommend `/mvp-feasibility` next.

## Phase 6: Log

Append: `## [<today>] mvp-deploy-plan | written`.

## Important principles

- **Thin.** Delegate to sub-skills.
- **Plan, never deploy.** Reaffirmed in every sub-skill.
- **Cross-check matters.** Misconfigured env vars across platforms
  cause silent failures.
