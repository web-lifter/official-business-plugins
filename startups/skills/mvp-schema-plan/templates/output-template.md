# MVP schema plan — orchestrator log

Thin orchestrator; the artefacts live in the sub-skill outputs.

## Sub-skill runs

1. **`/data-model-from-vpc`** → [entity-list](../schema/entity-list.md), [erd.mmd](../schema/erd.mmd)
2. **`/supabase-schema-design`** → [migrations-plan](../schema/migrations-plan.md)
3. **(optional) `database-design/postgres-schema-audit`** → audit report

## Cross-check results

| Check | Status | Notes |
|-------|--------|-------|
| Every entity in `entity-list.md` has a `create table` in `migrations-plan.md` | {{ok|drift}} | {{details}} |
| Every ERD relationship has a foreign key | {{ok|drift}} | {{details}} |
| Every table has RLS or is explicitly admin-only | {{ok|drift}} | {{details}} |

## Hand-off

- Next: `/auth-model-design`
- Then: `/migration-plan` (apply through gated flow)
