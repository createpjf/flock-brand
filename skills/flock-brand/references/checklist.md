# Quality Checklist · P0 / P1 / P2 / P3

**读本文件的时机**：每次生成完任何 FLock 品牌 deliverable 之后。P0 全部通过才算可交付。

```
P0 = 输出作废，必须修完再交付
P1 = 明显影响专业度，发现即修
P2 = 影响 polish，有时间再修
P3 = nice-to-have，用户要求才做
```

**使用顺序**：交付前先跑 §0 Pre-emit 自我批判 → 再跑 §shared P0 → §flock P0 → 有余力查 P1/P2 → 末尾速查表。

---

# §0 — Pre-emit 自我批判（交付前必做，先于所有 checklist）

在跑下面任何 P0 清单**之前**，先给即将交付的产物按 6 个轴各打 1–5 分。  
**任何一轴 < 3 分 → 触发一轮返工**，修完再重新打分。返工两轮是正常的；到第三轮说明是 brief 出了问题，回去重读需求，不要继续硬改。

| 轴 | 打分对象 | 1 分长啥样 | 5 分长啥样 |
|---|---|---|---|
| **P · Philosophy 立意** | 这份 deliverable 有没有一个清晰的「为什么」——一个明确的主张？ | 只是把信息排进版式 | 每一页都在推进一个论点 |
| **H · Hierarchy 层级** | 受众能否在 2 秒内分辨主次三级？ | 全页一个重量，眼睛无处落 | 主/次/辅一眼可分 |
| **E · Execution 执行** | 细节是否都在规范内（tracking、颜色占比、对齐、source line、badge 位置）？ | 骨架对了但细节糙 | 所有细节都在 spec 内 |
| **S · Specificity 针对性** | 这看起来像「这一个 brief」，还是像「任何 FLock deck 都能套」的通用模板？ | 换个客户名也成立 | 紧扣这次的受众和场景 |
| **R · Restraint 克制** | 有没有删掉所有不挣钱的元素（装饰、冗余、为留白而留白）？ | 次要色乱铺、动效堆砌 | 每个元素都有存在理由 |
| **V · Variety 连贯性** | （FLock 版与 hallmark 相反）这份产物和给同一客户/系列的上一份是否视觉连贯？ | 同系列三份各走各的 | 系列内 token/版式语言一致 |

> **注意 V 轴的方向**：hallmark 求异（每次结构都不同），FLock 求同（品牌一致性）。FLock 的 V 轴打分逻辑是——同一客户/同一系列的多份 deliverable **越一致分越高**。跨客户、独立项目则不适用此轴，记为 N/A。

**打完分 stamp 进产物**：

```
HTML deck — 写进 index.html 顶部注释：
<!-- FLock · pre-emit critique: P5 H4 E5 S4 R5 V5 -->

PPTX — 写进生成脚本顶部注释：
// FLock · pre-emit critique: P5 H4 E5 S4 R5 V5

DOCX / 其他 — 写进文档属性的 comments 字段，或交付说明里附一行
```

stamp 的作用：下次同系列任务可以读到上一份的弱项轴，针对性改进。

---

# §shared — 所有输出都必须过的 P0

## S-P0-1 · 模板类名必须在 `<style>` 里有定义（HTML deck 专属）

**症状**：大标题变 Arial/Helvetica、stat 数字挤成一团、grid 布局崩溃。  
**根因**：直接粘贴 deck-layouts.md 骨架，但 template.html 没有对应 class 定义。  
**做法**：生成前先 `read assets/template.html` 的 `<style>` 块，确认要用的每个 class 都存在。缺失的在模板 `<style>` 里补上，不要 inline 重写每个 slide。

---

## S-P0-2 · 翻页节奏必须规划（HTML deck，动手前必做）

**症状**：整个 deck 全是 `slide-dark`，或 hero 页 WebGL 不切换（背景一直是 dark canvas）。  
**做法**：
- 生成前填 `narrative.md` 的节奏表，每页写清 `slide-dark` / `slide-light` / `slide-dark slide-hero` / `slide-light slide-hero`
- JS 通过 classList 推断模式，必须明确写，不能缺
- 硬规则：❌ 连续 3 页同模式 ❌ 8 页以上无 hero 页

