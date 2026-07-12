---
title: Auth model
slug: auth-model
type: adr
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Auth model

**Pattern:** `saas` — users belong to one or more `orgs`; all domain data is RLS-scoped on `org_id`.
**Tech:** Supabase Auth + Postgres RLS.

## Tables

```sql
-- auth.users is Supabase-managed; we mirror identity into public.profiles
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  full_name text,
  created_at timestamptz default now()
);

create table public.orgs (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  abn text,                          -- Australian Business Number
  plan text default 'trial' check (plan in ('trial','starter','growth')),
  created_at timestamptz default now()
);

create table public.memberships (
  org_id uuid not null references public.orgs(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  role text not null check (role in ('owner','counsel','viewer')),
  invited_at timestamptz,
  joined_at timestamptz,
  primary key (org_id, user_id)
);

create index memberships_user_idx on public.memberships(user_id);
create index memberships_org_idx on public.memberships(org_id);
```

## Triggers

```sql
-- New auth user gets a profile row automatically
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer as $$
begin
  insert into public.profiles (id, email, full_name)
  values (new.id, new.email, new.raw_user_meta_data->>'full_name');
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();
```

## RLS policies

| Table | Operation | Policy |
|-------|-----------|--------|
| profiles | select | `auth.uid() = id` |
| profiles | update | `auth.uid() = id` |
| orgs | select | `public.is_member(id)` |
| orgs | update | `public.has_role(id, 'owner')` |
| memberships | select | `user_id = auth.uid() or public.has_role(org_id, 'owner')` |
| memberships | insert | `public.has_role(org_id, 'owner')` |
| contracts | select | `public.is_member(org_id)` |
| contracts | insert | `public.is_member(org_id)` |
| findings | select | `exists (select 1 from contracts c where c.id = contract_id and public.is_member(c.org_id))` |

All tables have `alter table … enable row level security;` — including `memberships` and `orgs`. No public-read tables in the MVP.

## RPC helpers

```sql
create or replace function public.is_member(p_org_id uuid)
returns boolean language sql security definer stable as $$
  select exists (
    select 1 from public.memberships m
    where m.org_id = p_org_id and m.user_id = auth.uid() and m.joined_at is not null
  );
$$;

create or replace function public.has_role(p_org_id uuid, p_role text)
returns boolean language sql security definer stable as $$
  select exists (
    select 1 from public.memberships m
    where m.org_id = p_org_id and m.user_id = auth.uid() and m.role = p_role
  );
$$;
```

## Auth flow

- **Sign-up:** OAuth via Google Workspace (primary — most AU/NZ in-house counsel use Workspace). Email + password fallback for non-Workspace customers.
- **Email confirmation:** on for password sign-up; OAuth is implicitly confirmed.
- **Session transport:** cookie-based via `@supabase/ssr` (HttpOnly, Secure, SameSite=Lax). PKCE flow on the client.
- **Org invitation:** owner creates a `memberships` row with `joined_at = null`; invitee follows a signed-URL link, authenticates, and `joined_at` is set.
- **Service role:** used only by Cloudflare Workers when writing classifier findings back to the DB; never exposed to the browser.

## Linked

- Schema: [migrations-plan](../schema/migrations-plan.md) — auth-model migrations are M-04 (orgs + memberships), M-05 (RLS), M-06 (RPC helpers).
- Tech stack: [tech-stack](../tech-stack.md)
- ADR-002: Multi-tenant RLS keyed on `org_id`.
