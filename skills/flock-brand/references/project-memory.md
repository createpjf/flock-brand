# Project Memory · 系列一致性记忆

**读本文件的时机**：开始任何 FLock deliverable 任务时，检查项目里有没有 `.flock/log.json`。  
有 → 读最近 3–5 条，**优先复用**已用过的版式和配色，保证系列连贯。  
无 → 第一次任务，正常进行，结束时创建该文件。

---

## 和 hallmark 的关键区别：求同，不是求异

hallmark 的项目记忆用来**强制多样性**——连续两次不能用同一个结构。  
FLock 的项目记忆用来**强制一致性**——给同一个客户/同一个系列做多份 deliverable 时，视觉语言必须连贯。

```
hallmark log.json  →  「上次用了 Bento Grid，这次必须换别的」
FLock  log.json    →  「上次用了 #11 Hero Stat + dark mode，这次同系列优先沿用」
```

原因：FLock 是品牌 skill。投资人看到 FLock 的 3 份材料，应该立刻认出「这是同一家公司」。系列内视觉漂移 = 品牌失败。

---

## `.flock/log.json` 数据结构

项目根目录下 `.flock/log.json`，JSON 数组，最新一条在最前：

```json
[
  {
    "date": "2026-05-20",
    "deliverable": "HTML deck",
    "mode": "dark",
    "narrative_arc": "pitch",
    "layouts_used": ["Cover", "#12 Problem", "#13 Solution", "#11 Hero Stat", "#17 Team", "Closing CTA"],
    "theme_accent": "brand-blue",
    "cjk": true,
    "preflight_critique": "P5 H4 E5 S5 R4 V5",
    "brief": "FLock 新加坡投资人路演 deck"
  },
  {
    "date": "2026-05-12",
    "deliverable": "PPTX",
    "mode": "dark",
    "narrative_arc": "consulting",
    "layouts_used": ["#1 Executive Summary", "#7 Process Flow", "#13 Solution Diagram"],
    "theme_accent": "brand-blue",
    "cjk": true,
    "preflight_critique": "P4 H5 E4 S5 R5 V5",
    "brief": "FLock 合作伙伴技术汇报"
  }
]
```

字段说明：
- `deliverable` — HTML deck / PPTX / Slidev / DOCX / 其他
- `mode` — dark / light
- `narrative_arc` — consulting / pitch / launch（见 narrative.md）
- `layouts_used` — 用到的版式编号列表（deck-layouts.md 的 #N 或 HTML deck 的命名）
- `theme_accent` — 主 accent，通常 `brand-blue`；若该 deliverable 重点用了某 pillar 色则记录
- `cjk` — 是否含中文内容
- `preflight_critique` — §0 六轴打分结果
- `brief` — 一句话任务摘要

---

## 任务开始时：读 log（Step 0.5）

在 narrative.md 的 7 问澄清**之前**插入一步：

```
1. 检查 .flock/log.json 是否存在
2. 存在 → 读最近 3–5 条，判断本次任务是否属于已有系列：
   - 同一客户 / 同一品牌项目 / 用户明说「跟上次那份一套」 → 属于系列
   - 完全不相关的新任务 → 不属于系列
3. 属于系列 → 进入「一致性模式」（见下）
4. 不属于系列 / 文件不存在 → 正常流程
```

判断是否同系列有疑问时，问用户一句：  
> 这份材料是和之前的 [上一条 brief] 同一个系列吗？需要保持视觉一致，还是独立的新风格？

---

## 一致性模式：本次任务属于已有系列

读到上一份同系列记录后：

| 维度 | 处理 |
|---|---|
| **mode** | 沿用上一份的 dark / light，不切换 |
| **narrative_arc** | 同类场景沿用同一叙事弧（都是 pitch / 都是 consulting） |
| **layouts_used** | 同类内容优先复用上次用过的版式编号——Hero Stat 上次用 #11，这次也用 #11；不要换 #14 |
| **theme_accent** | 完全沿用，pillar 色的使用规则也一致 |
| **cjk** | 字体方案保持一致 |

**§0 六轴中的 V 轴**：一致性模式下，V（连贯性）轴打分直接对照上一份——版式语言、配色、字体越一致分越高。

**例外**：如果某个版式在上一份里被证明效果不好（用户反馈过），可以换，但要在新 log 条目里记下原因。

---

## 任务结束时：写 log（最后一步）

deliverable 交付后，向 `.flock/log.json` 数组**头部**追加一条新记录：

```
1. 文件不存在 → 创建 .flock/ 目录和 log.json，写入第一条
2. 文件存在 → 读出数组，新记录 unshift 到最前，写回
3. 数组保留最近 20 条即可，更早的可截断
```

新记录必须包含上方结构的全部字段，`preflight_critique` 用 §0 实际打分结果。

---

## 环境差异

| ENV | 读 log | 写 log |
|---|---|---|
| `claude` | 无文件系统 → 让用户粘贴上一份的 stamp 注释（`<!-- FLock · pre-emit critique: ... -->`），或口述上次用的 mode/版式 | 输出一段 JSON 让用户保存为 `.flock/log.json` |
| `claude-code` / `codex` | 直接 `read .flock/log.json` | 直接写文件 |

Claude 环境下退而求其次：产物里的 pre-emit stamp 注释（见 checklist.md §0）本身就是一条精简记忆——用户下次把上一份的 stamp 贴进来，就能恢复部分上下文。

---

## 单次任务 vs 系列任务速判

```
属于系列（进一致性模式）：
  - 用户说「跟上次那份一套」「同一个项目」「系列第二份」
  - brief 提到同一个客户名 / 同一个产品发布
  - .flock/log.json 最近条目的 brief 和本次明显相关

独立新任务（正常流程）：
  - 完全不同的客户 / 场景
  - 用户明说「这次想要不一样的风格」
  - 项目里没有 .flock/log.json
```
