# Deck Layouts · Part I — 咨询风 10 版式（#1–#10）

> 由 `deck-layouts.md` 路由至此。前置:已读路由文件的 §0–3(grid / 主轴 / 不对称技法)并用决策树选好版式编号。
> 每个版式假设 PPTX 用 `FLOCK_CONTENT_DARK` master、Slidev 用 `default` layout,除非另注。

---

### 1. Executive Summary / One-Pager

**何时用**：把 30+ 页分析压成 1-2 页给高管看；deck 开篇定锚。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE （H2 横跨 12 列）         [badge] │
├────────────┬──────────────┬────────────────────┤
│ 关键洞察    │ 决策张力      │ 含义 & 下一步       │
│ (4 col)    │ (4 col)      │ (4 col)            │
│ • bullet 1 │  [小图/2×2]   │ • bullet 1         │
│ • bullet 2 │              │ • bullet 2         │
│ • bullet 3 │              │ • bullet 3         │
└────────────┴──────────────┴────────────────────┘
                                Source: ...
```

**FLock Grid**：12 列 4+4+4，每栏内边距 `space-md`，三栏共享 body baseline。

**FLock 字号**：标题 `--flock-text-h2`（48px Medium）；三栏小标题 `--flock-text-h3`（36px Medium）；bullet body `--flock-text-body`（24px Regular）。

**FLock 颜色**：背景 `--flock-black`，文字 `--flock-white`，三栏小标题 `--flock-brand-blue` 或对应 pillar 色（见 `colors.md` §2.1）。

**现有资源**：PPTX `FLOCK_CONTENT_DARK`（`pptx.md` L61）；Slidev `default` + 自定义 grid。

**Light mode swap**：背景 → `--flock-off-white`，body → `--flock-black`，小标题 → `--flock-brand-blue`，用 `FLOCK_CONTENT_LIGHT` master（`pptx.md` L147）。

**Anti-pattern**：三栏字号不一致；中栏放大段文字而不是张力可视化（应该是 2×2 或小图）。

---

### 2. Three-Column Comparison

**何时用**：评估 3 个方案 / 3 个产品线（恰好对应 Sovereign / Operations / Gateway）/ 3 阶段对比。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
├──────────────┬──────────────┬─────────────────┤
│ Option A     │ Option B     │ Option C        │
│ Cost: $X     │ Cost: $Y     │ Cost: $Z        │
│ Time: ...    │ Time: ...    │ Time: ...       │
│ Risk: HIGH   │ Risk: LOW    │ Risk: MED       │
│ ✓ pro 1     │ ✓ pro 1     │ ✓ pro 1        │
│ ✗ con 1     │ ✗ con 1     │ ✗ con 1        │
└──────────────┴──────────────┴─────────────────┘
                                Source: ...
```

**FLock Grid**：12 列 4+4+4，列间细分隔线（1px `--flock-text-on-dark` at 20% opacity）。每列内顶部用 `--flock-radius-lg` 圆角卡片或纯文字。

**FLock 字号**：标题 `--flock-text-h2`；列标题 `--flock-text-h3`；指标行 `--flock-text-body`；pro/con `--flock-text-caption`。

**FLock 颜色**：当三栏对应 3 个产品 pillar，用 `colors.md` §2.1 的 pillar 色给列标题着色（Sovereign Blue / Operations Turquoise / Gateway Purple）。否则统一 `--flock-white`。

**现有资源**：PPTX `FLOCK_CONTENT_DARK`；Slidev `default` + 3-col grid（参考 `slidev.md` L216 三-pillar 模式）。

**Light mode swap**：列卡片用 `--flock-white` 背景 + `--flock-radius-lg` + 1px 边框（参考 `colors.md` §2.2 surface tokens）。

**Anti-pattern**：每栏指标数量不齐；用 emoji 替代 ✓/✗；三栏选三个不同 pillar 色但内容跟产品线无关（违反 pillar 色语义）。

---

### 3. 2×2 Matrix

