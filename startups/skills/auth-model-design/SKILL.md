---
name: auth-model-design
description: Design the auth.users / profiles / roles / RLS-policy stack for typical SaaS patterns. Output is SQL plus a policy table. Supabase MCP optional. Read-only.
argument-hint: [optional: --pattern=user|saas|tenant|marketplace]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# auth-model-design

Idempotency: side-effect-free planner; rewrites `09-mvp/architecture/auth-model.md` in place. Mutations to Supabase happen only via `/migration-plan`.

Graceful degrade: no MCP calls in this skill — design only. Schema introspection (if needed) belongs to `/supabase-schema-design`.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `tech-stack.md`, `mvp-spec.md`, primary segment profile.
3. Default pattern is `user` (one user account per person) unless
   override.

## Phase 2: Pattern selection

Patterns:

- **user**: single user account per person; user-owned data via
  `auth.uid() = user_id`
- **saas**: user accounts within tenants (organisations); RLS uses
  `tenant_id` join
- **tenant**: B2B SaaS with strict tenant isolation; service-role for
  cross-tenant
- **marketplace**: two-sided, separate auth flows or roles per side

## Phase 3: Compose

For the pattern, design:

1. **Tables**: `auth.users` (Supabase-managed), public `profiles`
   (one-to-one with auth.users), `tenants` if applicable, `roles`
   table for RBAC, join tables (`memberships`).
2. **Triggers**: on `auth.users` insert → create matching `profiles`
   row.
3. **RLS policies**: per-table for select / insert / update / delete.
4. **RPC functions**: `current_tenant_id()`, `current_role()` helpers.
5. **Sign-up / sign-in flow**: which Supabase auth methods (email
   magic link, OAuth, password)? Email confirmations on/off?

## Phase 4: Write

Write `09-mvp/architecture/auth-model.md`:

```markdown
---
title: Auth model
slug: auth-model
type: adr
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Auth model

Pattern: <user|saas|tenant|marketplace>
Tech: Supabase Auth + Postgres RLS

## Tables

\`\`\`sql
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  created_at timestamptz default now()
);
\`\`\`

(... more tables for the chosen pattern ...)

## Triggers

\`\`\`sql
create or replace function public.handle_new_user() returns trigger
as $$
begin
  insert into public.profiles (id, email) values (new.id, new.email);
  return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();
\`\`\`

## RLS policies

| Table | Operation | Policy |
|---|---|---|
| profiles | select | auth.uid() = id |
| profiles | update | auth.uid() = id |
| ... |

## RPC helpers

- `current_role()` — returns the role of the current authenticated user
- `is_member(tenant_id)` — checks tenant membership

## Auth flow

- Sign-up via: <email magic link / OAuth / password>
- Email confirmation: on / off
- Session: cookie-based via @supabase/ssr

## Linked

- Schema: [migrations-plan](../schema/migrations-plan.md)
- Tech stack: [tech-stack](../tech-stack.md)
```

## Phase 5: Cascade

Append the auth-model migrations to `09-mvp/schema/migrations-plan.md`
as a separate migration step (typically migrations 4 or 5 in the
sequence).

## Phase 6: Log

Append: `## [<today>] auth-model | <pattern> designed`.

## Important principles

- **RLS, always.** Every public table has RLS.
- **Profiles separate from auth.users.** Don't put PII or app data in
  the auth schema.
- **Triggers for invariants.** New auth.users → matching profiles row.
- **Service role used only for explicit admin endpoints.** Not in
  user-facing routes.
- **Connector calls only via the gated flow.** This skill is mostly
  design; mutating happens through `migration-plan`.
