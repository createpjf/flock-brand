# Narrative · Deck Content Planning

**读本文件的时机**：收到任何 deck / 演示文稿 / pitch 任务后，**动手生成 slide 之前第一步**。  
跳过规划直接写 slide = 结构返工代价极高。

---

## Step 1 · 7 问澄清清单（动手前必做）

用户已给出完整大纲 + 图片/截图需求 → 可跳过直接进 Step 2。  
用户只给了主题或模糊想法 → 必须逐一对齐以下 7 问。

**环境适配**：
- **Claude / Claude Code**：在对话里列出 7 问，等用户逐条回答；Claude Code 可用 `ask_question` 工具
- **Codex**：普通对话询问，一次最多问 1–3 个最关键问题；不影响开工的项先做合理假设并说明

| # | 问题 | 为什么要问 |
|---|---|---|
| 1 | **受众是谁？场合是什么？**（投资人 / 合作方 / 行业分享 / 内部汇报 / demo day） | 决定叙事深度、术语密度、pitch 还是咨询风 |
| 2 | **输出格式？**（HTML deck / PPTX / Slidev / 其他） | 决定用 template.html 还是 pptx.md / slidev.md |
| 3 | **分享时长？**（5 分钟 ≈ 5 页 / 15 分钟 ≈ 10 页 / 30 分钟 ≈ 18 页 / pitch 8–12 页） | 决定页数和叙事密度 |
| 4 | **有没有原始素材？**（文档 / 数据 / 旧 PPT / 文章链接） | 有素材就基于素材，没有就从头搭骨架 |
| 5 | **有没有图片或截图？希望怎么处理？** | 决定图文版式、槽位选择、是否需要 AI 配图 |
| 6 | **dark mode 还是 light mode？**（默认 dark；打印 / 讲义用 light） | 决定主题模式，见 SKILL.md Mode Selection |
| 7 | **有没有硬约束？**（必须包含某 KPI / 不能出现某竞品名 / 页数上限） | 避免后期大返工 |

---

## Step 2 · 选叙事弧

根据受众和场景选一套叙事模板。选完后在下方填入具体内容。

### 叙事弧 A · 咨询风（行业分享 / 内部汇报 / 研究报告）

```
Situation（现状）    1–2 页  背景、现状、你是谁、为什么讲这个
Complication（张力） 1–2 页  现状的问题、矛盾或待解决的机会
Resolution（方案）   3–5 页  核心内容：FLock 的解法、数据、案例、方法论
Implication（含义）  1–2 页  对受众的意义、下一步行动
```

### 叙事弧 B · Pitch 风（投资人 / 合作伙伴 / demo day）

```
Hook             1 页   一个反差数据或尖锐问题，让人停下来
Problem          1 页   目标市场的真实痛点（不是泛泛而谈）
Solution         1–2 页 FLock 的解决方案（是什么、为什么有效）
Why Now          1 页   时机 — 为什么现在？市场窗口证据
Traction         1 页   牵引力证据（用户 / 收入 / 合作 / 技术里程碑）
Market           1 页   TAM / SAM / SOM
Competition      1 页   竞争定位（你在空白象限）
Team             1 页   核心创始团队 + 可信凭证
Ask / CTA        1 页   融资金额 / 合作提案 / 下一步
```

### 叙事弧 C · 产品发布 / demo day（5 分钟快闪）

```
Hook            1 页   一个数字或场景：「这件事现在要 X 天，我们让它变成 Y 秒」
What We Built   1 页   产品一句话 + 核心截图
How It Works    1 页   3 步流程或架构图
Proof           1 页   用户 / 案例 / 数据
Call to Action  1 页   试用 / 联系 / 投资
```

---

## Step 3 · 页面规划表（动手写 slide 之前填完）

三张表对齐后再进入 slide 生成阶段。

### 3a · 页数规划

| 分段 | 对应叙事弧节点 | 建议页数 | 备注 |
|---|---|---|---|
| 开场 | Hook / Situation | 1 | |
| 背景 | Context / Complication | 1–2 | |
| 核心 | Core / Resolution / Solution | 3–5 | 主要内容在这里 |
| 证据 | Traction / Data / Case | 1–3 | |
| 收束 | Implication / Ask / CTA | 1–2 | |

### 3b · 主题节奏表（HTML deck 必填 / PPTX 可选）

HTML deck 的 WebGL 背景随 slide 主题自动切换，必须规划暗/亮节奏。

| 页码 | 内容 | 模式 | 版式编号 | 主轴 |
|---|---|---|---|---|
| 01 | 封面 | `slide-dark slide-hero` | Cover | 居中 |
| 02 | ... | `slide-dark` | ... | 左偏 |
| ... | | | | |

**节奏硬规则**（HTML deck）：
- ❌ 连续 3 页以上相同模式
- ❌ 8 页以上没有至少 1 个 hero（cover/CTA/section divider）
- ❌ 每页主轴都相同（全左偏 / 全居中 = 视觉发闷）
- ✅ Cover 和 Closing CTA 页用 `slide-hero`，WebGL 背景透出
- ✅ 数据密集页用 `slide-dark`（深色更聚焦）
- ✅ 图片 / 截图多的页面可交替用 `slide-light`
- ✅ 居中主轴只用于 cover / section divider / closing CTA；主轴定义见 `deck-layouts.md` §2

