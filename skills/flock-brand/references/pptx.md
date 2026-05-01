# PPTX — FLock-styled PowerPoint

This file gives you working PptxGenJS recipes for both **dark mode** (primary) and **light mode** decks. Read it whenever you generate or edit a `.pptx` for FLock.

> Do not preload this file. Load only when the task is "create / edit a `.pptx`".

---

## Stack

- **Generation**: [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) (Node.js). `npm i -g pptxgenjs` or per-project `npm i pptxgenjs`.
- **Editing existing PPTX templates**: unzip → edit `slide{N}.xml` → re-zip. See `editing` section.
- **Text inspection**: `markitdown deck.pptx`.
- **Visual inspection**: `soffice --headless --convert-to pdf deck.pptx && pdftoppm -r 100 deck.pdf slide -jpeg`.

---

## Known PptxGenJS Bugs (must memorize)

These will silently corrupt your `.pptx` or render incorrectly. They are **not optional gotchas** — they are file-level bugs.

| Bug | Wrong | Right |
|---|---|---|
| Hex with `#` | `color: "#3773FF"` | `color: "3773FF"` (no leading `#`) |
| Transparency in hex | `color: "00000020"` | use `transparency: 80` (0–100) on shape options |
| Negative shadow offset | `shadow: { offset: -2 }` | use `angle: 270` for upward shadows; `offset` ≥ 0 |
| Unicode `•` bullets | `text: "• Item"` | `text: "Item", bullet: true` |
| Reusing options object across calls | `slide.addText(t, opts); slide.addText(t2, opts)` (PptxGenJS mutates `opts` in place) | clone: `slide.addText(t2, {...opts})` |
| Sharing `pptxgen()` instance across decks | one global `pres` for multiple files | `const pres = new pptxgen()` per output file |
| `roundRect` accent overlay | mixing `roundRect` and rectangle accent | keep accent shapes the same type |

Auto-grep your generator code for `color: "#`, `'•'`, and `shadow: { offset: -` before saving.

---

## Slide Masters — Dark Mode (Primary)

```js
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();

pres.defineLayout({ name: "FLOCK_16_9", width: 13.333, height: 7.5 });
pres.layout = "FLOCK_16_9";

// ---- COVER (hero) ----
pres.defineSlideMaster({
  title: "FLOCK_COVER_DARK",
  background: { color: "3773FF" },                 // Brand Blue hero
  objects: [
    { rect: { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: "3773FF" } } },
    // FLock badge top-right
    { rect: { x: 12.0, y: 0.3, w: 1.2, h: 0.35, fill: { color: "FFFFFF" }, line: { color: "FFFFFF" } } },
    { text: { text: "FLock.io",
      options: { x: 12.0, y: 0.3, w: 1.2, h: 0.35, fontFace: "Inter", fontSize: 12,
                 color: "3773FF", align: "center", valign: "middle" } } },
  ],
});

// ---- CONTENT (default content slide, dark) ----
pres.defineSlideMaster({
  title: "FLOCK_CONTENT_DARK",
  background: { color: "000000" },                 // Black
  objects: [
    // top-right blue pill badge
    { rect: { x: 12.0, y: 0.3, w: 1.2, h: 0.35, fill: { color: "3773FF" } } },
    { text: { text: "FLock.io",
      options: { x: 12.0, y: 0.3, w: 1.2, h: 0.35, fontFace: "Inter", fontSize: 12,
                 color: "FFFFFF", align: "center", valign: "middle" } } },
    // bottom-left page number placeholder
    { placeholder: {
        options: { name: "footer", type: "body", x: 0.5, y: 7.05, w: 1.5, h: 0.3,
                   fontFace: "SF Mono", fontSize: 10, color: "FFFFFF" },
        text: "01"
    } },
  ],
});

// ---- SECTION DIVIDER ----
pres.defineSlideMaster({
  title: "FLOCK_SECTION_DARK",
  background: { color: "000000" },
  objects: [
    // huge watermark numeral
    { text: { text: "01",
      options: { x: 0.5, y: 1.5, w: 6, h: 5, fontFace: "Inter", fontSize: 360,
                 bold: true, color: "3773FF", transparency: 85, align: "left" } } },
  ],
});
```

