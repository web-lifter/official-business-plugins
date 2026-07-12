# Migration execution plan

**Project:** `contractiq-prod` (ref `xkqj…7w2a`)
**Plan source:** [migrations-plan](../schema/migrations-plan.md)
**Generated:** 2026-05-21

## Already applied (from `list_migrations`)

_Empty — fresh project._

## Pending

### M-01 — bootstrap-extensions
- **Risk class:** low (additive only)
- **Pre-conditions:** none
- **Estimated runtime:** < 1 s
- **Rollback:** `drop extension "pgcrypto"; drop extension "uuid-ossp";`

```sql
create extension if not exists "pgcrypto";
create extension if not exists "uuid-ossp";
```

### M-02 — core-tables
- **Risk class:** low (additive only)
- **Pre-conditions:** M-01
- **Estimated runtime:** < 1 s on empty schema
- **Rollback:** `drop table public.findings; drop table public.classifier_runs; drop table public.contracts; drop table public.memberships; drop table public.orgs; drop table public.profiles;`

```sql
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  full_name text,
  created_at timestamptz default now()
);

create table public.orgs (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  abn text,
  plan text default 'trial' check (plan in ('trial','starter','growth')),
  created_at timestamptz default now()
);

create table public.memberships (
  org_id uuid not null references public.orgs(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  role text not null check (role in ('owner','counsel','viewer')),
  invited_at timestamptz default now(),
  joined_at timestamptz,
  primary key (org_id, user_id)
);

create table public.contracts (
  id uuid primary key default gen_random_uuid(),
  org_id uuid not null references public.orgs(id) on delete cascade,
  uploaded_by uuid not null references public.profiles(id),
  title text,
  file_path text not null,
  file_kind text check (file_kind in ('docx','pdf')),
  page_count int,
  status text default 'queued' check (status in ('queued','classifying','ready','failed')),
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table public.classifier_runs (
  id uuid primary key default gen_random_uuid(),
  contract_id uuid not null references public.contracts(id) on delete cascade,
  model text not null,
  started_at timestamptz default now(),
  finished_at timestamptz,
  status text default 'running' check (status in ('running','succeeded','failed')),
  error text
);

create table public.clause_categories (
  id text primary key,
  display_name text not null,
  risk_default text check (risk_default in ('high','medium','low')),
  jurisdiction_tag text check (jurisdiction_tag in ('AU','NZ','generic'))
);

create table public.findings (
  id uuid primary key default gen_random_uuid(),
  contract_id uuid not null references public.contracts(id) on delete cascade,
  run_id uuid not null references public.classifier_runs(id) on delete cascade,
  category_id text not null references public.clause_categories(id),
  clause_text text not null,
  page_number int,
  risk_score numeric check (risk_score between 0 and 1),
  risk_level text check (risk_level in ('high','medium','low')),
  status text default 'pending' check (status in ('pending','accepted','rejected')),
  reviewed_by uuid references public.profiles(id),
  reviewer_comment text,
  reviewed_at timestamptz
);
```

### M-03 — indexes
- **Risk class:** low
- **Pre-conditions:** M-02
- **Estimated runtime:** < 1 s on empty tables
- **Rollback:** corresponding `drop index ...` statements

```sql
create index memberships_user_idx on public.memberships(user_id);
create index memberships_org_idx on public.memberships(org_id);
create index contracts_org_idx on public.contracts(org_id);
create index contracts_status_idx on public.contracts(status);
create index findings_contract_idx on public.findings(contract_id);
create index findings_run_idx on public.findings(run_id);
create index findings_status_idx on public.findings(status);
create index classifier_runs_contract_idx on public.classifier_runs(contract_id);
```

### M-04 — auth trigger
- **Risk class:** medium (definer function — security review note in the audit log)
- **Pre-conditions:** M-02
- **Estimated runtime:** < 1 s
- **Rollback:** `drop trigger on_auth_user_created on auth.users; drop function public.handle_new_user();`

```sql
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

### M-05 — RLS policies
- **Risk class:** medium (denies access by default — verify before deploying any client)
- **Pre-conditions:** M-02, M-04
- **Estimated runtime:** < 1 s
- **Rollback:** disable RLS per table.

```sql
-- profiles
alter table public.profiles enable row level security;
create policy "profiles_self_select" on public.profiles for select using (auth.uid() = id);
create policy "profiles_self_update" on public.profiles for update using (auth.uid() = id);

-- orgs / memberships
alter table public.orgs enable row level security;
alter table public.memberships enable row level security;
-- (helper functions defined in M-06; policies depend on them)
```

### M-06 — RPC helpers
- **Risk class:** medium (definer functions; reviewed)
- **Pre-conditions:** M-05

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

create policy "orgs_member_select" on public.orgs for select using (public.is_member(id));
create policy "orgs_owner_update" on public.orgs for update using (public.has_role(id, 'owner'));
create policy "memberships_self_select" on public.memberships for select using (user_id = auth.uid() or public.has_role(org_id, 'owner'));
create policy "memberships_owner_insert" on public.memberships for insert with check (public.has_role(org_id, 'owner'));

-- contracts / runs / findings policies (org-scoped) — abbreviated for brevity
alter table public.contracts enable row level security;
create policy "contracts_org_member" on public.contracts for select using (public.is_member(org_id));
create policy "contracts_org_member_write" on public.contracts for insert with check (public.is_member(org_id));
```

### M-07 — seed clause_categories
- **Risk class:** low (data only)
- **Pre-conditions:** M-02

```sql
insert into public.clause_categories (id, display_name, risk_default, jurisdiction_tag) values
  ('uncapped-liability', 'Uncapped liability', 'high', 'generic'),
  ('auto-renewal', 'Auto-renewal without notice', 'high', 'generic'),
  ('indemnity-unfavourable', 'Unfavourable indemnity', 'high', 'generic'),
  ('governing-law-foreign', 'Foreign governing law', 'medium', 'AU'),
  ('ppsa-missing', 'PPSA security interest not addressed', 'medium', 'AU'),
  ('privacy-act-schedule-1', 'Privacy Act 1988 schedule 1 not referenced', 'medium', 'AU'),
  ('modern-slavery-missing', 'Modern Slavery Act 2018 reporting clause missing', 'medium', 'AU')
  -- ... 14 total per H-003
  on conflict (id) do nothing;
```

## Apply flow

Each pending migration runs through the connector-confirmation flow before `apply_migration` is called.

Suggested initial run: `--apply-through=M-03` to land the schema without RLS, then a review pass, then `--apply-through=M-07` to land auth + RLS + seed.

## Post-apply

- [ ] `generate_typescript_types` → `src/lib/database.types.ts`
- [ ] Append `## [2026-05-21] migration-plan | M-01..M-07 applied` to `.memex/log.md`
- [ ] Run smoke test via `npm run test:rls` (which signs in as two distinct users in two distinct orgs and confirms cross-org reads return 0 rows).
