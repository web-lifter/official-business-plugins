# Web Lifter Claude Plugins — Development Standards

## Conventions

- **Australian English** in all narrative text (colour, optimise, behaviour, organisation)
- **Markdown-first** outputs — every skill produces structured markdown
- **Evidence-backed** — findings include file:line references and confidence scores where applicable

## Skill Structure

Every skill lives under `<plugin-name>/skills/<skill-name>/` (where `<plugin-name>` is one of the five plugins: `business-operations`, `data-science`, `economics`, `marketing`, `startups`) and must contain:

```
<skill-name>/
├── SKILL.md              # Main skill instructions (under 500 lines)
├── LICENSE.txt           # MIT or Apache 2.0
├── templates/
│   └── output-template.md    # Output format skeleton with {{placeholders}}
└── examples/
    └── example-output.md     # Realistic completed example
```

Optional:

- `reference.md` — Dense reference material (SQL templates, scoring rubrics, lookup tables) extracted to keep SKILL.md under 500 lines
- `scripts/` — Python or Bash helpers for the skill

## SKILL.md Frontmatter

The authoritative reference is [the Claude Code Skills docs](https://code.claude.com/docs/en/skills.md). The repo's contract follows that schema verbatim. Every SKILL.md must validate cleanly under `claude plugin validate <plugin-path>` — that command exercises the same parser Claude Code uses at install time.

### Canonical shape

```yaml
---
name: skill-name-in-kebab-case
description: One-line use case, front-loaded with the trigger and outcome.
argument-hint: [what-the-user-should-provide]
allowed-tools: Read Write Edit Glob Grep Bash Agent
effort: medium
---
```

### Required vs optional

Per the official spec, **only `description` is recommended** — every field including `name` is technically optional (the parent directory name is used as the skill identifier if `name` is omitted). In this repo we additionally require `name` (for explicitness), `argument-hint` (so users see what to pass), and `effort` (so the harness can route appropriately).

| Field | Status in this repo | Format / constraint |
|-------|--------------------|---------------------|
| `name` | Required | Kebab-case, must equal the parent directory name. Max 64 chars. |
| `description` | Required | Single line, up to 1,536 chars combined with `when_to_use` (the official cap). Front-load the trigger. |
| `argument-hint` | Required | Bracket form `[placeholder]`. Quote the whole value if it contains nested brackets, `|`, or `:` — those characters break YAML parsing. |
| `allowed-tools` | Optional | Space-separated string. Quote the value if it contains `*` followed by `)`, or `:` inside `Bash(...)` patterns that YAML mis-parses as anchors. |
| `effort` | Required | One of `low`, `medium`, `high`, `xhigh`, `max`. |
| `when_to_use` | Optional | Extra trigger context appended to `description`. Counts toward the 1,536-char cap. |
| `arguments` | Optional | Named positional arguments for `$name` substitution in skill content. Space-separated string or YAML list. |
| `paths` | Optional | Glob patterns that scope auto-activation. Comma-separated string or YAML list. Pick one form per file. |
| `context` | Optional | Only valid value is `fork` — runs the skill in a forked subagent context. |
| `agent` | Optional | Subagent type to use when `context: fork` is set. |
| `model` | Optional | Override the session's model for this skill. |
| `disable-model-invocation` | Optional | `true` prevents Claude from auto-loading the skill (manual `/`-invocation only). |
| `user-invocable` | Optional | `false` hides the skill from the `/` menu (Claude-only). |
| `shell` | Optional | `bash` (default) or `powershell` — affects `` !`command` `` blocks. |

### Frontmatter rules to enforce

1. File MUST begin with `---` on line 1.
2. `ultrathink` is NOT a frontmatter field. Put it in the body, on a line of its own after the closing `---` (typically right under the title).
3. Quote the value if it contains any of: nested `[...]`, `|`, `*)` (YAML alias), or unbalanced `:` outside a `Bash(name:pattern)` group. When in doubt, wrap the whole value in double quotes.
4. Do NOT use undocumented fields. Unknown fields are silently dropped in older CLIs and surface as validation warnings in newer ones.
5. Run `claude plugin validate <plugin-path>` after every frontmatter change. If validation fails for the parent plugin, the skill loads with empty metadata at runtime.

## SKILL.md Body

After frontmatter, structure the skill as:

1. **Title** (`# Skill Name`) — followed by `ultrathink` on its own line if needed
2. **User Context** — receives `$ARGUMENTS` from the user
3. **System Prompt** — defines the persona and constraints
4. **Phases** — sequential workflow steps (typically 3-6 phases)
5. **Output Specification** — references the output template

### Phase Pattern

```markdown
## Phase N: Phase Title

### Objective
What this phase accomplishes.

### Steps
1. Step one
2. Step two

### Output
What this phase produces.
```

## Plugin Structure

Each plugin lives under `<plugin-name>/` and must contain:

```
<plugin-name>/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── skills/
│   └── <skill-name>/         # One or more skills
├── hooks/                    # Optional lifecycle hooks
│   ├── hooks.json
│   └── scripts/
│       └── suggest-related.sh
├── settings.json             # Plugin settings (usually empty {})
└── README.md                 # Plugin-level documentation
```

## Plugin Manifest (`plugin.json`)

Authoritative reference: [Claude Code Plugins reference](https://code.claude.com/docs/en/plugins-reference.md). Per the spec, **only `name` is required**; unrecognised top-level fields are warnings (not errors) in v2.1.143+, but historical CLIs (v2.1.141 and earlier) treat unrecognised keys as hard validation failures. **Keep manifests to the documented field set** so plugins install across the version range.

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Short description of what the plugin provides",
  "author": {
    "name": "John O'Connor",
    "email": "john@weblifter.com.au",
    "url": "https://github.com/johnoconnor0"
  },
  "homepage": "https://github.com/web-lifter/official-business-plugins/tree/main/plugin-name",
  "repository": "https://github.com/web-lifter/official-business-plugins",
  "license": "MIT",
  "keywords": ["relevant", "keywords"],
  "skills": "./skills/"
}
```

### Field-shape rules that have bitten us

1. **`agents` paths must be individual `.md` files**, not directory paths. The schema accepts a string or array of strings, but each string must point to a `.md` file — not `./skills/foo/agents/` (trailing slash directory). Enumerate every agent file explicitly. This is the field most likely to fail `claude plugin validate` with `agents: Invalid input`.
2. **`commands` paths follow the same rule** — individual `.md` files, or a directory like `./commands/` that contains them.
3. **`displayName`** is only recognised by Claude Code v2.1.143+. Omit it. Claude Code falls back to `name`, so there is no functional loss.
4. **Do NOT add `"hooks": "./hooks/hooks.json"` to `plugin.json`.** Claude Code automatically loads `hooks/hooks.json` if it exists — specifying it explicitly causes a "Duplicate hooks file detected" error that prevents the entire plugin from loading and hides all skills from the `/` menu. Only reference hooks in `plugin.json` if you need to load a *non-standard* hooks file at a different path. The hooks file itself uses the documented Stop / SessionStart / PreToolUse / PostToolUse schema with the outer `"hooks"` key and inner `"hooks"` array of handlers (see Hooks section below).
5. **Run `claude plugin validate <plugin-path>` after every change.** Treat any `× Validation failed` as an install blocker.

## Marketplace Registration

When adding a new plugin, add an entry to `.claude-plugin/marketplace.json`:

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Short description",
  "source": "./plugin-name",
  "category": "category-name",
  "homepage": "https://github.com/web-lifter/official-business-plugins/tree/main/plugin-name"
}
```

Categories: `lifestyle`, `smb`, `marketing`, `engineering`, `data-science`, `economics`, `utilities`, `seo`, `startups`, `venture-os`

## Hooks

The standard Stop hook suggests related skills after a skill completes:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash \"${CLAUDE_PLUGIN_ROOT}/hooks/scripts/suggest-related.sh\"",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

## Version Management

- Marketplace entry version in `marketplace.json` **must match** the plugin's `plugin.json` version
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Run `node scripts/check-versions.mjs` to validate consistency

## Quality Checklist

Before submitting a new skill:

- [ ] SKILL.md has valid YAML frontmatter with `name`, `description`, `argument-hint`, `effort`
- [ ] SKILL.md is under 500 lines
- [ ] Uses `$ARGUMENTS` for user input
- [ ] Description is single-line, front-loaded with the trigger, and within the 1,536-char official cap
- [ ] `effort` field is one of `low`, `medium`, `high`, `xhigh`, `max`
- [ ] `argument-hint` is bracket form `[placeholder]`. Quote the whole value if it contains nested brackets, `|`, or `:`
- [ ] `allowed-tools` is quoted if its value contains `*)` or `:` patterns that YAML would mis-parse
- [ ] No undocumented frontmatter fields (no `version:`, `models:`, `stack:`, etc.)
- [ ] `templates/` directory has at least one output template
- [ ] `examples/` directory has at least one example output
- [ ] Dense reference material is in `reference.md`, not SKILL.md
- [ ] Australian English used throughout
- [ ] `claude plugin validate <plugin-path>` exits 0 from the repo root

Before submitting a new plugin:

- [ ] `.claude-plugin/plugin.json` includes `name`, `version`, `description`; no `displayName`
- [ ] `agents` field (if present) lists individual `.md` files, never directory paths
- [ ] All paths referenced in the manifest resolve on disk
- [ ] Marketplace entry in `.claude-plugin/marketplace.json` matches the plugin's `version`
- [ ] `claude plugin validate <plugin-path>` passes
