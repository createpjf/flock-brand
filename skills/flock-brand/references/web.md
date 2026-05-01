# Web — HTML / React / Tailwind

For any web/HTML/React deliverable: landing page, web app, interactive demo, embed.

> Load only when the task touches HTML/CSS/React/Tailwind. For slide decks, prefer `slidev.md`.

---

## Quick start — drop-in CSS

```html
<link rel="stylesheet" href="./flock-brand/assets/tokens.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&display=swap">
```

That gives you all `--flock-*` variables. Use them directly in your CSS.

---

## Tailwind preset

```js
// tailwind.config.js
const flock = require('./flock-brand/assets/tailwind.preset.js');
module.exports = {
  presets: [flock],
  content: ['./src/**/*.{js,jsx,ts,tsx,vue}'],
};
```

Then in components:

```jsx
<div className="bg-flock-black text-white font-flock">
  <h1 className="text-flock-h1 text-flock-blue">Real AI. Real Impact.</h1>
  <p className="text-flock-body">Sovereign · Compliant · Integrated · Research-backed</p>
</div>
```

---

## Page structure

### Dark mode (default)

```html
<body class="bg-flock-black text-white font-flock min-h-screen">
  <header class="px-6 py-4 flex justify-between items-center">
    <img src="/flock-mark-white.svg" alt="FLock" height="32">
    <nav class="flex gap-6"><!-- ... --></nav>
  </header>
  <main class="px-6 max-w-6xl mx-auto"><!-- ... --></main>
</body>
```

### Light mode

```html
<body class="bg-[#F2F2F2] text-flock-black font-flock min-h-screen">
  <main class="px-6 max-w-6xl mx-auto py-12">
    <div class="bg-white border border-flock-border rounded-flock-lg p-6">
      <h2 class="text-flock-h2 text-flock-blue">Why FLock</h2>
      <p class="text-flock-body mt-4">…</p>
    </div>
  </main>
</body>
```

---

## Hero section

```jsx
function FlockHero() {
  return (
    <section className="bg-flock-blue text-white py-32">
      <div className="max-w-6xl mx-auto px-6">
        <h1 className="text-[64px] leading-none tracking-flock-tight font-bold">
          Real AI. Real Impact.
        </h1>
        <p className="text-[24px] mt-8 tracking-flock-normal opacity-90">
          Sovereign · Compliant · Integrated · Research-backed
        </p>
        <button className="mt-12 bg-white text-flock-blue px-6 py-3 rounded-flock-md
                           font-medium tracking-flock-normal">
          Get Started
        </button>
      </div>
    </section>
  );
}
```

---

## Three-pillar grid (signature layout)

```jsx
const PILLARS = [
  { num: '01', name: 'Sovereign AI', color: '#3773FF', tint: '#98B8F8',
    desc: 'Federated learning for regulated data' },
  { num: '02', name: 'Operations',   color: '#03BFD4', tint: '#B8E8F0',
    desc: 'Compliance-grade audit trail and orchestration' },
  { num: '03', name: 'Gateway',      color: '#9C59F3', tint: '#D0B8F8',
    desc: 'Sovereign model deployment and access control' },
];

function PillarGrid() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {PILLARS.map(p => (
        <div key={p.num}
             className="bg-white border border-flock-border rounded-flock-lg p-6">
          <div className="text-[12px] font-mono" style={{ color: p.color }}>{p.num}</div>
          <h3 className="text-flock-h3 mt-2" style={{ color: p.color }}>{p.name}</h3>
          <p className="text-flock-body mt-4 text-flock-black">{p.desc}</p>
        </div>
      ))}
    </div>
  );
}
```

---

## Subtle brand grid texture

```css
.flock-grid-bg {
  position: relative;
}
.flock-grid-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--flock-border) 1px, transparent 1px),
    linear-gradient(90deg, var(--flock-border) 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.06;
  pointer-events: none;
  z-index: 0;
}
.flock-grid-bg > * { position: relative; z-index: 1; }
```

---

## Buttons

```css
.flock-btn-primary {
  background: var(--flock-brand-blue);
  color: #FFFFFF;
  padding: 12px 24px;
  border-radius: var(--flock-radius-md);
  font-family: var(--flock-font-primary);
  font-weight: 500;
  font-size: 16px;
  letter-spacing: -0.02em;
  transition: filter 0.15s ease;
}
.flock-btn-primary:hover { filter: brightness(1.08); }

.flock-btn-secondary {
  background: transparent;
  color: var(--flock-brand-blue);
  border: 1px solid var(--flock-brand-blue);
  /* … */
}
```

---

## Cards

```css
.flock-card {
  background: #FFFFFF;
  border: 1px solid var(--flock-border);
  border-radius: 12px;
  padding: 24px;
}
/* dark mode card variant */
.flock-card-dark {
  background: #0A0A0A;
  border: 1px solid #1A1A1A;
}
```

---

## CJK content rule

Always set `lang="zh"` on Chinese sections so the CSS in `typography.md` can downgrade tracking automatically:

```html
<section lang="zh">
  <h1>主权 AI</h1>
  <p>面向受监管数据的联邦学习</p>
</section>
```

`lang="zh"` is required — otherwise the default `-4%` tracking will mash Chinese characters.

---

## Forbidden patterns

- ❌ `bg-blue-500`, `bg-blue-600`, or any other Tailwind blue (only `bg-flock-blue` / `#3773FF`)
- ❌ `bg-white` as the page background — use `bg-[#F2F2F2]` (Off White)
- ❌ Default Tailwind `font-sans` — use `font-flock`
- ❌ Default tracking on headings — always `tracking-flock-tight` (-4%) or `tracking-flock-normal` (-3%)
- ❌ Pure black `#000` text on Off White — body is fine in `#000`, but headings on Off White should be Brand Blue
