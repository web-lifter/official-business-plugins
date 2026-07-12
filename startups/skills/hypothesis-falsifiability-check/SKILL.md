---
name: hypothesis-falsifiability-check
description: Audit a hypothesis for the four failure modes — no falsifier, no measurement, no threshold, no timeframe. Blocking. --force overrides and is logged.
argument-hint: [hypothesis-id-or-text]
allowed-tools: Read Edit Glob Grep
effort: low
---

# hypothesis-falsifiability-check

**Blocking gate.** Refuses to add or update a hypothesis that lacks an observable falsifier, a named measurement, a specific threshold, or a timeframe. Override with `--force`; the override is logged to `.memex/log.md`.

**Why it is blocking.** Eric Ries (*The Lean Startup*, 2011) defines validated learning as the difference between progress and motion: a startup advances when it runs experiments that can produce a refutation. A hypothesis without a falsifier cannot be refuted, so any experiment built on it is theatre. This skill enforces the discipline upstream of `/test-card-build`. See `references.md`.

**Override behaviour.** `--force` proceeds with the unsafe hypothesis and writes a `gate-override` entry to `.memex/log.md` so the bypass is traceable in the venture's audit trail. Use sparingly; the next reviewer (often you, three weeks later) will see it.

**Idempotency:** read-only on the register unless `--force` is set; safe to call repeatedly.

## User Context

$ARGUMENTS

If `$ARGUMENTS` is a hypothesis ID (`H-NN`), check that registered
hypothesis. If it's free text, treat as a candidate.

## Phase 1: Resolve target

1. If `H-NN` ID, read the row from `01-hypotheses/hypothesis-register.md`.
2. Otherwise treat `$ARGUMENTS` as a candidate statement; user must
   provide falsifier / measurement / threshold / timeframe via
   `AskUserQuestion`.

## Phase 2: Run the four checks

For each:

1. **Falsifier present** — answers "we are wrong if ..." with an
   observable outcome.
2. **Measurement present** — names the data source / instrument.
3. **Threshold present** — a specific pass/fail line.
4. **Timeframe present** — when we decide.

If any is missing or vague, refuse and surface the failure mode.

Vagueness heuristics from `reference.md` §1:

- Falsifier contains "users will love it" / "most" / "many" without
  numbers → vague
- Threshold contains "high adoption" / "good conversion" → vague
- Timeframe missing → vague

## Phase 3: Report

Return a structured JSON block:

```json
{
  "id": "H-NN",
  "verdict": "pass|fail",
  "issues": [
    {"check": "threshold", "severity": "fail", "message": "no
     specific number — replace 'most users' with '≥60% of segment-A'"}
  ]
}
```

Plus a markdown summary printed to chat.

## Phase 4: Apply or block

- `pass` — return success; the calling skill (e.g.
  `hypothesis-register`) proceeds.
- `fail` (no `--force`) — refuse, surface the gap list.
- `fail` with `--force` — proceed but log to `.memex/log.md`:
  `## [<today>] gate-override | hypothesis-falsifiability-check
  bypassed for H-NN (issues: <list>)`.

## Important principles

- **Read-only on the register** unless force-applying. The skill
  doesn't add or remove hypotheses; it audits.
- **Specific failure messages.** "Threshold vague" is useless; "no
  number — replace 'most users' with '≥60% of segment-A interviewees'"
  is actionable.
- **--force is logged.** Bypassing the gate is allowed; silently
  bypassing is not.

## Edge cases

1. Hypothesis is already `accepted` or `refuted` — informational only;
   doesn't gate further changes.
2. Multi-claim hypothesis ("X and Y") — split before checking; each
   half needs its own falsifier.
3. Hypothesis is a market sizing claim with public benchmark data —
   threshold is the benchmark; cite it explicitly.
