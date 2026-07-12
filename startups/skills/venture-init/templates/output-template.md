# venture-init — scaffold result

This skill produces no single output file; it scaffolds a `.memex/` venture workspace. After a successful run the working directory contains:

```
{{venture-slug}}/
├── memex.config.json          # profile: venture
├── CLAUDE.md                  # substituted with {{venture-name}}
└── .memex/
    ├── index.md
    ├── log.md
    ├── 00-vision/
    │   ├── vision-sketch.md   # stub
    │   └── day-in-life.md     # stub
    ├── 01-hypotheses/
    │   └── hypothesis-register.md   # empty table
    ├── 02-customer-discovery/
    ├── 03-value-proposition/
    ├── 04-competitors/
    ├── 05-business-model/
    ├── 06-relationships-channels/
    ├── 07-validation/
    ├── 08-prototype/
    └── 09-mvp/
```

## Stub: vision-sketch.md

```yaml
---
title: Vision sketch
slug: vision-sketch
type: vision
status: draft
owner: {{venture-slug}}
created: {{today}}
updated: {{today}}
---
```

```markdown
# Vision sketch — {{venture-name}}

## Customers' top problems
*To be answered.*

## How our idea helps
*To be answered.*

## Day-in-the-life: before vs after
*To be answered.*
```

## Stub: hypothesis-register.md

```yaml
---
title: Hypothesis register
slug: hypothesis-register
type: hypothesis
status: draft
owner: {{venture-slug}}
created: {{today}}
updated: {{today}}
---
```

```markdown
# Hypothesis register — {{venture-name}}

| ID | Cell | Statement | Status | Updated |
|----|------|-----------|--------|---------|

Add entries via `/hypothesis-register add`. Every row needs a falsifier, measurement, threshold, and timeframe before it can be tested.
```

## Log entry

```
## [{{today}}] init | venture {{venture-slug}} created via venture-init
```

## Next-step message printed to chat

```
✓ Venture {{venture-slug}} scaffolded.

Next 3 actions:
  1. /vision-sketch — write the real vision (replaces the stub).
  2. /customer-segment-define <segment-name> — name your first segment.
  3. /interview-guide-build <segment-name> — generate an interview guide.
```
