---
name: mvp-schema-plan
description: Translate MVP scope and VPC into a database schema. Sequenced delegation to data-model-from-vpc → supabase-schema-design → optionally upstream database-design/postgres-schema-audit for QA. Thin orchestrator.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# mvp-schema-plan

Idempotency: safe to re-run; thin orchestrator. Sub-skills overwrite their own files.

Delegation chain: `/data-model-from-vpc` → `/supabase-schema-design` → optionally upstream `database-design/postgres-schema-audit`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `mvp-spec.md`, `tech-stack.md`. Halt if either missing.
3. Confirm tech stack includes Supabase (or compatible Postgres
   target).

## Phase 2: Sequenced delegation

1. **`/data-model-from-vpc`** → produces
   `09-mvp/schema/erd.mmd` and `09-mvp/schema/entity-list.md`.
2. **`/supabase-schema-design`** → produces
   `09-mvp/schema/migrations-plan.md` with full SQL.
3. (Optional) **upstream `database-design/postgres-schema-audit`**
   for a QA pass once the schema is stable. Invoke as a sub-skill if
   the upstream plugin is installed.

## Phase 3: Cross-check

- Every entity in `entity-list.md` has a corresponding `create table`
  in `migrations-plan.md`.
- Every relationship in the ERD has a foreign key.
- Every table has RLS or is explicitly admin-only.

If any discrepancy, surface; don't auto-fix.

## Phase 4: Cascade

Recommend `/auth-model-design` and `/migration-plan` next.

## Phase 5: Log

Append: `## [<today>] mvp-schema-plan | <N> tables`.

## Important principles

- **Thin.** Orchestrate, don't duplicate.
- **Cross-check is mandatory.** ERD vs SQL drift is a known bug
  source.
- **Connector calls only via the gated flow.** Schema work that
  mutates Supabase goes through `migration-plan`.
