---
name: customer-segment-define
description: Walk the user through specifying customer segments — occupation, demographics, problems they have. Distinguishes users from paying customers per Blank's customer-development model. Scaffolds the segment folder with required files. Optional richer personas via brand-manager.
argument-hint: <segment-slug> [optional one-line description]
allowed-tools: Read Write Bash Glob
effort: medium
---

# customer-segment-define

Idempotency: refuses to overwrite an existing segment without `--update`. With `--update`, re-runs preserve already-populated profile / early-adopter / interview-guide content.

Method: customer-segment definition per Steve Blank's customer-development model. Insists on the user-vs-paying-customer distinction (a user is not necessarily a buyer; the *Startup Owner's Manual* treats these as separate roles). See `references.md` and `startups/SOURCES.md`.

## User Context

$ARGUMENTS

`<segment-slug>` is required (kebab-case). The optional description
seeds the question loop in Phase 2.

---

## Phase 1: Pre-flight

**Objective:** Confirm we're in a venture and the slug is fresh.

1. Verify `memex.config.json#/profile == "venture"`.
2. Confirm `02-customer-discovery/segments/<slug>/` does **not** already
   exist. If it does:
   - If `--update` was passed, proceed to Phase 2 with existing values
     pre-loaded.
   - Otherwise refuse and suggest `--update`.
3. Read `00-vision/vision-sketch.md` and the hypothesis register —
   pre-fill candidate problems for the segment from the vision's
   "Customers' top problems" section.

---

## Phase 2: Define the segment

**Objective:** Produce specific, observable answers — not abstractions.

Use `AskUserQuestion` to gather:

1. **Who they are** (occupation, role, function in their org, life
   stage). Be specific: "café owner with 2-5 employees in inner Sydney
   suburbs," not "small business owner."
2. **Where they are** (geography — city / region / country, channel —
   online / in-store / phone). If multiple, list each.
3. **What they're trying to do** (the *job to be done*; one sentence,
   active voice).
4. **What's currently in their way** (the top 1-3 problems —
   observable, not abstract).
5. **User vs paying customer** — explicit declaration of which one we
   mean. If they're different people, both need to be defined; create
   one sub-segment per role (`<slug>-user` and `<slug>-buyer`).
6. **Sub-segments** — if there are obvious sub-types (e.g. "café owner"
   splits into "single store" vs "multi-site"), name them.
7. **Optional richer persona** — ask whether the user wants to delegate
   to `brand-manager/target-audience` for a deeper psychographic
   persona. If yes, hand off (the brand-manager skill writes its output
   into a `persona.md` alongside `profile.md`).

---

## Phase 3: Scaffold the segment folder

**Objective:** Create the directory and stub files. The
`readme-required` hook insists on `README.md`; we satisfy it
immediately.

Create:

- `02-customer-discovery/segments/<slug>/README.md` — folder map for
  the segment, with the answers from Phase 2 distilled.
- `02-customer-discovery/segments/<slug>/profile.md` — empty stub with
  three `## ` headings (Jobs / Pains / Gains), filled in by
  `customer-profile-build`.
- `02-customer-discovery/segments/<slug>/early-adopters.md` — empty
  stub, filled in by `early-adopter-profile`.
- `02-customer-discovery/segments/<slug>/interview-guide.md` — empty
  stub, filled in by `interview-guide-build`.
- `02-customer-discovery/segments/<slug>/interviews/.keep` — empty file
  to preserve the directory; interviews land here.

All files require frontmatter:

```yaml
---
title: <segment label>
slug: <segment-slug>
type: segment
status: draft
owner: <venture name>
created: <today>
updated: <today>
---
```

The `README.md` is the only file with `type: segment`; the others use
`type: profile`, `type: profile`, `type: profile`, etc. (see
`reference.md` §1 for the per-file type mapping).

---

## Phase 4: Update the index and log

**Objective:** Make the segment discoverable.

1. Memex's `index-update.py` hook will pick up the new `README.md` and
   add it to the `Segments` section of `index.md` automatically.
2. Append a log entry:
   `## [<today>] segment | <slug> defined`.
3. Print the next-step suggestion:
   - `/customer-profile-build <slug>` — fill in jobs/pains/gains
   - `/early-adopter-profile <slug>` — identify earlyvangelists

---

## Important principles

- **Observable, not abstract.** Reject "small business owners struggle
  with efficiency"; require "Owners of independent cafés in inner
  Sydney spend 4+ hours each Friday reconciling supplier invoices on
  paper."
- **User ≠ paying customer always.** If they differ, model both. Blank is explicit about this distinction (`references.md`).
- **One folder per segment.** Sub-segments are sub-folders; never use a
  shared folder for two distinct segments.
- **Don't pre-write the profile.** This skill scaffolds shells; the
  next skill in the sequence (`customer-profile-build`) fills them in.
- **Re-entrant.** With `--update`, re-run safely without clobbering
  filled-in profile / early-adopter / interview-guide content.

## Edge cases

1. **Slug collision** — refuse, suggest a more specific slug.
2. **Multiple segments at once** — run the skill once per segment; the
   orchestrator agent handles the loop.
3. **User describes a market segment, not a customer segment** — push
   back: "ABS small businesses" is a market; "café owners with 2-5
   staff in inner Sydney" is a customer segment.
4. **Optional persona delegation chosen but `brand-manager` not
   installed** — skip with a warning; `profile.md` and
   `early-adopters.md` are still scaffolded.
