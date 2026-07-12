# references — learning-card-build

The four-part learning card — **we tested / observed / learned / will now** — is from:

- **Osterwalder, Alexander; Pigneur, Yves; Bernarda, Greg; Smith, Alan.** *Value Proposition Design.* Wiley, 2014. ISBN 978-1-118-96805-5. — Section 3.3 ("Learn").

The validated-learning discipline that requires every test to produce a follow-up decision (confirm / refute / refine-and-retest / pivot) is from:

- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011. — "a test that produces no follow-up decision is wasted work."

The skill enforces:

1. **One learning card per concluded test card.** No batch closing.
2. **Observed must be specific.** Numbers, quotes, behaviours — not "it went well."
3. **The will-now decision is mandatory.** Without it the test is not validated learning.
4. **Hypothesis flip is the user's choice.** The skill outputs the recommended `/hypothesis-register flip` command but does not auto-flip — the user reviews and runs explicitly. This preserves the audit trail and prevents silent register mutations.

See `startups/SOURCES.md` for the full bibliography.

## Related skills

- `test-card-build` — produces the TC that this skill closes.
- `experiment-run-tracker` — populates the run-log that the learning card cites.
- `hypothesis-register` — receives the flip recommendation.