### Adding slides

```js
// Cover
const cover = pres.addSlide({ masterName: "FLOCK_COVER_DARK" });
cover.addText("Real AI. Real Impact.", {
  x: 0.7, y: 3.0, w: 12, h: 1.5,
  fontFace: "Inter", fontSize: 64, bold: true,
  color: "FFFFFF", charSpacing: -2,           // -4% of 64 ≈ -2.56pt; charSpacing in 1/100 em
});
cover.addText("FLock.io · 2026", {
  x: 0.7, y: 4.5, w: 12, h: 0.6,
  fontFace: "Inter", fontSize: 24, color: "FFFFFF", charSpacing: -1,
});

// Content
const c1 = pres.addSlide({ masterName: "FLOCK_CONTENT_DARK" });
c1.addText("Sovereign AI", {
  x: 0.7, y: 0.7, w: 8, h: 1,
  fontFace: "Inter", fontSize: 48, bold: true,
  color: "3773FF", charSpacing: -2,
});
c1.addText([
  { text: "Federated learning for regulated data", options: { bullet: true } },
  { text: "Compliance-grade audit trail",            options: { bullet: true } },
  { text: "Sovereign model deployment",              options: { bullet: true } },
], {
  x: 0.7, y: 2.0, w: 12, h: 4,
  fontFace: "Inter", fontSize: 24, color: "FFFFFF", charSpacing: -1,
  paraSpaceAfter: 12,
});

await pres.writeFile({ fileName: "flock-deck.pptx" });
```

### `charSpacing` ≠ CSS letter-spacing

PptxGenJS `charSpacing` is **1/100 of an em** (so `-4` = -0.04em), but in practice it behaves close to "points × 100" — calibrate by eye for headings:

| Type level | font-size | charSpacing |
|---|---|---|
| H1 64pt | 64 | -2 to -3 |
| H2 48pt | 48 | -2 |
| H3 36pt | 36 | -1 to -2 |
| Body 24pt | 24 | -1 |

For Chinese headings, drop charSpacing to **0 or -1** — never tighter.

---

## Slide Masters — Light Mode

Same structure, swap colors:

```js
pres.defineSlideMaster({
  title: "FLOCK_CONTENT_LIGHT",
  background: { color: "F2F2F2" },                 // Off White (NOT FFFFFF as base)
  objects: [
    { rect: { x: 12.0, y: 0.3, w: 1.2, h: 0.35, fill: { color: "3773FF" } } },
    { text: { text: "FLock.io",
      options: { x: 12.0, y: 0.3, w: 1.2, h: 0.35, fontFace: "Inter", fontSize: 12,
                 color: "FFFFFF", align: "center", valign: "middle" } } },
  ],
});

// Card on white
const slide = pres.addSlide({ masterName: "FLOCK_CONTENT_LIGHT" });
slide.addShape(pres.ShapeType.roundRect, {
  x: 0.7, y: 1.5, w: 11.9, h: 5,
  fill: { color: "FFFFFF" },
  line: { color: "E0E4F0", width: 1 },
  rectRadius: 0.12,
});
// H1/H2 in Brand Blue on light
slide.addText("Real AI. Real Impact.", {
  x: 1.2, y: 2.0, w: 11, h: 1.5,
  fontFace: "Inter", fontSize: 48, bold: true,
  color: "3773FF", charSpacing: -2,
});
// Body in black
slide.addText("Sovereign · Compliant · Integrated · Research-backed", {
  x: 1.2, y: 3.5, w: 11, h: 0.6,
  fontFace: "Inter", fontSize: 24,
  color: "000000", charSpacing: -1,
});
```

---

## Charts (data slides)

PptxGenJS native charts default ugly. Always override:

