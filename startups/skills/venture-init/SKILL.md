---
name: venture-init
description: "Create a self-contained venture workspace, or reuse a verified existing one, without overwriting files or requiring Memex."
argument-hint: "[venture-slug]"
allowed-tools: Read Write Edit Glob Grep Bash
effort: medium
---

# venture-init

## Runtime preflight

Read [the runtime guide](../../RUNTIME.md) before this workflow.

## User Context

$ARGUMENTS

## Phase 1: Select the workspace

Resolve the project and venture from the user's request. Use a lowercase kebab-case slug. Existing Memex ventures remain in place under the optional legacy adapter described in the runtime guide; do not reinitialise them or overwrite their config. When more than one venture exists, ask which one the user means. An empty input is not permission to create a workspace with an invented name.

## Phase 2: Initialise safely

With local execution, run the bundled helper from the installed plugin:

```bash
python3 <plugin-root>/scripts/venture_workspace.py init --project <project-root> --venture <slug>
```

The root is `.project/plans/startups/<slug>/`. The helper creates `venture.json`, `index.md`, `log.md`, numbered phase directories, `.open-questions/`, a draft vision, day-in-life draft and hypothesis register. It uses exclusive file creation: an existing file is preserved, including user edits; there is no destructive `--force` mode. A partial initialisation can be rerun. Surface errors and preserve partial state, never delete it automatically.

Without execution but with file-write tools, follow the same exclusive-create contract and use the [output template](templates/output-template.md). Without a mounted project, return the scaffold as a clearly labelled proposed artefact; do not say it was installed.

## Phase 3: Verify and report

Read back the profile and created files. Report the actual root, created files, preserved files and any missing directories. Do not mark draft vision content as validated evidence. Log only a successful initial creation; a no-op rerun must not append duplicate init entries.

Recommend `vision-sketch` as the next substantive action. Skills remain available under their existing names. No Memex, MCP connection or infrastructure deployment is required.
