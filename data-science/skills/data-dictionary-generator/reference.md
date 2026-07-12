# Data Dictionary Generator -- Reference Material

## Table of Contents

- [PostgreSQL Introspection Queries](#postgresql-introspection-queries)
- [CSV Type Inference Rules](#csv-type-inference-rules)
- [PII Detection Patterns](#pii-detection-patterns)
- [Common Naming Convention Recognition](#common-naming-convention-recognition)

## PostgreSQL Introspection Queries

### List All Tables with Row Counts

```sql
SELECT
    schemaname,
    relname AS table_name,
    n_live_tup AS estimated_row_count
FROM pg_stat_user_tables
WHERE schemaname = 'public'
ORDER BY relname;
```

### All Columns with Types, Nullability, and Defaults

```sql
SELECT
    table_name,
    column_name,
    data_type,
    udt_name,
    character_maximum_length,
    is_nullable,
    column_default,
    ordinal_position
FROM information_schema.columns
WHERE table_schema = 'public'
ORDER BY table_name, ordinal_position;
```

### Primary Keys, Foreign Keys, and Unique Constraints

```sql
SELECT
    tc.table_name,
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
LEFT JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.table_schema = tc.table_schema
WHERE tc.table_schema = 'public'
ORDER BY tc.table_name, tc.constraint_type;
```

### All Indexes with Types

```sql
SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
```

### Column and Table Comments

```sql
SELECT
    c.relname AS table_name,
    a.attname AS column_name,
    d.description AS comment
FROM pg_class c
JOIN pg_attribute a ON a.attrelid = c.oid
LEFT JOIN pg_description d ON d.objoid = c.oid AND d.objsubid = a.attnum
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
    AND a.attnum > 0
    AND NOT a.attisdropped
ORDER BY c.relname, a.attnum;
```

### Enum Types and Values

```sql
SELECT
    t.typname AS enum_name,
    e.enumlabel AS enum_value,
    e.enumsortorder
FROM pg_type t
JOIN pg_enum e ON t.oid = e.enumtypid
JOIN pg_namespace n ON n.oid = t.typnamespace
WHERE n.nspname = 'public'
ORDER BY t.typname, e.enumsortorder;
```

### Supabase RLS Policies

```sql
SELECT
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual,
    with_check
FROM pg_policies
WHERE schemaname = 'public'
ORDER BY tablename, policyname;
```

### Supabase auth.users References

```sql
SELECT
    tc.table_name,
    kcu.column_name,
    ccu.table_schema AS foreign_schema,
    ccu.table_name AS foreign_table
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
    AND ccu.table_schema = 'auth'
    AND ccu.table_name = 'users';
```

---

## CSV Type Inference Rules

| Pattern | Inferred Type | Confidence |
|---------|--------------|------------|
| All integers, no decimals | `integer` or `bigint` | High |
| Decimal numbers | `numeric` or `double precision` | High |
| `true`/`false`, `0`/`1`, `yes`/`no` | `boolean` | High |
| ISO 8601 date (`YYYY-MM-DD`) | `date` | High |
| ISO 8601 datetime (`YYYY-MM-DDTHH:MM:SS`) | `timestamptz` | High |
| UUID format (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | `uuid` | High |
| Email pattern (`*@*.*`) | `text` (PII: email) | Medium |
| URL pattern (`http(s)://...`) | `text` (URL) | Medium |
| JSON object or array | `jsonb` | Medium |
| Short text, few distinct values | `text` (candidate enum) | Low |
| Long text, high cardinality | `text` | High |
| Empty / all nulls | `text` (unknown) | Low |

---

## PII Detection Patterns

| Column Name Pattern | PII Type | Sensitivity | Recommendation |
|--------------------|----------|-------------|----------------|
| `email`, `email_address`, `e_mail` | Email | Medium | Mask in non-prod, audit access |
| `phone`, `phone_number`, `mobile`, `tel` | Phone | Medium | Mask in non-prod |
| `first_name`, `last_name`, `full_name`, `name` (on user/profile tables) | Name | Medium | Audit access |
| `address`, `street`, `city`, `postcode`, `zip`, `suburb` | Address | Medium | Encrypt at rest |
| `date_of_birth`, `dob`, `birth_date` | DOB | High | Encrypt, restrict access |
| `ssn`, `social_security`, `tax_file_number`, `tfn` | Government ID | Critical | Encrypt, strict access control |
| `ip_address`, `ip`, `user_agent` | Technical PII | Low | Audit access, retention policy |
| `avatar_url`, `profile_image`, `photo` | Biometric-adjacent | Low | Review retention policy |
| `password`, `password_hash`, `secret` | Credential | Critical | Never expose, verify hashing |
| `credit_card`, `card_number`, `pan` | Financial | Critical | PCI compliance required |
| `abn`, `acn` | Business ID (AU) | Low | Generally public, audit access |
| `medicare`, `medicare_number` | Health ID (AU) | Critical | Encrypt, strict access control |

---

## Common Naming Convention Recognition

| Pattern | Detected Convention | Implication |
|---------|-------------------|-------------|
| `created_at`, `inserted_at` | Audit: creation timestamp | Row creation tracking |
| `updated_at`, `modified_at` | Audit: modification timestamp | Row update tracking |
| `deleted_at` (nullable timestamptz) | Soft delete | Rows are logically deleted, not removed |
| `is_deleted`, `is_archived` (boolean) | Soft delete (boolean variant) | Rows are logically deleted |
| `created_by`, `author_id` | Audit: actor tracking | Who created the row |
| `updated_by`, `modified_by` | Audit: actor tracking | Who last modified the row |
| `org_id`, `organisation_id`, `tenant_id` | Multi-tenancy | Data isolation per tenant |
| `workspace_id`, `team_id` | Multi-tenancy (workspace model) | Data isolation per workspace |
| `parent_id` (self-referencing) | Tree / hierarchy | Recursive parent-child structure |
| `slug` | URL-friendly identifier | Used for permalinks |
| `version`, `revision` | Row versioning | Optimistic concurrency or history |
| `sort_order`, `position`, `rank` | Manual ordering | User-controlled display order |
| `*_type` + `*_id` pair | Polymorphic association | Single FK references multiple tables |
| `metadata`, `extra`, `properties` (jsonb) | Flexible schema | Semi-structured extension data |
| `status`, `state` | State machine | Row lifecycle management |
| `*_count` | Denormalised counter | Cached aggregate for performance |
