# funnel-instrumentation-spec — references

## Canonical product analytics

- **PostHog — Funnels.** <https://posthog.com/docs/product-analytics/funnels> — funnel semantics, time-window definition, cohort filters.
- **PostHog — Identifying users.** <https://posthog.com/docs/data/identify> — anonymous → identified alias flow assumed by this skill.
- **PostHog — Privacy and EU data residency.** <https://posthog.com/docs/privacy>
- **GA4 — Events.** <https://support.google.com/analytics/answer/9322688> — for the alternative tool path.

## Funnel-model lineage

- **Dave McClure — "AARRR" pirate metrics.** Acquisition / Activation / Retention / Referral / Revenue. The canonical funnel model the upstream `funnel-model.md` draws from.
- **Reichheld, Frederick.** *The Loyalty Effect.* Harvard Business Press, 1996. — Retention math used in any downstream churn modelling.

## Rules this skill enforces

1. **One canonical event per stage.** Multiple competing definitions of "activation" make the funnel ambiguous.
2. **Window is mandatory.** "≥ 30% paid" means nothing without "within N days".
3. **Identity model explicit.** Anonymous-to-identified alias must be defined; orphaned funnel steps are a known defect class.
4. **Dashboards in repo.** Source-controlled config (PostHog API import in CI). No dashboards built by hand in the UI.
5. **No PII in events.** Email, full name, contract title, document text all excluded.

See `startups/SOURCES.md` for the broader citation context.
