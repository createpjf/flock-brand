# Audit · FLock 品牌合规审计

**读本文件的时机**：用户要求审计/检查现有 deliverable 是否符合 FLock 品牌时。  
触发语：`flock audit <文件>`、「检查这份 deck 符不符合 FLock 品牌」、「这个 PPT 哪里不对」、「audit 一下」。

---

## audit 是什么

audit 是一个**只评估、不修改**的动词。读入一份现有的 deliverable（HTML / PPTX / 截图 / 代码），对照 FLock 品牌规范打分，输出一份**分级整改清单**。

```
audit  →  读 + 评分 + 输出整改清单（punch list），不改任何代码
fix    →  audit + 动手修（保内容,改视觉）→ references/fix.md
生成   →  从零做一份新 deliverable
```

**audit 绝不直接改文件**。用户看完整改清单后，可以再要求「按这个清单改」——那时才进入修改流程。

---

## audit 流程

```
Step 1 · 确认审计对象
  - 文件路径 / 粘贴的代码 / 上传的截图
  - 问清：要审计的是 HTML deck / PPTX / 单页 / 整套？

Step 2 · 读取
  - HTML / 代码 → 直接 read 文件
  - PPTX → 按 pptx.md 方法解析
  - 截图 → 视觉审查（颜色、字体、版式、logo）
  - 无法读取 → 说明原因，请用户换格式

Step 3 · 逐项对照打分
  - 先跑 §0 六轴自我批判（给现有产物打分）
  - 再对照 checklist.md 的 §shared P0 + §flock P0 + P1/P2
  - 每个命中的问题记录：位置 + 违反的规则 + 严重级别

Step 4 · 输出整改清单
  - 按 P0 → P1 → P2 排序
  - 每条：问题 + 在哪 + 为什么违规 + 怎么改
  - 不写代码，只描述

Step 5 · 给总评
  - 六轴分数 + P0/P1/P2 命中数量
  - 一句话结论：能否直接用 / 必须改 P0 / 建议优化
```

---

## 审计维度（对照 checklist.md）

audit 复用 `checklist.md` 的全部规则，不另立标准。审计时逐节过：

| 维度 | 对照 checklist.md 节 | 重点 |
|---|---|---|
| 立意与质量 | §0 六轴 | 给现有产物打 P/H/E/S/R/V 分 |
| 通用结构 | §shared P0 | 模板类名、节奏、emoji、图片裁切、动效 |
| 品牌合规 | §flock P0 | 颜色、logo、badge、CJK 字体、次要色、action title |
| 视觉节奏 | P1 | hero 交替、文字密度、pillar 色语义、source line |
| 打磨细节 | P2 | WebGL 遮罩、对齐、头像处理 |

审计时优先用 checklist.md 里给出的 grep 命令做机器检测，再做人工视觉判断。

---

## 整改清单输出格式

```markdown
# FLock 品牌审计报告 · [文件名]

## 总评
- Pre-emit 六轴：P3 H4 E2 S4 R3 V—
- P0 命中：3 项（必须修复才能交付）
- P1 命中：5 项
- P2 命中：2 项
- 结论：**不可直接交付**，存在 3 个 P0 品牌违规

## P0 · 必须修复（输出当前作废）

### P0-1 · 颜色违规
- 位置：slide 4、slide 7 标题
- 问题：标题色用了 #2B6FE0，不是 FLock Brand Blue #3773FF
- 规则：Iron Rule §1 — Brand Blue 必须是 #3773FF
- 改法：全局替换为 var(--flock-blue) / #3773FF

### P0-2 · Logo 手绘
- 位置：封面左上
- 问题：logo 是 inline SVG path 手绘近似，非官方文件
- 规则：Iron Rule §8 — 必须用 assets/logos/ 官方 SVG
- 改法：替换为 flock-lockup-white.svg（深色封面用白色版）

### P0-3 · ...

## P1 · 影响专业度（建议修复）

### P1-1 · action title 缺失
- 位置：slide 3、slide 5、slide 8
- 问题：标题是话题词「市场分析」，不是结论句
- 改法：改写为结论句，例如「联邦学习市场 2026 年将超 $12B」

### P1-2 · ...

## P2 · 打磨项（有时间再改）

### P2-1 · ...

## 修复优先级建议
1. 先修 3 个 P0（颜色 / logo / 字体）——这是品牌红线
2. 再修 P1 中的 action title——影响 deck 说服力
3. P2 可选
```

---

## audit 的两个原则

1. **只诊断，不动手**。audit 输出的是清单，不是改好的文件。用户明确说「按清单修」之后才进入修改。

2. **引用具体规则**。每条问题必须指明违反了 checklist.md / SKILL.md Iron Rules 的哪一条，不说「感觉不对」。让用户能验证、能反驳。

---

## audit 完成后的去向

整改清单交付后，用户通常有三种反应：

- **「按清单全改」** → 进入 `fix` 流程（references/fix.md），逐条修 P0 → P1，修完重新跑 lint + checklist 验证
- **「只改 P0」** → 只修品牌红线，P1/P2 保留
- **「知道了」** → audit 本身就是完整交付，结束

audit 不写 `.flock/log.json`——它没有产出新 deliverable，只是评估。但如果 audit 后接了修改流程，修改产出的新版本要按 project-memory.md 写 log。
