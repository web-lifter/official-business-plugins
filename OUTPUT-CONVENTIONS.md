# Output Conventions — `.project/` Folder Scheme

Every skill in this repo that writes files to disk MUST emit them under a
canonical `.project/<output-type>/` folder inside the working directory. This
keeps the user's project root clean and makes outputs discoverable, gitignorable,
and easy to clean up.

## Folder scheme

```
.project/
├── audits/        # audit reports + JSON sidecars + suggested patches
├── plans/         # plan files, migration plans, strategy plans
├── reports/       # analysis reports, snapshots, readouts
├── scaffolds/     # generated code, schemas, scaffolded artefacts
├── data/          # CSVs, JSON datasets, keyword lists, design tokens
└── briefs/        # creative briefs, content briefs, stakeholder briefs
```

## Shared workspace with John OS

`.project/` is a **shared workspace root** — the John OS marketplace
(https://github.com/johnoconnor0/johns-os) writes to the same root, one
namespace per plugin:

- `.project/.engineering/` — owned by John OS `engineering-lifecycle`
  (profiles, initiatives, decisions, ledger, dashboards, hygiene reports).
- `.project/business-development/` — owned by John OS `business-development`.

**Skills in THIS marketplace must never write inside those namespaces.**
Our skills own the generic output types above plus the per-family
sub-namespaces (`.project/.data-science/`, `.project/.economics/`,
`.project/.marketing-os/`, `.project/marketing/.branding/`,
`.project/marketing/.ppc/`). Because everything shares one root, John OS
dashboards and hygiene tooling can discover this marketplace's artefacts
without extra configuration — keep filenames descriptive and timestamped
so they read well in those rollups.

## Rules

1. **Always create the target folder first.** Before any `Write`, run
   `mkdir -p .project/<type>/` (or the multi-file subfolder equivalent).
2. **Never write to the project root.** No more `./<skill-name>.md` or
   `./report.json` at cwd. Every output goes under `.project/<type>/`.
3. **Filenames stay as before.** The convention only changes the prefix, not
   the basename. `database-design-audit.md` becomes
   `.project/audits/database-design-audit.md` — not renamed.
4. **Skills emitting multiple artefacts get their own subfolder.** A skill
   that writes a report plus an agent-reports directory plus sidecar JSON
   should write to `.project/<type>/<skill-name>/...` (or use a run ID for
   audits — see `application-audit` as the reference implementation).
5. **Templates and scripts must use the same paths.** Update
   `templates/*.md` and `scripts/*.sh` / `scripts/*.py` alongside `SKILL.md`
   so the convention is documented end-to-end.
6. **`.project/` belongs in `.gitignore` for downstream user projects.**
   This repo's own `.gitignore` may explicitly NOT ignore it for fixtures.

## Output-type guidance

| Type | When to use |
|---|---|
| `.project/audits/` | A review of existing state — code, config, schema, infrastructure, content, finance — producing findings + severity + suggested fixes. |
| `plans/` | A forward-looking sequence of steps the user will execute — migrations, rollouts, strategy plans, training programs. |
| `reports/` | A point-in-time analysis or summary — snapshots, performance reports, readouts, projections. Read-only narrative, no required action list. |
| `scaffolds/` | Generated executable artefacts — SQL bootstrap, RLS policies, JSON-LD schema, scaffolded skill directories. The output is meant to be applied as-is. |
| `data/` | Structured data the user feeds into other tools — CSV keyword lists, design tokens, entity graphs, redirect tables. |
| `briefs/` | Short input documents for collaborators — creative briefs, content briefs, stakeholder briefs, logo briefs. |

When in doubt, pick `reports/`. Cross-type artefacts go where the *primary*
artefact belongs (e.g. an audit with a tiny scaffold sidecar lives in
`.project/audits/`).

## Exclusions

**Plugins under `official-lifestyle-plugins/` are out of scope** for this
convention. The lifestyle category (`health-wellness`, `home-life-logistics`,
`personal-finance`, `personal-productivity`) is designed for chat / Cowork
environments, not
Claude Code project sessions. Those skills render their output in the chat
transcript itself; a working-directory `.project/` folder has no meaning in
that context.

Lifestyle skills retain their existing "save as" semantics for callers that
do happen to invoke them inside Claude Code. Do NOT retrofit them.

## Reference implementations

- The John OS `engineering-lifecycle` plugin
  (https://github.com/johnoconnor0/johns-os) — namespaced workspace under
  `.project/.engineering/` with a machine-readable ledger.
- `official-business-plugins/marketing` — per-family output root pattern under
  `.project/.marketing-os/`.

New skills SHOULD model their output layout on whichever of these is closer
to their shape.

## Adding a new skill

When scaffolding a new skill with `skill-creator`:

1. Pick the matching output type from the table above.
2. In `SKILL.md`'s output section, use:
   ```
   Save as: .project/<type>/<skill-name>.md
   (Run `mkdir -p .project/<type>` first.)
   ```
3. If the skill writes multiple files, use
   `.project/<type>/<skill-name>/<artefact>` instead.
4. Update `templates/` and `scripts/` to match.
