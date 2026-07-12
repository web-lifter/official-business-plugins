# Data collection plan — TC-{{NNN}}

(Appended to the test card at `02-customer-discovery/test-cards/TC-{{NNN}}.md`.)

## Source
{{PostHog | Supabase SQL | external API | survey export}}

## Schema
{{event_name | table_name}}: {{columns / properties used}}

## Pre-test checks

- [{{x|space}}] Source exists (event firing / table created / API reachable)
- [{{x|space}}] Sample size reachable in the timeframe
- [{{x|space}}] Threshold can be computed unambiguously

If any check is unticked, the experiment cannot run yet — surface as a blocker.

## Query

```sql
-- or PostHog DSL / external query
```

## Decision rule

At end of timeframe ({{window}}):
- If {{condition crossing threshold}} → confirm hypothesis
- Else → refute or refine

## Linked

- Test card: [TC-{{NNN}}](TC-{{NNN}}.md)
- Hypothesis: [H-{{NN}}](../../01-hypotheses/hypothesis-register.md)
- Events spec: [events-spec](../../09-mvp/analytics/events-spec.md)