**何时用**：两个独立维度交叉（市场 × 利润 / 难度 × 价值 / 风险 × 回报）；BCG-style 战略定位。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│              ↑ Y轴标签 (高)                    │
│       ┌──────────┬──────────┐                 │
│       │  Star    │ Question │  ← 象限名       │
│  高Y  │ (Invest) │ (Monitor)│                 │
│       ├──────────┼──────────┤                 │
│       │ Cash Cow │   Dog    │                 │
│  低Y  │(Optimize)│ (Divest) │                 │
│       └──────────┴──────────┘                 │
│         低X        高X      → X轴标签           │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：矩阵居中占 8 列（左右各留 2 列）；轴标签**外置**在矩阵外侧。每象限边长 ~2.5in，用 `space-sm` 内边距。

**FLock 字号**：标题 `--flock-text-h2`；象限名 `--flock-text-h3`；象限副标 `--flock-text-body`；轴标签 `--flock-text-caption`。

**FLock 颜色**：象限格用 `--flock-text-on-dark` 10% 不透明描边；推荐象限填 `--flock-brand-blue` 20% 不透明背景做高亮，其余三个保持透明。

**现有资源**：PPTX 自绘（无 master 预置；用 `addShape(rect)` × 4 + `addText` × 4 + 2 条轴线）。Slidev `default` + 自定义 CSS grid 2×2。

**Light mode swap**：象限边线用 `--flock-text-on-light` 20%；高亮象限填 `--flock-tint-blue`（`colors.md` §2.1）。

**Anti-pattern**：标题不在矩阵上方而塞进象限内；4 个象限都填色（推荐象限失去对比）；坐标轴方向不一致（X 应永远从左低到右高）。

---

### 4. Waterfall

**何时用**：把"总变化"分解成各驱动因素的累计贡献（收入差异 / 成本下降 / 利润变动）。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│  $50M ┐                                       │
│       │  ┐  +6                                │
│       │  │  ┐ -18  ┐                          │
│       │  │  │      │ -2  ┐                    │
│       │  │  │      │     │ → $32M             │
│  Base Pri Vol     Mix     End                 │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：图表占 10 列居中；左右各 1 列留白；每个 bar 等宽，bar 间距 `space-sm`。

**FLock 字号**：标题 `--flock-text-h2`；bar 上方数值 `--flock-text-body`；bar 下方标签 `--flock-text-caption`；source `--flock-text-caption`。

**FLock 颜色**：起止柱用 `--flock-brand-blue`；正贡献用 `--flock-turquoise`；负贡献用 `--flock-orange`；连接虚线 `--flock-text-on-dark` 30%。

**现有资源**：PPTX 用 PptxGenJS `addChart({ type: 'bar', ... })` 但需要手算 base+offset；推荐改用 Mermaid + Slidev（`slidev.md` L226–266 的 ECharts 配置可改成 waterfall）。

**Light mode swap**：保持品牌色不变（waterfall 颜色编码语义 > 模式），仅背景换 `--flock-off-white`、文字换 `--flock-black`。

**Anti-pattern**：正负贡献用同色（破坏分解可读性）；连接线缺失（眼睛追不到累计逻辑）；超过 7 个驱动因素一页（拆成两页或聚类）。

---

### 5. Time-Series with Annotation Arrows

**何时用**：时间趋势 + 关键节点的因果叙事（产品上线 / 市场事件 / 干预措施的影响）。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│ 100 ┐                  ↗ Q2 重定位             │
│  80 │              ╱─                          │
│  60 │           ╱                              │
│  40 │_____╱                                    │
│  20 │                                          │
│     └──────────────────────                    │
│     Q1  Q2  Q3  Q4  Q1  Q2                    │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：图表占 8-10 列；标注文字/箭头出在 chart **外**右侧 2-4 列空白处，用 `space-md` 与图表分隔。

**FLock 字号**：标题 `--flock-text-h2`；轴标签 `--flock-text-caption`；标注 `--flock-text-body`。

**FLock 颜色**：主曲线用 `--flock-brand-blue`，2.5px 描边；高亮节点圆点 `--flock-brand-blue` 6px + 1px `--flock-white` 描边；标注箭头 `--flock-text-on-dark`；网格线 30% 不透明。详细 chart 规则见 `infographics.md` § Chart-Type Rules。