**自检**：`grep 'class="slide' index.html` 目视节奏有交错

---

## S-P0-3 · 不使用 emoji 作图标

❌ 🎯 💡 ✅ 出现在任何 FLock 输出里立刻破坏专业感。  
HTML deck 用 Lucide（`<i data-lucide="target" class="ico-md"></i>`）；PPTX 用内置图形。

---

## S-P0-4 · 图片只裁底部（HTML deck）

容器用 `height:Nvh + overflow:hidden`，不用 `aspect-ratio`（会在 grid 中撑破）。  
`object-fit: cover; object-position: top center` — 只裁底部，保留顶部和左右。

---

## S-P0-5 · data-anim 覆盖率足够（HTML deck）

**症状**：翻页时内容「啪」一下全出，无节奏。  
**做法**：每页至少给 action-title / 主要 stat / callout / figure 加 `data-anim`。  
**自检**：`grep -c 'data-anim' index.html` ≥ 页数 × 3

---

# §flock — FLock 品牌专属 P0

## F-P0-1 · Iron Rules 颜色违规（直接作废）

```bash
grep -n "#282828" output          # → 必须是 #000000
grep -n "#F2F2F0\|#F8F8F8" output # → 必须是 #F2F2F2
grep -n "#00A8C0\|#6030D0" output # → 用 #03BFD4 / #9C59F3
grep -n "letter-spacing:\s*normal\|letter-spacing:\s*0" output  # heading 必须有 tracking
```

任何一条命中 = 必须修。

---

## F-P0-2 · Logo 违规

- ❌ inline 手绘、SVG path 近似、文字模拟 — 必须引用 `assets/logos/` 官方 SVG
- ❌ 深色背景放黑色 logo → 改用 `flock-lockup-white.svg`
- ❌ 浅色背景放白色 logo → 改用 `flock-lockup-black.svg` 或 `flock-lockup-blue.svg`
- ❌ logo 拉伸变形 → 保持原始宽高比，只设 height 或 width 单边

Logo 使用规则详见 `references/logo.md`。

---

## F-P0-3 · FLock Badge 规则（deck 专属）

- Content 页（非 cover / section divider / closing CTA）右上角必须有 FLock badge
- Cover / Section Divider / Closing CTA 页**不放** badge（Logo 已经在 hero 区域）
- Badge 高度 18–24px，不拉伸，不旋转

---

## F-P0-4 · CJK / 中文内容必须用 Alibaba PuHuiTi 3.0

- 中文标题 / 正文走 `--flock-font-primary` 中的 `'Alibaba PuHuiTi 3.0'`
- `@font-face` 必须引用 `assets/fonts/AlibabaPuHuiTi-3-*.woff2`（4 个字重）
- PingFang SC / Noto Sans SC 是系统 fallback，不是主字体
- 详细字体规则 → `references/typography.md`

---

## F-P0-5 · 次要色不得作为主背景

`#FF8B00` (Orange) / `#03BFD4` (Turquoise) / `#9C59F3` (Purple)：
- ❌ 大面积铺页面背景
- ❌ 替代 Brand Blue 作主色
- ✅ 只用于 pillar 标签、accent 线、数据高亮、图表序列色

---

## F-P0-6 · Action Title 规则（deck 专属）

- 每页有且只有一个 governing thought
- 标题是 **action title（结论句）**，不是 topic title（话题词）
  - ❌ 「市场分析」  ✅ 「联邦学习市场 2026 年将超 $12B，FLock 处于最佳卡位」
  - ❌ 「产品介绍」  ✅ 「FLock Gateway 让模型推理成本降低 60%」
- 三条 baseline 锁定（HTML deck）：action title 距顶 0.5in，body 区 1.4in，source line 距底 0.3in

---

## F-P0-7 · PPTX 专属违规

```bash
grep -n '"#' *.js  # PptxGenJS hex 不能带 # 前缀，否则 corrupt 文件
grep -n "•"        # 不得用 Unicode •，用 bullet:true
```

完整 PPTX 坑列表 → `references/pptx.md` § Known Bugs

---

## F-P0-8 · PPTX 几何完整性（生成和 fix 都查）

```bash
python scripts/pptx_lint.py output.pptx   # exit 1 = 有 P0,必须修
```

