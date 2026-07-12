---
name: experiment-data-collection-plan
description: Given a test card, design the data capture — source, table/event, query for "are we right?" Pairs with experimentation/test-card-build to make the experiment instrumentable.
argument-hint: <test-card-id>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# experiment-data-collection-plan

Method: test card / learning card discipline from Osterwalder et al. 2014 — see `references.md` and `startups/SOURCES.md`.

Idempotency: safe to re-run; appends or replaces the `## Data collection plan` section on the named test card.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `02-customer-discovery/test-cards/<TC-NNN>.md`. Halt if
   missing or status `concluded`.
3. Read `mvp-analytics-plan` events spec if it exists.

## Phase 2: Map "Measure" to data sources

For the test card's "Measure" field, identify:

- **Source**: PostHog event? Supabase table? Stripe API? Survey tool
  export?
- **Schema**: which event/table, which columns
- **Query**: SQL or PostHog query that returns the metric value
- **Filtering**: which subjects count (segment, cohort, time window)

## Phase 3: Pre-test checks

Before the experiment can run, confirm:

- The data source exists (event is being sent / table exists / API
  available)
- Sample size will be reachable in the timeframe
- Threshold can be computed unambiguously

If any check fails, surface as a blocker — the experiment can't run
yet.

## Phase 4: Compose query

Write the actual query. Examples:

PostHog funnel:
```
funnel "Pre-order conversion test"
  step 1: pricing_viewed
  step 2: payment_completed (within 14 days)
filter: signup_source = "<test-channel>"
```

Supabase SQL:
```sql
select
  count(*) filter (where status = 'paid') as paid_count,
  count(*) as total_count,
  (count(*) filter (where status = 'paid'))::float / count(*) as
   conversion_rate
from public.pre_orders
where created_at >= '<start>' and created_at < '<end>';
```

## Phase 5: Write

Append a `## Data collection plan` section to the test card itself
(`02-customer-discovery/test-cards/<TC-NNN>.md`) — keep the data plan
co-located with the test design:

```markdown
## Data collection plan

### Source
<PostHog | Supabase | external>

### Schema
<event/table>: <columns>

### Pre-test checks
- [x] Source exists
- [x] Sample size reachable
- [x] Threshold computable

### Query

\`\`\`sql or PostHog DSL
...
\`\`\`

### Decision rule
At end of timeframe (<window>):
- If query result <crosses threshold> → confirm
- Else → refute or refine
```

## Phase 6: Log

Append: `## [<today>] experiment-data | TC-<NNN> data plan`.

## Important principles

- **Co-locate with the test card.** The data plan and the experiment
  design belong together.
- **Pre-test checks are blocking.** A test that can't compute its
  metric is not a test.
- **Concrete query.** Pseudocode is allowed; vague isn't.
- **Timeframe matters.** Decision rule fires at the end of the window,
  not whenever someone looks.
