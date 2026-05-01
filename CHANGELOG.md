# Changelog

All notable changes to the `flock-brand` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [SemVer](https://semver.org/) (MAJOR.MINOR.PATCH).

---

## [1.2.0] — 2026-05-01

### Added
- **Cursor plugin manifest** at `.cursor-plugin/plugin.json` — mirrors `.claude-plugin/` so Cursor can install via the same plugin format
- **Multi-agent install instructions** in README — one-paste blocks for Claude Code, Cursor, Codex CLI, generic agents, and direct (no-agent) asset use
- **"The flow" section** in README — documents the 5-stage pipeline (Detect → Intake → Plan → Generate → Iterate) with per-stage trigger / loaded-files / user-visible columns
- **"What you can ask for" matrix** in README — maps each artifact type to its default mode, style, output format, and named layouts
- **"See it work" worked example** in README — full conversational transcript from `/flock-brand` invocation through Q1–Q4 → Plan → Generate

### Changed
- README expanded from 80 to ~190 lines, restructured around "Quick install per agent" as the lead section
- Repository layout diagram now includes `.cursor-plugin/`

### Notes
- No changes to `SKILL.md`, `references/`, `assets/`, or any brand rules. Existing v1.1.0 installations behave identically.

---

## [1.1.0] — 2026-05-01

### Added
- **Conversational entry flow** — new `## Entry — context check & dialogue flow` section in `SKILL.md`
  - Step 1: context self-check (decides whether to enter dialogue)
  - Step 2: 4-question intake (Q1 use case · Q2 content · Q3 light/dark · Q4 visual style) — questions presented in English
  - Step 3: Outline Preview before generation, with [Looks good / Edit / Start over] confirm
- **Self-adaptive trigger** — skill skips dialogue entirely when context is already sufficient (zero disruption to existing direct-generation path)
- **Smart-default table** — documents which decisions are inferred (format, length, language, brand pillar) vs user-held (light/dark)

### Changed
- Light/Dark mode is now an explicit user-held switch (Q3), no longer silently inferred. Default still pre-selected per Q1 scenario.

### Notes
- Iron Rules, Routing, Mode selection, Application Quick-Reference, and Pre-flight checklist sections are unchanged. Existing usage patterns (where the user has already supplied full context) are unaffected.

---

## [1.0.0] — 2026-05-01

### Added
- Unified `flock-brand` skill replacing the previously separate Light Mode and Dark Mode skills
- Eight Iron Rules covering brand color (`#3773FF`), Off White (`#F2F2F2`), tracking, typography fallback chain, secondary-color constraints, and logo color rules
- Routing table for on-demand loading of 9 reference files (colors, typography, logo, pptx, slidev, web, docs, social, infographics) plus deck-layouts
- 18 named deck layout patterns (10 consultant + 8 pitch) mapped to PPTX master + Slidev pointers
- 9 official logo SVGs (mark / lockup / vertical × black / white / blue) under `assets/logos/`
- Alibaba PuHuiTi 3.0 self-hosted CJK font integration (4 weights, auto-loaded via `tokens.css` `@font-face`)
- Drop-in resources: `tokens.css`, `tokens.json`, `tailwind.preset.js`
- Mode-selection rationale table mapping deliverable type to default Light/Dark mode
- Pre-flight checklist auto-grep covering hex constants, tracking, font fallbacks, logo placement, CJK fonts, PPTX gotchas

---

## Pre-history (`_archive/`)

Earlier static brand artifacts kept for reference, not maintained:

| File | Date | Notes |
|---|---|---|
| `FLock.io Brand Styling SKILL.pdf` | 2026-02-10 | Static brand guide (PDF) |
| `FLock Design SKILL(Light).md` | 2026-03-12 | First Markdown skill (Light mode only) |
| `flock-brand-light.skill` | 2026-03-13 | Standalone Light variant |
| `FLock_Brand_SKILL_Dark.skill` | 2026-03-13 | Standalone Dark variant |

These were superseded by the unified `flock-brand` skill at `1.0.0`.
