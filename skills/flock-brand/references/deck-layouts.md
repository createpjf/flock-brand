# Deck Layouts

18 个命名版式（10 个咨询风 + 8 个 pitch deck），每个都映射到 FLock 现有的 grid / type / color token 和 PPTX/Slidev 资源。**这个文件回答"用什么版式"，`pptx.md` / `slidev.md` 回答"代码怎么写"**。

---

## 0. 怎么用

- **路由原则**：选一个版式 → 套现有 PPTX master 或 Slidev layout → 用 `tokens.css` 里的 `--flock-*` 变量填字号/颜色/间距。本文档不重述任何数值，全部引用 token 名称。
- **默认 Dark Mode**（Iron Rule #5）；每个版式末尾标 Light Mode 差异。
- **18 个版式不是穷举**，是 FLock 品牌 deck 的最常用骨架。新场景套不上时按 Part III 决策树挑近邻。
- **行为约束**：每页一个 governing thought + action title；数据页必标 source line（caption 字号）。

---

## 1. 通用 Slide Grid

继承 `pptx.md` L42 的 `FLOCK_16_9` 定义（13.333" × 7.5"），叠加 12-column 软网格：

| 元素 | 数值 | 来源 |
|---|---|---|
| 画布 | 16:9 (13.333" × 7.5") | `pptx.md` L42 |
| 列数 | 12 等宽 | 本文档约定 |
| 列宽 | ~1.0in | 派生 |
| Gutter | ~0.08in | 派生 |
| 左右 margin | 0.5in | 派生 |
| Action title baseline | 距顶 0.5in | 本文档约定 |
| Body content baseline | 距顶 1.4in | 本文档约定 |
| Source line baseline | 距底 0.3in | 本文档约定 |
| 元素间距 | 用 `--flock-space-*`（≥ `space-md` = 16px） | `tokens.css` L112–119 |
| 圆角 | 用 `--flock-radius-*`（卡片默认 `radius-lg` = 12px） | `tokens.css` L121–125 |
| FLock badge | 右上固定（content 页必带） | `logo.md` L49–84 |

**12 列分配速查**：
- 半分：6+6（A vs B）
- 三分：4+4+4（三栏对比 / 三 pillar）
- 四分：3+3+3+3（团队四人 / 四象限标签）
- 黄金分：5+7 或 4+8（图右文左 / 数据页）

---

# Part I — 咨询风 10 个版式

每个版式假设 PPTX 用 `FLOCK_CONTENT_DARK` master、Slidev 用 `default` layout，除非另注。

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

# Part II — Pitch Deck 8 个版式

每个版式比咨询风更激进：极低密度、超大字号、留白 30-40%。默认用 `FLOCK_COVER_DARK` 或全屏 layout，大量 Brand Blue 主导。

---

### 11. Hero Stat

**何时用**：单页一个巨大数字 + 1 行 context；TAM、用户数、关键转化率、性能指标。

**结构**：
```
┌────────────────────────────────────────────────┐
│                                                │
│                                                │
│              $2.1B                             │
│       2030 短租 TAM 预测                        │
│                                                │
│                                                │
│                              [logo bottom-left]│
└────────────────────────────────────────────────┘
```

**FLock Grid**：数字+context 居中；上下各留 2in 空白；不带 12 列约束。

**FLock 字号**：数字 **96-144px Bold**（超出现有 type scale，按需定义 inline `font-size: 144px`）；context 行 `--flock-text-h3`（36px Regular）。tracking 收紧到 -5%（数字越大 tracking 越紧）。

**FLock 颜色**：背景 `--flock-black` 或 `--flock-brand-blue`（hero 二选一）；数字 `--flock-white`；context `--flock-white` 70%。

**现有资源**：PPTX `FLOCK_COVER_DARK` master（`pptx.md` L47）；Slidev `cover` layout（`slidev.md` L211），title 字段塞数字、subtitle 塞 context。

**Light mode swap**：背景 `--flock-off-white`；数字 `--flock-brand-blue`；context `--flock-black` 70%。

**Anti-pattern**：数字 + 装饰图标（破坏极简张力）；context 超过 8 字（变成解释而非锚定）；数字字号小于 96px（失去 hero 量级）。

---

### 12. Problem Narrative

**何时用**：pitch deck 第 2 页讲痛点；3 个痛点列表 或 1 个故事图。

**结构**：
```
┌────────────────────────────────────────────────┐
│ HOOK HEADLINE                         [badge] │
│                                                │
│   ❌ AI 模型训练数据被巨头垄断                   │
│                                                │
│   ❌ 中小机构数据散落，价值释放不出来             │
│                                                │
│   ❌ 现有联邦学习方案缺乏激励 + 验证             │
│                                                │
└────────────────────────────────────────────────┘
```