### 3c · 图片槽位表（有图时填）

| 页码 | 图片用途 | 槽位比例 | 处理方式 | data-image-slot |
|---|---|---|---|---|
| 03 | 系统架构图 | 16:9 | AI 生成信息图 | `03-arch-diagram-16x9` |
| 07 | 产品截图 | 16:10 | 截图美化 | `07-dashboard-16x10` |

图片生成详见 `references/image-gen.md`。

---

## Step 4 · 内容 → 版式快速映射

选好叙事弧节点之后，查 `references/deck-layouts.md`(路由)的决策树找版式编号。常用速查：

| 你想表达 | 推荐版式 | 适用叙事节点 |
|---|---|---|
| 开场 / 高管摘要 | #1 Executive Summary | Hook / Situation |
| 一个关键数据 | #11 Hero Stat | Hook / Traction |
| 两个方案对比 | #8 Side-by-Side | Competition |
| 三个产品线 / 三个概念 | #2 Three-Column | Solution / Why Now |
| 四维矩阵 | #3 2×2 Matrix | Competition |
| 时间趋势 + 事件 | #5 Time-Series | Traction |
| 步骤 / 流程 | #7 Process Flow | How It Works |
| 章节切换 | #10 Section Divider | 任意章节开头 |
| 痛点叙事 | #12 Problem Narrative | Problem |
| 解决方案 | #13 Solution Diagram | Solution |
| 市场规模 | #14 Market Size (TAM/SAM/SOM) | Market |
| 竞争定位 | #16 Competition Matrix | Competition |
| 团队 | #17 Team Grid | Team |
| 产品截图 | #18 Product Screenshots | What We Built |

决策树与共用规则 → `references/deck-layouts.md`(路由);版式正文按需读 `deck-layouts-consulting.md`(#1–10)或 `deck-layouts-pitch.md`(#11–18)。

---

## 常用叙事技巧

**Action Title 原则**（咨询风必用）：  
每页标题是结论句，不是话题词。  
❌ 「联邦学习市场分析」  ✅ 「联邦学习市场 2026 年将突破 $12B，FLock 处于最佳卡位」

**Hook 的三种写法**：
1. 反差数据：「中心化 AI 训练平均泄露 23% 私有数据。FLock 把这个数字变成 0。」
2. 场景问题：「你的模型在用别人的数据训练，但你不知道。」
3. 硬时机：「GDPR 罚款总额 2025 年翻倍——现在是联邦学习的窗口期。」

**收束三选一**：
- 金句：一句话浓缩整场分享
- 悬念问题：把最难的问题留给观众思考
- 明确 Next Step：「扫码试用 / 发邮件 / 下周同步」

---

## 禁用短语库（写文案时对照）

这些是 LLM 默认会吐出来的「AI 套话」——看起来像内容，实际是零信息量的填充。FLock deck 里出现任何一条都要改写。

### 通用禁用（中英文都禁）

| 禁用 | 为什么 | 改成 |
|---|---|---|
| 「赋能」「赋能千行百业」 | 万能词，不传递任何具体信息 | 说清到底做了什么：「把模型训练时间从 3 天压到 4 小时」 |
| 「打造」「倾力打造」「精心打造」 | 自我表扬，受众不关心你多努力 | 直接说结果 |
| 「一站式解决方案」 | 每个产品都这么说 | 说清覆盖哪几个具体环节 |
| 「行业领先」「业界领先」 | 无证据的自夸 | 给可验证的排名/数据/第三方背书 |
| 「众所周知」「毋庸置疑」 | 回避论证 | 给出论据，或删掉这句 |
| 「在当今数字化时代」「随着 AI 的发展」 | 万能开场，浪费 Hook | 用反差数据或场景问题开场 |
| Built for the modern team | hallmark 明令禁用的英文套话 | 说清为哪类具体团队、解决什么 |
| Empower / Unlock / Supercharge / Seamless | 英文 AI slop 高频词 | 用具体动词：reduce, cut, ship, verify |
| Revolutionary / Game-changing / Next-generation | 无证据的形容词 | 让数据自己说话 |
| Trusted by teams worldwide | 模糊背书 | 列出具体客户名 / 具体数字 |

### 编造内容红线（honest-copy 规则）

**用户没给的数据，绝不编造。** 这是硬规则，不是建议。

- ❌ 自己写「转化率提升 47%」「已服务 50,000+ 团队」「速度快 10 倍」——只要是编的，就是 slop
- ❌ 编造客户 logo、客户名、案例数量、用户评价
- ✅ 用户提供了真实数据 → 用真实数据
- ✅ 用户没提供 → 用占位符：`—` + 灰块 + 标注「数据待确认」，或换一个不需要该数据的版式

Pitch deck 的 Traction / Market 页尤其容易触发——宁可留占位符让用户填，也不要编一个数字蒙混过关。编造的数字一旦被投资人/合作方追问，整场信任崩塌。

### FLock 专属注意

- 不要把 FLock 三产品线（Sovereign / Operations / Gateway）的能力混着说，每条 claim 对应明确的产品线
- 不要用「去中心化」当万能形容词贴在每一页——只在内容真正涉及去中心化机制时用
- 涉及隐私/合规的 claim（GDPR、数据主权）必须基于事实，不夸大
