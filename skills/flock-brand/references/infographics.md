# Infographics & Data Visualization

Charts, icons, patterns, and imagery — the visual systems that show up in decks, reports, social carousels, and product pages.

## Iconography

**Style**: line-art, geometric, **stroke-only** (never filled).

| Property | Value |
|---|---|
| Stroke weight | **1.2pt** (1.2px at 1× equivalent) |
| Stroke color | Brand Blue `#3773FF` on light surfaces, White `#FFFFFF` on dark/blue |
| Stroke linecap | `round` |
| Stroke linejoin | `round` |
| Corner radius | Geometric — match the F-mark's angular construction, no fully-rounded "blob" icons |
| Fill | None |

Three motif families align to the three product pillars:

| Pillar | Motif direction |
|---|---|
| 01 — Sovereign AI | Containment / boundary shapes (shields, bounded grids, perimeters) |
| 02 — Operations | Flow / cycle shapes (arrows, loops, pipelines) |
| 03 — Gateway | Connection / network shapes (nodes, links, bridges) |

When an icon represents a pillar, recolor its stroke to the pillar color (see § Chart Color Sequence below). Otherwise default to Brand Blue or White.

**Forbidden**: filled icons, multi-color icons, gradient strokes, drop shadows, hand-drawn / sketched style, emoji-as-icon.

## Chart Color Sequence

Charts use the pillar palette as the canonical series order. Brand Blue is always the primary metric.

| Series | Color | Hex |
|---|---|---|
| 1 (primary) | Brand Blue | `#3773FF` |
| 2 | Turquoise | `#03BFD4` |
| 3 | Purple | `#9C59F3` |
| 4 (only if needed) | Orange | `#FF8B00` |
| Reference / baseline | Mid Gray | `#9A9A9A` |
| Highlight / "current" | Brand Blue with stroke `#000000` 1px or white halo |

For >4 series, use tints (`#98B8F8`, `#B8E8F0`, `#D0B8F8`, `#F8D0A8`) to extend, in the same order. If you need more than 8 distinguishable series in one chart, the chart is wrong — break into small multiples instead.

### Chart-Type Rules

| Chart | Rule |
|---|---|
| Bar / column | Solid fill, no border, 4px corner radius on top edge only (or square — both acceptable, never bottom-rounded) |
| Line | 2.5px stroke, no markers unless data is sparse (<10 points), `round` linejoin |
| Area | 60% opacity fill under a 2.5px solid stroke |
| Pie / donut | Donut only (≥40% inner radius), max 5 slices, others bucketed; never pie |
| Scatter | 6px circles, 1px white stroke for separation on dark backgrounds |
| Sparkline | 1.5px stroke Brand Blue, no axes, no labels |

### Chart Backgrounds

- Dark mode chart: `#000000` background, white axis labels, `#3A3A3A` gridlines at 30% opacity
- Light mode chart: `#FFFFFF` card on `#F2F2F2` page, black axis labels, `#E0E4F0` gridlines

Axis label tracking: `-0.02em`. Numeric labels: tabular figures (`font-feature-settings: "tnum"`).

## Patterns & Motifs

Two signature patterns derived from the F-mark's angular geometry:

1. **Chevron Diamond** — rows of chevron arrows in diamond formation. Use as section dividers, card backgrounds, slide watermarks.
2. **Dot Globe** — spherical dot grid suggesting decentralized nodes. Use behind hero text, on "network / federation" themed visuals.

**Opacity rule**: patterns sit at **3–8% opacity** on Brand Blue or Black surfaces, **6–10% opacity** on Off White. Above 10% they compete with content.

**Color**: pattern strokes are always Brand Blue on light surfaces, White on dark surfaces. Never use a secondary color for patterns.

## Imagery

### Portraits / People

Apply the **blue halftone duotone** treatment:

- Shadows map to Brand Blue `#3773FF`
- Highlights map to Blue Tint `#98B8F8`
- Maintain visible halftone dot texture (don't smooth into a flat duotone)
- For light mode, reduce the duotone to **40–60% opacity** as an accent panel rather than full-bleed

Prefer hands / human gesture over face-forward portraits — the brand's visual voice is collaborative, not personal.

### Abstract / Conceptual

- Geometric constructions (grids, networks, particle systems)
- Repeated F-arrow motifs in formation (echoes the logo)
- High contrast, minimal compositions
- No stock photography of generic "tech" tropes (suit + laptop, glowing brain, server racks)

### Forbidden

- ❌ Full-color photography on brand-primary surfaces — always duotone or Brand Blue overlay
- ❌ Drop shadow on imagery
- ❌ Tilted / dutch-angle compositions
- ❌ AI-generated imagery with visible artifacts (warped hands, melted geometry) — quality bar applies

## Diagrams (architecture, flow)

| Element | Style |
|---|---|
| Node / box | 1.5px stroke Brand Blue, white fill (light) or black fill (dark), 8px radius |
| Connector | 1.5px stroke `#9A9A9A`, arrowhead at terminal, `round` linejoin |
| Highlighted path | 2.5px stroke Brand Blue, no other styling change |
| Label | Inter / TWK Everett 14px, tracking `-0.02em`, sits inside or directly above the node |
| Annotation | Brand Blue 12px italic — sparingly |

For multi-pillar diagrams, color nodes by their pillar (Sovereign Blue / Operations Turquoise / Gateway Purple). Connectors stay neutral gray regardless.

## Pre-flight (data-viz / infographic-specific)

- [ ] Icons stroke-only at 1.2pt, no fills
- [ ] Chart series follows pillar order: Blue → Turquoise → Purple → Orange
- [ ] Primary metric is Brand Blue, not a secondary color
- [ ] Donut not pie; ≤5 slices; bucketed "Other" if needed
- [ ] Gridlines at 30% opacity, not solid
- [ ] Axis labels in `-0.02em` tracking, tabular figures
- [ ] Patterns at 3–10% opacity, never above
- [ ] Portraits in blue halftone duotone, not full color
- [ ] No drop shadows anywhere
- [ ] No more than one secondary color per visual (unless a pillar diagram)
