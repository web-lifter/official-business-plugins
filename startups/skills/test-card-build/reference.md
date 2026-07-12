# test-card-build — reference

## §1. Experiment-type menu

From COMP1100 Ch. 5:

| Type | What it tests | Sample | Time | Cost |
|---|---|---|---|---|
| **Customer interview** | Problem real? Workaround real? Budget? | 5-10 per segment | 1-2 weeks | $0-300 |
| **Survey** | Pattern frequency across larger n | 50-200 | 1-2 weeks | $0-500 |
| **Smoke test** | Demand for a value prop | Audience (1k+ visitors) | 1-2 weeks | $200-1k |
| **Concierge MVP** | Will they pay manual delivery? | 3-10 paying | 4-8 weeks | $1-5k |
| **Wizard of Oz** | Do they engage when they think it's automatic? | 10-50 | 2-4 weeks | $500-3k |
| **Fake door** | Demand for a feature | Existing users | 1 week | $0-200 |
| **A/B** | Variant lift | Live audience | 2-4 weeks | $0-1k |
| **Pre-order** | Will they pay? | Segment audience | 2-4 weeks | $200-2k |
| **Letter of intent** | B2B commitment | 3-10 prospects | 2-6 weeks | $0-500 |

## §2. Picking the right type

| Hypothesis cell | Best test types |
|---|---|
| Customer Segments | Customer interview, Survey |
| Value Propositions | Smoke test, Concierge, Wizard of Oz |
| Channels | A/B, Smoke test |
| Customer Relationships | Concierge, Wizard of Oz |
| Revenue Streams | Pre-order, Letter of intent, A/B on pricing |
| Key Activities / Resources / Partners | Concierge, Letter of intent |
| Cost Structure | Concierge (real costs), benchmarks |

## §3. Threshold guidance

- For a binary outcome (paid / not paid), use a percentage threshold
  with a sample-size minimum: "≥30% of n=50."
- For a continuous metric (time, dollars), use median or 90th
  percentile, not mean: "median time ≤ 4 minutes."
- For a directional change, state the baseline: "from 12 minutes to
  ≤ 4 minutes."

## §4. Common failure modes

- **Threshold set after looking at the data** — invalid; the
  threshold is set at design time.
- **Sample too small** — n < 5 for interviews, n < 30 for surveys is
  usually under-powered. Acceptable for very high-effect-size tests.
- **Confirmation bias setup** — recruiting from your own network for
  validation is a known trap; surface the bias in the Risk section.
