# Metric decision contract

Every hypothesis needs a metric definition, denominator/cohort, direction (`>=`, `<=` or an explicit interval), threshold, timeframe, data source, minimum usable sample, guardrails and a decision rule. A refund/churn ceiling must not be treated as a minimum target. Freeze rules before looking at outcomes. Missing data, instrumentation failures and insufficient samples yield `inconclusive`, not success or refutation. Passing an MVP test supports that hypothesis in that context; it does not automatically justify scale. See [sources](../../SOURCES.md).