**FLock Grid**：3 个痛点纵向排列；每个痛点行间距 `space-2xl`（48px）；痛点居左对齐，`--flock-orange` ❌ 标记距文字 `space-md`。

**FLock 字号**：标题 `--flock-text-h2`；痛点 `--flock-text-h3`（36px）；不要 bullet point，用 `❌` / `▎` 替代。

**FLock 颜色**：背景 `--flock-black`；标题 `--flock-white`；痛点文字 `--flock-white`；❌ 标记 `--flock-orange`（强调"问题"用次要色，避免抢 Brand Blue 的"解决"角色）。

**现有资源**：PPTX `FLOCK_CONTENT_DARK`；Slidev `default` 简化为 3 行。

**Light mode swap**：背景 `--flock-off-white`；文字 `--flock-black`；❌ 保持 `--flock-orange`。

**Anti-pattern**：超过 3 个痛点（投资人记不住）；用通用 stock photo 配图（FLock 是技术品牌，无图比配差图好）；痛点写成完整段落（应该是 8-12 字短语）。

---

### 13. Solution Diagram（Before/After 或 Workflow）

**何时用**：pitch deck 第 3 页，展示"你解决了什么"；可视化 > 文字描述。

**结构**（Before/After）：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│                                                │
│  Before                          After         │
│  ┌──────────┐         →         ┌──────────┐  │
│  │ 集中训练 │                    │ 联邦协作 │  │
│  │ 数据上传 │                    │ 数据本地 │  │
│  │ 信任风险 │                    │ 加密验证 │  │
│  └──────────┘                    └──────────┘  │
└────────────────────────────────────────────────┘
```

**结构**（Workflow）：用 Process Flow（Part I #7）但只 3 步，每步配 1 个 icon。

**FLock Grid**：Before/After 用 12 列 5+2+5（中间箭头占 2 列）；Workflow 用 4+4+4。

**FLock 字号**：标题 `--flock-text-h2`；卡片标题 `--flock-text-h3`；卡片内 bullet `--flock-text-body`。

**FLock 颜色**：Before 卡片 `--flock-text-on-dark` 30% 描边（"灰暗"语义）；After 卡片 `--flock-brand-blue` 实色 + 白字（"解决"语义）；箭头 `--flock-brand-blue` 4px。

**现有资源**：PPTX `FLOCK_CONTENT_DARK` + `addShape(roundRect)` × 2 + `addShape(line)` 箭头；Slidev `two-cols-header`（`slidev.md` L215）。

**Light mode swap**：Before 卡片 `--flock-text-on-light` 30% 描边；After 卡片保持 Brand Blue 主色。

**Anti-pattern**：Before/After 卡片视觉重量相同（应该 After 抢眼）；用 Brand Blue 在 Before（破坏色彩语义）；workflow 超过 4 步（pitch 节奏太慢）。

---

### 14. Market Size（TAM/SAM/SOM）

**何时用**：pitch deck 第 5 页；市场容量定义 + 你的可获得部分。

**结构**：
```
┌────────────────────────────────────────────────┐
│ ACTION TITLE                          [badge] │
│                                                │
│         ┌────────────────────┐                 │
│         │   TAM  $100B       │                 │
│         │ ┌────────────┐     │                 │
│         │ │ SAM $10B   │     │                 │
│         │ │ ┌──────┐   │     │                 │
│         │ │ │ SOM  │   │     │                 │
│         │ │ │$500M │   │     │                 │
│         │ │ └──────┘   │     │                 │
│         │ └────────────┘     │                 │
│         └────────────────────┘                 │
└────────────────────────────────────────────────┘
                                Source: ...
```

**FLock Grid**：同心圆居中占 6 列；外圆直径 ~5in；圆心对齐画布水平中线。每环标 $ + 1 句话上下文。

**FLock 字号**：标题 `--flock-text-h2`；环上数字 `--flock-text-h3` Bold；环上下文 `--flock-text-caption`。

**FLock 颜色**：TAM 环 `--flock-brand-blue` 30% 不透明；SAM 环 `--flock-brand-blue` 60%；SOM 环 `--flock-brand-blue` 实色（颜色饱和度 = 业务可触达度）。文字反白。

**现有资源**：PPTX 用 `addShape(ellipse)` × 3 同心；Slidev 用 SVG 内联 `<circle>` × 3。

**Light mode swap**：环颜色递进 `--flock-tint-blue` → `#98B8F8` 60% → `--flock-brand-blue` 实色；文字在外两环用 `--flock-black`，最内 SOM 环用白。

