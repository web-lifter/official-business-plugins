---
name: early-adopter-profile
description: Identify the early-adopter (earlyvangelist) sub-set of a segment using Blank's five criteria — has the problem, knows it, looking for a solution, cobbled a workaround, has budget. Writes segments/<slug>/early-adopters.md.
argument-hint: <segment-slug>
allowed-tools: Read Write Edit Bash Glob
effort: medium
---

# early-adopter-profile

Idempotency: re-running adds new named earlyvangelists to the roster without erasing existing rows.

Method: the five-criteria earlyvangelist definition from Steve Blank & Bob Dorf, *The Startup Owner's Manual* (K&S Ranch, 2012). See `references.md` and `startups/SOURCES.md`.

Earlyvangelists aren't just "early customers"; they're the sub-set who
will *evangelise* for the venture if it solves their problem. They are
the most reliable test population.

## User Context

$ARGUMENTS

`<segment-slug>` is required.

---

## Phase 1: Pre-flight

1. Verify the venture profile.
2. Verify the segment folder exists with at least a `profile.md`. If
   the profile is empty, recommend running `customer-profile-build`
   first.

---

## Phase 2: Apply the five criteria

**Objective:** Define the earlyvangelist persona within the segment by
walking through the five criteria.

Use `AskUserQuestion` to gather, for the segment:

1. **Have the problem** — describe the specific behaviour or context
   that signals they have the problem. Cite the segment's
   highest-priority pains.
2. **Know they have it** — they can name and articulate the problem
   themselves; they don't need to be educated about it. State how to
   distinguish "knows" from "feels vague discomfort."
3. **Actively looking for a solution** — they've Googled, asked peers,
   posted on forums, evaluated tools. Name 2-3 search terms or forum
   keywords they'd use.
4. **Cobbled together a workaround** — they're using spreadsheets,
   manual processes, second-best tools, or paying for something else.
   Describe the workaround.
5. **Has budget** — the budget exists somewhere (their own money, the
   department's tool budget, a personal subscription). Identify where
   it sits.

A real earlyvangelist scores yes on **all five**. People who score on
fewer are still potential customers, but not the test population.

---

## Phase 3: Name actual people if possible

**Objective:** Move from persona to roster.

Use `AskUserQuestion` to ask whether the user can name actual
earlyvangelists. For each named individual, capture:

- Name (or pseudonym if privacy is needed)
- Role / employer
- Contact channel (email / DM / referral path)
- Which of the 5 criteria they meet (ideally all)
- How we found them
- Last contact date (if any)
- Permission state (have they agreed to be contacted? for what?)

Targets:

- **3 named earlyvangelists per primary segment**, contact details
  available, who have engaged at least twice (interview + follow-up).
  This is the bar `customer-discovery-status` checks for question 3.

If the user can't name three, that's fine — the file can be filled
incrementally. The status gate will stay yellow until three are named.

---

## Phase 4: Write the file

Replace the contents of
`02-customer-discovery/segments/<slug>/early-adopters.md` (preserving
frontmatter, bumping `updated:`):

```markdown
---
<frontmatter, type: profile, status: active when at least one named>
---

# Early adopters — <segment label>

## The five criteria for this segment

### 1. Have the problem
<answer>

### 2. Know they have it
<answer>

### 3. Actively looking for a solution
<answer>

### 4. Cobbled together a workaround
<answer>

### 5. Has budget
<answer>

## Named earlyvangelists

| Name | Role | Contact | Criteria met | Found via | Last contact | Permission |
|---|---|---|---|---|---|---|
| <name> | <role> | <channel> | 5/5 | <referral path> | <date> | <interview-only|follow-up-ok|...> |

## How we'll find more

- <plan: who else to ask, what events, what forums>
```

---

## Phase 5: Log

Append:
`## [<today>] early-adopters | <slug> profile <created|updated, N named>`.

---

## Important principles

- **All five, or it's not an earlyvangelist.** The criteria are
  conjunctive. A budget-less "knows-they-have-it-and-looking" is still
  great, but they're a customer, not an evangelist.
- **Privacy by default.** Pseudonyms allowed; encode the real-name
  mapping in a private file outside the venture if needed.
- **Permission state matters.** "Will be interviewed once" is different
  from "Happy to be a design partner for 6 months." Distinguish.
- **3-named-per-segment is the bar for green.** Two is yellow. One is
  red. Tracked by `customer-discovery-status`.
- **Re-runnable.** Re-running adds new names without erasing existing
  rows.

## Edge cases

1. **B2B venture with one buyer per company** — earlyvangelists are
   often individual people, not companies. Roster individuals.
2. **Very early venture, zero named** — fine; describe the persona,
   leave the table empty, name the channels you'll use to find them.
3. **Earlyvangelists turn out to be different people from the segment
   profile** — that's a signal to re-segment. Recommend
   `customer-segment-define` for a sub-segment.
4. **Privacy regulations affect the contact column** — replace direct
   contact with referral path; never store real PII against pseudonyms
   in the same file.
