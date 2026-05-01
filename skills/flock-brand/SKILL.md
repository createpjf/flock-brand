---
name: flock-brand
version: 1.1.0
description: "Applies FLock.io's official brand identity — colors, typography, logo, layout — to any artifact: presentations (PPTX/Slidev/Reveal), documents (DOCX/PDF), web pages (HTML/React/Tailwind), infographics, and social media visuals. Supports both DARK MODE (primary) and LIGHT MODE. Trigger when the user mentions FLock branding, FLock styling, FLock dark/light mode, FLock品牌, FLock亮色, FLock暗色, federated learning visual identity, Real AI Real Impact, Sovereign AI / Operations / Gateway product styling, or asks to style any deliverable for FLock.io. Brand essence: trust, technological sophistication, decentralized collaboration. Tagline: Real AI. Real Impact. Brand pillars: Sovereign · Compliant · Integrated · Research-backed."
---

# FLock.io Brand Styling

This skill applies FLock.io's official brand identity to any deliverable. FLock.io is a decentralized AI platform focused on federated learning, model tokenization, and AI infrastructure. Brand identity conveys **trust · technological sophistication · decentralized collaboration**.

**Tagline**: Real AI. Real Impact.

**Brand Essence**: Sovereign · Compliant · Integrated · Research-backed

---

## Entry — context check & dialogue flow

Before producing anything, gauge whether the user has supplied enough context. **If not, run the 4-question dialogue.** If yes, skip straight to Outline Preview.

### Step 1 · Context self-check

Inspect the current conversation for these signals:

| Signal | Maps to |
|---|---|
| Mentioned scenario (pitch / whitepaper / onepager / social / infographic / DOCX...) | Q1 |
| Has draft, outline, URL, or substantive content brief | Q2 |
| Mentioned light/dark explicitly | Q3 |
| Mentioned visual style (data-heavy / minimal / dense / product) | Q4 |

| Signals present | What to do |
|---|---|
| All 4 | Skip dialogue → jump to Step 3 (Outline Preview) |
| Q1 + Q2 (+ implied Q3) | Ask only the missing of Q3 / Q4 |
| Q1 only | Ask Q2 + Q3 + Q4 |
| Q2 only | Ask Q1 + Q3 + Q4 |
| None / unclear | Run full 4-question flow |

Bias toward asking when in doubt: a 30-second clarifier beats regenerating a 12-slide deck.

### Step 2 · The 4 questions (ask in English, one per turn)

Show the recommended default pre-selected. Wait for the user's pick before advancing.

#### Q1. What are you making?

```
What are you creating today?

  ◯  Investor pitch deck
  ◯  Product launch / announcement
  ◯  Whitepaper / technical deep-dive
  ◯  One-pager / company intro
  ◯  Social post (X, LinkedIn)
  ◯  Infographic
  ◯  Internal doc / training
  ◯  Something else: ___________
```

#### Q2. What's it about?

```
What's the core message?

  ◯  Let me sketch a few bullets:    [open text]
  ◯  I have a draft / source:        [paste URL or content]
  ◯  Propose an outline for me       [enters proposal mode]
```

If "Propose for me" → use Q1 + brand pillars to draft an outline; show it; let user edit before continuing.

#### Q3. Light or Dark?

```
Light or Dark mode?

  ◯  Dark   — recommended for pitch decks, launches, social, product UI
  ◯  Light  — recommended for whitepapers, one-pagers, internal docs, long reads
```

Pre-select per Q1: pitch / launch / social / product → **Dark**; whitepaper / onepager / internal / DOCX → **Light**. User must still confirm or override — this is the user-held switch.

#### Q4. Visual style?

```
Which visual direction fits best?

  ◯  Data-driven    — charts, numbers, evidence-heavy
  ◯  Story-minimal  — bold statements, max whitespace, one idea per page
  ◯  Dense          — consulting-style grid, multi-module, comprehensive
  ◯  Product-led    — screenshots, UI showcases, feature highlights
```

