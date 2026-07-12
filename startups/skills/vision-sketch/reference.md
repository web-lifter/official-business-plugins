# vision-sketch — reference

## BMC cell mapping for seed hypotheses

When `vision-sketch` seeds hypotheses, it tags each one with a BMC cell.
Heuristic mapping from the answer type to the cell:

| Answer | Cell |
|---|---|
| "Top customer problem" | `Customer Segments` (the segment that has this problem) |
| "How the idea helps solve it" | `Value Propositions` |
| "Day-in-the-life: who they're talking to" | `Channels` if the conversation is mediated; `Customer Relationships` if direct |
| "Day-in-the-life: what tools they use" | `Key Resources` (if we're replacing the tool); `Key Activities` (if we're augmenting it) |

When in doubt, tag `Value Propositions` and let the BMC build pass
correct it later.

## Frontmatter checklist

```yaml
---
title: Vision sketch
slug: vision-sketch
type: vision           # must match the venture profile enum
status: active         # draft if the user explicitly said "still figuring it out"
owner: <venture name>  # not a person — the venture itself owns vision pages
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Style for the "Day in the life" sections

- 150-200 words per side
- Concrete: name the customer, the time of day, the tools, the people
- One specific frustration per paragraph
- "After" must change at least one observable behaviour from "Before"

A "Day in the life" with no behaviour changes between Before and After
is a sign the value proposition isn't real yet — flag it.

## When to bump to v2

The vision sketch isn't versioned the same way the BMC is. It's
refreshed in place when:

- A pivot happens (per `pivot-refine-log`)
- ≥ 5 interviews have suggested the customer's day-in-the-life is
  different from what was sketched
- The BMC value-propositions cell has been substantially rewritten

Each refresh archives the prior version under `00-vision/.archive/`.