P0 标准（脚本自动判）:
- 含文字元素超出画布（12192000 × 6858000 EMU）
- off-brand 颜色命中 colors.md §5 重映射表

P1 advisory（脚本报,人工渲染图确认）:
- 文字 bbox 相交 >40%（bbox 相交 ≠ 视觉重叠,必须看渲染图）
- 宽 footer 与页码横向碰撞
- 文字元素贴底边 <0.15in

**lint 通过 ≠ 视觉通过** — soffice 渲染 + 逐页目视仍然必做（pptx.md § QA）。

---

# P1 — 视觉节奏（发现即修）

## P1-1 · Hero 页与 Content 页交替（HTML deck）

推荐节奏：每 3–4 个 content 页插入 1 个 hero（cover / section divider / closing CTA）。  
连续 4 页 content = 节奏死；连续 2 页 hero = 视觉疲劳。

## P1-2 · 每页文字密度匹配 deck 类型

| deck 类型 | 单页密度 |
|---|---|
| 咨询风（顾问汇报）| 最多 200 字 |
| Pitch deck | 最多 30 字 |
| Hero Stat 页 | 数字 ≥ 96px，文字 ≤ 2 行注释 |

## P1-3 · Pillar 色语义正确

只在内容明确对应 FLock 三产品线时使用 pillar 色：
- **Sovereign Blue** → FLock Sovereign 产品相关内容
- **Operations Turquoise** → FLock Operations 产品相关内容  
- **Gateway Purple** → FLock Gateway 产品相关内容

不要用 pillar 色做纯装饰，或把三色随机分配给无关内容。  
Pillar 色 hex → `references/colors.md` §2.1

## P1-4 · 数据页必须标 source line

格式：`Source: [来源机构] · [年份]`，caption 字号（14px），source line baseline 距底 0.3in。

## P1-5 · 术语一致性

整个 deck 同一个词只有一种写法。「Federated Learning」「联邦学习」「FLock」不要中英混用或随意缩写。

## P1-6 · 动效纪律（HTML deck）

动效是 deck 里最容易出现「随机数值」的地方。HTML deck 必须遵守：

**时长只来自 5 个 bucket**——`template.html` 的 `:root` 已定义 `--f-dur-instant / micro / minor / major / page`。不在 CSS 或 JS 里写裸 `0.45s` / `duration:.65` 这类自创数值。改动效快慢 = 改 token，不是改散落的数字。

```bash
# CSS 里不应出现裸 cubic-bezier（:root 的 3 条定义除外）
grep -n "cubic-bezier" index.html   # 命中行若不在 :root → 改用 --f-ease-* token
# 不应出现 transition: all（hallmark slop-test gate 11）
grep -n "transition:\s*all" index.html  # 命中 → 改成显式属性列表
# JS 里不应出现裸 duration 数值
grep -n "duration:\.\|duration:0\." index.html  # 命中 → 改用 DUR 常量
```

**0ms 是常见的正确答案**——焦点态、错误态不该有过渡。键盘用户需要焦点环立刻出现，淡入的焦点环是 a11y bug。焦点样式用 `--f-dur-instant`。

**一页最多 3 个动效原语**——一个级联入场 + 一个 hover + 一个数字 reveal = 3，到此为止。「再加一个就好」的冲动就是 slop。

**按页型分配动效**：
- Section divider（版式 #10）页 → 零额外动效，静止本身是节奏
- Hero Stat（版式 #11）页 → 默认带数字 reveal（0 → 目标值，用 `--f-dur-major`）
- Cover / Closing CTA → 用 `hero` recipe（已内置），不另加
- 数据密集 content 页 → `cascade` 级联即可，不堆叠多种动效

**可交互元素必须有焦点态**——HTML deck 的 nav 圆点、B 键提示等可交互元素必须有 `:focus-visible` 样式，焦点环 ≥ 2px、对比度 ≥ 3:1。

---

# P2 — 视觉打磨（有时间再查）

## P2-1 · WebGL 遮罩透明度（HTML deck）

| 页面类型 | 遮罩 |
|---|---|
| `slide-hero`（cover / closing CTA） | 12–16%，WebGL 大幅透出 |
| content page（`slide-dark` / `slide-light`） | 100% 不透，保证可读 |

