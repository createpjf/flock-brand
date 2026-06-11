---
name: flock-brand v2.0
description: "Applies FLock.io's official brand identity to any deliverable — HTML deck, PPTX, Slidev, web (HTML/React/Tailwind), DOCX/PDF, infographics, social media. Supports deck narrative planning, brand-compliance audit, cross-session series consistency, image generation (Codex), and Claude/Codex dual-runtime. Trigger when: FLock branding, FLock styling, FLock品牌, Real AI Real Impact, Sovereign AI/Operations/Gateway styling, making a deck/pitch/presentation for FLock.io, auditing a deck for brand compliance, 做PPT, 做演示文稿, 生成配图, 审计/检查品牌合规, 修复/优化现有 deck（布局优化/修排版/fix layout/brand-normalize/把现有 PPT 套 FLock 品牌）."
---

# FLock.io Brand Skill 2.0

FLock.io is a decentralized AI platform focused on federated learning, model tokenization, and AI infrastructure. Brand identity: **trust · technological sophistication · decentralized collaboration**.

**Tagline**: Real AI. Real Impact.  
**Brand Pillars**: Sovereign · Compliant · Integrated · Research-backed

---

## Iron Rules (apply every time, no exceptions)

1. **Brand Blue is `#3773FF`** — the dominant brand color. No other blue is acceptable.
2. **Off White is `#F2F2F2`** — NOT `#F2F2F0`, NOT `#F8F8F8`, NOT pure white. Replaces white for soft surfaces.
3. **Black is `#000000`** — for both backgrounds and text on light surfaces. Not `#282828`, not dark gray.
4. **Tight tracking is identity** — never default letter-spacing. `-0.04em` for H1/H2, `-0.03em` for H3/body.
5. **Dark mode is primary** — Light mode is the secondary adaptation. See Mode Selection below.
6. **TWK Everett is the primary typeface** — Inter is the canonical fallback. Never substitute a different sans-serif unless the full chain fails.
7. **Secondary colors (Orange / Turquoise / Purple) are accents only** — never as primary backgrounds, never to replace Brand Blue.
8. **Logo color follows background** — White on dark/blue, Black or Brand Blue on Off White. Always use official SVGs at `assets/logos/`. Source: <https://logo.flock.io>.

---

## Verbs

This skill has one default behavior and one explicit verb.

| Invocation | What it does |
|---|---|
| *(default)* | Build a new FLock-branded deliverable. Follow the Deck Workflow below. |
| `flock audit <target>` | Score an existing deliverable against FLock brand rules. Output a graded punch list. **Does not edit files.** Load `references/audit.md`. Triggers: `flock audit`, 「检查品牌合规」, 「这份 deck 哪里不对」, 「audit 一下」. |
| `flock fix <target>` | **Repair an existing deliverable** — layout problems (overlap / overflow / alignment) and brand-color normalization. Content text stays 1:1 untouched. Load `references/fix.md`. Run `scripts/pptx_lint.py` first. Triggers: 「布局优化」「修排版」「fix this deck」「brand-normalize」「把这份套成 FLock 品牌」. |

Routing: existing file + "is this on-brand?" → `audit`. Existing file + "修一下 / 优化布局 / 套品牌" → `fix`. Make something new → default. When in doubt between audit and fix, ask one question: 只要诊断报告,还是直接修?

---

## Routing — load on demand, never preload

### Core brand references

| Need | File | When to load |
|---|---|---|
| Exact color values, dark/light tokens, secondary palette, pillar colors, tints | `references/colors.md` | Any time you set a color |
| Type scale, font stack, **CJK / 中文** rules, tracking, weight rules | `references/typography.md` | Any time you set type — **always for Chinese content** |
| Logo variations, clearspace, sizing, background combinations | `references/logo.md` | When placing the logo |
| Iconography (1.2pt stroke), chart color sequence, halftone, diagrams | `references/infographics.md` | Charts, icons, diagrams, data viz |

### Deliverable-specific references

| Need | File | When to load |
|---|---|---|
| Deck layout **router** — grid specs, 主轴, 不对称技法, decision tree (no layout bodies) | `references/deck-layouts.md` | Planning any multi-slide deck — read first, then load only the Part below you need |
| Consulting layouts #1–#10 (full ASCII structures + token mapping) | `references/deck-layouts-consulting.md` | Narrative arc A (consulting) decks, after picking layout numbers |
| Pitch layouts #11–#18 (full ASCII structures + token mapping) | `references/deck-layouts-pitch.md` | Narrative arc B/C (pitch / launch) decks, after picking layout numbers |
| Slide master code, PptxGenJS recipes, **known PptxGenJS bugs** | `references/pptx.md` | Generating or editing `.pptx` |
| Slidev theme, layout components, MDC examples | `references/slidev.md` | Generating Slidev / Reveal.js slides |
| **Runnable single-file HTML deck template** (WebGL + Motion One + FLock tokens) | `assets/template.html` | Generating HTML format deck |
| CSS variables, Tailwind preset, React component examples | `references/web.md` | Web / HTML / React work |
| DOCX/PDF heading hierarchy, tables, callouts | `references/docs.md` | Document deliverables |
| Platform sizes, safe zones, carousel & avatar conventions | `references/social.md` | Social media posts, banners, OG images |

### Workflow references (new)