Maps to the four layout groups in `references/deck-layouts.md`.

### Step 3 · Outline Preview (always show before generating)

Once Q1–Q4 are settled (whether asked or inferred), present the plan **before** generating any file:

```
Plan
────
Format:    [PPTX 12 slides / PDF whitepaper / HTML onepager / SVG infographic ...]
Mode:      [Dark / Light]
Style:     [Data-driven / Story-minimal / Dense / Product-led]
Language:  [English / Chinese / 中英双语]

Outline
1.  Cover               → hero-statement
2.  ...                 → ...

  [ Looks good — generate ]   [ Edit outline ]   [ Start over ]
```

User confirms → proceed to generation using the Routing table below. User edits → revise outline, re-show. User restarts → return to Q1.

### What this skill never asks (smart defaults)

| Decision | Source |
|---|---|
| Format (PPTX / PDF / HTML / SVG / DOCX) | Inferred from Q1; user can override at Outline Preview |
| Length (slide count, word count) | Inferred from Q1 + Q4 |
| Language | Detected from Q2 input; CJK input auto-loads PuHuiTi |
| Brand pillar emphasis (Sovereign / Compliant / Integrated) | Inferred from Q2 keywords |
| Logo variant, primary color, tracking, tokens | Iron Rules — never asked |

---

## Iron Rules (apply every time, no exceptions)

1. **Brand Blue is `#3773FF`** — the dominant brand color. No other blue is acceptable.
2. **Off White is `#F2F2F2`** (NOT `#F2F2F0`, NOT `#F8F8F8`, NOT pure white). Replaces white for soft surfaces.
3. **Black is `#000000`** for both backgrounds and text on light surfaces. Not `#282828`, not dark gray.
4. **Tight tracking is a defining brand characteristic** — never use default letter-spacing. -4% for H1/H2, -3% for H3/body.
5. **Dark mode is the primary brand mode**; Light mode is the secondary adaptation. Both are valid; pick by deliverable type (see routing below).
6. **TWK Everett is the primary typeface**; Inter is the canonical fallback. Never substitute a different sans-serif unless none of the chain is available.
7. **Secondary colors (Orange / Turquoise / Purple) are accents only** — never as primary backgrounds, never to replace Brand Blue.
8. **Logo color follows background**: White on dark/blue, Black or Brand Blue on Off White. Never recolor outside this rule. **Always use the official SVGs at `assets/logos/`** — never hand-draw or approximate. Source: <https://logo.flock.io>.

---

## Routing — read on demand, do not preload

This SKILL.md is the router. Load detail files only when the task requires them.

| Need | File | When to load |
|---|---|---|
| Exact color values, light/dark mode tokens, secondary palette, pillar colors, tints | `references/colors.md` | Any time you set a color |
| Type scale, font stack, **CJK / 中文** rules, tracking, weight rules | `references/typography.md` | Any time you set type — **always for Chinese content** |
| Logo variations, clearspace, sizing, background combinations | `references/logo.md` | When placing the logo |
| Slide master code, PptxGenJS recipes, **known PptxGenJS bugs**, OOXML editing | `references/pptx.md` | Generating or editing `.pptx` |
| Slidev theme, layout components, MDC examples for Reveal.js | `references/slidev.md` | Generating HTML/Slidev/Reveal slides |
| CSS variables, Tailwind preset, React component examples, page background rules | `references/web.md` | Web/HTML/React work |
| DOCX/PDF heading hierarchy, tables, callouts | `references/docs.md` | Document deliverables |
| Platform sizes (Twitter/LinkedIn/IG/OG), safe zones, carousel & avatar conventions | `references/social.md` | Social media posts, banners, OG images, avatars |
| Iconography (1.2pt stroke), chart color sequence, patterns, halftone imagery, diagrams | `references/infographics.md` | Charts, icons, diagrams, infographic visuals, data viz |
| 18 named deck layout patterns (10 consultant + 8 pitch deck), each mapped to FLock grid/type/color tokens with PPTX master + Slidev layout pointers, plus pattern-selection decision tree | `references/deck-layouts.md` | Planning or producing a multi-slide deck — picking which layout pattern fits the content |

