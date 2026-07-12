# references — hypothesis-falsifiability-check

The falsifiability discipline this skill enforces comes from:

- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011. — defines **validated learning** as the unit of progress for a startup. A learning is "validated" only when it could have been falsified by the experiment but was not. A hypothesis that cannot be falsified produces no validated learning, no matter how much data is collected.
- **Popper, Karl.** *The Logic of Scientific Discovery.* Routledge, 1959 (English edition). — the philosophical root: a claim is scientific only if it could in principle be refuted. Ries imports this directly into startup practice.

The four-check rubric (**falsifier, measurement, threshold, timeframe**) implements Popper's criterion as a practical gate:

1. **Falsifier present** — the hypothesis answers "we are wrong if…" with an observable outcome.
2. **Measurement present** — a named instrument or data source.
3. **Threshold present** — a specific pass/fail line, set before the test runs.
4. **Timeframe present** — when the decision is made.

A hypothesis missing any of these is **not testable**, only debate-able. The skill is intentionally blocking so the venture cannot accidentally invest in an experiment that cannot conclude.

## Why this is the blocking gate (and not advice-only)

The cost of running a doomed experiment compounds: a vague hypothesis produces an ambiguous result, which produces a "more data" decision, which produces another doomed experiment. Catching the failure upstream — at hypothesis-registration time — is the cheapest possible intervention.

The Strategyzer test-card and learning-card templates (Osterwalder et al., *Value Proposition Design*, 2014) assume a falsifiable hypothesis; this skill is the bouncer at the door.

## Override behaviour

`--force` proceeds despite a failed check. The override is logged to `.memex/log.md` as `gate-override | hypothesis-falsifiability-check bypassed for H-NN (issues: <list>)` so the audit trail is intact. Use override when the user has accepted the risk knowingly (e.g. a quick exploratory test on a directional claim).

See `startups/SOURCES.md` for the full bibliography.
