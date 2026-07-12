# venture-init — ContractIQ scaffold result

After running `/venture-init contractiq` in an empty `~/ventures/contractiq/` directory, the workspace looks like:

```
contractiq/
├── memex.config.json
├── CLAUDE.md                  # ProjectName substituted with "ContractIQ"
└── .memex/
    ├── index.md
    ├── log.md
    ├── 00-vision/
    │   ├── vision-sketch.md
    │   └── day-in-life.md
    ├── 01-hypotheses/
    │   └── hypothesis-register.md
    ├── 02-customer-discovery/
    ├── 03-value-proposition/
    ├── 04-competitors/
    ├── 05-business-model/
    ├── 06-relationships-channels/
    ├── 07-validation/
    ├── 08-prototype/
    └── 09-mvp/
```

## `.memex/00-vision/vision-sketch.md` (stub)

```yaml
---
title: Vision sketch
slug: vision-sketch
type: vision
status: draft
owner: contractiq
created: 2026-04-02
updated: 2026-04-02
---
```

```markdown
# Vision sketch — ContractIQ

## Customers' top problems
*To be answered.*

## How our idea helps
*To be answered.*

## Day-in-the-life: before vs after
*To be answered.*
```

## `.memex/01-hypotheses/hypothesis-register.md` (empty)

```yaml
---
title: Hypothesis register
slug: hypothesis-register
type: hypothesis
status: draft
owner: contractiq
created: 2026-04-02
updated: 2026-04-02
---
```

```markdown
# Hypothesis register — ContractIQ

| ID | Cell | Statement | Status | Updated |
|----|------|-----------|--------|---------|

Add entries via `/hypothesis-register add`. Every row needs a falsifier, measurement, threshold, and timeframe before it can be tested.
```

## `.memex/log.md` entry

```
## [2026-04-02] init | venture contractiq created via venture-init
```

## Chat output

```
✓ Venture contractiq scaffolded.

Next 3 actions:
  1. /vision-sketch — write the real vision (replaces the stub).
  2. /customer-segment-define au-midmarket-inhouse-counsel — name your first segment.
  3. /interview-guide-build au-midmarket-inhouse-counsel — generate an interview guide.

Tip: open the workspace in the @web-lifter/memex desktop app for graph view
and BM25 search across the venture wiki.
```

Founder Priya Natarajan ran this on 2026-04-02 before the first peer interview the same week. The `vision-sketch.md` and `hypothesis-register.md` stubs were filled out in subsequent skill runs (see [`/vision-sketch`](../../vision-sketch/examples/example-output.md) and [`/hypothesis-register`](../../hypothesis-register/examples/example-output.md)).
