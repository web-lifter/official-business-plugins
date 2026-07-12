---
name: supabase-schema-design
description: Design the full Supabase schema for the MVP — tables, columns, FKs, indexes, RLS policies, RPC functions, triggers. Uses the Supabase MCP for live introspection when available; gracefully degrades. Mutations gated by connector-confirmation idiom.
argument-hint: [optional: --supabase-project=<ref>]
allowed-tools: Read Write Edit Glob Grep AskUserQuestion
effort: high
---

# supabase-schema-design

Cites the connector-confirmation idiom in
[`shared/reference/connector-confirmation.md`](../../../../shared/reference/connector-confirmation.md). See `references.md` for the RLS / index / FK rules this skill enforces.

Idempotency: side-effect-free planner by default; rewrites `09-mvp/schema/migrations-plan.md` in place. Optional Phase 6 apply is destructive on re-run and refuses to re-apply migrations already in `list_migrations`.

Graceful degrade: without the Supabase MCP the plan is docs-only; the user runs the SQL through `supabase db push` or the dashboard SQL editor.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `09-mvp/schema/entity-list.md` and `09-mvp/schema/erd.mmd`.
   Halt if missing — route to `/data-model-from-vpc`.
3. Read `tech-stack.md` to confirm Supabase is the chosen DB.
4. If Supabase MCP is available and `--supabase-project` is supplied,
   call `list_tables` (read-only) to see what's already there.

## Phase 2: Design tables

For each entity in the entity list, design a table:

- Table name (snake_case plural, e.g. `users`)
- Columns: name, type (`uuid`, `text`, `timestamptz`, `jsonb`,
  `numeric`, `bool`), nullability, default
- Primary key (typically `id uuid default gen_random_uuid()`)
- Foreign keys (with `references ... on delete <action>`)
- Unique constraints
- Indexes (especially for FK columns and frequent query patterns)
- Generated columns where useful

Default conventions:

- `id uuid default gen_random_uuid() primary key`
- `created_at timestamptz default now()`
- `updated_at timestamptz default now()` with a trigger to bump on
  update

## Phase 3: Design RLS policies

For each table, decide the policy class:

- **User-owned** — `auth.uid() = user_id` for select / insert /
  update / delete
- **Public read, owner write** — public select, owner-only write
- **Admin only** — service-role only
- **Per-tenant** — `auth.uid()` lookup + `tenant_id` match

Write the policies in SQL.

## Phase 4: Design RPC functions / triggers

- RPC functions for atomic multi-step writes (e.g. signup + profile
  create)
- Triggers for `updated_at` bumps
- Optional triggers for audit logs / soft deletes

## Phase 5: Write

Write `09-mvp/schema/migrations-plan.md`:

```markdown
---
title: Schema migrations plan
slug: migrations-plan
type: schema
status: draft
owner: <venture name>
created: <today>
updated: <today>
---

# Schema migrations plan

Project: <ref>
Tech stack: [tech-stack](../tech-stack.md)
Entity list: [entity-list](entity-list.md)
ERD: [erd.mmd](erd.mmd)

## Migration sequence

### Migration 1: bootstrap
- Enable extensions (uuid-ossp, pgcrypto)
- ...

### Migration 2: tables
\`\`\`sql
create table public.users (
  id uuid default gen_random_uuid() primary key,
  email text unique not null,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
\`\`\`

### Migration 3: indexes
\`\`\`sql
create index users_email_idx on public.users (email);
\`\`\`

### Migration 4: RLS policies
\`\`\`sql
alter table public.users enable row level security;
create policy "users_select_own" on public.users for select
  using (auth.uid() = id);
\`\`\`

### Migration 5: triggers
- updated_at bump trigger
- ...

### Migration 6: RPC functions
- ...

### Migration 7: seed data
- ...
```

## Phase 6: Optional — apply (gated)

If the user asks to apply migration 1, follow the connector-confirmation
flow:

1. Build the preview block (full SQL diff, project ref, branch,
   rollback steps).
2. Use `AskUserQuestion` with options "Yes, apply" and "No, abort."
3. If yes, call `apply_migration` via the Supabase MCP. On success,
   log the migration to `.memex/log.md`.
4. If no, log the abort.

## Phase 7: Cascade

Recommend `/auth-model-design` and `/migration-plan` next. Recommend
`postgres-schema-audit` (upstream `database-design` plugin) as a
quality check once the schema is stable.

## Phase 8: Log

Append: `## [<today>] supabase-schema | designed (<N> tables, <P> policies)`.

## Important principles

- **Read-only by default.** Listing tables, schema introspection — yes.
  Mutating — only via the gated flow.
- **Every table has RLS.** Never ship a Supabase table with RLS
  disabled (except service-role-only admin tables that are explicitly
  marked).
- **Indexes for FKs.** Postgres doesn't auto-index FKs.
- **Migrations are sequenced.** Bootstrap → tables → indexes → RLS →
  triggers → RPCs → seed.
- **Graceful degrade.** Without the Supabase MCP, the plan is
  docs-driven and the migrations are written for the user to apply
  manually.
