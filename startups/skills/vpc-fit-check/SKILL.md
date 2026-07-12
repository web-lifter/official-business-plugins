---
name: vpc-fit-check
description: Cross-check that every prioritised pain on a segment profile has at least one pain reliever and every prioritised gain has at least one gain creator. Appends a fit-report block to the latest VPC. Sets status to active if fit; draft if partial.
argument-hint: <segment-slug>
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# vpc-fit-check

Idempotency: re-runs overwrite the `## Fit report` section in the latest VPC. The skill never appends duplicate fit reports.

Method: the "fit" check of the Value Proposition Canvas — does every prioritised pain have a reliever and every prioritised gain a creator? Per Osterwalder et al., *Value Proposition Design* (Wiley, 2014). See `references.md` and `startups/SOURCES.md`.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `02-customer-discovery/segments/<slug>/profile.md` — extract
   the pains and gains tables, only `high` and `medium` priority rows.
3. Read the latest `03-value-proposition/vpc-<slug>-v*.md` —
   extract pain relievers and gain creators with their mappings.

## Phase 2: Cross-check

For each `high`-priority pain: count linked relievers. Each `medium`
pain: same. Same for gains.

A VPC has **fit** when:

- Every `high` pain has ≥ 1 reliever
- Every `high` gain has ≥ 1 creator
- ≥ 70% of `medium` pains have ≥ 1 reliever
- ≥ 70% of `medium` gains have ≥ 1 creator

## Phase 3: Write fit-report

Append to the VPC file (under a new `## Fit report` section, or
overwrite if one already exists):

```markdown
## Fit report

Generated <today>.

| Pain (priority) | Relievers | Status |
|---|---|---|
| <pain> (high) | <count> | ✓ | ✗ |

| Gain (priority) | Creators | Status |
|---|---|---|
| <gain> (high) | <count> | ✓ | ✗ |

### Verdict

- Fit: <yes | partial — <gap-summary> | no — <gap-summary>>
- Action: <if not fit, propose value-map-build refresh>
```

If fit: bump VPC frontmatter `status:` to `active`. If partial: leave
as `draft`. If no: leave as `draft` and surface the gap list as
recommended next actions.

## Phase 4: Log

Append: `## [<today>] vpc-fit | <slug> v<N>: <fit-status>`.

## Important principles

- **High priority is non-negotiable.** A single unmatched high pain or
  gain blocks fit.
- **Medium can be partial.** The 70% rule.
- **Low priority is informational.** Doesn't gate fit.
- **Read-only on the segment profile.** This skill never modifies
  jobs/pains/gains; it only audits the relievers/creators.

## Edge cases

1. No prioritised pains/gains (all "low") — refuse, route to
   `customer-profile-build` to force prioritisation.
2. Latest VPC version is empty — refuse, route to `value-map-build`.
3. Fit report already exists — overwrite the section, don't append a
   second copy.
