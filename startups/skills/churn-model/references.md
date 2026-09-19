# Retention model derivation

Let monthly retention be `r` and churn `c=1-r`. A starting cohort of one has expected surviving share `r**n` after n periods. Expected paid periods, including the initial period, are the geometric sum `1 + r + r**2 + ... = 1/(1-r)` for `0 <= r < 1`. This is a derivation, not a quotation from a book. At `r=1` the sum does not converge.

The model assumes constant hazards and ignores expansion revenue, discounting, censoring and customer heterogeneity. Mean lifetime is not median lifetime. Five-percentage-point sensitivity is a scenario choice, not an empirical claim of a specific profit improvement. External retention benchmarks need independently verified sources and comparable populations. See [source boundaries](../../SOURCES.md).
