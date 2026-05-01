# flock-brand

> Apply [FLock.io](https://flock.io)'s official brand identity to any artifact — slides, docs, web pages, infographics, social. A Claude Code skill.

Supports both **Dark Mode** (primary) and **Light Mode**. Includes the official logo set, Alibaba PuHuiTi 3.0 CJK fonts, design tokens (CSS / JSON / Tailwind preset), and 18 named deck layout patterns.

---

## Install

```
/plugin marketplace add createpjf/flock-brand
/plugin install flock-brand@createpjf
```

After install, mention FLock styling in any prompt and Claude routes the request through the skill.

## Usage

```
Make me a FLock-style investor pitch deck about our Q2 results.
```

Claude will:

1. Detect FLock branding intent and load the skill
2. Run a 4-question intake when context is sparse — what you're making, content, light/dark, visual style — or skip it when you've already supplied everything
3. Show an outline preview before generating
4. Produce the PPTX / PDF / HTML / SVG with brand-correct colors, typography, logo, layout

The intake questions are presented in English. The output language follows your input.

## What's included

- **18 named deck layout patterns** (10 consultant + 8 pitch deck) with PPTX master + Slidev pointers
- **9 official logo SVGs** — mark / lockup / vertical × black / white / blue
- **4 Alibaba PuHuiTi 3.0 CJK font weights** (self-hosted, free commercial use)
- **Drop-in design tokens** — `tokens.css`, `tokens.json`, `tailwind.preset.js`
- **9 reference docs** — colors, typography, logo, PPTX (with known-bug list), Slidev, web, docs, social, infographics, deck layouts

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

## Versioning & upgrade

- Versions follow [SemVer](https://semver.org/) (MAJOR.MINOR.PATCH).
- See [CHANGELOG.md](./CHANGELOG.md) for release history.
- Upgrade: `/plugin marketplace update flock-brand`

## License

[MIT](./LICENSE) — the skill's structure, documentation, and tooling are MIT-licensed.

**FLock.io brand assets** (logo SVGs, color values, typography rules, brand voice) remain the intellectual property of FLock.io. Use of these brand assets should follow FLock.io brand guidelines and is intended for FLock.io-related work.

## Repository layout

```
.
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/
│   └── flock-brand/
│       ├── SKILL.md             # Skill router (Iron Rules, dialogue flow, routing)
│       ├── assets/              # Logos, fonts, tokens, Tailwind preset
│       └── references/          # 9 detail docs loaded on demand
├── VERSION
├── CHANGELOG.md
├── LICENSE
└── README.md
```
