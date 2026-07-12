# Brand Colour Palette — {{Brand Name}}

**Date:** {{DD/MM/YYYY}}
**Brand stage:** {{stage}}
**Where it's used:** {{web | product UI | print | packaging | video}}
**Accessibility target:** {{WCAG 2.2 AA | AA + AAA body text | AAA throughout}}

---

## 1. Palette Snapshot

| Role | Name | HEX | OKLCH (L, C, H) |
|---|---|---|---|
| Primary 1 | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Primary 2 | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Secondary 1 | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Success | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Warning | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Error | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Info | {{name}} | `{{#hex}}` | `{{L}}, {{C}}, {{H}}` |
| Neutral 50 → 950 | (ramp) | (see §5) | (see §5) |

---

## 2. Primary Colours

### {{Primary Name 1}}
- **HEX:** `{{#hex}}`
- **RGB:** `rgb({{r}}, {{g}}, {{b}})`
- **HSL:** `hsl({{h}}, {{s}}%, {{l}}%)`
- **OKLCH:** `oklch({{L}} {{C}} {{H}})`
- **Rationale:** {{Why this hue, this saturation, this lightness, given Phase 1 context.}}
- **Reference brands:** {{Brand 1}}, {{Brand 2}}
- **Cultural notes:** {{Any regional connotations the user should know about.}}

### {{Primary Name 2 — optional}}
{{...same fields...}}

---

## 3. Secondary Colours

### {{Secondary Name 1}}
- **HEX:** `{{#hex}}`
- **OKLCH:** `oklch({{L}} {{C}} {{H}})`
- **Rationale:** {{...}}
- **Where it appears:** {{e.g. illustrations, marketing only, never in product UI}}

<!-- 1–3 secondary colours -->

---

## 4. Semantic Colours

### Success
- **HEX:** `{{#hex}}`
- **OKLCH:** `oklch({{L}} {{C}} {{H}})`
- **AA on white:** {{ratio}} ✓ / ✗
- **AA on neutral-900:** {{ratio}} ✓ / ✗

### Warning
- **HEX:** `{{#hex}}`
- **OKLCH:** `oklch({{L}} {{C}} {{H}})`
- **AA on white:** {{ratio}}
- **AA on neutral-900:** {{ratio}}

### Error
- **HEX:** `{{#hex}}`
- **OKLCH:** `oklch({{L}} {{C}} {{H}})`
- **AA on white:** {{ratio}}
- **AA on neutral-900:** {{ratio}}

### Info
- **HEX:** `{{#hex}}`
- **OKLCH:** `oklch({{L}} {{C}} {{H}})`
- **AA on white:** {{ratio}}
- **AA on neutral-900:** {{ratio}}

---

## 5. Neutral Ramp

| Token | HEX | OKLCH L | Use |
|---|---|---|---|
| `neutral-50` | `{{#hex}}` | {{L}} | Page background (light mode) |
| `neutral-100` | `{{#hex}}` | {{L}} | Card background, hover |
| `neutral-200` | `{{#hex}}` | {{L}} | Subtle borders, dividers |
| `neutral-300` | `{{#hex}}` | {{L}} | Stronger borders, disabled |
| `neutral-400` | `{{#hex}}` | {{L}} | Placeholder, decorative icons |
| `neutral-500` | `{{#hex}}` | {{L}} | Secondary text, captions |
| `neutral-600` | `{{#hex}}` | {{L}} | Body text on light bg |
| `neutral-700` | `{{#hex}}` | {{L}} | Strong body, headings |
| `neutral-800` | `{{#hex}}` | {{L}} | Display headings |
| `neutral-900` | `{{#hex}}` | {{L}} | Highest emphasis text |
| `neutral-950` | `{{#hex}}` | {{L}} | Near-black background (dark mode) |

**Tint direction:** {{pure | warm | cool — and chroma value used}}

---

## 6. Contrast Validation

| Foreground | Background | Ratio | AA Body | AAA Body | AA Large | Status |
|---|---|---|---|---|---|---|
| Primary 1 | white | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | {{notes}} |
| Primary 1 | neutral-900 | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |
| neutral-900 | neutral-50 | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |
| neutral-600 | white | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |
| white | Primary 1 | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |
| white | Success | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |
| white | Warning | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |
| white | Error | {{ratio}}:1 | {{✓/✗}} | {{✓/✗}} | {{✓/✗}} | |

All ratios computed via `scripts/contrast-checker.py`.

---

## 7. Usage Hierarchy

| Surface | Background | Primary text | Buttons | Accents |
|---|---|---|---|---|
| Marketing landing pages | white / neutral-50 | neutral-900 | Primary 1 | Secondary 1 |
| Product UI (light) | white | neutral-900 | Primary 1 | (semantic) |
| Product UI (dark) | neutral-950 | neutral-100 | Primary 1 (lightened) | (semantic) |
| Print / brochures | white / neutral-50 | neutral-900 | Primary 1 | Secondary 1 |

---

## 8. Accessibility Notes

- {{e.g. "Colour-blindness check: success vs error pair has ΔL = 0.18, distinguishable for deutan and protan users."}}
- {{e.g. "AAA target met for body text on light mode; large text only for dark mode."}}
- {{e.g. "Cultural note: red is positive in Chinese markets; brand uses red sparingly to avoid danger connotation in Western audience."}}

---

## 9. Decision Log

| Decision | Options considered | Chosen | Rationale |
|---|---|---|---|
| Primary hue | {{...}} | {{...}} | {{...}} |
| Neutral tint | Pure / warm / cool | {{...}} | {{...}} |
| Semantic green hue | {{...}} | {{...}} | {{...}} |

---

## Appendix: JSON for `design-tokens` ingestion

```json
{
  "primary": {
    "1": {"hex": "{{#hex}}", "oklch": "oklch({{L}} {{C}} {{H}})", "name": "{{name}}"}
  },
  "secondary": {},
  "semantic": {
    "success": {"hex": "{{#hex}}"},
    "warning": {"hex": "{{#hex}}"},
    "error": {"hex": "{{#hex}}"},
    "info": {"hex": "{{#hex}}"}
  },
  "neutral": {
    "50": "{{#hex}}",
    "100": "{{#hex}}",
    "200": "{{#hex}}",
    "300": "{{#hex}}",
    "400": "{{#hex}}",
    "500": "{{#hex}}",
    "600": "{{#hex}}",
    "700": "{{#hex}}",
    "800": "{{#hex}}",
    "900": "{{#hex}}",
    "950": "{{#hex}}"
  }
}
```
