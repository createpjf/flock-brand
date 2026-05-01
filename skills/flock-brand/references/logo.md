# Logo

## Variations

1. **Primary Mark (F-Arrow)** — stylized "F" with integrated forward arrow pointing upper-right. Symbolizes progress, direction, decentralized coordination. Used as primary icon / favicon.
2. **Wordmark** — `FLock.io`. "F" capitalized with distinctive stylized treatment, "Lock" in standard weight, ".io" appended.
3. **Short Wordmark** — `FLock` (no `.io`). Use when the domain isn't relevant.
4. **Full Lockup** — Mark + Wordmark, horizontal arrangement.

## Construction

- Built on a geometric grid with precise proportions.
- Arrow within the "F" points upper-right, symbolizing growth and forward momentum.
- Construction lines define consistent angles and curves — never approximate by drawing freehand.

## Color by Background (PDF rule)

| Background | Logo color |
|---|---|
| Black `#000000` | **White** (default dark mode) |
| Brand Blue `#3773FF` | **White** (brand highlight) |
| Off White `#F2F2F2` / White | **Black** or **Brand Blue** |

Never recolor the logo outside these combinations.

## Clearspace

Minimum clearspace on all sides = the height of the "F" mark itself. Treat this as a hard padding — no other element (text, image, edge) may enter this zone.

## Minimum Sizes (Extended)

| Context | Minimum size |
|---|---|
| Digital — F-Arrow mark | 24px height |
| Print — F-Arrow mark | 8mm height |
| Wordmark | 80px / 28mm height |

Below these sizes, legibility breaks and stroke weight collapses. Use the F-Arrow mark alone instead of the wordmark when the artifact is too small.

## Forbidden Manipulations

- ❌ Distort, stretch, or skew
- ❌ Rotate to any angle other than 0°
- ❌ Recolor outside the approved combinations above
- ❌ Apply drop shadow, glow, or bevel
- ❌ Set on a busy photographic background without a solid color underlay
- ❌ Place text within the clearspace zone

## FLock.io Badge (Extended — internal layout convention)

A blue pill badge — `#3773FF` background, white text reading `FLock.io`, ~28px tall, fully rounded — sits **top-right** on every content page of branded multi-page artifacts (decks, PDF reports). This is a signature layout element.

### CSS

```css
.flock-badge {
  display: inline-flex;
  align-items: center;
  background: var(--flock-brand-blue);
  color: #FFFFFF;
  padding: 4px 12px;
  border-radius: 9999px;
  font-family: var(--flock-font-primary);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: -0.02em;
}
```

### PptxGenJS

```js
slide.addShape(pres.ShapeType.roundRect, {
  x: 12.0, y: 0.3, w: 1.2, h: 0.35,
  fill: { color: "3773FF" },          // no leading #
  line: { color: "3773FF" },
  rectRadius: 0.18,
});
slide.addText("FLock.io", {
  x: 12.0, y: 0.3, w: 1.2, h: 0.35,
  fontFace: "Inter", fontSize: 12, color: "FFFFFF",
  align: "center", valign: "middle", bold: false,
});
```

## Logo Asset Files

The official logo SVGs are bundled at `flock-brand/assets/logos/`. **Use these directly — never approximate or hand-redraw.**

```
flock-brand/assets/logos/
  ├── flock-mark-black.svg          # F-Arrow only, black fill — for Off White backgrounds
  ├── flock-mark-white.svg          # F-Arrow only, white fill — for Black/Blue backgrounds
  ├── flock-mark-blue.svg           # F-Arrow only, blue fill — for Off White hero accents
  ├── flock-lockup-black.svg        # F-Arrow + "FLock.io" wordmark, horizontal, black
  ├── flock-lockup-white.svg        # F-Arrow + "FLock.io" wordmark, horizontal, white
  ├── flock-lockup-blue.svg         # F-Arrow + "FLock.io" wordmark, horizontal, blue
  ├── flock-vertical-black.svg      # F-Arrow + wordmark, stacked vertical, black
  ├── flock-vertical-white.svg      # F-Arrow + wordmark, stacked vertical, white
  └── flock-vertical-blue.svg       # F-Arrow + wordmark, stacked vertical, blue
```

Source: <https://logo.flock.io>. Files were fetched from the official asset CDN.

### Quick selection rule

