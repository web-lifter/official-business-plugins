---
title: Schema migrations plan
slug: migrations-plan
type: schema
status: draft
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Schema migrations plan

**Project:** `contractiq-prod` (ref `xkqj…7w2a`)
**Tech stack:** [tech-stack](../tech-stack.md)
**Entity list:** [entity-list](entity-list.md)
**ERD:** [erd.mmd](erd.mmd)

Seven migrations cover bootstrap → tables → indexes → auth trigger → RLS → RPC helpers → seed. Full SQL is in [migration-plan example](../../migration-plan/examples/example-output.md); summary follows.

## Migration sequence (summary)

| # | Name | Risk | Notes |
|---|------|------|-------|
| M-01 | bootstrap-extensions | low | `pgcrypto`, `uuid-ossp` |
| M-02 | core-tables | low | profile, org, membership, contract, classifier_run, clause_categories, finding |
| M-03 | indexes | low | FK indexes + status / contract / run filter indexes |
| M-04 | auth-trigger | medium | `handle_new_user` definer function |
| M-05 | rls-enable + base-policies | medium | RLS on all six tenant tables |
| M-06 | rpc-helpers + tenant-policies | medium | `is_member`, `has_role`, org-scoped policies |
| M-07 | seed-clause-categories | low | 14 categories per H-003 taxonomy |

## RLS policy summary

| Table | Class | Predicate |
|-------|-------|-----------|
| `profiles` | user-owned | `auth.uid() = id` (select, update) |
| `orgs` | tenant | `public.is_member(id)` (select); `public.has_role(id, 'owner')` (update) |
| `memberships` | tenant + role | `user_id = auth.uid() OR public.has_role(org_id, 'owner')` (select); `public.has_role(org_id, 'owner')` (insert/delete) |
| `contracts` | tenant | `public.is_member(org_id)` (select); `public.is_member(org_id)` (insert, with role check on update) |
| `classifier_runs` | tenant (via contract) | join: `exists (select 1 from contracts c where c.id = contract_id and public.is_member(c.org_id))` |
| `findings` | tenant (via contract) | same as classifier_runs |
| `clause_categories` | public-read, admin-write | RLS disabled with explicit comment — reference data; writes via service-role only |

## Indexes

All FK columns are indexed (`memberships(user_id)`, `memberships(org_id)`, `contracts(org_id)`, `classifier_runs(contract_id)`, `findings(contract_id)`, `findings(run_id)`, `findings(category_id)`). Additional indexes on `contracts(status)`, `findings(status)` to support the dashboards.

## Triggers

- `on_auth_user_created` — `auth.users` insert → `public.profiles` insert.
- `bump_updated_at` — generic trigger on `contracts` to refresh `updated_at`.

## RPC functions

- `public.is_member(p_org_id uuid) returns boolean` — security definer, stable.
- `public.has_role(p_org_id uuid, p_role text) returns boolean` — security definer, stable.

## Phase 6 apply (gated)

The migrations are not applied by this skill. `/migration-plan --apply-through=M-03` lands the schema (no RLS yet) for review, then `--apply-through=M-07` lands auth + RLS + seed via the connector-confirmation flow.

## Hand-off

Next: `/auth-model-design` to formalise the `saas` RLS pattern, then `/migration-plan`. After first production deploy: run upstream `database-design/postgres-schema-audit` as a quality gate.
