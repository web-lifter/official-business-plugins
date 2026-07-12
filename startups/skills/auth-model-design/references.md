# auth-model-design — references

## Canonical specifications

- **PostgreSQL Row Security Policies.** <https://www.postgresql.org/docs/current/ddl-rowsecurity.html> — the authoritative reference for RLS predicates, `USING` vs `WITH CHECK`, and policy precedence.
- **Supabase Auth — Row Level Security.** <https://supabase.com/docs/guides/database/postgres/row-level-security> — Supabase-specific patterns including `auth.uid()`, `auth.jwt()`, and how policies interact with the API gateway.
- **Supabase Auth — server-side auth (`@supabase/ssr`).** <https://supabase.com/docs/guides/auth/server-side> — the canonical Next.js / SSR session pattern this skill assumes.

## OAuth and identity

- **RFC 6749 — The OAuth 2.0 Authorization Framework.**
- **RFC 7636 — Proof Key for Code Exchange (PKCE).** The browser sign-in flow Supabase implements.
- **OpenID Connect Core 1.0.** Underpins Google Workspace sign-in.

## Multi-tenant patterns

- **Microsoft — Multi-tenant SaaS database patterns.** <https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns> — useful background on per-tenant vs shared-database trade-offs. This skill defaults to shared-database, RLS-scoped.

## Rules this skill enforces

1. **RLS, always.** Every public table has RLS enabled. No exceptions for MVP.
2. **Profiles separate from `auth.users`.** Never put PII or app data in the `auth` schema.
3. **Triggers maintain invariants.** New `auth.users` row → matching `profiles` row, atomically.
4. **`security definer` functions for RLS helpers.** `is_member()` and `has_role()` must run with definer rights so callers cannot read the underlying tables directly.
5. **Service role is server-only.** Never reachable from the browser; only Workers and trusted server routes use it.
6. **Indexes on FKs.** Postgres does not auto-index foreign-key columns; RLS predicates that join over FKs will sequential-scan without them.

See `startups/SOURCES.md` for the broader citation context.