Drop-in resources (no markdown, just import these directly):

| File | What it is |
|---|---|
| `assets/tokens.css` | Single CSS file with all `--flock-*` variables, light + dark, ready to `@import` |
| `assets/tokens.json` | Same tokens in JSON, style-dictionary compatible |
| `assets/tailwind.preset.js` | Tailwind preset to add via `presets: [require('./flock-brand/assets/tailwind.preset.js')]` |
| `assets/logos/*.svg` | **9 official logo SVGs** from logo.flock.io — mark / lockup / vertical × black / white / blue. Always reference these, never approximate. See `references/logo.md` for which file to use when. |
| `assets/fonts/AlibabaPuHuiTi-3-*.woff2` | **4 self-hosted CJK font weights** (55 Regular / 65 Medium / 75 SemiBold / 85 Bold). Auto-loaded by `tokens.css` via `@font-face` with CJK-only `unicode-range`. License: Alibaba free commercial use. |

---

## Mode selection — when to use Light vs Dark

Default to **Dark Mode** unless the deliverable is one of these:

| Deliverable | Default mode | Why |
|---|---|---|
| Pitch deck / hero marketing | **Dark** | Brand-defining tech-premium look |
| Product UI screenshots / app | **Dark** | Matches product itself |
| Investor / partner deck | **Dark** | Brand voice |
| Whitepaper / research PDF | **Light** | Print legibility |
| DOCX / Word document | **Light** | Print + collaborative editing |
| One-pager / handout | **Light** | Print + handoff |
| Internal training material | **Light** | Long-form readability |
| Educational slides / course | Either | Ask user — Dark for live talks, Light for handouts |

**Always ask the user once** if uncertain. Don't switch modes within the same deliverable.

---

## Application Quick-Reference

### Dark Mode (Primary)
- Background: `#000000`
- Text: `#FFFFFF`
- Headings: White or `#3773FF` accent
- Hero/CTA blocks: `#3773FF` background, white text
- Cards: subtle dark surface or `#3773FF` highlights

### Light Mode (Secondary)
- Page: `#F2F2F2` (or `#FFFFFF` for cards)
- Text body: `#000000`
- H1/H2: `#3773FF` (Brand Blue) — this is the brand signature on light
- H3 / body: `#000000`
- Cards: White `#FFFFFF` with subtle border, 10–12px radius

For full color matrix, tints, pillar encoding, and gradient spectrum → `references/colors.md`.

---

## Pre-flight checklist (run before declaring done)

Auto-grep these against your output:

- [ ] No hex `#282828` (use `#000000`)
- [ ] No hex `#F2F2F0` (use `#F2F2F2`)
- [ ] No hex `#00A8C0`, `#6030D0` (use `#03BFD4`, `#9C59F3`)
- [ ] No `letter-spacing: normal` or default tracking on headings
- [ ] No font fallback that drops Inter before SF Pro Display
- [ ] All logo placements use a file from `assets/logos/` — no inline-drawn approximations
- [ ] Logo color variant matches its background (white on dark/blue; black or blue on Off White)
- [ ] If Chinese content: Alibaba PuHuiTi 3.0 as primary CJK font (loaded via @font-face), with PingFang SC / Noto Sans SC as system fallback
- [ ] If PPTX: hex values do NOT have leading `#` in PptxGenJS calls (it corrupts the file)
- [ ] If PPTX: no Unicode `•` bullets — use `bullet: true`
- [ ] Secondary colors used as accents only, not as primary backgrounds

For the full PPTX-specific gotcha list → `references/pptx.md` § Known Bugs.
