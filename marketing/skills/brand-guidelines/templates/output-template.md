# {{Brand Name}} Brand Guidelines

**Version:** {{1.0}}
**Date:** {{DD/MM/YYYY}}
**Brand owner:** {{name + email}}
**Audience:** {{in-house team | agency | freelancer pool | all}}

---

## Table of Contents

1. About These Guidelines
2. Brand Story
3. Logo
4. Colour
5. Typography
6. Imagery and Iconography
7. Voice and Messaging
8. Application Examples
9. Asset Library
10. Contact and Governance

---

## 1. About These Guidelines

### Purpose
{{Why this document exists, who it's for, and what it covers.}}

### How to use this document
{{Where to look for what — a quick orientation.}}

### Update cadence
Reviewed quarterly. Last reviewed: {{DD/MM/YYYY}}.

### Exception requests
{{How to request an exception to a rule and who approves it.}}

---

## 2. Brand Story

### Mission
> {{Mission statement from brand-identity.}}

### Vision
> {{Vision statement.}}

### Core Values
- **{{Value 1}}** — {{definition}}
- **{{Value 2}}** — {{definition}}
- **{{Value 3}}** — {{definition}}

### Brand Archetype
**Primary:** The {{Archetype}}
**What this means in practice:** {{2 sentences.}}

### Who we serve
{{ICP and key personas — link to target-audience output.}}

### Who we are NOT for
- {{Anti-segment 1}}
- {{Anti-segment 2}}
- {{Anti-segment 3}}

---

## 3. Logo

### 3.1 Variants

| Variant | When to use |
|---|---|
| Primary horizontal lockup | Default for headers, marketing surfaces |
| Stacked vertical lockup | Square or vertical contexts |
| Mark only | Favicon, app icon, very small contexts |
| Wordmark only | Text-heavy contexts where the mark is redundant |
| Single-colour (black on white) | Print, single-ink reproduction |
| Reverse (white on dark) | Dark backgrounds, dark mode |
| App icon | iOS, Android, Mac/Windows app icon |

### 3.2 Clear Space

Maintain clear space equal to **{{1× cap height of the wordmark}}** on all sides. No element may enter this zone.

### 3.3 Minimum Size

| Context | Minimum |
|---|---|
| Web (mark only) | 16×16px |
| Web (full lockup) | 120px width |
| Print (full lockup) | 25mm width |
| Print (mark only) | 8mm |

### 3.4 Approved Backgrounds

| Background | Logo variant |
|---|---|
| White / `neutral-50` | Primary (full colour) |
| `neutral-100` to `neutral-200` | Primary (full colour) |
| `neutral-900` / `neutral-950` | Reverse (white) |
| Brand primary | White or reverse |

### 3.5 Misuse — Do Not

1. **Don't stretch or distort.** The logo's proportions are fixed.
2. **Don't change the colour** outside the approved palette.
3. **Don't add effects** — no drop shadows, glows, gradients, bevels, or 3D treatment.
4. **Don't rotate** the logo unless explicitly approved.
5. **Don't outline** the logo.
6. **Don't recreate the logo** from memory or hand-draw it.
7. **Don't place on busy backgrounds** without sufficient contrast.
8. **Don't combine with other logos** in lockups without brand owner approval.
9. **Don't change the typeface** or letter spacing of the wordmark.
10. **Don't crop** the logo or use it as a partial element.

---

## 4. Colour

### 4.1 Palette

(See `color-palette` skill output for full palette specification.)

| Role | Name | HEX | OKLCH |
|---|---|---|---|
| Primary | {{name}} | `{{#hex}}` | `{{...}}` |
| Secondary | {{name}} | `{{#hex}}` | `{{...}}` |
| Success | {{name}} | `{{#hex}}` | `{{...}}` |
| Warning | {{name}} | `{{#hex}}` | `{{...}}` |
| Error | {{name}} | `{{#hex}}` | `{{...}}` |
| Info | {{name}} | `{{#hex}}` | `{{...}}` |

Plus an 11-step neutral ramp from `neutral-50` to `neutral-950`.

### 4.2 Usage Hierarchy

| Surface | Primary background | Primary text | Buttons | Accents |
|---|---|---|---|---|
| Marketing | white / `neutral-50` | `neutral-900` | Brand primary | Secondary |
| Product UI (light) | white | `neutral-900` | Brand primary | Semantic |
| Product UI (dark) | `neutral-950` | `neutral-100` | Brand primary | Semantic |

### 4.3 Approved Combinations

| Foreground | Background | Contrast | Use |
|---|---|---|---|
| `neutral-900` | white | {{ratio}}:1 | Body text |
| Brand primary | white | {{ratio}}:1 | Primary CTA |
| white | brand primary | {{ratio}}:1 | Reverse CTA |

### 4.4 Forbidden Combinations

- Brand primary on accent (contrast fails)
- Warning amber as text on white (contrast fails — use as background fill only)
- Any pair below WCAG AA (4.5:1 for body text)

### 4.5 Accessibility Commitment

All body text in product UI passes **WCAG 2.2 AA**. Body text in dark mode passes **AAA**. Validated via `color-palette/scripts/contrast-checker.py`.

---

## 5. Typography

### 5.1 Type Families

| Role | Family | Fallback | License |
|---|---|---|---|
| Display / Heading | {{Typeface}} | {{fallback}} | {{license}} |
| Body | {{Typeface}} | system-ui, sans-serif | {{license}} |
| Monospace | {{Typeface}} | ui-monospace, monospace | {{license}} |

### 5.2 Type Scale

(See `design-tokens` output for the full scale.)

| Token | Size | Use |
|---|---|---|
| `text-xs` | 12px | Captions, footnotes |
| `text-sm` | 14px | Secondary body, labels |
| `text-base` | 16px | Body text |
| `text-lg` | 18px | Lead body |
| `text-xl` | 20px | Subheadings |
| `text-2xl` | 24px | h3 |
| `text-3xl` | 30px | h2 |
| `text-4xl` | 36px | h1 |
| `text-5xl` | 48px | Display |

### 5.3 Hierarchy Rules

- **Display:** Hero pages only. One per page max.
- **h1:** Page title. Use `font-display` family.
- **h2, h3:** Section headings. Use `font-display` for h2, `font-sans` for h3.
- **Body:** Always `font-sans`. Always `text-base` minimum on web.

### 5.4 Legibility Minimums

- Minimum body text (web): **16px**
- Minimum body text (print): **9pt**
- Maximum line length: **75 characters**
- Body line height: **1.5**

### 5.5 Forbidden Type Usage

- Don't set body text in the display family.
- Don't track headings below the spec (typically 0% to -2%).
- Don't use Comic Sans, Papyrus, or system Times unless ironically and approved.
- Don't use the system font as a substitute outside the approved fallback chain.
- Don't justify body text on the web.

---

## 6. Imagery and Iconography

### 6.1 Photography Style

**Direction:** {{e.g. "Natural light, candid moments, real customers, documentary not commercial."}}

**Subject matter:**
- {{Allowed: ...}}
- {{Allowed: ...}}
- {{Forbidden: stock photography, posed business shots, Instagram filters}}

**Treatment:**
- {{e.g. "No filters. Slight desaturation OK. No oversaturated colour grading."}}

### 6.2 Illustration Style

**Direction:** {{e.g. "Single-line, geometric, two-colour."}}

**When to use:** {{Where illustration is preferred over photography.}}

### 6.3 Iconography

**Set:** {{Lucide / Heroicons / Phosphor / Custom}}
**Stroke:** {{1.5px}}
**Style:** {{outlined / filled / mixed}}
**Usage rules:** {{Always pair with label / Icon-only when ... / Consistency rules}}

**Forbidden:**
- Clip art icons
- Gradient or 3D icons
- Mixing stroke styles
- Icons that don't appear in the official set

### 6.4 Data Visualisation

- **Default chart colours:** Brand primary → secondary → semantic info → semantic success
- **Forbidden:** Pie charts > 5 slices; 3D charts; rainbow palette
- **Type in charts:** {{font-sans}}; minimum 12px

---

## 7. Voice and Messaging

### 7.1 Voice Attributes

#### {{Attribute 1}} — this, not {{opposite}}
- **DO:** "{{example}}"
- **DON'T:** "{{example}}"

#### {{Attribute 2}} — this, not {{opposite}}
- **DO:** "{{example}}"
- **DON'T:** "{{example}}"

(Add 3–5 attributes total — consolidated from `brand-identity` output.)

### 7.2 Tone Sliders

| Dimension | Default | Flex when |
|---|---|---|
| Formality | {{position}} | {{condition}} |
| Energy | {{position}} | {{condition}} |
| Humour | {{position}} | {{condition}} |
| Warmth | {{position}} | {{condition}} |

### 7.3 Vocabulary

**Approved phrases:** {{e.g. "the work that matters", "your daily focus", "ship something today"}}
**Brand-specific terms:** {{e.g. product feature names that should be capitalised consistently}}

### 7.4 Banned Words

We do not use:
- {{innovative}}
- {{world-class}}
- {{robust}}
- {{leverage}}
- {{synergy}}
- {{best-in-class}}
- {{seamless}}
- {{game-changer}}
- {{revolutionary}}
- {{... add brand-specific bans}}

### 7.5 Capitalisation and Punctuation

- **Brand name:** {{e.g. "all lowercase 'verdant'" or "Title Case 'Verdant'"}}
- **Product names:** {{e.g. "Title Case"}}
- **Headings:** {{Sentence case / Title Case}}
- **Oxford comma:** {{Yes / No}}
- **Em dash:** {{with spaces / without spaces}}
- **Numbers:** {{Spell out 0–9 or "use figures throughout"}}

### 7.6 Tagline and Key Messages

**Primary tagline:** "{{tagline}}"

**Elevator pitch (one sentence):** {{...}}

**Elevator pitch (30 seconds):** {{...}}

**Key product benefits:**
1. {{Benefit 1}}
2. {{Benefit 2}}
3. {{Benefit 3}}

### 7.7 Voice in Context

#### Product UI microcopy
> "{{example}}"

#### Marketing landing page (hero)
> # {{Headline}}
> {{Subhead.}}

#### Customer support email
> Subject: {{...}}
>
> Hi {{name}},
>
> {{Body in voice.}}
>
> {{Sign-off}}

#### Social post (X / LinkedIn)
> {{Post body in voice.}}

---

## 8. Application Examples

### 8.1 Landing page hero
{{Right way / wrong way example.}}

### 8.2 Social media post
{{Right way / wrong way example.}}

### 8.3 Email signature
{{Right way / wrong way example.}}

### 8.4 Ad creative
{{Right way / wrong way example.}}

### 8.5 Product UI screen
{{Right way / wrong way example.}}

---

## 9. Asset Library

| Asset | Location | Notes |
|---|---|---|
| Logo files (SVG, PNG) | {{path or URL}} | All variants |
| Icon set | {{path or URL}} | {{Lucide v0.300+}} |
| Photography library | {{path or URL}} | Approved real-customer photos |
| Email templates | {{path or URL}} | |
| Slide deck template | {{path or URL}} | |
| Design tokens | {{path or URL}} | See `design-tokens` output |
| Fonts | {{path or URL}} | License info included |

---

## 10. Contact and Governance

**Brand owner:** {{Name + email}}
**Approval process:** {{Who approves new use cases}}
**Exception requests:** {{How to ask}}
**Update cadence:** Quarterly review
**Last reviewed:** {{DD/MM/YYYY}}

### Change log

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | {{DD/MM/YYYY}} | {{name}} | Initial brand book |
