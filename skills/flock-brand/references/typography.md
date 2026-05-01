# Typography

## Primary Typeface: TWK Everett

TWK Everett is the sole brand font across all weights (Regular 400, Medium 500, Bold 700).

### Font Stack (Latin)

```
'TWK Everett', 'Inter', 'SF Pro Display', 'Helvetica Neue', 'Arial', sans-serif
```

**Order matters.** Inter is the canonical web fallback (load from Google Fonts). SF Pro Display is the macOS system fallback. Never insert another sans-serif before Inter.

### Loading Inter on the web

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap">
```

For self-hosting TWK Everett (preferred when license permits), drop the `.woff2` files into `assets/fonts/` and `@font-face` them with `font-display: swap`.

---

## Type Scale (PDF-canonical)

| Level | Weight | Size | Line Height | Tracking |
|---|---|---|---|---|
| H1 | Bold (700) | 64px | 100% (1.0) | -4% (`-0.04em`) |
| H2 | Medium (500) | 48px | 100% (1.0) | -4% (`-0.04em`) |
| H3 | Medium (500) | 36px | 120% (1.2) | -3% (`-0.03em`) |
| Body / Paragraph | Regular (400) | 24px | 120% (1.2) | -3% (`-0.03em`) |

### Extended (not in PDF, internal-only)

| Level | Weight | Size | Line Height | Tracking | Use |
|---|---|---|---|---|---|
| Caption | Regular (400) | 14px | 140% (1.4) | normal | Captions, footnotes, secondary labels |
| Data / Spec | Mono Regular | 12px | 140% (1.4) | normal | Page numbers, citation, code, data labels |

Monospace stack: `'SF Mono', 'Fira Code', 'JetBrains Mono', 'Consolas', monospace`.

---

## Iron Rules

1. **Tight tracking is a defining brand characteristic.** Never use default letter-spacing on Latin headings or body. -4% on H1/H2, -3% on H3/body.
2. H1/H2 use 100% line-height for visual density and impact. H3/body use 120% for readability.
3. All headings use TWK Everett exclusively (or Inter fallback).
4. **On dark backgrounds**: all text in white `#FFFFFF`.
5. **On light backgrounds (Off White)**: H1/H2 in Brand Blue `#3773FF`, body in `#000000`.
6. The alphabet showcase highlights Dd, Ff, Ss, Vv in blue — emulate this when introducing brand letterforms in a brand reveal artifact.
7. **Data highlights** (callouts inside body text — e.g., `#3773FF · 24px · NeurIPS 2023`) use Brand Blue monospace for the call-out token.

---

## CJK / 中文支持（Extended — not in PDF）

The official guide is Latin-only. For Chinese / 中日韩 content, use the rules below.

### Primary CJK Font: 阿里巴巴普惠体 3.0 (Alibaba PuHuiTi 3.0)

The canonical CJK typeface for FLock. System fonts (PingFang SC / Microsoft YaHei / Noto Sans SC) drop to fallback role.

- **Why**: 开源、商用免费、9 个字重齐全（35→105）、屏幕阅读优化、与 TWK Everett / Inter 视觉重量协调
- **License**: 阿里巴巴免费商用许可，无需单独授权
- **Source**: <https://www.alibabafonts.com/#/font>
- **CSS family name**: `"Alibaba PuHuiTi 3.0"`（family 名）或具体字重文件名 `"AlibabaPuHuiTi-3-55-Regular"` / `"AlibabaPuHuiTi-3-85-Bold"`
- **Weight 映射**：

  | Weight 数字 | 名称 | FLock 用法 |
  |---|---|---|
  | 35 | Thin | — |
  | 45 | Light | — |
  | **55** | **Regular** | **Body / Caption** |
  | **65** | **Medium** | **H3 / Subhead** |
  | **75** | **SemiBold** | **H2** |
  | **85** | **Bold** | **H1** |
  | 95 | ExtraBold | 超粗强调（极少用） |
  | 105 | Heavy | 海报巨标题（特殊场合） |

- **Already bundled**: 4 个 FLock 用到的字重已经放在 `flock-brand/assets/fonts/`（55 Regular / 65 Medium / 75 SemiBold / 85 Bold，共 ~21MB WOFF2），并在 `assets/tokens.css` 顶部用 `@font-face` 自动加载。`@import './tokens.css'` 就能用，不需要额外配置。
- **Self-host (Web) — 如果要自定义路径**：从 alibabafonts.com 下载 WOFF2 或继续从 jsDelivr 抓（`https://cdn.jsdelivr.net/npm/alibabapuhuiti-3-{weight}@1.0.0/AlibabaPuHuiTi-3-{Weight}.woff2`），放任意目录或自家 CDN，用 `@font-face` 声明：

  ```css
  @font-face {
    font-family: 'Alibaba PuHuiTi 3.0';
    src: url('/fonts/AlibabaPuHuiTi-3-55-Regular.woff2') format('woff2');
    font-weight: 400;
    font-display: swap;
    unicode-range: U+4E00-9FFF, U+3000-303F, U+FF00-FFEF;  /* 仅 CJK 区段触发下载 */
  }
  @font-face {
    font-family: 'Alibaba PuHuiTi 3.0';
    src: url('/fonts/AlibabaPuHuiTi-3-75-SemiBold.woff2') format('woff2');
    font-weight: 600;
    font-display: swap;
    unicode-range: U+4E00-9FFF, U+3000-303F, U+FF00-FFEF;
  }
  @font-face {
    font-family: 'Alibaba PuHuiTi 3.0';
    src: url('/fonts/AlibabaPuHuiTi-3-85-Bold.woff2') format('woff2');
    font-weight: 700;
    font-display: swap;
    unicode-range: U+4E00-9FFF, U+3000-303F, U+FF00-FFEF;
  }
  ```

  `unicode-range` 限定到 CJK 区段是关键 —— 这样 Latin 字符不会触发下载，避免拖慢首屏。

