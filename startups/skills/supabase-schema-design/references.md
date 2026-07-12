# supabase-schema-design — references

## Canonical specifications

- **PostgreSQL Row Security Policies.** <https://www.postgresql.org/docs/current/ddl-rowsecurity.html> — `USING` vs `WITH CHECK`, policy precedence, permissive vs restrictive policies.
- **PostgreSQL `CREATE INDEX`.** <https://www.postgresql.org/docs/current/sql-createindex.html> — index types and concurrent creation.
- **PostgreSQL `gen_random_uuid()`.** Provided by the `pgcrypto` extension.
- **Supabase — Row Level Security.** <https://supabase.com/docs/guides/database/postgres/row-level-security> — `auth.uid()`, `auth.jwt()`, and the API-gateway interaction.
- **Supabase — Database Functions and RPCs.** <https://supabase.com/docs/guides/database/functions>
- **Supabase Storage — security.** <https://supabase.com/docs/guides/storage/security/access-control> — signed URLs and RLS on `storage.objects`.

## Operational

- **Supabase migrations workflow.** <https://supabase.com/docs/guides/local-development/overview#database-migrations>
- **PostgreSQL — `EXPLAIN`.** <https://www.postgresql.org/docs/current/sql-explain.html> — RLS predicates that join over un-indexed FKs sequential-scan; verify with `EXPLAIN`.

## Australian context (where relevant for examples)

- **Privacy Act 1988 — APP 8.** <https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-8-app-8-cross-border-disclosure-of-personal-information>

## Rules this skill enforces

1. **Every public table has RLS enabled.** No exceptions other than explicitly reference-data tables marked admin-only, with the reason in a SQL comment.
2. **Indexes on every FK.** Postgres does not auto-index foreign-key columns; RLS predicates joining over un-indexed FKs degrade quickly.
3. **`security definer` functions for RLS helpers.** `is_member()` / `has_role()` must run with definer rights so callers cannot read the underlying tables directly.
4. **`gen_random_uuid()` for surrogate keys.** Avoid `serial`/`bigserial` for tenant-scoped tables — enumerable IDs leak tenant size.
5. **Migrations sequenced and idempotent at the file level.** Bootstrap → tables → indexes → auth trigger → RLS → RPC helpers → seed. Re-running `/migration-plan` refuses to re-apply.
6. **Service role server-only.** Never reachable from the browser; only Workers and trusted server routes use it.
7. **Storage buckets are private by default.** Public read requires an explicit policy with a justification comment.

## Graceful degrade

Without the Supabase MCP the plan is docs-only; the user applies the SQL via `supabase db push` or the dashboard SQL editor. Phase 6 (gated apply) is skipped.

See `startups/SOURCES.md` for the broader citation context.