**Anti-pattern**：TAM 写"$500B 因为人们花钱"（投资人立刻识破）；同心圆比例失真（应反映真实倍数）；缺数字旁的 source line 来源。

---

### 15. Traction（"上和向右"折线）

**何时用**：pitch deck 中段，展示用户/收入/订单/留存的真实增长 + 拐点叙事。

**结构**：参考 Part I #5 Time-Series with Annotation Arrows，但更简化、更激进。

**FLock Grid**：图表占满 10 列（左右各 1 列留白）；2-3 个拐点标注内置，不出 chart 外。

**FLock 字号**：标题 `--flock-text-h2`；曲线终点数字 `--flock-text-h1`（64px Bold，强调"现在"）；轴标签 `--flock-text-caption`；拐点标注 `--flock-text-body`。

**FLock 颜色**：曲线 `--flock-brand-blue` 3px 描边（比 Part I #5 更粗，pitch 视觉冲击优先）；最后数据点 8px 圆 + 2px 白描边；轴线 `--flock-text-on-dark` 30%。

**现有资源**：Slidev `default` + ECharts（`slidev.md` L256–266 已有 brand 主题）；PPTX `addChart({ type: 'line' })`。

**Light mode swap**：曲线保持 Brand Blue；终点圆 `--flock-brand-blue` + 2px 黑描边。

**Anti-pattern**：纯 hockey stick（投资人警觉）；折线 ≥ 3 条（pitch 简化原则）；X 轴粒度太粗（季度而非月，藏住真实增长）。

---

### 16. Competition Matrix 2×2

**何时用**：pitch deck 第 6 页；竞争定位，你在空白象限。

引用 Part I #3 的完整结构 + token 映射。**Pitch 语境差异**：

- **更大、更全屏**：矩阵占 10 列（vs 咨询风 8 列），上下留白更多
- **不带象限名**（不写 Star/Cash Cow），只放公司 logo 散点
- **你的 logo** 用 `--flock-brand-blue` 高亮 + 12px 圆环；竞争对手 logo 用灰阶
- **两条轴标签**用更醒目的 `--flock-text-h3`（vs 咨询风 caption）

**Anti-pattern (Pitch-specific)**：声称"无竞品"（投资人解读为没做调研）；轴选错（应该是你的优势维度，如"federated + native incentive"）；超过 5 个对手 logo（视觉嘈杂）。

---

### 17. Team Grid

**何时用**：pitch deck 第 9 页；团队 photo + 1 行可信凭证。

**结构**：
```
┌────────────────────────────────────────────────┐
│ TEAM                                  [badge] │
│ ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐       │
│ │ photo│  │ photo│  │ photo│  │ photo│       │
│ │      │  │      │  │      │  │      │       │
│ └──────┘  └──────┘  └──────┘  └──────┘       │
│ Name      Name      Name      Name             │
│ Title     Title     Title     Title            │
│ ex-X      ex-Y      ex-Z      ex-W             │
└────────────────────────────────────────────────┘
```

**FLock Grid**：12 列 3+3+3+3（最多 4 人/页）；photo 卡片正方形 ~2.5in × 2.5in，`--flock-radius-md` 圆角。

**FLock 字号**：标题 `--flock-text-h2`；姓名 `--flock-text-h3`；title `--flock-text-body`；凭证 `--flock-text-caption`。

**FLock 颜色**：photo 用 **halftone 蓝双色调**处理（`infographics.md` § Imagery：shadow → `--flock-brand-blue`，highlight → `#98B8F8`）；卡片背景 `--flock-black`；姓名 `--flock-white`；title `--flock-white` 70%；凭证 `--flock-brand-blue`。

**现有资源**：Slidev `image-right` + 4-人 grid 自定义（`slidev.md` L220 提到 halftone 处理）；PPTX `addImage` × 4 + 文字。photo 处理需预先在 Photoshop / sharp-cli 转 duotone。

**Light mode swap**：背景 `--flock-off-white`；姓名 `--flock-black`；保持 halftone 蓝双色调。

**Anti-pattern**：≥ 5 人/页（应该是创始团队，不是公司花名册）；用 avatar 而不是真实头像（失去人性信任）；凭证写"哈佛毕业"等无差异内容（应是"前 OpenAI 研究员"等可验证项）。

---

### 18. Product Screenshots（全屏 + 设备框）

**何时用**：pitch deck 第 7 页；让产品本身说话。

**结构**：
```
┌────────────────────────────────────────────────┐
│                                                │
│         ┌────────────────────────┐             │
│         │   [iPhone / MacBook]   │             │
│         │   产品截图 1            │             │
│         │                        │             │
│         └────────────────────────┘             │
│                                                │
│         产品 tagline （可选，≤ 8 字）            │
└────────────────────────────────────────────────┘
```