- **PPTX**: 把 OTF/TTF 嵌入幻灯片（File → Options → Save → ✅ Embed fonts in the file）确保跨机器渲染。Mac PowerPoint 不支持嵌入字体 —— 改用 PDF 分发或要求接收方预装。

### CJK Font Stack

Insert CJK fonts **after** Latin so Latin glyphs render in TWK Everett/Inter and only CJK glyphs fall through to the CJK font:

```
'TWK Everett', 'Inter', 'SF Pro Display',
'Alibaba PuHuiTi 3.0',
'PingFang SC', 'Hiragino Sans GB', 'Noto Sans SC', 'Source Han Sans SC',
'Microsoft YaHei', '微软雅黑',
'Helvetica Neue', 'Arial', sans-serif
```

| Layer | Font | Role |
|---|---|---|
| Primary | Alibaba PuHuiTi 3.0 | 自托管或 CDN 加载，所有平台一致 |
| macOS / iOS fallback | PingFang SC | 普惠体未加载时兜底 |
| Windows fallback | Microsoft YaHei | 普惠体未加载时兜底 |
| Web open-source fallback | Noto Sans SC | Google Fonts 公网兜底 |
| PPTX cross-platform | Alibaba PuHuiTi 3.0（embed）/ Source Han Sans SC | 嵌入字体；不支持嵌入则降级到 Source Han Sans SC |

### CJK-specific Rules

1. **Do NOT apply -4% tracking to Chinese characters.** It causes visual collision (CJK glyphs are designed with built-in side-bearings; tight tracking destroys legibility). Use **-1% to -2%** maximum on CJK headings, and **`normal`** on CJK body.
2. When a heading mixes Chinese and English ("FLock 主权 AI"), let the Latin run keep -4% via per-script CSS:
   ```css
   .flock-h1 {
     letter-spacing: -0.04em;            /* Latin */
     font-feature-settings: "palt";     /* CJK proportional */
   }
   .flock-h1:lang(zh), .flock-h1 :lang(zh) { letter-spacing: -0.01em; }
   ```
3. **Heading sizes for CJK should drop one step** — CJK characters are visually denser than Latin at the same px size. Use H1 56px / H2 42px / H3 32px for Chinese-dominant artifacts. (Or keep PDF sizes if the deck mixes ~50/50.)
4. **Line height bumps**: 110% for CJK H1/H2 (vs 100% Latin), 140% for CJK body (vs 120% Latin). CJK glyphs need more vertical breathing room.
5. **Punctuation**: Chinese uses full-width punctuation `，。：；！？""''` and `——` for em-dash, `……` for ellipsis. Never substitute Latin `,.;:!?` in Chinese sentences.
6. **Bold weight**: TWK Everett doesn't ship a CJK weight. For Chinese bold headings, use Alibaba PuHuiTi 3.0 SemiBold (75) for H2 or Bold (85) for H1. PingFang SC Semibold / Noto Sans SC 700 are acceptable system fallbacks.
7. **Numbers and English in CJK runs** stay in TWK Everett/Inter — don't let them fall through to PingFang.

### CSS Snippet — CJK-aware Heading

```css
.flock-h1 {
  font-family:
    'TWK Everett', 'Inter', 'SF Pro Display',
    'Alibaba PuHuiTi 3.0',
    'PingFang SC', 'Noto Sans SC', 'Source Han Sans SC',
    'Microsoft YaHei', sans-serif;
  font-weight: 700;
  font-size: clamp(2.25rem, 5vw, 4rem);   /* 36–64px responsive */
  line-height: 1.0;
  letter-spacing: -0.04em;
  font-feature-settings: "palt" 1, "ss01" 1;  /* proportional kana, alt set */
}

.flock-h1:lang(zh), :lang(zh).flock-h1 {
  letter-spacing: -0.01em;
  line-height: 1.1;
}
```

---

## CSS Utility Classes (Latin)

```css
.flock-h1 {
  font-family: var(--flock-font-primary);
  font-weight: 700;
  font-size: 64px;
  line-height: 1.0;
  letter-spacing: -0.04em;
}

.flock-h2 {
  font-family: var(--flock-font-primary);
  font-weight: 500;
  font-size: 48px;
  line-height: 1.0;
  letter-spacing: -0.04em;
}

.flock-h3 {
  font-family: var(--flock-font-primary);
  font-weight: 500;
  font-size: 36px;
  line-height: 1.2;
  letter-spacing: -0.03em;
}

.flock-body {
  font-family: var(--flock-font-primary);
  font-weight: 400;
  font-size: 24px;
  line-height: 1.2;
  letter-spacing: -0.03em;
}

.flock-caption { font-size: 14px; line-height: 1.4; letter-spacing: normal; }
.flock-data    { font-family: var(--flock-font-mono); font-size: 12px; line-height: 1.4; }
```

For full token names see `assets/tokens.css`.
