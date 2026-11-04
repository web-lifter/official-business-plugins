# phase-router — decision rules

Rules are evaluated top-to-bottom. The first 1-3 matches become the
recommended actions, prioritised by curriculum phase order. Each rule
uses the local heuristics described in
[`methodology-notes.md`](../../references/methodology-notes.md).

## Rules

| # | Trigger condition | Recommend | Repository rationale (not verified curriculum) |
|---|---|---|---|
| 1 | `00-vision/vision-sketch.md` missing or `status: draft` | `/vision-sketch` | *vision sketch precedes hypotheses* |
| 2 | Vision active, but no folders under `02-customer-discovery/segments/` | `/customer-segment-define` | segments come before any solution work |
| 3 | Segment exists, no `profile.md` | `/customer-profile-build <segment>` | profile (jobs/pains/gains) is the right half of the VPC |
| 4 | Profile exists, no `early-adopters.md` | `/early-adopter-profile <segment>` | earlyvangelists are the test population |
| 5 | Early adopters listed, no `interview-guide.md` | `/interview-guide-build <segment>` | interviews need a structured guide |
| 6 | Guide exists, < 5 interviews logged | `/interview-log <segment>` | minimum sample for the four-question gate |
| 7 | ≥ 5 interviews logged, no `interview-summary.md` | `/interview-analyse <segment>` | aggregate before deciding |
| 8 | Hypothesis register has entries lacking `falsifier:` | `/hypothesis-falsifiability-check` | every hypothesis must be falsifiable before testing |
| 9 | Customer profile exists, no VPC for that segment | `/value-map-build <segment>` | VPC needs the profile |
| 10 | VPC exists, no `fit-report.md` | `/vpc-fit-check <segment>` | fit means every prioritised pain has a reliever |
| 11 | No `05-business-model/bmc-v*.md` | `/bmc-build` | BMC is the master canvas |
| 12 | BMC has cells tagged `hypothesis`, fewer than 50% of hypotheses have test cards | `/test-card-build` for highest-priority hypothesis | testing is how guesses become facts |
| 13 | Concluded test cards with recorded observations but no matching learning card | `/learning-card-build TC-NNN` | close the loop |
| 14 | No `04-competitors/uvp.md`, ≥ 3 competitors in `competitor-table.md` | `/uvp-statement` | UVP frames the venture against competitors |
| 15 | Fewer than 3 SWOTs filed, ≥ 3 competitors | `/swot-build <competitor>` for next missing | top 3 SWOTs minimum |
| 16 | No `06-relationships-channels/get-keep-grow.md`, BMC has channels cell tagged `hypothesis` | `/get-keep-grow-design` | channels are designed, not assumed |
| 17 | Channel strategy exists, no `funnel-model.md` | `/funnel-model` | funnel is the quantitative version |
| 18 | Three or more pivots in `07-validation/pivot-refine-log.md` in the last 90 days | Halt — recommend revisiting discovery (no skill invocation; print warning) | pivot frequency signals instability |
| 19 | `customer-discovery-status` would return 🔴 / 🟡, but the user is asking about MVP | Recommend the gap-filling action that turns the gate green; do **not** recommend `/mvp-scope` | |
| 20 | `customer-discovery-status` returns 🟢, no `09-mvp/mvp-spec.md` | `/mvp-scope` | MVP requires evidence |
| 21 | MVP scope exists, no `mvp-metrics.md` | `/mvp-metrics` | no hypothesis without a metric |
| 22 | MVP scope and metrics exist, no `tech-stack.md` | `/mvp-tech-plan` | Engineering bridge — Phase F |
| 23 | tech-stack exists, no `architecture/ADR-*.md` | `/architecture-design` | ADRs land architectural choices |
| 24 | Architecture exists, no `schema/erd.mmd` | `/mvp-schema-plan` | Engineering bridge |
| 25 | Schema plan exists, no `deploy/{vercel,cloudflare}.md` | `/mvp-deploy-plan` | Engineering bridge |
| 26 | All of the above exist, no `analytics/events-spec.md` | `/mvp-analytics-plan` | Engineering bridge |
| 27 | Full MVP plan exists, no `feasibility.md` | `/mvp-feasibility` | Final feasibility check before build |
| 28 | Full MVP plan exists, feasibility green | `/mvp-build-plan` then `/pitch-1min-build` | Ready to build |

## Tie-breaking

- When multiple rules match, prefer the lower-phase rule first.
- When two rules at the same phase match, prefer the one whose
  blocked-downstream count is higher (i.e. fixing it unblocks more work).
- Never recommend more than three actions.

## Pivot frequency check (rule 18)

Count only `pivot` entries, not `refine` entries, in `07-validation/pivot-refine-log.md` whose date is within
the last 90 days. The check uses the entry's date heading
(`## [YYYY-MM-DD] pivot|refine | ...`). If three or more match, the
router prints a warning instead of recommending a forward action — the
right move is usually to slow down, not add another experiment.

## Focus-area filter

If `$ARGUMENTS` contains a focus area, only consider rules whose action
falls into that area. Areas:

- `discovery` — rules 2-8
- `vpc` — rules 9-10
- `bmc` — rules 11-12
- `competitor` — rules 14-15
- `channels` — rules 16-17
- `prototype` — paper/digital prototype recommendations (no rules above
  cover this directly; defer to the prototyping plugin's orchestrator)
- `mvp` — rules 20-28

## Evidence guardrails

Unrun or incomplete tests need execution/data collection, not invented learning cards. Interview and competitor counts are triage heuristics, not sufficient evidence of market fit. Canvas mapping coverage is not validation. Inconclusive results do not authorise scale.
