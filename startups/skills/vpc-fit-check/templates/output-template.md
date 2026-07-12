# Fit report — {{segment-label}} v{{N}}

Generated {{today}}.

## Pain coverage

| Pain (priority) | Relievers | Status |
|-----------------|-----------|--------|
| {{pain}} (high) | {{count}} | {{✓ | ✗}} |
| {{pain}} (medium) | {{count}} | {{✓ | ✗}} |

## Gain coverage

| Gain (priority) | Creators | Status |
|-----------------|----------|--------|
| {{gain}} (high) | {{count}} | {{✓ | ✗}} |
| {{gain}} (medium) | {{count}} | {{✓ | ✗}} |

## Verdict

- **Fit:** {{yes | partial — <gap-summary> | no — <gap-summary>}}
- **VPC status set to:** {{active | draft}}
- **Action:** {{if not fit, recommend value-map-build refresh; if fit, ready for downstream skills}}

## Gap list (if partial or no)

- {{specific gap, e.g. "P-04 (confidentiality) has no reliever — value-map-build should add an explicit data-handling story"}}
- {{...}}
