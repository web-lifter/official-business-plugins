---
title: Hypothesis priority — top {{N}}
slug: hypothesis-priority-{{YYYY-MM-DD}}
type: experiment-prioritise
status: draft
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Hypothesis priority — top {{N}}

Formula: `score = risk × impact × ease`. Max 125. Each dimension 1–5.

## Ranked list

| Rank | ID | Statement (short) | Risk | Impact | Ease | Score | Suggested type |
|---|---|---|---|---|---|---|---|
| 1 | H-{{NN}} | {{short}} | {{1-5}} | {{1-5}} | {{1-5}} | {{score}} | {{experiment-type}} |

## Recommendation

Run `/experiment-design H-{{top-id}}` to confirm experiment type, then
`/test-card-build H-{{top-id}} {{type}}`.

## Scoring notes

- {{note-on-any-score-the-user-overrode}}
- {{note-on-hypotheses-excluded-due-to-existing-test-cards}}
