# Design Tokens — Cadence

**Date:** 11/04/2026
**Source palette:** Cadence brand palette (Inkwell + Coral + warm neutrals)
**Platforms:** Web (React + Tailwind v4), iOS (via Style Dictionary)
**Modes:** Light + dark
**Tailwind version:** v4

---

## 1. Token System Overview

Cadence is a task management app for teams of 2–10 people. The token system covers all colour, type, space, and radius needs for the marketing site (Next.js) and the product UI (React Native + React Native Web). Shadow and motion are in scope because the product has heavy use of layered surfaces and micro-interactions.

| Category | Token count (raw) | Token count (semantic) | In scope? |
|---|---|---|---|
| Colour | 18 | 22 | ✓ |
| Typography | 18 | 9 | ✓ |
| Spacing | 11 | — | ✓ |
| Radius | 6 | 4 | ✓ |
| Shadow | 4 | 3 | ✓ |
| Motion | 7 | 4 | ✓ |
| Z-index | 6 | — | ✓ |

**Total tokens:** 121 (62 raw + 42 semantic + 11 spacing + 6 z-index)

---

## 2. Naming Convention

- **Format:** dot-notation in W3C JSON, kebab-case in CSS variables
- **Raw token pattern:** `category.subcategory.variant` (e.g. `color.brand.inkwell`, `space.4`)
- **Semantic token pattern:** `category.role.variant` (e.g. `color.bg.page`, `color.text.primary`)
- **Spacing scale base:** 4px
- **Type scale steps:** 9 (xs through 5xl, plus a fluid `display` for hero)

---

