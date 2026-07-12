# experiment-data-collection-plan — references

## Canonical sources

- **Osterwalder, Pigneur, Bernarda & Smith.** *Value Proposition Design.* Wiley, 2014.
  - Source of the **test card** (hypothesis / test / metric / criterion / cost-time) and **learning card** (observed / learned / decided / next) templates this skill assumes upstream.
- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011.
  - Validated learning, falsifiability discipline, the build-measure-learn loop.
- **Maurya, Ash.** *Running Lean* (3rd ed.). O'Reilly, 2022.
  - Concrete tactics for instrumentable experiments — pre-test checks, sample-size sanity, decision rules set at design time.

## Data sources cited in examples

- **PostHog events documentation.** <https://posthog.com/docs/data> — event shape, distinct_id semantics, funnel queries.
- **PostgreSQL — `percentile_cont` / `percentile_disc`.** <https://www.postgresql.org/docs/current/functions-aggregate.html#FUNCTIONS-ORDEREDSET-TABLE> — the canonical aggregate for medians.

## Rules this skill enforces

1. **Co-locate with the test card.** The data plan and the experiment design belong together. One file, not two.
2. **Pre-test checks are blocking.** An experiment that cannot compute its metric is not an experiment. All three checkboxes must be ticked before the test card moves to `status: running`.
3. **Concrete query.** Pseudocode is allowed only where the underlying tool is not yet picked; a vague query is a refusal condition.
4. **Decision rule set at design time.** "We'll see when the data comes in" is forbidden. The rule fires automatically at the end of the timeframe.
5. **Timeframe is mandatory.** Indefinite experiments never conclude.

See `startups/SOURCES.md` for the broader citation context.