**现有资源**：Slidev `default` + ECharts；PPTX 用 `addChart({ type: 'line' })` + `addShape(line)` 画注释箭头。

**Light mode swap**：曲线保持 Brand Blue；网格线换 `--flock-off-brand-border` 等价值；标注文字 `--flock-black`。

**Anti-pattern**：标注塞进 chart 内部覆盖数据；折线超过 3 条（用 small multiples）；没有节点标注（这版式失去叙事意义）。

---

### 6. Value Driver Tree / Hypothesis Tree

**何时用**：把目标分解成可执行杠杆（25% EBITDA → 收入增长 / 成本下降 / OpEx 优化）；展示逻辑依赖。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│                  ┌──────────┐                  │
│                  │  Goal    │                  │
│                  └────┬─────┘                  │
│           ┌───────────┼───────────┐            │
│      ┌────┴───┐  ┌────┴───┐  ┌────┴───┐       │
│      │ Lever1 │  │ Lever2 │  │ Lever3 │       │
│      │ +4pp   │  │ -3pp   │  │ -2pp   │       │
│      └────────┘  └────────┘  └────────┘       │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：根节点居中（横跨 4 列），子节点扇出；树深 ≤ 3 层（再深拆页）；节点用 `--flock-radius-md` 圆角矩形。

**FLock 字号**：标题 `--flock-text-h2`；根节点 `--flock-text-h3`；子节点名 `--flock-text-body`；子节点指标 `--flock-text-caption`。

**FLock 颜色**：节点边框 `--flock-brand-blue` 1.5px，填充 `--flock-black` 或透明；连接线 `--flock-text-on-dark` 50%；根节点可填 `--flock-brand-blue` 实色 + 白字突出。详细规则见 `infographics.md` § Diagrams。

**现有资源**：Slidev `default` + Mermaid `graph TD`（参考 `slidev.md` L226–249）；PPTX 用 `addShape(roundRect)` + `addShape(line)` 手绘。

**Light mode swap**：节点描边 `--flock-brand-blue`；填充 `--flock-white`；根节点保持 `--flock-brand-blue` 实色 + 白字。

**Anti-pattern**：树超过 3 层（视觉密度爆掉）；子节点没标贡献量（树失去定量意义）；节点形状不一致（圆角与方角混用）。

---

### 7. Process Flow（左到右）

**何时用**：步骤序列 / 客户旅程 / 决策过程；显示阶段时长或负责方。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│ Stage 1 → Stage 2 → Stage 3 → Stage 4         │
│ ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐           │
│ │ Doc │→ │Check│→ │Setup│→ │Train│           │
│ │10d  │  │ 7d  │  │ 5d  │  │ 5d  │           │
│ └─────┘  └─────┘  └─────┘  └─────┘           │
│                                               │
│ 注：Check 与 Setup 可并行，节省 7 天           │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：4-5 个等宽阶段格（12 列 / N 个阶段，加 gutter）；阶段名在格上，时长/owner 在格内/下；箭头 `space-sm` 间距。

**FLock 字号**：标题 `--flock-text-h2`；阶段名 `--flock-text-body`；时长/owner `--flock-text-caption`。

**FLock 颜色**：节点边框/填充按 `infographics.md` § Diagrams 规则；高亮路径（如关键路径）用 `--flock-brand-blue` 2.5px 描边，非关键路径 `--flock-text-on-dark` 50%。

**现有资源**：Slidev `default` + Mermaid `graph LR`（参考 `slidev.md` L217 process/flow 模式）。

**Light mode swap**：节点白底 + Brand Blue 描边；连接 `--flock-off-brand-border`。

**Anti-pattern**：超过 7 个阶段（主线断了）；箭头方向不统一（有的下、有的右）；并行用斜线表达而不是空间分支。

---

### 8. Side-by-Side Data + Chart

