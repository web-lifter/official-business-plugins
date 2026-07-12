---
name: figma-design-handoff
description: Pull metadata from a Figma file via the Figma MCP — file metadata, design context, variables, screenshots, libraries. Produces a component spec, proposes a code-connect map, surfaces design tokens. Read-only with graceful degrade.
argument-hint: <figma-file-id-or-url>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# figma-design-handoff

Read-only Figma MCP integration. No mutating calls (`add_code_connect_map`, `send_code_connect_mappings`) are issued.

Idempotency: re-running for the same `<slug>` overwrites the README and `tokens.json`; screenshots are versioned by frame name.

Graceful degrade: if the Figma MCP is not connected, the skill produces a docs-only template the user can hand-fill, and instructs them to connect the MCP and re-run.

## User Context

$ARGUMENTS

`<figma-file-id-or-url>` is required.

## Phase 1: Pre-flight

1. Verify venture profile.
2. Detect whether the Figma MCP is connected. If not, fall back to a
   docs-only plan that lists what *would* be pulled, and instruct the
   user to connect the MCP and re-run.

## Phase 2: Probe

If Figma MCP available, in parallel:

- `mcp__4a7796cc-...__get_metadata` — file name, last modified,
  page count
- `mcp__4a7796cc-...__get_design_context` — components and variants
- `mcp__4a7796cc-...__get_variable_defs` — design tokens (colour,
  spacing, typography)
- `mcp__4a7796cc-...__get_libraries` — linked design libraries
- For 1-3 key screens: `mcp__4a7796cc-...__get_screenshot`

## Phase 3: Compose component spec

For each major component:

- Name (Figma)
- Variants
- Props inferred from variants
- Likely React component name
- Code-connect mapping proposal

## Phase 4: Write

Write `08-prototype/digital/<slug>/README.md`:

```markdown
---
title: Digital prototype handoff — <slug>
slug: digital-handoff-<slug>
type: prototype
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Digital prototype handoff

Figma file: <name>
File id: <id>
Last modified: <timestamp>
Pages: <count>

## Screens captured

- ![Screen 1](screen-1.png)
- ...

## Component inventory

| Figma component | Variants | Inferred props | React name | Code-connect map |

## Design tokens

### Colour
| Variable | Value | OKLCH |

### Spacing
| Variable | Value |

### Typography
| Variable | Family | Size | Weight |

## Linked libraries

- ...

## Hand-off to engineering

- Token export plan: <where these go in the codebase>
- Code-connect mapping plan: <which components map first>
- Open design questions: <any> file under `.open-questions/` if
  blocking
```

## Phase 5: Export tokens

Write `08-prototype/digital/<slug>/tokens.json` with the design tokens
in a portable format (CSS variables / Tailwind config-ready).

## Phase 6: Log

Append: `## [<today>] figma-handoff | <slug>`.

## Important principles

- **Read-only.** No `add_code_connect_map` or `send_code_connect_mappings`
  in this skill — those are explicit mutations and would require the
  gated flow if added later.
- **Graceful degrade.** Without the MCP, the skill produces a
  template the user can fill in manually.
- **Tokens exported in portable JSON.** Then any downstream skill
  (CSS variables, Tailwind, Style Dictionary) can consume them.
- **Screenshots saved as files.** Not embedded base64.
- **No mutating Figma calls.** Currently the Figma MCP scope used is
  all read-only.