| What you need | File |
|---|---|
| Tiny icon / favicon / inline F | `flock-mark-{color}.svg` |
| Standard horizontal lockup (header, deck cover) | `flock-lockup-{color}.svg` |
| Stacked / square layout (social avatar, FigJam, narrow column) | `flock-vertical-{color}.svg` |

Color suffix:

| Background | Use |
|---|---|
| Black `#000000` | `*-white.svg` |
| Brand Blue `#3773FF` | `*-white.svg` |
| Off White `#F2F2F2` / White | `*-black.svg` or `*-blue.svg` |

### Embedding examples

**HTML / Slidev**:

```html
<img src="/flock-brand/assets/logos/flock-mark-white.svg" alt="FLock.io" height="32">
```

**React**:

```jsx
import FlockMark from '@/flock-brand/assets/logos/flock-mark-white.svg';
// or as <img>:
<img src="/flock-brand/assets/logos/flock-lockup-white.svg" alt="FLock.io" />
```

**PptxGenJS**:

```js
slide.addImage({
  path: "./flock-brand/assets/logos/flock-mark-white.svg",
  x: 0.4, y: 0.4, w: 0.5, h: 0.88,            // F-mark is 69×121 viewBox; preserve ~0.57 aspect ratio
  sizing: { type: "contain" },
});
```

PptxGenJS supports SVG natively in modern versions. If the deployment environment falls back to raster, pre-rasterize at 2× target size with `sharp`:

```bash
npx sharp-cli -i flock-mark-white.svg -o flock-mark-white@2x.png --width 256
```

### ⚠️ Known color discrepancy

The official SVGs at `logo.flock.io` use `fill="#366FFF"` — slightly **different** from the PDF brand book's `#3773FF`:

| Source | Hex | RGB |
|---|---|---|
| Brand Book PDF | `#3773FF` | `rgb(55, 115, 255)` |
| Logo SVG (logo.flock.io) | `#366FFF` | `rgb(54, 111, 255)` |

Difference is small (~2% lightness shift), but real. Until FLock design team clarifies which is canonical:

- **Treat `#3773FF` as canonical** for all brand applications (CSS, PPTX fills, charts) — it's documented in the official brand book.
- **Do not modify the SVG `fill` attributes** — using the asset as-is preserves auditability and avoids one-off tweaks compounding over time.
- If a designer raises this, point them to `logo.flock.io/flock-brand-book` vs the SVG fill mismatch.

### Refreshing the assets

If the upstream changes, refetch with:

```bash
cd flock-brand/assets/logos
curl -sSL -o flock-lockup-black.svg   "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/5570718e-7c40-462e-8116-ea17b7bd8d92/logo-full.svg"
curl -sSL -o flock-lockup-blue.svg    "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/74c48cc2-84f0-45df-9f89-17d2eee67c04/logo-full.svg"
curl -sSL -o flock-lockup-white.svg   "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/94b106be-9d28-4ac0-9219-b07919941827/logo-full.svg"
curl -sSL -o flock-mark-black.svg     "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/e0cb91fc-7931-4ae8-8d2a-f6b1169359d3/Single.svg"
curl -sSL -o flock-mark-white.svg     "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/2538e7c5-81a9-472b-b726-21c7cf53a3d3/logo_white.svg"
curl -sSL -o flock-mark-blue.svg      "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/47dbc25a-46f4-4be7-8963-1d4d874c4da0/single_blue.svg"
curl -sSL -o flock-vertical-black.svg "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/c9b20c57-408a-4e38-88f7-90b13cdc1ec9/Logo.svg"
curl -sSL -o flock-vertical-white.svg "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/c9e9e142-10a3-461e-895b-b2c314ec0284/logo.svg"
curl -sSL -o flock-vertical-blue.svg  "https://assets.super.so/fa93bcd3-68d8-4675-be45-9c7f290dac2c/images/18b6a5eb-338a-4a73-83f1-caead23f3c31/logo.svg"
```

Other assets at `logo.flock.io` not currently bundled (fetch as needed):

- `/flock-tech` — FLock Tech sub-brand variants
- `/flock-token-logo` — Token-specific branding
- `/flock-brand-book` — Full brand book PDF

### Forbidden

- ❌ Don't redraw the F-Arrow by hand or generate it via SVG primitives — the construction grid is non-trivial and approximations look off-brand
- ❌ Don't apply CSS filters (`filter: invert`, `hue-rotate`) to recolor — fetch the correct color variant instead
- ❌ Don't ship a deck/site without the official SVG and a `<!-- TODO: official logo -->` comment — fetch the asset instead
