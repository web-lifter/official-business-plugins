---
title: Funnel model
slug: funnel-model
type: funnel
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Funnel model

Primary channel: Direct founder-led LinkedIn outbound to AU/NZ in-house counsel (see [channel-strategy.md](channel-strategy.md)).

Numbers below model a single 12-week outbound cohort at the founder's current bandwidth. These are working hypotheses — every rate is sourced or flagged as a guess.

| Stage | Definition (event) | Volume | Rate from prior | Source | Hypothesis |
|-------|--------------------|--------|-----------------|--------|------------|
| Awareness (LinkedIn outreach) | Connection request + opener message sent to a primary-segment GC | **500** | — | Founder bandwidth: ~6 messages/business-day × 12 weeks | — |
| Sign-up (discovery booked) | Calendly booking confirmed for a 30-min discovery call | **50** | 10% | Skok / Boz inside-sales benchmarks for warm-net LinkedIn outbound, adjusted down for cold | H-201 |
| Activation (demo completed) | Live ContractIQ demo (Wizard-of-Oz or click-through) attended | **20** | 40% | Founder's own conversion in past advisory work; first-pass guess | H-202 |
| Conversion (pilot signed) | Signed pilot LoI committing to a 60-day paid trial at AU$300/seat/month | **5** | 25% | Guess — anchored to "1 in 4 demos convert" SaaS rule of thumb | H-001 |
| Retention (paying at month 4) | Pilot converted to paid month-to-month after 60-day trial | **2** | 40% | Guess — high pilot→paid drop-off is normal pre-PMF | H-203 |

**End-to-end yield: 0.4%** (2 paying / 500 outreached).

## Reality check

- **Industry benchmark for primary channel:** AU mid-market B2B SaaS LinkedIn outbound typically yields 0.2%–1.0% end-to-end at the pre-PMF stage. Our 0.4% sits in the middle of that band — defensible, not over-optimistic.
- **Our model is on-par** with the benchmark. No revisions needed at this stage.
- **Risk:** the 25% demo→pilot rate is a guess. It is the rate we have least signal on, and a 5pp swing here changes paying-customer volume by 1 logo over the 12-week cohort. Treat H-001 as the highest-priority unknown.

## Stage-by-stage notes

- **Awareness → Sign-up (10%):** depends on opener-message quality. Founder Priya has the ex-GC credibility advantage; without it, the rate would more likely be 4–6%.
- **Sign-up → Activation (40%):** discovery → demo no-shows and reschedules account for most of the drop. Tighten with same-week scheduling.
- **Activation → Conversion (25%):** the binding constraint. The Wizard-of-Oz prototype must produce a credible enough redline that the GC commits to a paid pilot.
- **Conversion → Retention (40%):** the 60-day trial must produce ≥ 3 reviewed contracts per pilot user. If the pilot doesn't get the user into a habit, the trial won't convert.

## Hypothesis cross-reference

- **H-001 (demand):** tested at the Conversion stage. ≥ 30% of 20 discovery interviewees expressing willingness to pay translates to ≥ 6 pilots; the funnel models a softer 25%.
- **H-201 (acquisition):** new — "warm-net LinkedIn outbound yields ≥ 8% connect-to-discovery rate." Modelled at 10%.
- **H-202 (qualification):** new — "≥ 35% of discovery calls convert to a demo." Modelled at 40%.
- **H-203 (retention):** new — "≥ 35% of paid pilots renew month-to-month at end of trial." Modelled at 40%.

## Hand-off

Run `mvp-planning/funnel-instrumentation-spec` to translate these stages into concrete PostHog events once the MVP exists. Until then, all measurement is manual (Calendly bookings + CRM tally).
