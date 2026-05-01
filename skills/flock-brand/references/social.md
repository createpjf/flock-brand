# Social Media

Platform-standard sizes paired with FLock brand layout rules. Use this whenever you produce a post, banner, OG image, story, or avatar.

## Canvas Sizes

| Platform | Asset | Size (px) | Default mode |
|---|---|---|---|
| Twitter / X | In-feed image | 1200 × 675 (16:9) | Dark |
| Twitter / X | Header / banner | 1500 × 500 | Dark |
| Twitter / X | Profile avatar | 400 × 400 | Brand Blue or Black |
| LinkedIn | Single-image post | 1200 × 627 | Dark |
| LinkedIn | Company banner | 1584 × 396 | Dark |
| LinkedIn | Company logo | 300 × 300 | Brand Blue or Black |
| Instagram | Square post | 1080 × 1080 | Dark |
| Instagram | Portrait post | 1080 × 1350 | Dark |
| Instagram | Story / Reel cover | 1080 × 1920 | Dark |
| Open Graph (universal) | OG image | 1200 × 630 | Dark |
| Discord | Server icon | 512 × 512 | Brand Blue or Black |
| YouTube | Thumbnail | 1280 × 720 | Dark |
| YouTube | Channel banner | 2560 × 1440 (safe area 1546 × 423) | Dark |

Default to **Dark Mode** for any in-feed visual — that's the brand-defining surface. Switch to Light only for printed handouts or partner co-branded posts where the partner's identity is light-anchored.

## Logo Variant by Aspect Ratio

| Aspect | Use | File |
|---|---|---|
| Square (1:1) — avatars, square posts | Vertical lockup | `flock-vertical-{color}.svg` |
| Landscape (≥16:9) — banners, OG, headers | Horizontal lockup | `flock-lockup-{color}.svg` |
| Portrait (9:16) — stories, reels | Vertical lockup, top-anchored | `flock-vertical-{color}.svg` |
| Tiny (favicon, channel icon ≤64px) | Mark only | `flock-mark-{color}.svg` |

Color suffix follows the standard background rule (`*-white` on dark/blue, `*-black` or `*-blue` on Off White).

## Safe Areas

Reserve a margin equal to **2× the F-mark height** from every edge. Headlines, logos, and CTAs must sit inside this safe zone — platforms crop unpredictably, especially LinkedIn (banner cropping on mobile) and YouTube (channel banner shows different regions per device).

For Instagram stories, reserve the **top 250px and bottom 350px** for UI overlays (profile, reactions, caption). Place the FLock badge or logo inside the central 1080 × 1320 zone.

## Layout Rules

1. **Brand Blue dominance**: hero post = `#3773FF` background with white headline, OR black background with `#3773FF` accent block. Avoid all-white or all-Off-White social posts — they read off-brand.
2. **FLock badge top-right**: the blue pill `FLock.io` badge (see `logo.md` § FLock.io Badge) appears top-right on every multi-image carousel page and every branded one-off. Skip only on bare logo posts.
3. **One headline per asset**: don't stack a primary + subhead + body on a 1080² post. Use 1 headline (≤8 words) at H1 size, optional 1 supporting line.
4. **Tracking stays tight**: `-0.04em` on the headline even at large display sizes. This is the most-violated rule on social — designers tend to relax tracking when the type gets big.
5. **Imagery**: portraits use the halftone duotone treatment (`#3773FF` → `#98B8F8`). Abstract/conceptual visuals preferred over stock photography. See `references/infographics.md` § Imagery for the full treatment.
6. **No drop shadows on text or logos**. Ever, on social.

## Carousel Conventions

For a multi-slide carousel (LinkedIn, Instagram):

- **Slide 1 (hook)**: full-bleed Brand Blue with white headline + small white FLock vertical lockup bottom-left
- **Slides 2–n (content)**: black background, white text, Brand Blue accent rule or number, FLock badge top-right
- **Final slide (CTA)**: Brand Blue background, white CTA copy, white horizontal lockup centered

Maintain a consistent column grid across all slides — don't shift layout between slides 2–n.

## Avatar / Profile Images

- Use `flock-mark-white.svg` on a `#3773FF` square — most recognizable at small sizes
- Alternative: `flock-mark-blue.svg` on `#000000` — for platforms where most icons are colorful (avoids color washout)
- Never crop the F-mark; preserve its full clearspace inside the avatar canvas

## Forbidden

- ❌ Photographic backgrounds without a Brand Blue or Black overlay — kills brand recognition in feed
- ❌ Multiple secondary colors (Orange + Turquoise + Purple) on one post — pick one accent if needed
- ❌ Slanted / rotated text or logos for "energy" — brand voice is precise, not playful
- ❌ Emoji-as-accent inside headlines — clashes with the geometric typography
- ❌ Logo smaller than the platform's minimum tappable area (~44px on mobile)

## Pre-flight (social-specific)

- [ ] Asset matches the exact platform pixel size (no upscaling smaller asset)
- [ ] Safe zone respected — nothing critical within 2× F-mark height of any edge
- [ ] Story / reel: nothing critical in top 250px or bottom 350px
- [ ] Logo variant matches aspect ratio (vertical for square, horizontal for landscape)
- [ ] FLock badge present (unless intentional bare-logo post)
- [ ] Tracking tight at display sizes (`-0.04em` on headline)
- [ ] One headline only, ≤8 words at H1 size