FLock brand = 克制，WebGL 只在 hero 页透出。

## P2-2 · 左文右图对齐（HTML deck）

- 左列：`flex-direction: column; justify-content: space-between`（标题贴顶，callout 贴底）
- 右列：`align-items: start`（图片贴顶，不加 `align-self: end`）
- 图片跟正文内容区对齐，必要时加 `margin-top: 6vh`–`8vh`

## P2-3 · 团队头像用 halftone 蓝双色调

Team Grid 版式（#17）：头像必须用品牌蓝双色调处理（shadow → #3773FF，highlight → #98B8F8）。  
不用彩色原图。处理方式 → `references/infographics.md` § Imagery。

## P2-4 · 生成后浏览器视觉对齐（HTML deck）

代码正确 ≠ 视觉舒服：
1. 等入场动效稳定（约 1–2 秒）再看，不要把动画中间态当问题
2. 先看视觉：字重、间距、图片对齐、badge 位置
3. 再看代码：版式是否选对，必选组件是否齐

---

# P3 — 收尾细节（可选）

## P3-1 · `<title>` 已替换

```bash
grep "\[REPLACE\]" index.html  # 应无结果
```

## P3-2 · 图片路径用相对路径

`images/xx.png`，不用绝对路径。同名覆盖最稳（不需要改 HTML 路径）。

## P3-3 · HTML deck 导航完整

← → / 滚轮 / 触屏 / 底部圆点 / ESC 索引 / Home · End 全部可用。  
B 键切换低功耗模式，右下角提示文字同步更新。

## P3-4 · 低功耗模式降级（HTML deck）

`body.low-power` 下：WebGL 停止 RAF 循环，Motion One 动效 skip，`[data-anim]` 直接 opacity:1。  
用于演示现场 WebGL 卡顿时应急切换。

---

# 最终速查表

生成完打印出来逐项勾：

```
§0 Pre-emit 自我批判（先于一切）
  □ 6 轴打分完成：P / H / E / S / R / V
  □ 无任何一轴 < 3（有则返工后重打）
  □ 分数已 stamp 进产物注释

§shared（所有输出）
  □ HTML deck：模板类名预检通过（生成前已 read template.html）
  □ HTML deck：节奏表完整，无连续 3 页同模式
  □ 无 emoji 图标
  □ HTML deck：图片只裁底部，用 height:Nvh 不用 aspect-ratio
  □ HTML deck：data-anim 总数 ≥ 页数 × 3

§flock（所有 FLock 输出）
  □ 无禁用色：#282828 / #F2F2F0 / #F8F8F8 / #00A8C0 / #6030D0
  □ Heading 有 tracking（-0.04em H1/H2 或 -0.03em H3/body）
  □ Logo：引用 assets/logos/ 官方 SVG，颜色版本与背景匹配
  □ 中文内容：Alibaba PuHuiTi 3.0 主 CJK 字体（@font-face 引用）
  □ 次要色仅作 accent，不做主背景
  □ HTML deck：content 页有 FLock badge；cover/divider/closing 无
  □ HTML deck：每页 action title（结论句，非话题词）
  □ PPTX：hex 无 # 前缀；无 Unicode •
  □ PPTX：scripts/pptx_lint.py 通过（P0=0）

P1（发现即修）
  □ hero 页交替，无连续 4 页 content
  □ 单页密度：pitch ≤ 30 字；咨询风 ≤ 200 字
  □ Pillar 色只用于对应产品线内容，不做装饰
  □ 数据页有 source line
  □ 术语全 deck 一致
  □ HTML deck：动效时长全用 --f-dur-* token，无裸数值
  □ HTML deck：无 transition:all；焦点态用 0ms
  □ HTML deck：一页 ≤ 3 个动效原语；divider 页零动效
  □ HTML deck：可交互元素有 :focus-visible 样式

P2（有时间查）
  □ WebGL 遮罩：hero 12–16%，content 100%
  □ 团队头像：halftone 蓝双色调，不用彩色原图
  □ 浏览器视觉对齐：动效稳定后逐页目视

P3（可选）
  □ <title> 已替换，无 [REPLACE]
  □ 图片路径用相对路径
  □ 低功耗模式 B 键可用
```
