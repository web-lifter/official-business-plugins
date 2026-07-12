---
title: Digital prototype handoff — contractiq-clause-review
slug: digital-handoff-contractiq-clause-review
type: prototype
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Digital prototype handoff

Figma file: ContractIQ-MVP
File id: `ABC123` *(placeholder — replace with the actual ID once the Figma file is created at e.g. `https://www.figma.com/file/ABC123/ContractIQ-MVP`)*
Last modified: 2026-05-20T14:32:00+10:00
Pages: 3 (Flows, Components, Tokens)

> **Note for reviewers:** this example documents what the output spec looks like. The Figma file ID is illustrative; in a live run, the Figma MCP returns the real ID and the metadata block is populated automatically. If the MCP is not connected, this section is replaced with a stub and the user is asked to connect the MCP and re-run.

## Screens captured

- ![Upload screen](screen-1-upload.png)
- ![Findings list + clause detail](screen-3-findings.png)
- ![Annotation modal](screen-4-annotate.png)
- ![Export](screen-5-export.png)

## Component inventory

| Figma component | Variants | Inferred props | React name | Code-connect map |
|-----------------|----------|----------------|------------|------------------|
| `FindingCard`   | risky / missing / obligation; reviewed / pending | `kind`, `status`, `clauseRef`, `summary` | `<FindingCard />` | `components/findings/FindingCard.tsx` |
| `ClauseDetailPane` | with-rationale / without; approved / rejected / annotated | `clause`, `rationale`, `verdict`, `onVerdict` | `<ClauseDetailPane />` | `components/findings/ClauseDetailPane.tsx` |
| `AnnotateModal` | default / saving | `clauseId`, `presets`, `onSave` | `<AnnotateModal />` | `components/findings/AnnotateModal.tsx` |
| `UploadDropzone` | empty / dragging / processing | `accept`, `onDrop` | `<UploadDropzone />` | `components/upload/UploadDropzone.tsx` |
| `ExportButton` | docx / pdf / email | `kind`, `onClick` | `<ExportButton />` | `components/export/ExportButton.tsx` |

## Design tokens

### Colour

| Variable | Value | OKLCH |
|----------|-------|-------|
| `--ciq-risk-high` | #C0392B | oklch(0.55 0.18 28) |
| `--ciq-risk-low` | #E67E22 | oklch(0.71 0.14 55) |
| `--ciq-ok` | #27AE60 | oklch(0.66 0.16 150) |
| `--ciq-bg` | #FAFAFA | oklch(0.98 0 0) |
| `--ciq-fg` | #1A1A1A | oklch(0.20 0 0) |
| `--ciq-accent` | #2563EB | oklch(0.56 0.20 264) |

### Spacing

| Variable | Value |
|----------|-------|
| `--ciq-space-1` | 4px |
| `--ciq-space-2` | 8px |
| `--ciq-space-3` | 12px |
| `--ciq-space-4` | 16px |
| `--ciq-space-6` | 24px |
| `--ciq-space-8` | 32px |

### Typography

| Variable | Family | Size | Weight |
|----------|--------|------|--------|
| `--ciq-font-body` | Inter | 14px | 400 |
| `--ciq-font-clause` | "IBM Plex Serif" | 15px | 400 |
| `--ciq-font-heading` | Inter | 20px | 600 |
| `--ciq-font-mono` | "JetBrains Mono" | 13px | 400 |

## Linked libraries

- `shadcn/ui base` (v0.9) — buttons, modals, scroll-areas.
- `ContractIQ-icons` (internal) — clause-type pictograms.

## Hand-off to engineering

- **Token export plan:** write `tokens.json` to `08-prototype/digital/contractiq-clause-review/` for Tom (CTO) to import into `apps/web/lib/tokens.ts`. Tailwind config consumes the JSON via the `tokens-to-tailwind` script.
- **Code-connect mapping plan:** start with `FindingCard` and `ClauseDetailPane` — they are the highest-traffic components in the H-002 usability test. Defer `AnnotateModal` mapping to after the first feedback session.
- **Open design questions:** filed at `.open-questions/2026-05-21-clause-detail-layout.md` — sticky action bar vs in-pane. Not blocking the prototype; resolve after session 1.
