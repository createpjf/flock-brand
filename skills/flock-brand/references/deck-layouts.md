# Deck Layouts

**路由文件** — 共用规则（grid / 主轴 / 不对称技法）+ 18 版式决策树。版式正文已拆分:咨询风 #1–10 → `deck-layouts-consulting.md`,pitch #11–18 → `deck-layouts-pitch.md`,按需加载。**本文件回答"用什么版式",Part 文件给结构图,`pptx.md` / `slidev.md` 回答"代码怎么写"**。

---

## 0. 怎么用

- **路由原则**：选一个版式 → 套现有 PPTX master 或 Slidev layout → 用 `tokens.css` 里的 `--flock-*` 变量填字号/颜色/间距。本文档不重述任何数值，全部引用 token 名称。
- **选版式前先定主轴**（见 §2）：每页有明确视觉重心，居中只留给 hero 页。
- **默认 Dark Mode**（Iron Rule #5）；每个版式末尾标 Light Mode 差异。
- **18 个版式不是穷举**，是 FLock 品牌 deck 的最常用骨架。新场景套不上时按 Part III 决策树挑近邻。
- **规整骨架 ≠ 呆板**：多页版式相近时，用 §3 的不对称技法拉开差异。
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

## 2. 页面主轴 — 选版式前先定的事

每一页 deck 必须有一个**视觉主轴**，即这一页的重心偏向哪里。居中是默认值，不是选择——**居中只留给 cover / section divider / closing CTA 三类 hero 页**，content 页全部居中 = 最典型的 AI 套路感。

选版式前，先按内容定主轴：

| 主轴 | 长啥样 | 适合 | 典型版式 |
|---|---|---|---|
| **左偏** | 标题 + 正文靠左，图 / 数据靠右 | 大多数 content 页的默认 | #1, #8, #12, #13, #18 |
| **右偏** | 视觉元素靠左，结论 / 标题靠右 | 想让"图先说话、文字收尾" | #5, #15 变体 |
| **上重** | 大标题 / 大数字压在顶部，支撑信息在下 | 数据页、断言页 | #11, #14 |
| **下沉** | 内容上方留白，标题 / 结论锚在底部 | 章节切换、悬念收束 | #10, #12 变体 |
| **居中** | 标题 + 正文 + CTA 都居中 | **仅** cover / section divider / closing CTA | Cover, #10, Closing |

**用法**：在节奏表（narrative.md §3b）里，除了写每页的 mode 和版式编号，再加一列「主轴」。一份 deck 里如果每页主轴都是「居中」或都是「左偏」，视觉就会发闷——主轴本身也要有节奏变化。

**不对称读起来像「有意」，对称读起来像「生成的」**。拿不准时，往一侧偏。

---

## 3. 不对称技法 + 间距纪律

18 个版式是规整骨架，但规整 ≠ 呆板。在骨架之上用下面的技法制造「有意设计」的观感，尤其当一份 deck 里多页版式相近时，靠这些手法拉开差异。

### 3.1 不对称技法（4 种，按页选用）

| 技法 | 做法 | 注意 |
|---|---|---|
| **宽左留白** | 窄标签列（kicker / 编号 / 日期）+ 宽内容区。标签列约占 2–3 列，内容占 9–10 列 | 标签列只放微标签，不要把 action title 整个塞进窄列 |
| **元素越界** | 一个元素故意越出常规安全区——超大数字、出血图片、横贯的细线。一页只用一次 | 越界元素不能压住 action title 或 source line |
| **非均分 span** | 12 列里用 7+5、8+4，而不是永远 6+6。偶数列比奇数列宽，或反过来 | 黄金分（5+7 / 4+8）已是常用，刻意时可更极端 |
| **上松下紧** | body 区上方留白多、下方紧凑（或反过来），不必上下均匀 | baseline（action title 0.5in / source 0.3in）仍然锁死 |

### 3.2 间距纪律

FLock `tokens.css` 已有 9 级 `--flock-space-*`。补一条硬规则：

**同一页至少混用 2 档间距。** 如果一页里所有 gap 都是同一个值（例如全 `space-lg` = 24px），这页就是模板感。区块间用大间距（`space-xl` / `space-2xl`），区块内元素用中小间距（`space-sm` / `space-md`）——间距差本身就是层级。

- 卡片内边距 ≠ 区块间距 ≠ 页面 margin，三者相等 = 节奏发平
- 永远用 `--flock-space-*` token，不写裸 px

### 3.3 「这页看着平」急救清单

某页代码没错但视觉发闷时，交付前做其中一条：

1. 加一个越界元素（大数字 / 出血图 / 横线）
2. 把某一列拉宽，打破 6+6
3. 把主 CTA / 关键数字移出正中
4. 删掉一个次要卡片，换成留白
5. 改某个区块的间距，让上下节奏不均匀

---


---

# 版式详情 — 按需加载(本文件不含 18 个版式正文)

决策树(下方 Part III)选好编号后,只读对应 Part 文件:

| 编号 | 文件 | 内容 |
|---|---|---|
| #1–#10 咨询风 | `deck-layouts-consulting.md` | Executive Summary / Three-Column / 2×2 / Waterfall / Time-Series / Driver Tree / Process Flow / Side-by-Side / Quote / Section Divider |
| #11–#18 Pitch | `deck-layouts-pitch.md` | Hero Stat / Problem / Solution / Market / Traction / Competition / Team / Screenshots |

一份 deck 通常只命中一个 Part(叙事弧 A→consulting,弧 B/C→pitch)。混用时才两个都读。

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
- [ ] 每页有明确主轴；居中只用于 cover / section divider / closing CTA
- [ ] 整 deck 主轴有节奏变化，不是每页都左偏或都居中
- [ ] 同一页混用 ≥ 2 档 `--flock-space-*` 间距，没有全页等距
- [ ] 多列布局用过非均分 span（7+5 / 8+4），不是永远 6+6
- [ ] 左文右图：左列 `space-between`，右列顶对齐
- [ ] FLock badge 在右上（content 页），section / cover / hero stat 不带
- [ ] 数据页标 source line（caption 字号，14px）
- [ ] 用了正确的 pillar 色（Sovereign Blue / Operations Turquoise / Gateway Purple），不滥用
- [ ] 咨询风 deck：单页可至 200 字密度
- [ ] Pitch deck：单页 ≤ 30 字
- [ ] Hero Stat 数字 ≥ 96px
- [ ] 团队头像用 halftone 蓝双色调，不用彩色原图
- [ ] 越界元素（若有）没有压住 action title 或 source line
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