| Need | File | When to load |
|---|---|---|
| **Deck content planning** — 7-question intake, narrative arc, rhythm table, banned-phrase library | `references/narrative.md` | **First step before any deck task** |
| **Quality assurance** — pre-emit 6-axis critique + P0/P1/P2/P3 graded checklist | `references/checklist.md` | Before declaring any deliverable done |
| **Series consistency** — `.flock/log.json` memory, cross-deliverable visual continuity | `references/project-memory.md` | At task start — check if part of an existing series |
| **Brand audit** — score an existing deliverable against brand rules, output punch list | `references/audit.md` | When user invokes `flock audit` / asks to check brand compliance |
| **Fix existing deliverable** — repair workflow, EMU geometry recipes, sed safety rules | `references/fix.md` | When user invokes `flock fix` / asks to repair layout or normalize colors |
| **Runtime detection** — Claude vs Claude Code vs Codex behavior | `references/runtime.md` | At task start, identify environment |
| **Image generation** — Codex: direct generate; Claude: output prompts | `references/image-gen.md` | After HTML deck draft, if images needed |

### Drop-in assets (import directly, no markdown)

| File | What it is |
|---|---|
| `assets/tokens.css` | All `--flock-*` CSS variables, light + dark, ready to `@import` |
| `assets/tokens.json` | Same tokens in JSON, style-dictionary compatible |
| `assets/tailwind.preset.js` | Tailwind preset — `presets: [require('./flock-brand/assets/tailwind.preset.js')]` |
| `assets/logos/*.svg` | 9 official SVGs — mark / lockup / vertical × black / white / blue |
| `assets/fonts/AlibabaPuHuiTi-3-*.woff2` | 4 CJK font weights (Regular / Medium / SemiBold / Bold) |
| `assets/template.html` | Runnable FLock HTML deck — CSS vars, WebGL shaders, Motion One, 5 example slides |
| `scripts/pptx_lint.py` | Automated PPTX checker — off-brand colors (with remap suggestions), overflow, bbox overlap, footer/page-number collision. `python scripts/pptx_lint.py deck.pptx`. Exit 1 on P0. |

---

## Mode selection — Dark vs Light

Default to **Dark Mode** unless the deliverable type below calls for Light:

| Deliverable | Default mode |
|---|---|
| Pitch deck / hero marketing | **Dark** |
| Product UI screenshots / app | **Dark** |
| Investor / partner deck | **Dark** |
| HTML deck (presentation) | **Dark** (cover + CTA), Light allowed for content slides |
| Whitepaper / research PDF | **Light** |
| DOCX / Word document | **Light** |
| One-pager / handout | **Light** |
| Internal training material | **Light** |
| Educational slides | Ask user — Dark for live, Light for handout |

Ask once if uncertain. Never switch modes within the same deliverable.

---

## Quick-Reference Values

### Dark Mode
```
bg: #000000   text: #FFFFFF
heading: #FFFFFF or #3773FF
hero/CTA bg: #3773FF  text: #FFFFFF
card surface: #0A0A0A
```

### Light Mode
```
bg: #F2F2F2   text: #000000
H1/H2: #3773FF  H3/body: #000000
card bg: #FFFFFF, border: #E0E4F0, radius: 10–12px
```

For full matrix, tints, pillar encoding → `references/colors.md`.

---

## Deck Workflow (when task = deck / PPT / presentation)

```
Step 0    Read references/runtime.md → identify ENV (claude / claude-code / codex)

Step 0.5  Read references/project-memory.md → check .flock/log.json
          If part of an existing series → enter consistency mode
          (reuse prior mode / arc / layouts / accent)

Step 1    Read references/narrative.md
          → Run 7-question intake
          → Choose narrative arc (consulting SCR or pitch)
          → Draft rhythm table (page × mode × layout)
          → Apply banned-phrase library when writing copy

Step 2    Read references/deck-layouts.md (router) → pick layout numbers via decision tree
          → then read ONLY the matching Part file:
            consulting (#1–10) → deck-layouts-consulting.md
            pitch (#11–18)     → deck-layouts-pitch.md
          If HTML output → cp assets/template.html to project/index.html

Step 3    Fill slides
          Read references/typography.md for any CJK content
          Read references/colors.md for pillar color encoding

Step 4    Before declaring done → read references/checklist.md
          → §0 Pre-emit 6-axis critique (any axis <3 → revise)
          → §shared P0 + §flock P0 — all must pass
          → Stamp critique scores into the artifact

Step 5    [Optional images]
          Read references/image-gen.md
          Codex: generate directly. Claude: output prompts for user.

Step 6    Append a new entry to .flock/log.json
          (per references/project-memory.md)
```

---

## Iron Rules Pre-flight (fast grep — run before declaring done)

```bash
grep -n "#282828"                    # → use #000000
grep -n "#F2F2F0\|#F8F8F8"          # → use #F2F2F2
grep -n "#00A8C0\|#6030D0"          # → use #03BFD4 / #9C59F3
grep -n "letter-spacing:\s*normal"  # → must have -0.04em or -0.03em on headings
grep -rn "assets/logos" --include="*.html" --include="*.jsx"  # → confirm no hand-drawn logos
```

For PPTX the grep above is replaced by one command: `python scripts/pptx_lint.py output.pptx` (colors + geometry in one pass).

Full graded quality checklist (P0 / P1 / P2 / P3) → `references/checklist.md`  
PPTX-specific gotchas → `references/pptx.md` § Known Bugs
