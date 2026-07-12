# references — experiment-prioritise

The **risk × impact × ease** prioritisation rubric is from:

- **Maurya, Ash.** *Running Lean* (3rd ed.). O'Reilly, 2022. — Maurya frames hypothesis prioritisation as a deliberate triage: which hypotheses, if wrong, hurt the most (risk); which, when answered, change the plan the most (impact); which can be tested cheaply (ease).

The 1–5 scoring scale per dimension and the multiplicative combination (max score 125) make the heuristic transparent — there is no "the model decides," the user can see and override every input.

Defaults:

- **Risk** — Customer Segments and Value Propositions cells usually score 4–5; Cost Structure 2–3 (because being wrong about a cost is recoverable, whereas being wrong about the segment is not).
- **Impact** — full pivot implications score 5; refinements score 2.
- **Ease** — customer interviews score 5; pre-orders and concierge MVPs score 2–3 because they take weeks.

The "ease is honest" rule (a 3-week test is not easy) is a direct reaction to a common failure mode where teams describe a multi-week experiment as "quick" and then never start it.

See `startups/SOURCES.md` for the full bibliography.

## Related skills

- `experiment-design` — chooses the experiment type for the top-ranked hypothesis.
- `hypothesis-register` — the source of the open hypothesis list.
