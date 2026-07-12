---
title: Falsifiability check — H-{{NN}}
slug: falsifiability-check-H-{{NN}}-{{YYYY-MM-DD}}
type: falsifiability-check
status: {{pass|fail|fail-forced}}
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Falsifiability check — H-{{NN}}

## Verdict

**{{PASS|FAIL|FAIL (--force applied)}}**

## JSON sidecar

```json
{
  "id": "H-{{NN}}",
  "verdict": "{{pass|fail}}",
  "issues": [
    {
      "check": "{{falsifier|measurement|threshold|timeframe}}",
      "severity": "{{fail|warn}}",
      "message": "{{specific-actionable-message}}"
    }
  ]
}
```

## Detailed findings

### Falsifier

- {{present-or-vague-with-salvage-suggestion}}

### Measurement

- {{present-or-vague-with-salvage-suggestion}}

### Threshold

- {{present-or-vague-with-salvage-suggestion}}

### Timeframe

- {{present-or-vague-with-salvage-suggestion}}

## Override

{{If --force, this section logs the override to .memex/log.md.}}
