# flock-brand

> Apply [FLock.io](https://flock.io)'s official brand identity to any artifact — slides, docs, web pages, infographics, social. A Claude Code / Cursor / Codex skill.

Supports both **Dark Mode** (primary) and **Light Mode**. Includes the official logo set, Alibaba PuHuiTi 3.0 CJK fonts, design tokens (CSS / JSON / Tailwind preset), and 18 named deck layout patterns. Ships a 4-question conversational intake when context is sparse, or skips it entirely when you've already supplied scenario / content / mode / style.

---

## Quick install — one paste per agent

Pick your agent. Paste the block into its chat. Done.

### Claude Code

> Install flock-brand: run `/plugin marketplace add createpjf/flock-brand` then `/plugin install flock-brand@createpjf`. Confirm both commands succeed and the skill appears in the available skills list.

### Cursor

> Install flock-brand for Cursor: run `git clone --depth 1 https://github.com/createpjf/flock-brand.git ~/.cursor/plugins/flock-brand` then reload Cursor. The plugin is auto-discovered via `.cursor-plugin/plugin.json`.

### Codex CLI

> Install flock-brand for Codex: run `git clone --depth 1 https://github.com/createpjf/flock-brand.git /tmp/_fb && mkdir -p ~/.codex/skills && mv /tmp/_fb/skills/flock-brand ~/.codex/skills/ && rm -rf /tmp/_fb`. Verify `~/.codex/skills/flock-brand/SKILL.md` exists.

### Any other agent (manual)

> Install flock-brand: clone the repo with `git clone --depth 1 https://github.com/createpjf/flock-brand.git`. The skill lives at `skills/flock-brand/SKILL.md` — point your agent at that file, or copy the directory to wherever your agent reads skills from.

### No agent — direct asset use (designers, devs)

```bash
git clone --depth 1 https://github.com/createpjf/flock-brand.git
```

| File | Use directly |
|---|---|
| `skills/flock-brand/assets/tokens.css` | `@import` for `--flock-*` CSS variables (light + dark) |
| `skills/flock-brand/assets/tailwind.preset.js` | Add to your Tailwind `presets: []` |
| `skills/flock-brand/assets/logos/*.svg` | 9 official logo variants — never approximate |
| `skills/flock-brand/assets/fonts/` | Alibaba PuHuiTi 3.0 CJK (4 weights, free commercial) |
| `skills/flock-brand/references/*.md` | Human-readable brand rules — colors, type, layouts, PPTX gotchas |

---

## See it work

```
You:    /flock-brand
Claude: What are you creating today?
        ◯ Investor pitch deck    ◯ Product launch
        ◯ Whitepaper             ◯ One-pager
        ◯ Social post            ◯ Infographic
        ◯ Internal doc           ◯ Something else
You:    Investor pitch deck.

Claude: What's it about?
        ◯ Let me sketch a few bullets
        ◯ I have a draft / source
        ◯ Propose an outline for me
You:    Q2 results — $4.2M ARR, 320% YoY, 3 enterprise design partners signed.

Claude: Light or Dark mode?
        ◯ Dark   ← recommended for pitch decks (pre-selected)
        ◯ Light
You:    Dark.

Claude: Which visual direction fits best?
        ◯ Data-driven    ◯ Story-minimal    ◯ Dense    ◯ Product-led
You:    Story-minimal + data on the numbers slide.

Claude: Plan
        ────
        Format:    PPTX (12 slides)
        Mode:      Dark
        Style:     Story-minimal + data-driven
        Language:  English

        Outline
        1.  Cover               → hero-statement
        2.  Q2 in one number    → full-bleed-quote
        3.  $4.2M ARR / 320% YoY → data-trio
        4.  3 design partners   → logo-grid
        5-7. Pillar deep-dives  → split-product
        ...

        [ Looks good — generate ]   [ Edit outline ]   [ Start over ]
You:    Generate.

Claude: [writes 12 slides as PPTX with Brand Blue #3773FF, tight tracking,
         official Logo SVG, and TWK Everett → Inter fallback chain]
        Done. ./flock-q2-results.pptx
```

When your prompt already names the scenario, content, mode, and style, the skill skips the 4 questions and goes straight to the Plan.

---

## The flow

flock-brand is a 5-stage pipeline. Each stage knows what came before it.

**Detect → Intake → Plan → Generate → Iterate**

| Stage | What happens | Loads | You see |
|---|---|---|---|
| **1. Detect** | Skill triggers on FLock keywords or explicit invocation. Iron Rules (colors, type, logo) become non-negotiable. | `SKILL.md` only | (silent — skill loads) |
| **2. Intake** | Up to 4 multiple-choice questions — scenario · content · light/dark · visual style. Smart defaults pre-selected. **Skipped if your prompt already supplied the info.** | nothing | up to 4 question prompts |
| **3. Plan** | Outline preview: format · mode · visual style · language · numbered sections, each mapped to a named layout. **Always shown before generation.** | `references/deck-layouts.md` for multi-page | the outline preview block |
| **4. Generate** | Produces the final artifact. Format-specific bug list and recipes loaded on demand. | per-format: `pptx.md`, `slidev.md`, `web.md`, `docs.md`, `social.md`, `infographics.md` | the PPTX / PDF / HTML / SVG |
| **5. Iterate** | "Edit slide 3 to use data-trio instead." Skill revises the outline + regenerates that section. | varies | revised artifact |

The intake makes this skill conversational, but it's adaptive — supply enough context up front and the dialogue dissolves.

---

## What you can ask for

| You ask for... | Default mode | Default style | Output | Layouts |
|---|---|---|---|---|
| Investor pitch deck | Dark | story-minimal + data | PPTX | hero-statement · data-trio · three-pillars · logo-grid · timeline · cta-closing |
| Product launch | Dark | product-led | PPTX / HTML | hero-statement · split-product · feature-grid |
| Whitepaper | **Light** | dense / consulting | PDF / DOCX | header-grid · callout-block · data-table |
| One-pager | Dark | story-minimal | HTML | hero-cta · three-pillars |
| Social post (X / LinkedIn) | Dark | data-driven | PNG / SVG | single-data-point |
| Infographic | varies | dense | SVG / PDF | data-grid |
| Internal doc / training | Light | dense | DOCX | header-grid |

Every default is overridable in the Plan stage.

---

## What's included

- **18 named deck layout patterns** (10 consultant + 8 pitch deck) with PPTX master + Slidev pointers
- **9 official logo SVGs** — mark / lockup / vertical × black / white / blue
- **4 Alibaba PuHuiTi 3.0 CJK font weights** (self-hosted, free commercial use)
- **Drop-in design tokens** — `tokens.css`, `tokens.json`, `tailwind.preset.js`
- **10 reference docs** — colors, typography, logo, PPTX (with known-bug list), Slidev, web, docs, social, infographics, deck-layouts

---

## Brand essentials

| | |
|---|---|
| Brand Blue | `#3773FF` |
| Off White | `#F2F2F2` |
| Black | `#000000` |
| Typography | TWK Everett → Inter (fallback) |
| Tracking | -4% on H1/H2, -3% on H3/body |
| Tagline | **Real AI. Real Impact.** |
| Pillars | Sovereign · Compliant · Integrated · Research-backed |

For the full color matrix, light/dark token tables, secondary palette, pillar encoding, and gradient spectrum, see [`skills/flock-brand/references/colors.md`](./skills/flock-brand/references/colors.md).

---

## Versioning & upgrade

- Versions follow [SemVer](https://semver.org/) (MAJOR.MINOR.PATCH).
- See [CHANGELOG.md](./CHANGELOG.md) for release history.
- **Claude Code**: `/plugin marketplace update flock-brand`
- **Cursor / Codex / direct clone**: `cd <install-path> && git pull`

---

## License

[MIT](./LICENSE) — the skill's structure, documentation, and tooling are MIT-licensed.

**FLock.io brand assets** (logo SVGs, color values, typography rules, brand voice) remain the intellectual property of FLock.io. Use of these brand assets should follow FLock.io brand guidelines and is intended for FLock.io-related work.

---

## Repository layout

```
.
├── .claude-plugin/plugin.json    # Claude Code plugin manifest
├── .cursor-plugin/plugin.json    # Cursor plugin manifest
├── skills/
│   └── flock-brand/
│       ├── SKILL.md              # Skill router (Iron Rules · dialogue flow · routing)
│       ├── assets/               # Logos · fonts · tokens · Tailwind preset
│       └── references/           # 10 detail docs loaded on demand
├── VERSION
├── CHANGELOG.md
├── LICENSE
└── README.md
```
