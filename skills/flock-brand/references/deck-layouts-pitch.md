# Deck Layouts · Part II — Pitch Deck 8 版式（#11–#18）

> 由 `deck-layouts.md` 路由至此。前置:已读路由文件的 §0–3(grid / 主轴 / 不对称技法)并用决策树选好版式编号。

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
