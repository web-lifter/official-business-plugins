# Customer-discovery status — {{venture-name}}

Generated {{today}}. Primary segment: {{primary-slug}}.

## Venture rollup: {{🟢 | 🟡 | 🔴}}

{{One-paragraph summary of what the colour means and what to do next.}}

## Per-segment

### {{segment-slug}}: {{🟢 | 🟡 | 🔴}}

| # | Question | Status | Evidence |
|---|----------|--------|----------|
| 1 | Have we found a problem people care about? | {{✓ | ✗}} | {{N}}/{{total}} interviews mention high-pain in day-in-life |
| 2 | Have we got the right segment? | {{✓ | ✗}} | profile.md ({{N}} pains, {{N}} gains) + early-adopters.md ({{N/5}} criteria) |
| 3 | Have we got the right early adopters? | {{✓ | ✗}} | {{N}} named with ≥ 2× engagement (need ≥ 3) |
| 4 | Are they willing to engage? | {{✓ | ✗}} | {{N}} learning cards with hard-commitment evidence |

#### Gap list

- {{Q3: name 2 more earlyvangelists with 5/5 criteria and ≥ 2 contacts}}
- {{Q4: build a test card whose result is a hard commitment — see /test-card-build}}

## Machine-readable summary

```json
{
  "rollup": "{{green|yellow|red}}",
  "segments": {
    "{{slug}}": {
      "color": "{{green|yellow|red}}",
      "q1": {{true|false}},
      "q2": {{true|false}},
      "q3": {{true|false}},
      "q4": {{true|false}},
      "gaps": ["{{gap}}"]
    }
  }
}
```
