---
name: mvp-deploy-plan
description: "Plan deployment for the selected MVP stack, including Vercel or Cloudflare where applicable. Do not provision or deploy."
argument-hint: "[selected stack or venture]"
allowed-tools: Read Write Edit Glob Grep Bash
effort: medium
---

# mvp-deploy-plan

## Runtime preflight

Read [the runtime guide](../../RUNTIME.md) before this workflow.

## User Context

$ARGUMENTS

## Phase 1: Read constraints

Resolve the venture workspace and read `09-mvp/tech-stack.md`, architecture, schema/migration plan, traffic expectations, data residency, budget and rollback requirements. Do not assume any provider is required. See [connector confirmation](../../references/connector-confirmation.md).

## Phase 2: Produce provider plans

For Cloudflare, load the bundled `cloudflare-deploy-plan` workflow when relevant. For Vercel, write `09-mvp/deploy/vercel.md` directly: project/root directory, runtime/framework version to verify, build/output settings, preview/staging/production separation, environment variable names (never values), domains/DNS, database connectivity, migration sequence, observability, smoke checks and rollback. Verify current provider limits using official documentation when available; otherwise label them unverified.

For another host, use the same requirements-based plan and explain the provider-specific verification still needed. There is no bundled `vercel-deploy-plan` skill; do not invoke a nonexistent command. A missing optional connector does not prevent a plan from supplied evidence.

## Phase 3: Cross-check and deliver

Check domain ownership, TLS termination, environment alignment, secrets ownership, stateful dependencies, costs and rollback ordering across providers. Avoid duplicate hosting services without a stated requirement. Produce the [deployment summary](templates/output-template.md), individual provider plans and explicit open questions. Do not mutate resources, execute migrations or deploy as part of planning.
