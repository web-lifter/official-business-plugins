---
title: MVP scope v1
slug: mvp-spec
type: mvp-spec
status: draft
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# MVP scope — v1

**Primary hypothesis:** [H-{{NN}}](../01-hypotheses/hypothesis-register.md)
**Primary segment:** [{{slug}}](../02-customer-discovery/segments/{{slug}}/README.md)
**Primary value prop:** from [vpc-{{slug}}-vN](../03-value-proposition/vpc-{{slug}}-vN.md)

## Cut / Keep / Maybe

### Keep (the MVP)

| Feature | Why required (to test H-{{NN}}) | Test signal |
|---------|--------------------------------|-------------|
| {{feature}} | {{reason}} | {{event/metric}} |

### Maybe (post-v1 candidates)

| Feature | Why deferred | Trigger to revisit |
|---------|--------------|--------------------|
| {{feature}} | {{reason}} | {{condition}} |

### Cut (out of MVP scope)

| Feature | Why cut |
|---------|---------|
| {{feature}} | {{reason}} |

## What this MVP proves (or doesn't)

- **Confirms / refutes:** {{H-NN}}
- **Does NOT test:** {{list other hypotheses}}

## MVP type (selected via `/mvp-type-select`)

To be set by `mvp-type-select`. Pre-order, audience-building, show-and-tell, or partial product.
