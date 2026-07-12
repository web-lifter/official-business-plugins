# Logo Brief — Reference

Supplementary reference material for the `logo-brief` skill. Covers the seven mark types in detail, typography classifications for wordmarks, AI image-generation prompt patterns, and the favicon test.

---

## Table of Contents

- [1. The Seven Mark Types](#1-the-seven-mark-types)
- [2. Typography Classifications for Wordmarks](#2-typography-classifications-for-wordmarks)
- [3. AI Image Generation — Prompt Patterns](#3-ai-image-generation--prompt-patterns)
- [4. The Favicon Test](#4-the-favicon-test)
- [5. Clear Space and Minimum Sizes](#5-clear-space-and-minimum-sizes)
- [6. AI Generation vs Human Designer — Brief Differences](#6-ai-generation-vs-human-designer--brief-differences)
- [7. Validation Checklist](#7-validation-checklist)

---

## 1. The Seven Mark Types

### 1.1 Wordmark (Logotype)

The full brand name set in a custom or distinctive typeface. The name *is* the logo.

**Examples:** Google, Coca-Cola, FedEx, Visa, Mobil, eBay, Disney
**Best for:**
- Short, memorable, or already-recognised names
- Brands where the name is the primary brand asset
- Brands needing minimal complexity
**Worst for:**
- Long names (>12 characters becomes unwieldy)
- Names with awkward letter combinations
- Brands needing iconic compactness for app icons

**Design considerations:**
- Custom typography preferred (or significant modification of an existing typeface)
- Letter spacing is the second most important decision after typeface choice
- Test at 16px favicon size — many wordmarks fail here

### 1.2 Lettermark / Monogram

The brand initials only.

**Examples:** HBO, IBM, NASA, P&G, GE, NYT, BBC, GAP
**Best for:**
- Long names with strong abbreviations
- Established institutions
- B2B brands where the audience already knows the full name
**Worst for:**
- New brands with no name recognition
- Brands with awkward initials (II, WW, OO)
- Brands competing with bigger brands using similar initials

**Design considerations:**
- Each letter must work in isolation
- Spacing and weight matter more than in a wordmark
- Often combined with a containing shape (square, circle, custom)

### 1.3 Pictorial / Logomark

A literal image representing something concrete.

**Examples:** Apple, Twitter (bird), Target (bullseye), Shell, Mercedes (star), Playboy (bunny)
**Best for:**
- Brands with strong existing recognition
- Brands where the image telegraphs the offering
- Brands needing iconic, single-shape recognition
**Worst for:**
- New brands trying to establish what they do
- Categories where the literal image is overused (lightbulb, gear, house, leaf)

**Design considerations:**
- The shape must be silhouette-readable (a complex pictorial mark fails at small sizes)
- The image should be conceptually defensible (Apple's apple has a story; many pictorial marks don't)
- Cliché alert: avoid lightbulb (ideas), gear (tech), rocket (growth), leaf (eco), globe (global), handshake (partnership)

### 1.4 Abstract Mark

A geometric form not literally representing anything specific.

**Examples:** Nike swoosh, Pepsi globe, Adidas trefoil, Airbnb Bélo, Mitsubishi diamonds
**Best for:**
- Brands wanting to be category-agnostic
- Brands aiming for global recognition independent of language
- Brands willing to invest in long-term brand-building to give the abstract form meaning
**Worst for:**
- Brands needing immediate clarity about what they sell
- Small or new brands without a marketing budget to teach the meaning

**Design considerations:**
- Abstract marks require strong silhouette and memorable proportions
- They often take years to acquire meaning (Nike's swoosh meant nothing in 1971)
- Test the mark for accidental resemblance to other brands or symbols

### 1.5 Combination Mark

Wordmark + symbol working together.

**Examples:** Adidas (trefoil + name), Lacoste (crocodile + name), Burger King, Doritos, Slack
**Best for:**
- Most working brands
- Brands needing flexibility (the symbol can stand alone in compact contexts)
- Brands with both an established name and an iconic mark
**Worst for:**
- Brands needing maximum simplicity
- Brands without budget for both wordmark and symbol design

**Design considerations:**
- The wordmark and symbol must work both together and independently
- The lockup needs both horizontal and vertical (stacked) variants
- Spacing and alignment between wordmark and symbol is the most-violated brand standard

### 1.6 Emblem

Text contained inside a shape.

**Examples:** Starbucks, Harley-Davidson, BMW, NFL, NHL teams, Stella Artois
**Best for:**
- Heritage brands
- Sports teams and badges
- Traditional categories (beer, automotive, official institutions)
**Worst for:**
- Brands needing flexible application across surfaces
- Brands needing to work at small sizes (emblems are detail-heavy)

**Design considerations:**
- Emblems are the hardest mark type to scale down — they often need a "simplified emblem" for digital use
- The text and shape must read as one unit
- Modern emblems usually have a horizontal lockup variant for digital

### 1.7 Mascot

A character or illustrated figure representing the brand.

**Examples:** KFC's Colonel, Michelin Man, Mr. Peanut, Tony the Tiger, Ronald McDonald
**Best for:**
- Family / consumer brands
- Brands that benefit from anthropomorphic friendliness
- Brands that can sustain the mascot across animation and merch
**Worst for:**
- Premium / serious brands
- B2B brands
- Brands requiring minimalism

**Design considerations:**
- Mascots are expensive to produce and maintain
- Cultural sensitivity matters — many older mascots have aged badly
- Often combined with a wordmark in a lockup

---

## 2. Typography Classifications for Wordmarks

| Style | Examples | Brand Mood |
|---|---|---|
| **Geometric Sans** | Futura, Avenir, Gotham, Montserrat | Modern, technical, confident |
| **Humanist Sans** | Frutiger, Myriad, Open Sans, Source Sans | Friendly, approachable, accessible |
| **Grotesque Sans** | Helvetica, Inter, Akzidenz Grotesk | Neutral, professional, classic |
| **Industrial Sans** | DIN, Bebas Neue, Oswald | Strong, bold, urban |
| **Old Style Serif** | Garamond, Caslon, Sabon | Traditional, literary, refined |
| **Transitional Serif** | Times, Baskerville | Authoritative, established |
| **Modern Serif** | Bodoni, Didot | Luxury, fashion, editorial |
| **Slab Serif** | Rockwell, Roboto Slab, Tiempos Headline | Sturdy, friendly, contemporary |
| **Display** | Custom or expressive typefaces | Distinctive, often single-purpose |
| **Hand / Script** | Brush, calligraphic, signature | Personal, craft, artisanal |
| **Mono** | JetBrains Mono, IBM Plex Mono | Technical, code, dev tools |

### Choosing typography for a wordmark

1. The typeface should match the brand archetype (Sage = Old Style Serif or Humanist Sans; Outlaw = Industrial or Display; Innocent = Humanist Sans)
2. Custom modification is preferred over straight-out-of-the-box use of a Google Font
3. A wordmark using Inter or Roboto unmodified looks generic
4. Consider letter spacing as a separate decision — slightly tighter spacing reads as confident; expanded spacing reads as luxury

---

## 3. AI Image Generation — Prompt Patterns

When generating logo concepts via Midjourney, DALL-E, Imagen, or Stable Diffusion, the brief must include AI-friendly prompts.

### 3.1 Prompt structure

```
[mark type], [subject/form], [style modifiers], [colour], [background], [aspect ratio], [negative prompt]
```

### 3.2 Examples by mark type

**Wordmark:**
```
A wordmark logo for "Beacon", set in a custom geometric sans-serif inspired by Futura
and Gotham, with slightly tightened tracking, all caps, deep navy on white background,
vector art, centered, 1:1, --no gradients --no shadows --no 3d
```

**Pictorial mark:**
```
A minimalist single-line logo of a lighthouse beacon, geometric, two-colour (navy + mint),
flat vector art, centered on white background, app icon style, 1:1, --no text --no 3d
--no realistic details
```

**Abstract mark:**
```
An abstract geometric logo mark suggesting a north star, two intersecting lines,
asymmetric, deep navy on white, flat vector, no text, 1:1, --no gradients --no shadows
```

### 3.3 Negative prompts for logos

Always include these in the negative prompt:
- gradients
- drop shadows
- 3d
- bevel
- texture
- realistic
- watermark
- signature
- low resolution
- blurry

### 3.4 Aspect ratio

- `--ar 1:1` for app icons and most logo work
- `--ar 16:9` for horizontal lockup explorations
- `--ar 4:3` for emblem-style marks

### 3.5 Style modifiers

| Want | Add |
|---|---|
| Geometric, technical | "geometric, vector, flat" |
| Hand-drawn, organic | "hand-drawn, organic, brush, ink" |
| Premium, refined | "minimal, restrained, golden ratio" |
| Bold, industrial | "bold, heavy, industrial, stencil" |
| Friendly | "rounded, warm, playful" |

---

## 4. The Favicon Test

Every logo must pass the favicon test. Process:

1. Render the logo at 16×16 pixels
2. Squint at it from 2 meters away
3. Can you tell what brand it is?
4. Does it have a recognisable silhouette?

If the answer to either #3 or #4 is "no", the mark fails. Common failure modes:
- Pictorial marks with too much internal detail
- Wordmarks longer than 6–7 letters at favicon size
- Emblems with text inside — text becomes unreadable
- Two-colour marks where the colours blur together at 16px

**Standard solution:** Have a "favicon variant" of the logo that is a simplified or condensed version of the main mark. Apple's app icon is just the apple, not the full wordmark. Most working brands have at least two logo variants for this reason.

---

## 5. Clear Space and Minimum Sizes

### Clear space

The minimum padding around the logo, expressed as a multiple of a logo element. Common conventions:

- **Wordmarks:** 1× cap height of the wordmark
- **Lettermarks:** 1× the height of the letterform
- **Pictorial / abstract:** 0.5× the height of the mark
- **Emblems:** 0.25× the diameter of the emblem

Document this in the brief as: "Maintain clear space equal to {{X}} on all sides — no other element may enter this zone."

### Minimum sizes

Per use case:

| Use case | Minimum size |
|---|---|
| Favicon | 16×16 (often a simplified variant) |
| App icon | 24×24 (iOS minimum); the full app icon is 180×180 |
| Web header | 32×32 height for the mark; 24×24 for compact headers |
| Business card | 8mm height for primary mark |
| Packaging | 12mm height (depends on package size) |
| Vehicle / signage | 100mm minimum (typically much larger) |

If the logo cannot scale to a required minimum size, the brief must include a "small-size variant" specification.

---

## 6. AI Generation vs Human Designer — Brief Differences

### When using AI image generators

- Lean toward wordmark, lettermark, or simple abstract marks (AI is weakest at original pictorial concepts)
- Provide the prompt verbatim — don't just describe what you want
- Expect to generate 30–50 candidates and curate
- Plan to vectorise the best AI output by hand (or via Vectorizer.AI / Adobe Illustrator's vectorize tool)
- Budget time for refinement — AI logos rarely ship as-is

### When using a human designer

- Provide the brief and let them propose mark types
- Ask for 3 concepts in round 1, refine to 1 in round 2, finalise in round 3
- Provide feedback against the brief — "this concept doesn't address the favicon constraint" rather than "I don't like it"
- Pay for source files (vector AI, Figma, Sketch) — without source files, the brand can't iterate

---

## 7. Validation Checklist

Before sending the brief to a designer or generator:

- [ ] Mark type chosen and justified
- [ ] 3–5 concept directions generated, each distinct
- [ ] Each concept has a name, description, references, and risks
- [ ] Style direction defined (typography, form, colour)
- [ ] Smallest reproduction size specified
- [ ] Single-colour reproduction requirement noted
- [ ] Reverse/dark mode requirement noted
- [ ] Clear space rule included
- [ ] Deliverables checklist complete
- [ ] Positive references (3–5) with specific reasons
- [ ] Negative references (3–5) with specific reasons
- [ ] Avoid list (≥5 items) included
- [ ] AI prompts included if AI generation in scope
- [ ] Budget and timeline specified
