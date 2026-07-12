---
title: Digital prototype handoff — {{slug}}
slug: digital-handoff-{{slug}}
type: prototype
status: active
owner: {{venture_name}}
created: {{date}}
updated: {{date}}
---

# Digital prototype handoff

Figma file: {{figma_file_name}}
File id: {{figma_file_id}}
Last modified: {{timestamp}}
Pages: {{page_count}}

## Screens captured

- ![Screen 1]({{screen_1_filename}}.png)
- ![Screen 2]({{screen_2_filename}}.png)

## Component inventory

| Figma component | Variants | Inferred props | React name | Code-connect map |
|-----------------|----------|----------------|------------|------------------|
| {{component}}   | {{variants}} | {{props}}  | {{react}}  | {{map}}          |

## Design tokens

### Colour

| Variable | Value | OKLCH |
|----------|-------|-------|
| {{var}}  | {{hex}} | {{oklch}} |

### Spacing

| Variable | Value |
|----------|-------|
| {{var}}  | {{px}} |

### Typography

| Variable | Family | Size | Weight |
|----------|--------|------|--------|
| {{var}}  | {{family}} | {{size}} | {{weight}} |

## Linked libraries

- {{library}}

## Hand-off to engineering

- Token export plan: {{token_export_path}}
- Code-connect mapping plan: {{first_component_to_map}}
- Open design questions: {{any_blocking_questions}}
