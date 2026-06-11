# Image Generation · FLock 配图系统

**读本文件的时机**：HTML deck 初稿完成后，用户确认需要配图时。  
Codex 环境直接生成并落盘；Claude 环境输出提示词供用户在 ChatGPT / DALL-E 3 使用。  
先读 `references/runtime.md` 确认当前 ENV。

---

## 两个前提

1. **先完成 HTML 初稿，再考虑配图** — 没有骨架就讨论配图是浪费上下文
2. **先选版式槽位，再生成图片** — 不要先生成图再硬塞；先确定 layout 和槽位比例

---

## 四条生成硬规则（每次生成前默念）

1. **图片是嵌入素材，不是独立 slide** — 禁止图片自带页脚、页码、标题、角标、署名、装饰边框
2. **语言跟随 deck 语言** — 中文 deck 信息图用中文标签；英文 deck 用英文；不混用
3. **比例先匹配槽位**：

   | 槽位用途 | 比例 |
   |---|---|
   | cover / hero 全屏主视觉 | **16:9** |
   | 左文右图 / 主内容图 | **16:10** 或 **4:3** |
   | 截图再设计 / UI 情景图 | **16:10** |
   | 多图网格（统一） | 同组统一高度，不混用 |
   | 多图拼贴（极宽槽位） | **16:9**（内部分区） |

4. **用户截图保真优先程序化，不默认重画** — 先读截图处理系统，用内置背景程序化适配；只有内容需要重构时才 AI 重绘

---

## 是否需要配图？（deck 初稿完成后问一次）

**Codex 环境**，主动询问：
> 要不要为这份 PPT 生成几张配图？可以做：
> — 人文纪实照片：真实技术/研究/协作场景，增加现实感
> — 信息图 / 流程图 / 系统关系图：解释无法用实拍照片说明的概念
> — 对比图 / Before-After：展示 FLock 解决的问题
> — 截图美化 / 截图再设计：产品截图 + FLock 品牌背景
> — 数据大字报：把关键数字做成可直接插入的视觉素材
> — 多图拼贴：极宽槽位展示 2–4 个并列概念

**Claude 环境**：输出本文件中对应类型的提示词，告知用户使用方式。

---

## 命名规范（三环境通用）

```
images/{页码两位}-{语义}.{ext}

示例：
images/01-cover-hero.jpg
images/03-federated-arch.png
images/07-dashboard-redesign.png
images/11-product-screenshot.png
images/08-traction-a.jpg   ← 同组多图加 a/b/c 后缀
images/08-traction-b.jpg
```

- 页码补零（`01` 非 `1`）；语义用英文，简短具体
- 照片用 `.jpg`；带透明 / 信息图 / UI 再设计用 `.png`
- 总大小 ≤ 10MB（影响翻页流畅度）

---

## 图片类型 · 决策树

```
页面内容是...

真实技术场景 / 研究 / 工程 / 协作
  → 类型 A · 纪实照片

概念 / 架构 / 系统关系 / 数据与隐私对比
  → 类型 B · 信息图 / 系统关系图

步骤 / 流程 / 数据管道
  → 类型 C · 流程图

中心化 vs 去中心化 / 旧方案 vs FLock
  → 类型 D · 对比图

一个关键指标 / KPI
  → 类型 E · 数据大字报

用户提供了真实产品截图 / dashboard / 代码截图
  → 类型 F · 截图美化 / 再设计

21:9 极宽槽位，需展示 2–4 个并列概念
  → 类型 G · 多图拼贴
```

---

## FLock 配图提示词库

**视觉锚点**：FLock.io 品牌 · 精准技术 · 去装饰 · #3773FF Brand Blue  
**禁止**：圆角装饰 / 暖色调 / 衬线字体 / 卡通 / 霓虹 / 拟物 / 过度阴影 / PPT 外壳  
**语言**：`[中文 / 英文]` 替换为 deck 实际语言

---

### 类型 A · 纪实照片（技术场景）

适用版式：#18 Product Screenshots / 任何需要场景感的 content 页  
槽位比例：16:9 或 16:10

```
生成一张横向技术纪实摄影配图，主题是：[页面概念]。
风格是 minimal editorial tech：暗色调、低饱和、克制精准，
真实研究 / 工程 / 协作场景，少量 electric blue 光效作为环境光（非主视觉）。
主体居中，四角留白充足，适合深色背景 PPT。
不要 AI 机器人形象、大量 UI 元素、暖色调、圆角装饰卡片、logo、水印或文字。
输出 [16:9 / 16:10] 横向构图，主体居中保留边距，画面密度中等。
只保留核心照片，不要页眉、页脚、标题、页码、角标、署名或装饰边框。
```

