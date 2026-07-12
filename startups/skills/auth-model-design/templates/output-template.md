---
title: Auth model
slug: auth-model
type: adr
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Auth model

**Pattern:** {{user | saas | tenant | marketplace}}
**Tech:** Supabase Auth + Postgres RLS

## Tables

```sql
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  created_at timestamptz default now()
);

-- {{additional tables for the chosen pattern}}
```

## Triggers

```sql
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer as $$
begin
  insert into public.profiles (id, email) values (new.id, new.email);
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
| {{table}} | {{select|insert|update|delete}} | {{predicate}} |

## RPC helpers

- `{{current_role()}}` — {{purpose}}
- `{{is_member(tenant_id)}}` — {{purpose}}

## Auth flow

- **Sign-up:** {{email magic link | OAuth | password}}
- **Email confirmation:** {{on | off}}
- **Session transport:** cookie-based via `@supabase/ssr`

## Linked

- Schema: [migrations-plan](../schema/migrations-plan.md)
- Tech stack: [tech-stack](../tech-stack.md)
