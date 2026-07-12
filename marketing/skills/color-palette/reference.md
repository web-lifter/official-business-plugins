# Colour Palette — Reference

Supplementary reference material for the `color-palette` skill. Covers WCAG 2.2 contrast formulas, OKLCH theory, colour psychology by industry, neutral ramp construction, and the colour-blindness check matrix.

---

## Table of Contents

- [1. WCAG 2.2 Contrast Requirements](#1-wcag-22-contrast-requirements)
- [2. OKLCH — Why and How](#2-oklch--why-and-how)
- [3. Colour Psychology by Industry](#3-colour-psychology-by-industry)
- [4. Neutral Ramp Construction](#4-neutral-ramp-construction)
- [5. Semantic Colour Conventions](#5-semantic-colour-conventions)
- [6. Common Contrast Ratios for Reference](#6-common-contrast-ratios-for-reference)
- [7. Validation Checklist](#7-validation-checklist)

---

## 1. WCAG 2.2 Contrast Requirements

Contrast ratio is computed from relative luminance. The formula:

```
ratio = (L1 + 0.05) / (L2 + 0.05)
```

Where L1 is the lighter colour's relative luminance and L2 is the darker colour's relative luminance.

Relative luminance per WCAG:
```
L = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

Where R, G, B are linearised sRGB values:
```
linearise(c) = c / 12.92                  if c ≤ 0.03928
             = ((c + 0.055) / 1.055)^2.4  otherwise
```

The bundled `contrast-checker.py` implements this formula directly.

### Required ratios (WCAG 2.2)

| Use case | AA | AAA |
|---|---|---|
| Normal text (< 18pt or < 14pt bold) | ≥ 4.5:1 | ≥ 7.0:1 |
| Large text (≥ 18pt or ≥ 14pt bold) | ≥ 3.0:1 | ≥ 4.5:1 |
| UI components and graphical objects | ≥ 3.0:1 | (no AAA) |
| Incidental / decorative | (no requirement) | (no requirement) |

### What "incidental" means

Decorative elements that convey no information (background ornaments, decorative borders, brand watermarks) have no contrast requirement. Logos and brand names are also exempt.

### When to target AAA

Default to AA. Target AAA when:
- The brand serves users with low vision (medical, government, accessibility-first)
- The brand serves an older audience (50+)
- The audience is global and includes regions with high prevalence of colour deficiency
- The product is information-dense (financial, scientific, dashboards)

---

## 2. OKLCH — Why and How

OKLCH is a perceptually-uniform colour space with three components:
- **L** (Lightness) — 0 to 1, where 0 is black and 1 is white
- **C** (Chroma) — 0 to ~0.4, where 0 is fully desaturated (grey)
- **H** (Hue) — 0 to 360 degrees on the colour wheel

### Why OKLCH beats HSL

HSL is mathematically convenient but perceptually broken:
- HSL "lightness 50%" of yellow is much brighter than HSL "lightness 50%" of blue
- Adjusting HSL lightness changes how saturated a colour *looks*
- Two HSL colours with the same lightness can have very different contrast against the same background

OKLCH is designed so that two colours with the same `L` value have the same perceived lightness regardless of hue. This means:
- A neutral ramp built on uniform OKLCH lightness steps will look uniform to the eye
- Adjusting a colour to be "darker" by lowering OKLCH lightness produces predictable contrast changes
- Two semantic colours (e.g. success-green and error-red) at the same OKLCH lightness will be distinguishable by users with red-green colour blindness

### Conversion

OKLCH → HEX is standardised in CSS Color Module 4. The bundled `contrast-checker.py` accepts HEX input; conversions are done in colour-aware tools (CSS, Figma, OKLCH.com).

### Practical OKLCH ranges

| Role | Typical L | Typical C |
|---|---|---|
| Pure white | 1.0 | 0 |
| Page background (light mode) | 0.97–0.99 | 0–0.01 |
| Brand primary | 0.5–0.7 (vibrant) or 0.3–0.5 (grounded) | 0.1–0.25 |
| Body text | 0.15–0.3 | 0–0.04 |
| Pure black | 0 | 0 |
| Disabled / muted text | 0.55–0.65 | 0–0.04 |

---

## 3. Colour Psychology by Industry

These associations are partly real and partly post-hoc rationalisation. Use as a starting point, not a rule.

### Fintech / Banking
- **Convention:** Blue (trust, stability), navy (authority), green (growth, money — Western markets)
- **Watch out:** Red has positive financial connotations in Chinese markets (luck, prosperity); avoid in non-Asian fintech
- **Differentiation play:** Earth tones, soft neutrals, warm greys (signals "modern alternative to legacy banks")

### Health / Wellness
- **Convention:** Soft greens, muted blues, off-white, sage
- **Watch out:** Bright reds and oranges feel medical/clinical, not wellness
- **Differentiation play:** Warm earth tones (signals natural / holistic)

### Tech / SaaS
- **Convention:** Blue, purple, teal — broad and overused
- **Watch out:** Most B2B SaaS uses blue. Picking blue makes you invisible.
- **Differentiation play:** Warm neutrals + one strong accent; black with restraint; muted earth tones

### Food / Beverage
- **Convention:** Warm reds, oranges, yellows (appetite stimulants); greens (fresh)
- **Watch out:** Blue is unappetising for food (research-backed)
- **Differentiation play:** Premium food often uses muted, earth-toned palettes (signals craft, restraint)

### Children / Toys
- **Convention:** Saturated primary brights
- **Watch out:** Pastels feel "infant," not "child"
- **Differentiation play:** Sophisticated toys for older children use deeper, more grown-up palettes

### Luxury / Premium
- **Convention:** Black, gold, deep neutrals, restrained palettes
- **Watch out:** "Gold" as a brand colour is cliché; restraint signals premium more than ornament
- **Differentiation play:** A single saturated colour against a wide neutral ramp; high contrast; lots of white space

### Government / Public Service
- **Convention:** Blue, sometimes red or green; conservative and restrained
- **Watch out:** Must pass AAA for accessibility; bright/saturated colours feel inappropriate
- **Differentiation play:** Within constraints, modern public-service brands use careful neutrals + one signature colour

### Australian context
- The Australian flag's red/white/blue is rarely used directly in commercial branding
- "Australian" colour shorthand is often warm earth tones (red dirt, eucalyptus green, ochre, sand)
- Avoid "boomerang and Aboriginal art" colour palettes unless the brand is genuinely Indigenous-owned

---

## 4. Neutral Ramp Construction

A neutral ramp is the most-used part of any palette. It needs to be wide and uniformly-stepped.

### Standard 11-step ramp

```
neutral-50    L≈0.98    Page background (light mode)
neutral-100   L≈0.95    Card background, hover states
neutral-200   L≈0.90    Subtle borders, dividers
neutral-300   L≈0.84    Stronger borders, disabled buttons
neutral-400   L≈0.72    Placeholder text, icons (decorative)
neutral-500   L≈0.60    Secondary text, captions
neutral-600   L≈0.48    Body text on light background (passes AA)
neutral-700   L≈0.36    Strong body text, headings
neutral-800   L≈0.24    Display headings, high-emphasis text
neutral-900   L≈0.15    Highest-emphasis text, button text on light
neutral-950   L≈0.08    Near-black backgrounds (dark mode page)
```

### Tinted vs pure neutrals

**Pure neutrals** (Chroma = 0): Pure greys. Maximum flexibility; never clash with any hue. Recommended default.

**Tinted neutrals** (Chroma = 0.005–0.02): Slightly tinted toward the brand primary. More cohesive feel; can look muddy if chroma is too high. Use for premium / craft brands.

**Warm vs cool tint:**
- Warm tint (toward orange/red) — feels human, friendly, approachable
- Cool tint (toward blue) — feels professional, technical, premium

### Why uniform OKLCH steps

If you build the ramp by stepping HSL lightness uniformly (e.g. `hsl(0, 0%, 95%)`, `hsl(0, 0%, 90%)`, ...), the ramp will not *look* uniform. The middle steps will look bunched together while the ends look spread apart. OKLCH solves this — uniform L steps produce visually uniform progression.

---

## 5. Semantic Colour Conventions

| Role | Colour family | OKLCH guidance | Common mistakes |
|---|---|---|---|
| Success | Green | L 0.55–0.7, C 0.15–0.2, H 140–160 | Too dark (looks like olive); too saturated (looks like 1995 web) |
| Warning | Amber/Orange | L 0.7–0.8, C 0.15–0.2, H 60–80 | Too red (confused with error); too pale (looks like beige) |
| Error | Red | L 0.55–0.65, C 0.18–0.25, H 20–30 | Too bright (alarming); too pink (not taken seriously) |
| Info | Blue / Neutral | L 0.55–0.65, C 0.12–0.18, H 240–260 | Indistinguishable from brand primary if primary is blue |

### Colour-blindness check matrix

Run this mental check on every semantic palette:

| Pair | Deutan (red-green) | Protan (red-green) | Tritan (blue-yellow) |
|---|---|---|---|
| Success vs Error | ⚠ Same hue family | ⚠ Same hue family | ✓ |
| Success vs Warning | ✓ | ✓ | ⚠ Yellow/green confusion |
| Warning vs Error | ✓ | ✓ | ✓ |
| Info vs Brand primary (if blue) | ✓ | ✓ | ⚠ |

For pairs marked ⚠: ensure the OKLCH lightness differs by ≥ 0.15 so the colours are still distinguishable by lightness alone.

Tools to verify: macOS Display Accommodations colour filters, Figma "Colour Vision Deficiency" plugin, Sim Daltonism (Mac).

---

## 6. Common Contrast Ratios for Reference

| Pair | Approx ratio | AA Body | AAA Body | AA Large |
|---|---|---|---|---|
| Pure black on white (#000 / #FFF) | 21:1 | ✓ | ✓ | ✓ |
| #1A1A1A on white | 18.5:1 | ✓ | ✓ | ✓ |
| #404040 on white | 10.4:1 | ✓ | ✓ | ✓ |
| #595959 on white | 7.0:1 | ✓ | ✓ (just) | ✓ |
| #767676 on white | 4.5:1 | ✓ (just) | ✗ | ✓ |
| #949494 on white | 3.0:1 | ✗ | ✗ | ✓ (just) |
| Pure white on #0066CC | 5.3:1 | ✓ | ✗ | ✓ |
| Pure white on #007BFF (Bootstrap blue) | 4.0:1 | ✗ | ✗ | ✓ |

**Key insight:** Many "brand blues" used by tech companies do not pass AA for white text. You almost always need to darken the brand blue (or use it only on dark backgrounds) for accessible button copy.

---

## 7. Validation Checklist

Before declaring a palette complete:

- [ ] Every colour has HEX, RGB, HSL, OKLCH values
- [ ] Primary colours have rationale and reference brands
- [ ] Neutral ramp has at least 11 steps with uniform OKLCH lightness spacing
- [ ] Body text on background passes WCAG AA (≥4.5:1) — validated via script
- [ ] All button-text-on-button pairs pass WCAG AA — validated via script
- [ ] Semantic colours pass WCAG AA on both light and dark backgrounds
- [ ] Colour-blindness check passed for success/error/warning trio
- [ ] Cultural connotations flagged for any colour with strong regional meaning
- [ ] Print/CMYK considerations noted if print is in scope
- [ ] JSON snippet generated for `design-tokens` skill ingestion