```js
slide.addChart(pres.ChartType.bar, dataChartAreaLine, {
  x: 1, y: 1.5, w: 11, h: 5,
  chartColors: ["3773FF", "03BFD4", "9C59F3", "FF8B00"],   // FLock palette
  chartColorsOpacity: 100,
  showTitle: false,
  showLegend: true,
  legendPos: "b",
  legendFontFace: "Inter",
  legendFontSize: 12,
  catAxisLabelFontFace: "Inter",
  catAxisLabelFontSize: 11,
  catAxisLabelColor: "FFFFFF",                              // dark mode
  valAxisLabelFontFace: "Inter",
  valAxisLabelFontSize: 11,
  valAxisLabelColor: "FFFFFF",
  catGridLine: { style: "none" },                           // hide horizontal lines
  valGridLine: { color: "FFFFFF", style: "solid", size: 0.5, transparency: 90 },
  barGapWidthPct: 50,
  showValue: true,
  dataLabelFontFace: "Inter",
  dataLabelFontSize: 10,
  dataLabelColor: "FFFFFF",
  dataLabelPosition: "outEnd",
});
```

For light mode swap label colors to `000000` and grid line to `E0E4F0`.

**Single-series rule**: hide the legend (`showLegend: false`) — the title or a callout above the chart provides context.

---

## Editing existing PPTX templates (OOXML route)

Use this when the user has a corporate template they need updated, **not** when creating from scratch.

1. **Unpack**: `python -m office.unpack template.pptx /tmp/deck-unpacked`
2. **Inspect text content**: `python -m markitdown template.pptx` to find what to replace
3. **Edit XML**: open `/tmp/deck-unpacked/ppt/slides/slide{N}.xml` with the Edit tool
   - Multi-paragraph text: must be multiple `<a:p>` elements; do **not** concatenate into one paragraph
   - Smart quotes (Latin): `&#x201C;` `&#x201D;`
   - Chinese punctuation: use the literal characters `""''——……，。！？` directly — don't encode them as entities
   - Remove an element (image, shape, text box) by deleting **the whole block** including container; don't just empty `<a:t>`
4. **Clean orphan refs**: `python -m office.clean /tmp/deck-unpacked` — removes dangling rels and missing media references
5. **Repack**: `python -m office.pack /tmp/deck-unpacked output.pptx`
6. **Verify**: `markitdown output.pptx` (text), then visual audit (next section)

**Forbidden**: don't run `sed`, `awk`, or `xml.etree.ElementTree` on these files — they break the namespace. Use the Edit tool, or `defusedxml.minidom` if you must script it.

---

## QA — fix-and-verify (mandatory)

Don't declare done until both checks pass:

### A. Text-level grep

```bash
markitdown output.pptx > /tmp/deck.txt
grep -iE "(lorem|ipsum|xxx|TODO|placeholder|待补充|示例|请填写|tk|tbd)" /tmp/deck.txt && echo "FAIL: placeholders" || echo "PASS"
grep -E "#[0-9A-Fa-f]{6}" /tmp/deck.txt   # any leftover hex string in actual slide text? probably wrong
```

### B. Visual audit (sub-agent)

```bash
soffice --headless --convert-to pdf output.pptx --outdir /tmp/
pdftoppm -r 120 /tmp/output.pdf /tmp/slide -jpeg
```

Then spawn a sub-agent (fresh eyes) with this prompt:

> Look at each JPG. For each slide, report: (1) any text that overflows the slide edge, (2) any text that overlaps another element, (3) any low-contrast pair (e.g., body grey on a Brand-Blue background), (4) any heading not in Inter/TWK Everett, (5) any non-FLock blue used. Score each slide pass/fail. Only "all pass" allows declaring done.

If any slide fails, fix the relevant slide (re-render only those), re-run BOTH checks. **Do not skip re-verification** — a fix in one slide commonly introduces a regression elsewhere.

---

## Common pitfalls

- **Bullet font fallback**: when the bullet character is rendered, PowerPoint sometimes substitutes Wingdings. Force `bullet: { type: "bullet", code: "25CF" }` for a clean black/blue circle.
- **Font embedding**: TWK Everett rarely ships embedded; if the deck must look identical off your machine, **embed the font** (`pres.embedFont("Inter")`) or convert the title slide to an image. Brief the user.
- **Image scaling**: use `sizing: { type: "contain" }` for photos with critical content; `cover` for hero images that can crop; never default-stretch.
- **Hyperlink color**: PptxGenJS sets blue by default but it's the wrong blue. Force `color: "3773FF"` on link text.