**FLock Grid**：截图占 8-10 列居中；设备框 mockup 必带（iPhone 15 / MacBook Pro 真实设备框，不用通用矩形）；上下各留 1.5in。

**FLock 字号**：可选 tagline 用 `--flock-text-h3`；不需要标题（产品自身是标题）。

**FLock 颜色**：背景 `--flock-black`（让截图鲜艳跳出）；不加任何 overlay 或装饰。

**现有资源**：PPTX `addImage`（设备框 mockup 预置在 `assets/devices/` —— 当前未实施，需用户自备）；Slidev 用 `<img>` 直接嵌。

**Light mode swap**：背景 `--flock-off-white`（截图深色 UI 时反差好）；保持设备框真实色。

**Anti-pattern**：通用矩形包截图（廉价感）；多张小截图拼贴（应该 1 张大图 / 页，多功能用 carousel 多页）；加大段说明文字（pitch 模式让视觉说话）。

---

# Part III — Pattern 选择决策树

| 你想表达什么 | 推荐版式 |
|---|---|
| 介绍一个数据点 / 关键指标 | **#11 Hero Stat** |
| 比较 2 个方案 | **#8 Side-by-Side** |
| 比较 3 个方案 / 三个产品线 | **#2 Three-Column Comparison** |
| 比较 4 个项 + 二维矩阵 | **#3 2×2 Matrix** |
| 比较 ≥ 5 个项 | 拆成多页或用 #2 + #3 组合 |
| 分解一个变化的因果 | **#4 Waterfall** |
| 展示时间趋势 + 关键节点 | **#5 Time-Series with Annotation** / **#15 Traction** |
| 拆解目标到可执行杠杆 | **#6 Value Driver Tree** |
| 展示步骤 / 流程 | **#7 Process Flow** |
| 引用客户 / 专家声音 | **#9 Quote / Case Study** |
| 章节切换 | **#10 Section Divider** |
| 开篇 / 高管摘要 | **#1 Executive Summary** |
| Pitch 痛点叙事 | **#12 Problem Narrative** |
| Pitch 解决方案 | **#13 Solution Diagram** |
| Pitch 市场机会 | **#14 Market Size** |
| Pitch 竞争定位 | **#16 Competition Matrix** |
| Pitch 团队 | **#17 Team Grid** |
| Pitch 产品演示 | **#18 Product Screenshots** |

**速选规则**：内容是"分析说服" → Part I 优先；内容是"投资 / 招募 / 公关" → Part II 优先。

---

# Part IV — Pre-flight (deck-layouts-specific)

合并到 SKILL.md 主 pre-flight 之外，跑 deck 时额外检查：

- [ ] 每页只有一个 governing thought（覆盖整 deck 的"主论点"）
- [ ] 每页标题是 action title，不是 topic title
- [ ] 锁定三条 baseline（action title 0.5in / body 1.4in / source 0.3in 距底）
- [ ] FLock badge 在右上（content 页），section / cover / hero stat 不带
- [ ] 数据页标 source line（caption 字号，14px）
- [ ] 用了正确的 pillar 色（Sovereign Blue / Operations Turquoise / Gateway Purple），不滥用
- [ ] 咨询风 deck：单页可至 200 字密度
- [ ] Pitch deck：单页 ≤ 30 字
- [ ] Hero Stat 数字 ≥ 96px
- [ ] 团队头像用 halftone 蓝双色调，不用彩色原图
- [ ] 用 12 列 grid 软对齐（4+4+4 / 6+6 / 5+7 等标准分割）
- [ ] section divider 不带内容元素（保持节奏作用）
- [ ] 颜色全部从 `tokens.css` 取，不写裸 hex

---

## 路径速查（这 18 个版式映射到的资源）

| 资源 | 提供 | 引用最频繁的版式 |
|---|---|---|
| `references/typography.md` | Type scale token | 全部 18 个 |
| `references/colors.md` §2.1 | Pillar 色 + tints | #2, #6, #14, #16 |
| `references/pptx.md` L42–177 | 4 个 master + 16:9 | 全部 PPTX 输出 |
| `references/slidev.md` L205–266 | 8 个 layout + Mermaid/ECharts | 全部 Slidev 输出 |
| `references/infographics.md` § Diagrams / Imagery | 节点样式 / halftone | #5, #6, #7, #15, #17 |
| `references/logo.md` L49–84 | FLock badge | 全部 content 页 |
| `assets/tokens.css` | space / radius / type 变量 | 全部 18 个 |
