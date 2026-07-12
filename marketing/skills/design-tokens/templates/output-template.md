# Design Tokens — {{Brand Name}}

**Date:** {{DD/MM/YYYY}}
**Source palette:** {{e.g. "color-palette skill output, 11/04/2026"}}
**Platforms:** {{web | web + iOS | web + iOS + Android}}
**Modes:** {{light only | light + dark}}
**Tailwind version:** {{v4 | v3}}

---

## 1. Token System Overview

| Category | Token count (raw) | Token count (semantic) | In scope? |
|---|---|---|---|
| Colour | {{n}} | {{n}} | ✓ |
| Typography | {{n}} | {{n}} | ✓ |
| Spacing | {{n}} | — | ✓ |
| Radius | {{n}} | {{n}} | ✓ |
| Shadow | {{n}} | {{n}} | {{✓ / —}} |
| Motion | {{n}} | {{n}} | {{✓ / —}} |
| Z-index | {{n}} | — | {{✓ / —}} |

**Total tokens:** {{n raw + n semantic}}

---

## 2. Naming Convention

- **Format:** {{kebab-case | dot.notation}}
- **Raw token pattern:** `category.subcategory.variant` (e.g. `color.brand.primary`, `space.4`)
- **Semantic token pattern:** `category.role.variant` (e.g. `color.bg.page`, `color.text.primary`)
- **Spacing scale base:** {{4px | 8px}}
- **Type scale steps:** {{8 | 10}}

---

## 3. Token Set (W3C JSON)

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": { "$value": "{{#hex}}" },
      "secondary": { "$value": "{{#hex}}" }
    },
    "neutral": {
      "50":  { "$value": "{{#hex}}" },
      "100": { "$value": "{{#hex}}" },
      "200": { "$value": "{{#hex}}" },
      "300": { "$value": "{{#hex}}" },
      "400": { "$value": "{{#hex}}" },
      "500": { "$value": "{{#hex}}" },
      "600": { "$value": "{{#hex}}" },
      "700": { "$value": "{{#hex}}" },
      "800": { "$value": "{{#hex}}" },
      "900": { "$value": "{{#hex}}" },
      "950": { "$value": "{{#hex}}" }
    },
    "semantic": {
      "success": { "$value": "{{#hex}}" },
      "warning": { "$value": "{{#hex}}" },
      "error":   { "$value": "{{#hex}}" },
      "info":    { "$value": "{{#hex}}" }
    },
    "bg": {
      "page": { "$value": "{color.neutral.50}" },
      "card": { "$value": "#FFFFFF" }
    },
    "text": {
      "primary":   { "$value": "{color.neutral.900}" },
      "secondary": { "$value": "{color.neutral.600}" }
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
    "24": { "$value": "96px" }
  },
  "font": {
    "family": {
      "$type": "fontFamily",
      "sans": { "$value": "{{font stack}}" },
      "mono": { "$value": "{{font stack}}" }
    },
    "size": {
      "$type": "dimension",
      "xs":   { "$value": "12px" },
      "sm":   { "$value": "14px" },
      "base": { "$value": "16px" },
      "lg":   { "$value": "18px" },
      "xl":   { "$value": "20px" },
      "2xl":  { "$value": "24px" },
      "3xl":  { "$value": "30px" },
      "4xl":  { "$value": "36px" },
      "5xl":  { "$value": "48px" }
    },
    "weight": {
      "$type": "fontWeight",
      "regular":  { "$value": 400 },
      "medium":   { "$value": 500 },
      "semibold": { "$value": 600 },
      "bold":     { "$value": 700 }
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
  }
}
```

---

## 4. CSS Variables Export

```css
:root {
  /* Raw — colour */
  --color-brand-primary: {{#hex}};
  --color-brand-secondary: {{#hex}};
  --color-neutral-50: {{#hex}};
  --color-neutral-100: {{#hex}};
  /* ... */
  --color-neutral-950: {{#hex}};
  --color-success: {{#hex}};
  --color-warning: {{#hex}};
  --color-error: {{#hex}};
  --color-info: {{#hex}};

  /* Semantic — colour */
  --color-bg-page: var(--color-neutral-50);
  --color-bg-card: #FFFFFF;
  --color-text-primary: var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-600);
  --color-border-default: var(--color-neutral-200);

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;

  /* Typography */
  --font-sans: {{font stack}};
  --font-mono: {{font stack}};
  --text-xs: 0.75rem;
  --text-base: 1rem;
  --text-4xl: 2.25rem;

  /* Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
}

.dark {
  --color-bg-page: var(--color-neutral-950);
  --color-bg-card: var(--color-neutral-900);
  --color-text-primary: var(--color-neutral-100);
  --color-text-secondary: var(--color-neutral-400);
  --color-border-default: var(--color-neutral-800);
}
```

---

## 5. Tailwind v4 Export

```css
@import "tailwindcss";

@theme {
  /* Colour — brand */
  --color-brand-primary: {{#hex}};
  --color-brand-secondary: {{#hex}};

  /* Colour — neutral */
  --color-neutral-50: {{#hex}};
  --color-neutral-100: {{#hex}};
  --color-neutral-200: {{#hex}};
  --color-neutral-300: {{#hex}};
  --color-neutral-400: {{#hex}};
  --color-neutral-500: {{#hex}};
  --color-neutral-600: {{#hex}};
  --color-neutral-700: {{#hex}};
  --color-neutral-800: {{#hex}};
  --color-neutral-900: {{#hex}};
  --color-neutral-950: {{#hex}};

  /* Colour — semantic */
  --color-success: {{#hex}};
  --color-warning: {{#hex}};
  --color-error: {{#hex}};
  --color-info: {{#hex}};

  /* Typography */
  --font-sans: {{font stack}};
  --font-mono: {{font stack}};
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;

  /* Spacing — extends Tailwind defaults */
  --spacing-section: 4rem;
  --spacing-gutter: 1.5rem;

  /* Radius */
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
}
```

---

## 6. Style Dictionary Export

```json
{
  "color": {
    "brand": {
      "primary": { "value": "{{#hex}}" }
    },
    "neutral": {
      "50":  { "value": "{{#hex}}" },
      "900": { "value": "{{#hex}}" }
    }
  },
  "space": {
    "4": { "value": "1rem" }
  }
}
```

(Run `style-dictionary build` against this source to generate iOS, Android, and web exports.)

---

## 7. Usage Guide

### In React / Tailwind v4

```tsx
// Use semantic Tailwind utilities — they map to brand tokens
<div className="bg-bg-page text-text-primary">
  <button className="bg-brand-primary text-white px-4 py-2 rounded-md">
    Sign in
  </button>
</div>
```

### In raw CSS

```css
.button {
  background: var(--color-button-primary-bg);
  color: var(--color-button-primary-text);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
}
```

### Theme switching

```html
<html class="dark">
  <!-- Inherits .dark { ... } token overrides -->
</html>
```

---

## 8. Decision Log

| Decision | Options considered | Chosen | Rationale |
|---|---|---|---|
| Tailwind version | v3 (config.js) / v4 (@theme) | v4 | Current standard; CSS-first approach is simpler |
| Spacing grid | 4px / 8px | {{...}} | {{...}} |
| Semantic token coverage | minimal / standard / extensive | {{...}} | {{...}} |
| Dark mode | included / not included | {{...}} | {{...}} |
| Font scale | 8-step / fluid clamp | {{...}} | {{...}} |
