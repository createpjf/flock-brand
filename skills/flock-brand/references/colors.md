# Colors — Single Source of Truth

> **Authority hierarchy**: Section 1 (Official) is canonical, taken verbatim from the FLock.io Brand Styling SKILL PDF. Section 2 (Extended) is internal extension — useful but not in the official guide; mark it as such when sharing externally.

---

## 1. Official Palette (from PDF)

### Primary Palette

| Token | Name | Hex | RGB | Role |
|---|---|---|---|---|
| `brand-blue` | Brand Blue | `#3773FF` | `rgb(55, 115, 255)` | **Hero color** — primary brand identifier. Backgrounds, CTAs, key brand moments, dominant visual element |
| `black` | Black | `#000000` | `rgb(0, 0, 0)` | Primary dark background; text on light surfaces |
| `off-white` | Off White | `#F2F2F2` | `rgb(242, 242, 242)` | Light backgrounds, cards, containers |

### Secondary Palette (Accents only)

| Token | Name | Hex | RGB | Role |
|---|---|---|---|---|
| `orange` | Orange | `#FF8B00` | `rgb(255, 139, 0)` | Highlights, notifications, energy, CTA alternatives |
| `turquoise` | Turquoise | `#03BFD4` | `rgb(3, 191, 212)` | Data viz, complementary, tech-forward moments |
| `purple` | Purple | `#9C59F3` | `rgb(156, 89, 243)` | Premium features, differentiation, creative highlights |

### Color Usage Rules (verbatim from PDF)

1. **Brand Blue `#3773FF` is dominant** — use it boldly for hero sections, headers, primary CTAs.
2. **Black backgrounds with blue accents** create the core "tech premium" look. This is the brand-defining pairing.
3. Secondary colors (Orange, Turquoise, Purple) **sparingly as accents, never as primary**.
4. **High contrast always**: white text on blue/black backgrounds; dark text on Off White.
5. **Default pairing**: `Brand Blue + White`. **Dramatic pairing**: `Brand Blue + Black`.
6. Off White `#F2F2F2` **replaces pure white** for softer, more refined light surfaces.
7. **Dark mode is the brand's primary mode**; Light mode adapts the same hierarchy onto Off White.

### Semantic Tokens (PDF-derived)

```
--flock-bg-dark:        #000000   (primary background, dark mode)
--flock-bg-light:       #F2F2F2   (primary background, light mode)
--flock-bg-brand:       #3773FF   (hero / accent surfaces)

--flock-text-on-dark:   #FFFFFF
--flock-text-on-light:  #000000
--flock-text-on-brand:  #FFFFFF
```

---

## 2. Extended Guidelines (internal — NOT in the official PDF)

These extensions are house conventions for richer artifacts. Use them, but if a designer asks "is this in the official guide?" the answer is **no — these are extensions**.

### 2.1 Pillar Color Encoding

Three product pillars carry consistent color identity across all materials:

| Pillar | Color | Hex | Tint (panels) | Tint Hex |
|---|---|---|---|---|
| 01 — Sovereign AI | Brand Blue | `#3773FF` | Blue Tint | `#98B8F8` |
| 02 — Operations | Turquoise | `#03BFD4` | Teal Tint | `#B8E8F0` |
| 03 — Gateway | Purple | `#9C59F3` | Purple Tint | `#D0B8F8` |

Additional tint:

| Use | Color | Tint Hex |
|---|---|---|
| Trust / partnership content | Orange Tint | `#F8D0A8` |

**Rule**: full-saturation pillar colors are accents on text/icons/headings only. Pastel tints (the right column above) are for content panels, feature card backgrounds, and section dividers. Never use the full-saturation colors as background.

### 2.2 Off-Brand Surface Tokens (light mode only)

For richer light-mode layouts (cards on a page, multiple surface depths), these helpers extend the official palette:

| Token | Hex | Use |
|---|---|---|
| `surface` | `#F8F8F8` | Optional softer page base when `#F2F2F2` cards need to sit on a paler surface |
| `card` | `#FFFFFF` | Card surfaces, elevated elements |
| `border` | `#E0E4F0` | 1px borders on white cards for definition |

`#F2F2F2` (official) remains the default page background. `#F8F8F8` is only for "page beneath cards" depth play.

### 2.3 Status / Feedback Colors

Not in PDF. Approved internal extensions:

| Token | Hex | Use |
|---|---|---|
| `green` | `#22B473` | Success states, positive indicators |

If you need warning/error semantic colors, use Orange `#FF8B00` for warning and a distinct red (e.g., `#E5484D`) — but verify with brand owner before locking.