## 3. Token Set (W3C JSON)

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "inkwell":   { "$value": "#1A1B2E" },
      "coral":     { "$value": "#FF6B6B" },
      "parchment": { "$value": "#FFF8F0" }
    },
    "neutral": {
      "50":  { "$value": "#FBFAF7" },
      "100": { "$value": "#F4F2EC" },
      "200": { "$value": "#E5E2D8" },
      "300": { "$value": "#CFCABC" },
      "400": { "$value": "#A3A091" },
      "500": { "$value": "#76746A" },
      "600": { "$value": "#52514A" },
      "700": { "$value": "#3A3933" },
      "800": { "$value": "#26261F" },
      "900": { "$value": "#161611" },
      "950": { "$value": "#0A0A07" }
    },
    "semantic": {
      "success": { "$value": "#34A77E" },
      "warning": { "$value": "#E8A93C" },
      "error":   { "$value": "#D8504F" },
      "info":    { "$value": "#4A6FA5" }
    },
    "bg": {
      "page":    { "$value": "{color.neutral.50}" },
      "card":    { "$value": "#FFFFFF" },
      "subtle":  { "$value": "{color.neutral.100}" },
      "muted":   { "$value": "{color.neutral.200}" },
      "inverse": { "$value": "{color.neutral.900}" }
    },
    "text": {
      "primary":   { "$value": "{color.neutral.900}" },
      "secondary": { "$value": "{color.neutral.600}" },
      "disabled":  { "$value": "{color.neutral.400}" },
      "inverse":   { "$value": "{color.neutral.50}" },
      "link":      { "$value": "{color.brand.coral}" }
    },
    "border": {
      "subtle":  { "$value": "{color.neutral.200}" },
      "default": { "$value": "{color.neutral.300}" },
      "strong":  { "$value": "{color.neutral.400}" },
      "focus":   { "$value": "{color.brand.coral}" }
    },
    "button": {
      "primary": {
        "bg":       { "$value": "{color.brand.inkwell}" },
        "text":     { "$value": "{color.neutral.50}" },
        "bgHover":  { "$value": "{color.neutral.800}" }
      },
      "secondary": {
        "bg":   { "$value": "{color.neutral.100}" },
        "text": { "$value": "{color.neutral.900}" }
      }
    }
  },
  "space": {
    "$type": "dimension",
    "0":  { "$value": "0px" },
    "1":  { "$value": "4px" },
    "2":  { "$value": "8px" },
    "3":  { "$value": "12px" },
    "4":  { "$value": "16px" },
    "6":  { "$value": "24px" },
    "8":  { "$value": "32px" },
    "12": { "$value": "48px" },
    "16": { "$value": "64px" },
    "20": { "$value": "80px" },
    "24": { "$value": "96px" }
  },
  "font": {
    "family": {
      "$type": "fontFamily",
      "sans":    { "$value": "Inter, system-ui, -apple-system, sans-serif" },
      "display": { "$value": "Tiempos Headline, Georgia, serif" },
      "mono":    { "$value": "JetBrains Mono, ui-monospace, monospace" }
    },
    "size": {
      "$type": "dimension",
      "xs":      { "$value": "12px" },
      "sm":      { "$value": "14px" },
      "base":    { "$value": "16px" },
      "lg":      { "$value": "18px" },
      "xl":      { "$value": "20px" },
      "2xl":     { "$value": "24px" },
      "3xl":     { "$value": "30px" },
      "4xl":     { "$value": "36px" },
      "5xl":     { "$value": "48px" },
      "display": { "$value": "clamp(2.5rem, 1.8rem + 3.5vw, 4.5rem)" }
    },
    "weight": {
      "$type": "fontWeight",
      "regular":  { "$value": 400 },
      "medium":   { "$value": 500 },
      "semibold": { "$value": 600 },
      "bold":     { "$value": 700 }
    },
    "lineHeight": {
      "tight":   { "$value": "1.1" },
      "normal":  { "$value": "1.5" },
      "relaxed": { "$value": "1.75" }
    }
  },
  "radius": {
    "$type": "dimension",
    "none": { "$value": "0px" },
    "sm":   { "$value": "4px" },
    "md":   { "$value": "8px" },
    "lg":   { "$value": "12px" },
    "xl":   { "$value": "16px" },
    "full": { "$value": "9999px" }
  },
  "shadow": {
    "sm": {
      "$type": "shadow",
      "$value": { "color": "#1A1B2E0d", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px" }
    },
    "md": {
      "$type": "shadow",
      "$value": { "color": "#1A1B2E1a", "offsetX": "0px", "offsetY": "4px", "blur": "8px", "spread": "-2px" }
    },
    "lg": {
      "$type": "shadow",
      "$value": { "color": "#1A1B2E26", "offsetX": "0px", "offsetY": "12px", "blur": "24px", "spread": "-6px" }
    },
    "xl": {
      "$type": "shadow",
      "$value": { "color": "#1A1B2E33", "offsetX": "0px", "offsetY": "24px", "blur": "48px", "spread": "-12px" }
    }
  },
  "duration": {
    "$type": "duration",
    "instant": { "$value": "100ms" },
    "fast":    { "$value": "150ms" },
    "normal":  { "$value": "250ms" },
    "slow":    { "$value": "400ms" }
  }
}
```

---

## 4. CSS Variables Export

```css
:root {
  /* Brand */
  --color-brand-inkwell: #1A1B2E;
  --color-brand-coral: #FF6B6B;
  --color-brand-parchment: #FFF8F0;

  /* Neutral */
  --color-neutral-50:  #FBFAF7;
  --color-neutral-100: #F4F2EC;
  --color-neutral-200: #E5E2D8;
  --color-neutral-300: #CFCABC;
  --color-neutral-400: #A3A091;
  --color-neutral-500: #76746A;
  --color-neutral-600: #52514A;
  --color-neutral-700: #3A3933;
  --color-neutral-800: #26261F;
  --color-neutral-900: #161611;
  --color-neutral-950: #0A0A07;

  /* Semantic */
  --color-success: #34A77E;
  --color-warning: #E8A93C;
  --color-error:   #D8504F;
  --color-info:    #4A6FA5;

  /* Semantic — bg */
  --color-bg-page:    var(--color-neutral-50);
  --color-bg-card:    #FFFFFF;
  --color-bg-subtle:  var(--color-neutral-100);
  --color-bg-muted:   var(--color-neutral-200);
  --color-bg-inverse: var(--color-neutral-900);

  /* Semantic — text */
  --color-text-primary:   var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-600);
  --color-text-disabled:  var(--color-neutral-400);
  --color-text-inverse:   var(--color-neutral-50);
  --color-text-link:      var(--color-brand-coral);

  /* Semantic — border */
  --color-border-subtle:  var(--color-neutral-200);
  --color-border-default: var(--color-neutral-300);
  --color-border-strong:  var(--color-neutral-400);
  --color-border-focus:   var(--color-brand-coral);

  /* Spacing */
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;

  /* Typography */
  --font-sans:    "Inter", system-ui, -apple-system, sans-serif;
  --font-display: "Tiempos Headline", Georgia, serif;
  --font-mono:    "JetBrains Mono", ui-monospace, monospace;

  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.125rem;
  --text-xl:   1.25rem;
  --text-2xl:  1.5rem;
  --text-3xl:  1.875rem;
  --text-4xl:  2.25rem;
  --text-5xl:  3rem;
  --text-display: clamp(2.5rem, 1.8rem + 3.5vw, 4.5rem);

  --leading-tight:   1.1;
  --leading-normal:  1.5;
  --leading-relaxed: 1.75;

  /* Radius */
  --radius-sm:   0.25rem;
  --radius-md:   0.5rem;
  --radius-lg:   0.75rem;
  --radius-xl:   1rem;
  --radius-full: 9999px;

  /* Shadow */
  --shadow-sm: 0 1px 2px 0 rgba(26, 27, 46, 0.05);
  --shadow-md: 0 4px 8px -2px rgba(26, 27, 46, 0.10);
  --shadow-lg: 0 12px 24px -6px rgba(26, 27, 46, 0.15);
  --shadow-xl: 0 24px 48px -12px rgba(26, 27, 46, 0.20);

  /* Motion */
  --duration-instant: 100ms;
  --duration-fast:    150ms;
  --duration-normal:  250ms;
  --duration-slow:    400ms;
  --easing-standard:  cubic-bezier(0.2, 0, 0, 1);
  --easing-out:       cubic-bezier(0, 0, 0, 1);
  --easing-in:        cubic-bezier(0.4, 0, 1, 1);
}

