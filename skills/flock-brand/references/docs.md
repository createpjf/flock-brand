# Documents — DOCX / PDF / Markdown

For long-form deliverables: whitepapers, research PDFs, Word documents, internal reports, one-pagers.

> Default to **Light Mode** for documents — print legibility wins.

---

## DOCX (Word)

### Page setup

| Property | Value |
|---|---|
| Page background | White or Off White `#F2F2F2` |
| Margins | 1" / 25mm all sides minimum |
| Body font | TWK Everett → Inter → fallback chain |
| Body size | 11pt (standard print) — or 24pt if formatted as a deck-style report |
| Heading 1 | Brand Blue `#3773FF`, Bold, 28pt, tracking -2% |
| Heading 2 | Brand Blue `#3773FF`, Medium, 22pt, tracking -2% |
| Heading 3 | Black `#000000`, Medium, 16pt, tracking -1% |
| Body | Black `#000000`, Regular, 11pt, line-height 1.4 |
| Caption | Black `#000000`, Regular, 9pt, line-height 1.4 |

> Word doesn't honor sub-em tracking precisely. Use the Word "Character spacing" setting at -0.3pt (≈-2% on 14pt) for headings, none for body. Verify visually.

### Tables

- **Header row**: Brand Blue `#3773FF` background, white text, semibold
- **Body rows**: alternate White `#FFFFFF` and Off White `#F2F2F2`
- **Border**: `#E0E4F0` 0.5pt, all sides
- **Cell padding**: 6pt vertical, 8pt horizontal

### Pull quotes / callouts

- Background: Off White `#F2F2F2` with a 4px-wide Brand Blue left border
- Text: Black `#000000`, Regular, italics optional, +1pt size

### Numbered lists

Use Arabic numerals followed by an em-space, body-color text. For section numbering (whitepaper-style), use the pillar's color:

> **01.** Sovereign AI (Brand Blue)
> **02.** Operations (Turquoise)
> **03.** Gateway (Purple)

---

## PDF / Markdown export

For Markdown-driven documents that compile to PDF (Pandoc, Typst, Marp):

### Pandoc / Typst variables

```yaml
---
title: "FLock.io · Whitepaper"
author: "FLock.io Research"
date: 2026-05-01
geometry: margin=1in
mainfont: "TWK Everett"
sansfont: "TWK Everett"
monofont: "JetBrains Mono"
mainfontfallback: ["Inter", "Alibaba PuHuiTi 3.0", "PingFang SC", "Noto Sans SC"]
fontsize: 11pt
linkcolor: "[HTML]{3773FF}"
urlcolor: "[HTML]{3773FF}"
header-includes:
  - \usepackage{xcolor}
  - \definecolor{flockblue}{HTML}{3773FF}
  - \usepackage{titlesec}
  - \titleformat{\section}{\color{flockblue}\Large\bfseries}{\thesection}{1em}{}
  - \titleformat{\subsection}{\color{flockblue}\large\bfseries}{\thesubsection}{1em}{}
---
```

### Cover page convention (PDF reports)

- Brand Blue `#3773FF` full-bleed top band, ~30% of the page height, white title
- Off White `#F2F2F2` body
- FLock.io badge top-right (extended convention — see `logo.md`)
- Optional large `01` watermark at 10–15% opacity behind the title

---

## Citation / data callouts

When referencing a paper, dataset, or stat inside body text, format as:

> The federated training round completed in **`#3773FF · 4.2 min · NeurIPS 2023`** —

Brand Blue, monospace, 14px (or matching body cap-height). This is a brand signature pattern — emulate it whenever data needs to be highlighted inline.

---

## File naming

```
flock-{topic}-{type}-{YYYYMMDD}.{ext}
e.g.
flock-sovereign-ai-whitepaper-20260501.pdf
flock-q2-investor-update-deck-20260501.pptx
flock-research-roadmap-onepager-20260501.docx
```

---

## QA checklist for documents

- [ ] No `#282828`, `#F2F2F0`, `#00A8C0`, `#6030D0` anywhere
- [ ] Headings in Brand Blue `#3773FF`; body in Black `#000000`
- [ ] Body font is TWK Everett or Inter (verify by checking a paragraph in the rendered PDF)
- [ ] Hyperlinks in `#3773FF`, not browser default
- [ ] Tables: Brand Blue header row, alternating Off-White rows, `#E0E4F0` borders
- [ ] Page numbers present, monospace, low-contrast
- [ ] If Chinese: punctuation is full-width (`，。：；！？""''——……`)
- [ ] If exported to PDF: file opens cleanly in Preview and Acrobat without missing fonts
