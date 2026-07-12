# MVP schema plan — orchestrator log for ContractIQ

Thin orchestrator. Artefacts produced by the sub-skill runs.

## Sub-skill runs

1. **`/data-model-from-vpc --segment=au-mid-market-counsel`**
   - Output: [entity-list](../schema/entity-list.md), [erd.mmd](../schema/erd.mmd)
   - 7 in-scope entities (profile, org, membership, contract, classifier_run, clause_category, finding); 4 deferred (obligation, negotiation_brief, precedent_library, audit_log).
2. **`/supabase-schema-design --supabase-project=xkqj…7w2a`**
   - Output: [migrations-plan](../schema/migrations-plan.md)
   - 7 migrations: M-01 bootstrap, M-02 tables, M-03 indexes, M-04 auth trigger, M-05 RLS, M-06 RPC helpers, M-07 clause-category seed.
3. **Skipped:** `database-design/postgres-schema-audit` (upstream plugin not installed in this venture's worktree).

## Cross-check results

| Check | Status | Notes |
|-------|--------|-------|
| Every entity in `entity-list.md` has a `create table` in `migrations-plan.md` | ok | All 7 in-scope entities mapped 1:1 |
| Every ERD relationship has a foreign key | ok | profile/org/membership composite PK in place; org/contract, contract/finding, contract/classifier_run, run/finding, clause_category/finding all FK'd |
| Every table has RLS or is explicitly admin-only | ok | `clause_categories` is the only public-read table (reference data, RLS off with explicit note); all six others enforce RLS via `is_member` / `has_role` |

## Hand-off

- Next: `/auth-model-design` (formalises the `saas` RLS pattern → produces `auth-model.md`)
- Then: `/migration-plan --apply-through=M-03` first (schema only), review, then `--apply-through=M-07` (auth + RLS + seed)
- Recommended QA: install `database-design` upstream plugin and run `/postgres-schema-audit` before first production deploy.
