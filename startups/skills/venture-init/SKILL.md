---
name: venture-init
description: Scaffold a new venture workspace by invoking `/memex:init venture`, then seed the vision-sketch stub, hypothesis register, and index.md so the venture is immediately usable. Idempotent — refuses to clobber an existing venture without --force.
argument-hint: [venture-name]
allowed-tools: Read Write Bash Glob
effort: low
---

# venture-init

Idempotency: refuses to overwrite an existing venture without `--force`. A no-op safe re-run prints what would happen.

Scaffolds a new venture workspace on top of the `@web-lifter/claude-memex`
venture profile. After this skill runs the working directory has the full
`.memex/` tree (per the venture profile) plus an empty
`00-vision/vision-sketch.md` and an empty `01-hypotheses/hypothesis-register.md`
ready to populate.

## User Context

$ARGUMENTS

The user wants a fresh venture workspace. If the argument is empty, infer
the venture name from the current folder name and confirm before
proceeding.

---

## Phase 1: Pre-flight

**Objective:** Confirm we can scaffold safely.

1. Check for an existing `.memex/` or `memex.config.json` in the cwd. If
   either exists:
   - If both exist and `memex.config.json#/profile` is `venture`, this is
     a re-init. Refuse unless the caller passed `--force` and explain that
     re-init is destructive.
   - If they exist but the profile is something other than `venture`,
     refuse — the user should overlay rather than overwrite. Point them
     at `claude-memex/templates/profiles/venture/.memex/.rules/` and
     `/memex:init-profile` for an overlay flow.
   - If only one exists, refuse and ask the user to clean up first.
2. Validate the venture name. If `$ARGUMENTS` is empty, take the cwd's
   basename, slug-ify it (lower-case, replace spaces and underscores with
   hyphens), and ask the user to confirm with `AskUserQuestion` ("Use
   venture name `<slug>`? Yes / No, change name").
3. Verify the `claude-memex` plugin is installed and exposes the
   `/memex:init` slash command. If not, halt and tell the user to
   install `@web-lifter/claude-memex` first.

---

## Phase 2: Scaffold the venture profile

**Objective:** Run `/memex:init venture` and confirm the tree was created.

1. Invoke `/memex:init venture` (the slash command from `claude-memex`).
   This copies the venture profile template into the cwd and substitutes
   `{{ProjectName}}` in `CLAUDE.md` with the venture name confirmed in
   Phase 1.
2. Read back `memex.config.json` to confirm `profile == "venture"`. If the
   write failed, surface the error and halt without proceeding.
3. Confirm the 10 numbered phase folders exist by globbing
   `.memex/0[0-9]-*/`. If any are missing, the template copy failed —
   stop and report.

---

## Phase 3: Seed the vision and hypothesis stubs

**Objective:** Leave the venture in a state where the next skill in the
sequence has a real file to write to, not a placeholder.

1. Write `.memex/00-vision/vision-sketch.md` with a stub structure: three
   `## ` headings — *Customers' top problems*, *How our idea helps*,
   *Day-in-the-life: before vs after* — each with a `*To be answered.*`
   placeholder. Frontmatter:
   ```yaml
   ---
   title: Vision sketch
   slug: vision-sketch
   type: vision
   status: draft
   owner: <venture name>
   created: <today>
   updated: <today>
   ---
   ```
2. Write `.memex/00-vision/day-in-life.md` with two `## ` headings —
   *Before <venture-name>* and *After <venture-name>* — each with a
   `*To be answered.*` placeholder. Same frontmatter pattern with
   `slug: day-in-life`.
3. Write `.memex/01-hypotheses/hypothesis-register.md` with an empty table
   header (`| ID | Cell | Statement | Status | Updated |`) and a note
   explaining how to add entries. Frontmatter `slug: hypothesis-register`,
   `type: hypothesis`, `status: draft`.
4. Append a log entry to `.memex/log.md`:
   `## [<today>] init | venture <slug> created via venture-init`. Use the
   exact format from `memex.config.json#/log/entryPrefix`.

---

## Phase 4: Next-steps message

**Objective:** Tell the user what they should run next.

Print a short markdown block to the chat:

```
✓ Venture <slug> scaffolded.

Next 3 actions:
  1. /vision-sketch — write the real vision (replaces the stub).
  2. /customer-segment-define <segment-name> — name your first segment.
  3. /interview-guide-build <segment-name> — generate an interview guide.

Tip: open the workspace in the @web-lifter/memex desktop app for graph view
and BM25 search across the venture wiki.
```

---

## Important principles

- **Idempotent.** Re-running on the same directory without `--force` is a
  no-op that prints what would have happened. Re-running with `--force`
  warns first.
- **Read the venture profile, don't re-implement it.** The numeric folder
  layout, index sections, frontmatter enums all come from the profile.
  If the profile changes, this skill picks up the change automatically.
- **Don't mutate `memex.config.json`.** The profile is the source of
  truth. Edits go in the profile, not in this skill.
- **No connector calls.** This skill is local-only. No Supabase /
  Cloudflare / Figma / Vercel calls.
- **Log to `log.md`, not to the chat alone.** Memex's session-end hook
  augments the log; this skill also writes a synchronous entry on success
  so the chronology is complete the moment the skill ends.

## Edge cases

1. **Cwd contains a non-venture memex tree** — refuse, point to
   `/memex:init-profile` overlay.
2. **`/memex:init venture` fails partway** — report the error, do not
   delete partial state, ask the user to inspect.
3. **Venture name conflicts with an existing folder name in the cwd** —
   not a problem unless the user is creating a venture inside another
   project; warn but proceed.
4. **Empty `$ARGUMENTS`** — infer from cwd, confirm with `AskUserQuestion`.
5. **`--force` passed to a fresh dir** — still works; just doesn't trigger
   the safety prompt.
