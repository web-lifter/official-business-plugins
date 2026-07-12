---
name: migration-plan
description: Sequence migrations for a green-field MVP — bootstrap, seed data, RLS, edge functions, types regeneration. Pairs with supabase-schema-design. Optionally orchestrates apply_migration calls via the connector-confirmation flow.
argument-hint: [optional: --apply-through=<migration-N>]
allowed-tools: Read Write Edit Glob Grep AskUserQuestion
effort: medium
---

# migration-plan

Cites the connector-confirmation idiom in
[`shared/reference/connector-confirmation.md`](../../../../shared/reference/connector-confirmation.md).

Idempotency: destructive on re-run when `--apply-through` is used; refuses to re-apply migrations already in `list_migrations`. Without `--apply-through` it is side-effect-free.

Graceful degrade: without the Supabase MCP the skill prints the SQL plan and the user applies it via `supabase db push` or the dashboard SQL editor.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `09-mvp/schema/migrations-plan.md`. Halt if missing — route to
   `/supabase-schema-design`.
3. If Supabase MCP available, call `list_migrations` to see what's
   already applied.

## Phase 2: Compose execution plan

For each migration not yet applied:

- Order (must be sequential)
- Pre-conditions (extensions, prior migrations)
- Estimated runtime (read-only check via `list_tables` — empty schema
  = fast; non-empty = caution)
- Rollback procedure (CREATE TABLE → DROP TABLE; ALTER → REVERSE
  ALTER)
- Risk class (`low` — additive; `medium` — alters existing; `high` —
  drops or destructive)

## Phase 3: Display plan

Print the plan to chat in markdown. The user reviews each migration
before any apply.

## Phase 4: Optional — apply gated

If `--apply-through=<N>` is passed:

For each migration `1..N`:

1. Build preview (full SQL diff, project ref, branch, rollback).
2. `AskUserQuestion` with "Yes, apply" / "No, abort."
3. If yes:
   - Call `apply_migration` via the Supabase MCP.
   - On success, log the migration name to `.memex/log.md`.
   - On failure, surface the error, do not proceed.
4. If no, log the abort and stop.

## Phase 5: Generate types

After successful migrations, optionally call
`generate_typescript_types` (read-only) and write the output to the
project at the path the tech-stack ADR specifies (default
`src/lib/database.types.ts` for Next.js).

## Phase 6: Log

Append: `## [<today>] migration-plan | <applied> of <N> migrations
applied`.

## Important principles

- **Preview before each apply.** The connector-confirmation idiom is
  non-negotiable.
- **Sequential apply.** No skipping migrations.
- **Rollback documented.** If migration N fails, the user knows what
  to revert.
- **Types regenerated after schema changes.** Otherwise the codebase
  drifts.
