# Startups

**69 skills and nine optional Claude orchestrators.** No Memex installation is
required. All existing skill identifiers are retained; no usage evidence justified
deleting an entire skill as obsolete.

Read [RUNTIME.md](RUNTIME.md) and [SOURCES.md](SOURCES.md). Begin with `venture-init`
only when creating a venture, `venture-status` for a read-only summary, or
`phase-router` to choose the next evidence-based action. New workspaces use
`.project/plans/startups/<slug>/`; verified legacy workspaces remain in place.

```bash
python startups/scripts/venture_workspace.py init --project /path/to/project --venture example
python startups/scripts/venture_workspace.py resolve --project /path/to/project --venture example
```

Provider-specific engineering skills are optional planning recipes. A skill file
is not a connector, subagent or permission to deploy. Hosted chats without a
mounted project return the artefact and intended path rather than claiming a
persistent write. Orchestrator sequences can run sequentially when agents are
unavailable.

## Catalogue and refinement priorities

- [adr-writer](skills/adr-writer/SKILL.md)
- [api-design](skills/api-design/SKILL.md)
- [architecture-design](skills/architecture-design/SKILL.md)
- [auth-model-design](skills/auth-model-design/SKILL.md)
- [bmc-build](skills/bmc-build/SKILL.md)
- [bmc-front-back-split](skills/bmc-front-back-split/SKILL.md)
- [bmc-link-vpc](skills/bmc-link-vpc/SKILL.md)
- [bmc-revenue-cost-sketch](skills/bmc-revenue-cost-sketch/SKILL.md)
- [bmc-update](skills/bmc-update/SKILL.md)
- [channel-select](skills/channel-select/SKILL.md)
- [churn-model](skills/churn-model/SKILL.md)
- [cloudflare-deploy-plan](skills/cloudflare-deploy-plan/SKILL.md)
- [competitor-bmc-shadow](skills/competitor-bmc-shadow/SKILL.md)
- [competitor-discover](skills/competitor-discover/SKILL.md)
- [competitor-insights](skills/competitor-insights/SKILL.md)
- [competitor-table-build](skills/competitor-table-build/SKILL.md)
- [converge-ideas](skills/converge-ideas/SKILL.md)
- [customer-discovery-status](skills/customer-discovery-status/SKILL.md)
- [customer-profile-build](skills/customer-profile-build/SKILL.md)
- [customer-segment-define](skills/customer-segment-define/SKILL.md)
- [data-model-from-vpc](skills/data-model-from-vpc/SKILL.md)
- [digital-prototype](skills/digital-prototype/SKILL.md)
- [divergent-ideate](skills/divergent-ideate/SKILL.md)
- [early-adopter-profile](skills/early-adopter-profile/SKILL.md)
- [experiment-data-collection-plan](skills/experiment-data-collection-plan/SKILL.md)
- [experiment-design](skills/experiment-design/SKILL.md)
- [experiment-prioritise](skills/experiment-prioritise/SKILL.md)
- [experiment-run-tracker](skills/experiment-run-tracker/SKILL.md)
- [figma-design-handoff](skills/figma-design-handoff/SKILL.md)
- [funnel-instrumentation-spec](skills/funnel-instrumentation-spec/SKILL.md)
- [funnel-model](skills/funnel-model/SKILL.md)
- [get-keep-grow-design](skills/get-keep-grow-design/SKILL.md)
- [hypothesis-falsifiability-check](skills/hypothesis-falsifiability-check/SKILL.md)
- [hypothesis-register](skills/hypothesis-register/SKILL.md)
- [interview-analyse](skills/interview-analyse/SKILL.md)
- [interview-guide-build](skills/interview-guide-build/SKILL.md)
- [interview-log](skills/interview-log/SKILL.md)
- [learning-card-build](skills/learning-card-build/SKILL.md)
- [migration-plan](skills/migration-plan/SKILL.md)
- [mvp-analytics-plan](skills/mvp-analytics-plan/SKILL.md)
- [mvp-build-plan](skills/mvp-build-plan/SKILL.md)
- [mvp-deploy-plan](skills/mvp-deploy-plan/SKILL.md)
- [mvp-feasibility](skills/mvp-feasibility/SKILL.md)
- [mvp-metrics](skills/mvp-metrics/SKILL.md)
- [mvp-open-questions](skills/mvp-open-questions/SKILL.md)
- [mvp-schema-plan](skills/mvp-schema-plan/SKILL.md)
- [mvp-scope](skills/mvp-scope/SKILL.md)
- [mvp-tech-plan](skills/mvp-tech-plan/SKILL.md)
- [mvp-type-select](skills/mvp-type-select/SKILL.md)
- [paper-prototype](skills/paper-prototype/SKILL.md)
- [phase-router](skills/phase-router/SKILL.md)
- [pitch-1min-build](skills/pitch-1min-build/SKILL.md)
- [pivot-refine-log](skills/pivot-refine-log/SKILL.md)
- [product-channel-fit-check](skills/product-channel-fit-check/SKILL.md)
- [prototype-feedback-collect](skills/prototype-feedback-collect/SKILL.md)
- [prototype-vs-mvp-distinguish](skills/prototype-vs-mvp-distinguish/SKILL.md)
- [six-ways-to-innovate](skills/six-ways-to-innovate/SKILL.md)
- [supabase-schema-design](skills/supabase-schema-design/SKILL.md)
- [swot-build](skills/swot-build/SKILL.md)
- [tech-stack-recommender](skills/tech-stack-recommender/SKILL.md)
- [test-card-build](skills/test-card-build/SKILL.md)
- [uvp-statement](skills/uvp-statement/SKILL.md)
- [value-map-build](skills/value-map-build/SKILL.md)
- [venture-handoff-doc](skills/venture-handoff-doc/SKILL.md)
- [venture-init](skills/venture-init/SKILL.md)
- [venture-status](skills/venture-status/SKILL.md)
- [vision-sketch](skills/vision-sketch/SKILL.md)
- [vpc-fit-check](skills/vpc-fit-check/SKILL.md)
- [vpc-version](skills/vpc-version/SKILL.md)

The complete [per-skill audit](../docs/audits/2026-09-19-marketplace-audit.md#startups-skill-by-skill-disposition)
separates repaired defects from proposed consolidation. Do not remove aliases or
merge workflow contracts without evaluations and migration guidance.
