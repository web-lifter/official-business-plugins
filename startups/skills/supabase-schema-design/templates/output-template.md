---
title: Schema migrations plan
slug: migrations-plan
type: schema
status: draft
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Schema migrations plan

**Project:** {{ref}}
**Tech stack:** [tech-stack](../tech-stack.md)
**Entity list:** [entity-list](entity-list.md)
**ERD:** [erd.mmd](erd.mmd)

## Migration sequence

### M-01 — bootstrap
- Enable extensions (`pgcrypto`, `uuid-ossp` if needed)
- Optional schemas (`private`, `analytics`)

```sql
create extension if not exists "pgcrypto";
```

### M-02 — tables
```sql
-- one create table per entity, with FKs
```

### M-03 — indexes
```sql
-- FK indexes, common query indexes
```

### M-04 — auth trigger
```sql
-- handle_new_user trigger if Supabase Auth is used
```

### M-05 — RLS policies
```sql
-- alter table ... enable row level security;
-- create policy ... using (...);
```

### M-06 — RPC helpers
```sql
-- is_member, has_role, etc.
```

### M-07 — seed data
```sql
-- reference data only; no user data
```

## RLS policy summary

| Table | Class | Predicate |
|-------|-------|-----------|
| {{table}} | {{user-owned|tenant|public-read|admin}} | {{SQL predicate}} |