---

### 类型 B · 信息图 / 系统关系图

适用版式：#13 Solution Diagram / #7 Process Flow / #6 Value Driver Tree  
槽位比例：16:9 或 16:10

```
生成一张横向信息图，解释：[概念 / 系统 / 关系]。
FLock 品牌风格：纯黑 (#000000) 底，主要元素用 Brand Blue (#3773FF) 高亮，
细线、直角模块、极简短标签（每个标签 ≤ 6 字/词），无衬线字体（Inter 气质）。
12 列软网格构图，非对称留白，避免画面满溢。
禁止：渐变、圆角、玻璃拟态、彩色多 accent、衬线字体、3D 效果、SaaS 模板感。
图中文字使用 [中文 / 英文]。输出比例 [16:9 / 16:10]，主体居中保留大留白。
只保留核心信息图，不要 PPT 外壳。
```

---

### 类型 C · 流程图

适用版式：#7 Process Flow / #13 Solution Diagram 步骤变体  
槽位比例：16:9

```
生成一张横向流程信息图，展示：[步骤 1] → [步骤 2] → [步骤 3] → [结果]。
FLock 品牌工程图风格：纯黑底，Brand Blue (#3773FF) 箭头和高亮节点，
细线连接、步骤编号、极短注释，每步节点为直角方块。
禁止圆角、渐变、彩色多色节点。图中文字使用 [中文 / 英文]。比例 16:9。
只保留核心流程图，不要 PPT 外壳。
```

---

### 类型 D · 对比图（FLock vs 传统）

适用版式：#8 Side-by-Side / #13 Solution Diagram Before-After 变体  
槽位比例：16:9

```
生成一张横向对比信息图，左侧是 [传统 / 中心化方式]，右侧是 [FLock 方式]。
纯黑底，左侧用低饱和灰色调（旧/低效语义），右侧用 Brand Blue (#3773FF) 高亮（解决语义）。
细线分栏，直角，短标签，无衬线字体 Inter 气质。禁止圆角、渐变、多 accent。
图中文字使用 [中文 / 英文]。比例 16:9。只保留核心对比图，不要 PPT 外壳。
```

---

### 类型 E · 数据大字报

适用版式：#11 Hero Stat  
槽位比例：16:9

```
生成一张横向数据视觉，核心指标是：[数字]，含义是：[含义]。
FLock 品牌风格：纯黑底，超大无衬线数字（Inter ExtraBold 气质），
Brand Blue (#3773FF) 作为数字颜色或下划线 accent，少量极细辅助标注。
禁止衬线字体、暖色调、圆角装饰。图中文字使用 [中文 / 英文]。比例 16:9。
只保留核心数据视觉，不要 PPT 外壳。
```

---

### 类型 F · 截图美化 / 再设计

见下方「截图处理系统」章节。  
FLock 默认参数：`background: dark-brand, shadow: none, corners: square, inset: subtle`

---

### 类型 G · 多图拼贴（极宽槽位）

用于 16:9 极宽槽位展示 2–4 个并列概念，避免把多张独立图硬塞进等宽列。

**触发条件**：页面有 2–4 个并列概念 + 槽位是宽幅（整页或占页面 8 列以上）。

```
生成一张 16:9 横向拼贴配图，内部分为 [2/3/4] 个等分区域，
分别展示：[主题A] / [主题B] / [主题C]。
FLock 品牌风格：纯黑底，各区域用 1px 极细白线分隔，
Brand Blue (#3773FF) 作为各区域轻量 accent 线和高亮元素，
内部构图克制、留白充足，每区域有 1–2 个短标签（≤ 6 字/词）。
无衬线字体 Inter 气质，禁止渐变、圆角、彩色多 accent、阴影。
图中文字使用 [中文 / 英文]。只保留核心拼贴图，不要 PPT 外壳。
```

---

## 截图处理系统

用户提供了真实截图 → 先问 5 个问题再决定处理方式。

### 截图处理五问

1. 截图在哪个文件夹？内容是 App / dashboard / 代码 / 设计稿？
2. 要**保真展示**、**统一美化**，还是**重新设计成 UI 情景图**？
3. 最终放进哪个槽位（比例）？
4. 是否必须保留所有文字和数据？是否需要隐藏敏感信息？
5. 构图偏好：居中 / 左上 / 右下 / 自判？