### 2.4 Gradient Spectrum

For decorative gradient bands, sweeps, or hero treatments, the canonical left-to-right spectrum is:

```
Brand Blue (#3773FF)  →  Turquoise (#03BFD4)  →  Purple (#9C59F3)  →  Orange (#FF8B00)
```

Use sparingly — at most one gradient per artifact, and never with text on top of the gradient itself.

---

## 3. Mode-specific Color Behavior

### Dark Mode (Primary)

| Surface | Color |
|---|---|
| Page background | `#000000` |
| Hero / CTA section | `#3773FF` |
| Card / elevated surface | `#000000` with subtle Brand Blue accents, or `#3773FF` highlights |
| Body text | `#FFFFFF` |
| Headings | `#FFFFFF` (or Brand Blue accent for emphasis) |
| Dividers / borders | Brand Blue at low opacity, or `#FFFFFF` at 10% |
| Logo | White `F` on black; White `F` on Brand Blue hero |

### Light Mode (Secondary)

| Surface | Color |
|---|---|
| Page background | `#F2F2F2` |
| Card / elevated surface | `#FFFFFF` with `#E0E4F0` 1px border, 10–12px radius |
| Body text | `#000000` |
| H1 / H2 | `#3773FF` (Brand Blue) — this is the signature on light |
| H3 / smaller | `#000000` |
| Dividers / borders | `#E0E4F0` |
| Hero block (exception) | `#3773FF` background with white text — for cover/CTA pages even within a light-mode deck |
| Logo | Black or Brand Blue on Off White; White on Brand Blue hero |

---

## 4. Common Mistakes to Auto-Reject

When reviewing an artifact, flag any of these immediately:

- ❌ `#282828` anywhere — should be `#000000`
- ❌ `#F2F2F0` anywhere — should be `#F2F2F2`
- ❌ `#00A8C0` (old Turquoise) — should be `#03BFD4`
- ❌ `#6030D0` (old Purple) — should be `#9C59F3`
- ❌ Any blue that is not `#3773FF` claiming to be "Brand Blue"
- ❌ Pure white `#FFFFFF` as a page background (use Off White `#F2F2F2`); white is fine for cards
- ❌ Secondary color (Orange/Turquoise/Purple) as the page background
- ❌ Two pillar colors competing on the same content panel
- ❌ Brand Blue `#3773FF` mixed at low opacity producing a non-canonical pastel — use the explicit Tint hex from §2.1

---

## 5. Off-brand → FLock 重映射表（fix 任务专用）

修复继承来的 deck 时,off-brand 颜色按**语义**映射到 FLock 调色板,不是只换主蓝。
机器执行版在 `scripts/pptx_lint.py` 的 `REMAP` 字典 —— 那里是单一事实源,本表为人读摘要。

| 语义 | 常见 off-brand hex | → FLock |
|---|---|---|
| 主蓝(Tailwind blue 等) | `2D72F8` `2C68F0` `3B82F6` `2563EB` `1D4ED8` `1A4FB0` | `#3773FF` Brand Blue |
| 浅蓝 accent | `60A5FA` `93C5FD` | `#98B8F8` Blue Tint |
| 红 / 警示 | `DC2626` `EF4444` | `#FF8B00` Orange（FLock 无红,警示语义归 Orange） |
| 浅红底 | `FEE4E4` `FEE2E2` | `#F8D0A8` Orange Tint |
| 绿 / 青 | `0D9488` `0891B2` `10B981` | `#03BFD4` Turquoise |
| 浅绿底 | `ECFDF5` `D1FAE5` | `#B8E8F0` Teal Tint |
| 粉 / 紫 | `BE185D` `7C3AED` `8B5CF6` | `#9C59F3` Purple |
| 浅紫/粉底 | `FCE7F3` `EDE9FE` | `#D0B8F8` Purple Tint |
| 黄 / 琥珀 | `D97706` `F59E0B` | `#FF8B00` Orange |
| 浅黄底 | `FEF3C7` `FFEDD5` | `#F8D0A8` Orange Tint |
| 灰边框 | `DCE5F0` `D1D5DB` | `#E0E4F0` border |

**容忍不替换**：中性灰文字色（`1F2937` `4B5563` `6B7280` 等)在 fix 任务中可保留 —— 全换成纯黑会破坏原 deck 的层级灰阶,除非用户要求完全重做配色。

**成功语义例外**：原 deck 用绿表示「成功/通过」时,映射到 `#22B473`（FLock green）而非 Turquoise。
