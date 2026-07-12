# Migration execution plan

**Project:** {{supabase-project-ref}}
**Plan source:** [migrations-plan](../schema/migrations-plan.md)
**Generated:** {{YYYY-MM-DD}}

## Already applied (from `list_migrations`)

| # | Name | Applied at |
|---|------|-----------|
| {{n}} | {{name}} | {{ts}} |

## Pending

### M-{{NN}} — {{name}}
- **Risk class:** {{low | medium | high}}
- **Pre-conditions:** {{extensions, prior migrations}}
- **Estimated runtime:** {{ms..s}}
- **Rollback:** {{reverse statement}}

```sql
-- {{full SQL}}
```

## Apply flow

For each pending migration, when `--apply-through={{N}}` is passed:

1. Build preview block (SQL diff, project ref, branch, rollback).
2. `AskUserQuestion` → "Yes, apply" / "No, abort".
3. On yes: call `apply_migration` via Supabase MCP. On success, log; on failure, surface and stop.
4. On no: log abort and stop.

## Post-apply

- [ ] Regenerate TypeScript types via `generate_typescript_types`.
- [ ] Write to `{{src/lib/database.types.ts}}`.
- [ ] Append `## [{{date}}] migration-plan | {{applied}} of {{N}}` to `.memex/log.md`.