### 处理决策树

```
普通网页 / App / 桌面截图           → 程序化适配（背景 + 缩放 + 比例）
产品 UI，细节必须保真               → 程序化适配 + fit-contain，不重画
概念解释用，不需要保真              → GPT-Image 2.0 截图再设计（类型 F-2）
长网页截图 / 极窄 / 极高截图        → 截关键区域 or 拆 2–3 张同高面板
代码截图                           → FLock 深色背景 + 亮色字体风格
```

### 截图再设计提示词（类型 F-2）

用于需要重构视觉的截图：

```
生成一张横向 UI 情景图，把 [截图 / 界面 / 工作区内容] 再设计成适合 FLock 品牌 PPT 的视觉。
纯黑 (#000000) 底，极简 dashboard / workspace 结构，直角面板，
Brand Blue (#3773FF) accent 用于高亮边框和关键元素（低占比），无阴影无圆角。
图中文字使用 [中文 / 英文]，短而清晰，不要真实品牌 logo。
输出必须是 16:10 横向构图，适合放进 fit-contain 容器。
只保留核心 UI 画面，不要 PPT 外壳。
```

### 七参数语义（程序化适配时确定）

| 参数 | FLock dark slide | FLock light slide |
|---|---|---|
| `background` | `dark-brand`（#000000 + 极低 opacity 品牌蓝点阵）| `off-white`（#F2F2F2）|
| `shadow` | `none` | `none` |
| `corners` | `square` | `square` |
| `inset` | `subtle` | `subtle` |
| `padding` | `standard` | `standard` |
| `ratio` | 跟随槽位 | 跟随槽位 |
| `alignment` | 跟随页面构图 | 跟随页面构图 |

### 内置背景资产（FLock）

首次使用时生成，之后所有截图复用：

```
生成一张 16:9 crop-safe FLock 品牌截图背景。
纯黑 (#000000) 底，极低对比度的 Brand Blue (#3773FF) 点阵或等高线，
强度 3–5%，四角安静、中心安静，crop-safe 可裁成 21:9 / 16:10 / 4:3 / 1:1。
不要文字、logo、人物、边框、明显主体或方向性构图。
```

保存为 `assets/screenshot-backgrounds/flock/flock-dark.webp`（深色 slide 用）。

---

## Codex 图片生成代码模板

```python
import openai, os, re, urllib.request

client = openai.OpenAI()

def generate_image(prompt: str, slot: str, size: str = "1792x1024") -> str:
    """
    size 按比例选：
    16:9  → "1792x1024"
    16:10 → "1792x1024"（程序化裁剪）
    4:3   → "1024x1024"（再裁）
    1:1   → "1024x1024"
    """
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        n=1,
        size=size,
        quality="high",
    )
    os.makedirs("images", exist_ok=True)
    path = f"images/{slot}.png"
    urllib.request.urlretrieve(result.data[0].url, path)
    return path

def update_html_slot(html_path: str, slot: str, img_path: str, alt: str = ""):
    """通过 data-image-slot 找到 <img> 并更新 src, alt；移除占位属性"""
    with open(html_path) as f:
        html = f.read()

    def _replace_img(m):
        tag = m.group(0)
        # Update src attribute
        tag = re.sub(r'src="[^"]*"', f'src="{img_path}"', tag)
        # Update alt attribute to real description
        if alt:
            tag = re.sub(r'alt="[^"]*"', f'alt="{alt}"', tag)
        # Remove placeholder opacity style
        tag = re.sub(r'\s*style="opacity:\s*0\.15"', '', tag)
        return tag

    html = re.sub(
        rf'(<figure[^>]*data-image-slot="{re.escape(slot)}"[^>]*>.*?<img[^>]*>)',
        _replace_img,
        html, flags=re.DOTALL
    )
    # Remove data-image-slot from the figure after successful replacement
    html = re.sub(
        rf'\s*data-image-slot="{re.escape(slot)}"', '', html
    )
    with open(html_path, "w") as f:
        f.write(html)

# 使用示例：
# path = generate_image(PROMPT_B, "03-federated-arch-16x9")
# update_html_slot("index.html", "03-federated-arch-16x9", path)
```

---

## 生成后 HTML 更新规则

1. `data-image-slot` 值必须和文件名（去扩展名）完全匹配
2. 生成成功后移除 `data-image-slot` 属性和 `style="opacity:0.15"` 占位样式
3. 更新 `alt` 为真实内容描述
4. 生成失败时保留占位结构，打印警告但不中断整个 deck 构建
