# mvp-analytics-plan — references

## Tool documentation

- **PostHog — Identifying users.** <https://posthog.com/docs/data/identify>
- **PostHog — Groups (org-level analytics).** <https://posthog.com/docs/product-analytics/group-analytics>
- **PostHog — EU data residency.** <https://posthog.com/docs/privacy/data-storage>
- **GA4 — Measurement Protocol & event reference.** <https://developers.google.com/analytics/devguides/collection/protocol/ga4>
- **Plausible — events API.** <https://plausible.io/docs/events-api>
- **Mixpanel — JavaScript SDK.** <https://docs.mixpanel.com/docs/quickstart/connect-your-data?sdk=javascript>

## Privacy and residency

- **Australian Privacy Act 1988 — APP 8 (cross-border disclosure).** <https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-8-app-8-cross-border-disclosure-of-personal-information>
- **GDPR Article 5 (lawful processing) and Article 32 (security).**

## Naming conventions

- **Verb-object event names** (`user_signed_up`, `contract_uploaded`). Snake-case. No spaces, no past-tense inconsistencies.

## Rules this skill enforces

1. **No PII in analytics.** Email, full name, addresses, free-form text — never sent.
2. **Verb-object event names.** Consistent across client and server.
3. **Global super-properties keep events clean.** Don't repeat `app_version`, `route`, `auth_state` per event.
4. **Tool default: PostHog.** Override needs a deliberate reason recorded in the spec.
5. **Identity model documented up front.** Anonymous → identified alias must be defined; orphaned funnel steps are a known defect class.
6. **Server-side events for trust-critical funnels.** `checkout_completed`, `user_signed_up` fire from the server, not the browser.

See `startups/SOURCES.md` for the broader citation context.
