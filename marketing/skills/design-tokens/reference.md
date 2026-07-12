# Design Tokens — Reference

Supplementary reference material for the `design-tokens` skill. Covers the W3C Design Tokens spec, Tailwind v4 theming, semantic naming taxonomies, and a comparison of token formats.

---

## Table of Contents

- [1. The W3C Design Tokens Spec](#1-the-w3c-design-tokens-spec)
- [2. Tailwind v4 vs v3](#2-tailwind-v4-vs-v3)
- [3. Semantic Token Taxonomy](#3-semantic-token-taxonomy)
- [4. Spacing Scale Standards](#4-spacing-scale-standards)
- [5. Type Scale Standards](#5-type-scale-standards)
- [6. Format Comparison](#6-format-comparison)
- [7. The `token-converter.py` Script](#7-the-token-converterpy-script)
- [8. Validation Checklist](#8-validation-checklist)

---

## 1. The W3C Design Tokens Spec

The W3C Design Tokens Community Group defines a JSON format for design tokens. Most modern token tools (Style Dictionary v4, Tokens Studio, Penpot, Figma Variables) read or write this format.

### Format basics

Every token has at minimum:
- `$value` — the value of the token (string, number, or composite object)
- `$type` — the type of the token (`color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `shadow`, etc.)

Tokens are grouped via nested JSON objects. Group names do not start with `$`.

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": { "$value": "#0A2540" },
      "mint":    { "$value": "#2EC4B6" }
    },
    "neutral": {
      "50":  { "$value": "#FAFAFB" },
      "100": { "$value": "#F4F4F6" },
      "900": { "$value": "#15151B" }
    }
  }
}
```

When `$type` is set on a group, all child tokens inherit it unless overridden.

### Token references (aliases)

Semantic tokens reference raw tokens using `{}` notation:

```json
{
  "color": {
    "bg": {
      "page": { "$value": "{color.neutral.50}" },
      "card": { "$value": "{color.neutral.100}" }
    },
    "text": {
      "primary":   { "$value": "{color.neutral.900}" },
      "secondary": { "$value": "{color.neutral.600}" }
    }
  }
}
```

The reference `{color.neutral.50}` is resolved at build time. This is what enables the raw/semantic separation.

### Composite types

Some token types are composite — shadow, gradient, typography:

```json
{
  "shadow": {
    "md": {
      "$type": "shadow",
      "$value": {
        "color": "#0000001a",
        "offsetX": "0px",
        "offsetY": "4px",
        "blur": "6px",
        "spread": "-1px"
      }
    }
  }
}
```

```json
{
  "typography": {
    "heading.h1": {
      "$type": "typography",
      "$value": {
        "fontFamily": "{font.family.heading}",
        "fontSize": "{font.size.4xl}",
        "fontWeight": "{font.weight.bold}",
        "lineHeight": "{font.line-height.tight}"
      }
    }
  }
}
```

### What's NOT in the spec

The W3C spec does not yet standardise:
- Modes (light/dark) — handled by tools, not the spec
- Theme variants — handled by tools
- Conditional values

For modes, the convention is to maintain separate semantic-token files (one per mode) that all reference the same raw tokens.

---

## 2. Tailwind v4 vs v3

Tailwind v4 (released Q1 2025) replaced the JavaScript config file with a CSS-first approach using the `@theme` directive.

### v3 (legacy)

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    colors: {
      brand: {
        primary: '#0A2540',
      },
    },
    spacing: {
      4: '1rem',
    },
  },
}
```

### v4 (current)

```css
/* app.css */
@import "tailwindcss";

@theme {
  --color-brand-primary: #0A2540;
  --spacing-4: 1rem;
  --radius-md: 0.5rem;
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}
```

Tailwind v4 generates utility classes directly from the CSS variables in `@theme`. So `--color-brand-primary` automatically creates `bg-brand-primary`, `text-brand-primary`, `border-brand-primary`, etc.

### Naming conventions in Tailwind v4

| CSS variable | Generated utilities |
|---|---|
| `--color-X-Y` | `bg-X-Y`, `text-X-Y`, `border-X-Y`, `fill-X-Y`, `stroke-X-Y` |
| `--spacing-N` | `p-N`, `m-N`, `gap-N`, `space-x-N`, etc. |
| `--radius-X` | `rounded-X` |
| `--font-X` | `font-X` |
| `--text-X` | `text-X` (for sizes) |
| `--shadow-X` | `shadow-X` |
| `--font-weight-X` | `font-X` (e.g. `font-semibold`) |
| `--leading-X` | `leading-X` |
| `--tracking-X` | `tracking-X` |

### Dark mode in v4

```css
@theme {
  --color-bg-page: #FAFAFB;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg-page: #0A0A0E;
  }
}

/* Or class-based: */
.dark {
  --color-bg-page: #0A0A0E;
}
```

The semantic tokens flip between light and dark; the raw tokens stay the same.

---

## 3. Semantic Token Taxonomy

A standard semantic token vocabulary for product UI:

### Background tokens

| Token | Purpose | Light raw | Dark raw |
|---|---|---|---|
| `color.bg.page` | Outermost page background | neutral-50 | neutral-950 |
| `color.bg.card` | Card / panel background | white | neutral-900 |
| `color.bg.subtle` | Subtle accent backgrounds | neutral-100 | neutral-800 |
| `color.bg.muted` | Disabled / muted backgrounds | neutral-200 | neutral-700 |
| `color.bg.inverse` | High-contrast inverse | neutral-900 | neutral-100 |

### Text tokens

| Token | Purpose | Light raw | Dark raw |
|---|---|---|---|
| `color.text.primary` | Body text, default content | neutral-900 | neutral-100 |
| `color.text.secondary` | Captions, supporting text | neutral-600 | neutral-400 |
| `color.text.disabled` | Disabled inputs/text | neutral-400 | neutral-600 |
| `color.text.inverse` | Text on inverse bg | white | neutral-900 |
| `color.text.link` | Links | brand-primary | brand-primary-light |
| `color.text.link-visited` | Visited links | brand-primary-dark | brand-primary |

### Border tokens

| Token | Purpose | Light raw | Dark raw |
|---|---|---|---|
| `color.border.subtle` | Hairline dividers | neutral-200 | neutral-800 |
| `color.border.default` | Standard borders | neutral-300 | neutral-700 |
| `color.border.strong` | Emphasised borders | neutral-400 | neutral-600 |
| `color.border.focus` | Focus ring | brand-primary | brand-primary-light |

### Button tokens

| Token | Purpose |
|---|---|
| `color.button.primary.bg` | Primary button background |
| `color.button.primary.text` | Primary button text |
| `color.button.primary.bg-hover` | Primary button hover state |
| `color.button.secondary.bg` | Secondary button background |
| `color.button.secondary.text` | Secondary button text |
| `color.button.destructive.bg` | Destructive button background |
| `color.button.destructive.text` | Destructive button text |

### Status / feedback tokens

| Token | Purpose |
|---|---|
| `color.feedback.success.bg` | Success banner background |
| `color.feedback.success.text` | Success text |
| `color.feedback.success.border` | Success border |
| (same for `warning`, `error`, `info`) | |

---

## 4. Spacing Scale Standards

### 4px grid (recommended default)

| Token | Value (rem) | Value (px) | Use |
|---|---|---|---|
| `space-0` | 0 | 0 | (no space) |
| `space-1` | 0.25rem | 4px | Micro adjustments |
| `space-2` | 0.5rem | 8px | Tight inner spacing |
| `space-3` | 0.75rem | 12px | Small gaps |
| `space-4` | 1rem | 16px | Default body spacing |
| `space-5` | 1.25rem | 20px | (rare) |
| `space-6` | 1.5rem | 24px | Section spacing |
| `space-8` | 2rem | 32px | Group separation |
| `space-10` | 2.5rem | 40px | Larger groups |
| `space-12` | 3rem | 48px | Section break |
| `space-16` | 4rem | 64px | Page-level spacing |
| `space-20` | 5rem | 80px | Page-level spacing |
| `space-24` | 6rem | 96px | Hero sections |

Skip 5, 7, 9, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23 — these introduce arbitrary numbers that don't snap to the 4px grid.

### 8px grid (alternative)

Same scale, but values are 0/8/16/24/32/40/48/64/80/96/128. Better for marketing-heavy sites that don't need fine adjustment. Worse for product UIs that need 4px precision.

---

## 5. Type Scale Standards

### 8-step modular scale

| Token | rem | px (16 base) | Use |
|---|---|---|---|
| `text-xs` | 0.75rem | 12px | Captions, footnotes |
| `text-sm` | 0.875rem | 14px | Secondary body, labels |
| `text-base` | 1rem | 16px | Body text |
| `text-lg` | 1.125rem | 18px | Lead body, large body |
| `text-xl` | 1.25rem | 20px | Subheadings |
| `text-2xl` | 1.5rem | 24px | h3 |
| `text-3xl` | 1.875rem | 30px | h2 |
| `text-4xl` | 2.25rem | 36px | h1 (default) |
| `text-5xl` | 3rem | 48px | Display |
| `text-6xl` | 3.75rem | 60px | Hero display |

### Fluid typography (recommended for marketing)

```css
@theme {
  --text-base: clamp(1rem, 0.9rem + 0.4vw, 1.125rem);
  --text-2xl: clamp(1.5rem, 1.2rem + 1.5vw, 2rem);
  --text-4xl: clamp(2.25rem, 1.5rem + 3vw, 3.5rem);
}
```

Document the min and max viewport widths the clamp is calibrated for (typically 320px–1440px).

---

## 6. Format Comparison

| Format | Best for | Drawbacks |
|---|---|---|
| **W3C JSON** | Source of truth; tool interop | Verbose; not directly consumable by code |
| **CSS variables** | Direct browser consumption | Hand-maintained CSS is brittle; no type safety |
| **Tailwind v4 `@theme`** | Tailwind users | Tailwind-specific |
| **Style Dictionary source** | Multi-platform builds (web + iOS + Android) | Older format (`value` vs `$value`) |
| **Figma Variables** | Designer tooling | Limited interop with code |
| **JS/TS object** | TypeScript autocomplete in code | Not interoperable with design tools |

**Recommended pattern:** W3C JSON as source of truth → script transforms it into CSS variables (for direct web use) AND Tailwind config (for Tailwind users) AND Figma Variables import (for designers).

---

## 7. The `token-converter.py` Script

The bundled script reads tokens in any of the four formats and outputs them in any other format.

### Usage

```bash
# Convert W3C JSON → Tailwind v4 CSS
python token-converter.py --in tokens.json --out app.css --format tailwind

# Convert W3C JSON → CSS variables
python token-converter.py --in tokens.json --out tokens.css --format css

# Convert Style Dictionary → W3C JSON
python token-converter.py --in style-dict.json --out tokens.json --format w3c
```

### Supported conversions

| From | To |
|---|---|
| W3C JSON | CSS, Tailwind v4, Style Dictionary |
| Style Dictionary | W3C JSON, CSS, Tailwind v4 |
| CSS variables | (parse-only — can read into W3C JSON) |
| Tailwind v4 | (parse-only — can read into W3C JSON) |

The script intentionally does *not* support v3 Tailwind config conversion. v3 is being deprecated; the migration path is to convert to v4.

---

## 8. Validation Checklist

Before declaring the token system complete:

- [ ] Both raw and semantic layers exist
- [ ] No semantic token has a hardcoded value (all use `{}` references)
- [ ] No raw token has a category-prefixed name (raw tokens describe what, not where)
- [ ] Spacing scale is 4px-multiple, no arbitrary numbers
- [ ] Dark mode semantic mapping exists (if dark mode is in scope)
- [ ] All four export formats generated (W3C JSON, CSS, Tailwind v4, Style Dictionary)
- [ ] `token-converter.py` round-trip succeeds (JSON → CSS → JSON should produce equivalent tokens)
- [ ] Decision log explains category and naming choices