**何时用**：左侧 3-4 个关键指标，右侧 1 个支持图表；快速对比"事实"和"图形证据"。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
├──────────────┬─────────────────────────────────┤
│ ▎ 指标 1: $X │                                 │
│ ▎ 指标 2: Y% │       [Chart 区域]              │
│ ▎ 指标 3: ↑Z │                                 │
│ ▎ 指标 4: ✓  │                                 │
└──────────────┴─────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：12 列 4+8 或 5+7；左侧指标用 `--flock-brand-blue` 2px 左竖线（▎符号位置）做强调；图表占 8 列右侧。

**FLock 字号**：标题 `--flock-text-h2`；左侧指标 `--flock-text-h3` Medium（数字醒目）；指标说明 `--flock-text-caption`。

**FLock 颜色**：指标数字 `--flock-brand-blue` 或对应 pillar 色；指标说明 `--flock-white` 70% 不透明。

**现有资源**：Slidev `default` + 自定义 CSS grid 4+8；PPTX 用 `addText` × N + `addChart` × 1。

**Light mode swap**：左侧竖线和数字保持 Brand Blue；说明文字 `--flock-black` 70%。

**Anti-pattern**：左侧超过 4 个指标（变成清单）；图表与指标无关（破坏 side-by-side 因果）；数字字号小于 H3（核心指标失去视觉重量）。

---

### 9. Quote / Case Study Card

**何时用**：用真实客户/专家声音锚定一个论点；引用研究 / NeurIPS 论文 / 联盟成员证言。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│                                                │
│   ┌──────────────────────────────────────┐    │
│   │  " ... 这套联邦学习框架让我们模型      │    │
│   │     训练效率提升 3×。"                │    │
│   │                                       │    │
│   │  — Researcher, Top-3 Conference      │    │
│   │     (FLock 联盟成员，2024)            │    │
│   └──────────────────────────────────────┘    │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：引言框居中（占 8 列）或左偏（占 5 列）；卡片用 `--flock-radius-lg` 圆角；内边距 `space-xl`（32px）。

**FLock 字号**：标题 `--flock-text-h2`；引言 `--flock-text-h3` Regular（不要 Bold，让引语本身呼吸）；署名 `--flock-text-body`；身份补注 `--flock-text-caption`。

**FLock 颜色**：卡片背景 `--flock-brand-blue` 10% 不透明；引号符号 `--flock-brand-blue`；引文 `--flock-white`；署名 `--flock-white` 70%。

**现有资源**：Slidev `statement` layout（`slidev.md` L214）+ 缩短居中；PPTX `FLOCK_CONTENT_DARK` + `addShape(roundRect)` + `addText`。

**Light mode swap**：卡片背景 `--flock-tint-blue`（`colors.md` §2.1）；引文 `--flock-black`；署名 `--flock-black` 70%。

**Anti-pattern**：引言超过 30 字（这版式失去冲击力）；引言加 Bold（破坏 statement 的克制感）；署名匿名"某客户"（失去可信度）。

---

### 10. Section Divider

**何时用**：标记主章节切换（Situation → Analysis → Recommendations）；deck 节奏控制。

**结构**：
```
┌────────────────────────────────────────────────┐
│                                                │
│             02                                 │
│             ──────                             │
│             Analysis                           │
│             理解核心驱动                        │
│                                                │
└────────────────────────────────────────────────┘
```

**FLock Grid**：全宽（无 12 列约束，居中或左对齐）；大数字水印占左下 1/3 区域；标题/副标在数字右侧或下方。

**FLock 字号**：章节编号 96-144px Bold（超出 H1）；章节名 `--flock-text-h1`（64px）；副标 `--flock-text-h3`（36px）。

**FLock 颜色**：背景 `--flock-black`；编号 `--flock-brand-blue` 30% 不透明（水印感）；章节名 `--flock-white`；副标 `--flock-white` 60%。

**现有资源**：PPTX `FLOCK_SECTION_DARK` master（`pptx.md` L80，已含大水印数字）；Slidev `section` layout（`slidev.md` L213）。

**Light mode swap**：背景 `--flock-off-white`；编号 `--flock-brand-blue` 20%；章节名 `--flock-brand-blue`；副标 `--flock-black` 60%。

**Anti-pattern**：section 页加内容（破坏节奏作用）；FLock badge 出现在 section 页（专属 content 页元素）；编号字号小于 96px（水印感失效）。

---