.dark {
  --color-bg-page:    var(--color-neutral-950);
  --color-bg-card:    var(--color-neutral-900);
  --color-bg-subtle:  var(--color-neutral-800);
  --color-bg-muted:   var(--color-neutral-700);
  --color-bg-inverse: var(--color-neutral-100);

  --color-text-primary:   var(--color-neutral-100);
  --color-text-secondary: var(--color-neutral-400);
  --color-text-disabled:  var(--color-neutral-600);
  --color-text-inverse:   var(--color-neutral-900);

  --color-border-subtle:  var(--color-neutral-800);
  --color-border-default: var(--color-neutral-700);
  --color-border-strong:  var(--color-neutral-600);
}
```

---

## 5. Tailwind v4 Export

```css
@import "tailwindcss";

@theme {
  /* Brand */
  --color-brand-inkwell: #1A1B2E;
  --color-brand-coral: #FF6B6B;
  --color-brand-parchment: #FFF8F0;

  /* Neutral */
  --color-neutral-50:  #FBFAF7;
  --color-neutral-100: #F4F2EC;
  --color-neutral-200: #E5E2D8;
  --color-neutral-300: #CFCABC;
  --color-neutral-400: #A3A091;
  --color-neutral-500: #76746A;
  --color-neutral-600: #52514A;
  --color-neutral-700: #3A3933;
  --color-neutral-800: #26261F;
  --color-neutral-900: #161611;
  --color-neutral-950: #0A0A07;

  /* Semantic */
  --color-success: #34A77E;
  --color-warning: #E8A93C;
  --color-error:   #D8504F;
  --color-info:    #4A6FA5;

  /* Typography */
  --font-sans:    "Inter", system-ui, -apple-system, sans-serif;
  --font-display: "Tiempos Headline", Georgia, serif;
  --font-mono:    "JetBrains Mono", ui-monospace, monospace;

  --text-xs:      0.75rem;
  --text-sm:      0.875rem;
  --text-base:    1rem;
  --text-lg:      1.125rem;
  --text-xl:      1.25rem;
  --text-2xl:     1.5rem;
  --text-3xl:     1.875rem;
  --text-4xl:     2.25rem;
  --text-5xl:     3rem;
  --text-display: clamp(2.5rem, 1.8rem + 3.5vw, 4.5rem);

  /* Radius */
  --radius-sm:   0.25rem;
  --radius-md:   0.5rem;
  --radius-lg:   0.75rem;
  --radius-xl:   1rem;

  /* Shadow */
  --shadow-card:    0 1px 2px 0 rgba(26, 27, 46, 0.05);
  --shadow-popover: 0 12px 24px -6px rgba(26, 27, 46, 0.15);
  --shadow-modal:   0 24px 48px -12px rgba(26, 27, 46, 0.20);
}
```

---

## 6. Style Dictionary Export

```json
{
  "color": {
    "brand": {
      "inkwell": { "value": "#1A1B2E" },
      "coral":   { "value": "#FF6B6B" }
    },
    "neutral": {
      "50":  { "value": "#FBFAF7" },
      "900": { "value": "#161611" }
    }
  },
  "size": {
    "space": {
      "4": { "value": "16px" }
    },
    "radius": {
      "md": { "value": "8px" }
    }
  }
}
```

Run via: `style-dictionary build --config sd-config.json`

---

## 7. Usage Guide

### React + Tailwind v4

```tsx
// Card with primary button
<div className="bg-bg-card rounded-lg shadow-card p-6">
  <h3 className="font-display text-2xl text-text-primary">Welcome back</h3>
  <p className="text-text-secondary mt-2">Pick up where you left off.</p>
  <button className="bg-brand-inkwell text-neutral-50 px-4 py-2 rounded-md mt-4 transition-colors duration-fast">
    Continue
  </button>
</div>
```

### Raw CSS (no Tailwind)

```css
.card {
  background: var(--color-bg-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--space-6);
}
```

### Theme switching (dark mode)

```html
<html data-theme="dark">
```

```css
[data-theme="dark"] {
  /* same overrides as .dark in section 4 */
}
```

---

## 8. Decision Log

| Decision | Options considered | Chosen | Rationale |
|---|---|---|---|
| Tailwind version | v3 / v4 | **v4** | Cadence is greenfield; no migration cost; v4 is current standard |
| Spacing grid | 4px / 8px | **4px** | Product UI needs precision in card layouts and form spacing |
| Display font | Tiempos Headline / Söhne / Inter (no display) | **Tiempos Headline (Georgia fallback)** | The brand identity called for "literary, considered" — a serif display fits |
| Radius scale | 5-step / 6-step | **6-step (none + 5)** | Need both `none` (sharp corners on data tables) and `xl` (hero panels) |
| Shadow | Excluded / 4-step / 6-step | **4-step** | Product UI uses card / popover / modal elevations only |
| Dark mode | Light only / Light + dark | **Light + dark** | Product UI is used heavily during late-night work sessions; dark mode requested by users |
| Semantic token coverage | Minimal / Standard / Extensive | **Standard** | Cover bg, text, border, button — skip exotic categories until needed |
