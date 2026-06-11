# Runtime · 运行环境适配

**读本文件的时机**：每次任务开始时，先识别当前运行环境，再决定行为。  
同一份 SKILL.md 会被 Claude、Claude Code 和 Codex 三个环境加载，但能力集完全不同。

---

## 环境识别

```
有 ask_question 工具 + 有 shell 权限          → Claude Code
有 GPT-Image 2.0 image generation 权限       → Codex
有 bash_tool / create_file（容器文件系统）     → Claude.ai (computer-use 版,能力≈Claude Code)
以上都没有，纯对话                             → Claude (纯文本,API 或老界面)
```

**2026 起 Claude.ai 默认带容器**（bash + 文件读写 + soffice/pdftoppm 全套）。检测到 bash_tool 即按 `claude-code` 行为执行：直接 cp 模板、跑 lint 脚本、渲染验证。只有纯对话环境才降级到「输出代码让用户保存」。

---

## 三环境能力对比

| 能力 | Claude 纯对话 | Claude.ai 容器版 | Claude Code | Codex |
|---|---|---|---|---|
| 生成 HTML / PPTX 代码 | ✅ | ✅ | ✅ | ✅ |
| 写文件到磁盘 | ❌ | ✅ | ✅ | ✅ |
| 执行 shell 命令 | ❌ | ✅ | ✅ | ✅ |
| `ask_question` 类工具 | ❌ | ✅ (ask_user_input) | ✅ | ❌ |
| GPT-Image 2.0 生图 | ❌ | ❌ | ❌ | ✅ |
| soffice/pdftoppm 渲染验证 | ❌ | ✅ | ✅ | ✅ |
| 运行 lint / validate 脚本 | ❌ | ✅ | ✅ | ✅ |

---

## 各环节行为差异

### 需求澄清（Step 1）

| ENV | 做法 |
|---|---|
| `claude` | 对话里列出 narrative.md 的 7 问，等用户回答 |
| `claude-code` | 调用 `ask_question` 工具逐项澄清 |
| `codex` | 普通对话询问，**不调用** ask_question；一次最多问 1–3 个关键问题；不影响开工的项先假设并说明 |

### 拷贝模板（Step 2）

| ENV | 做法 |
|---|---|
| `claude` | 把 `assets/template.html` 内容完整输出，用户自行保存 |
| `claude-code` / `codex` | `cp assets/template.html {项目目录}/index.html && mkdir -p images` |

### 图片生成（Step 5）

| ENV | 做法 |
|---|---|
| `claude` | 输出 `references/image-gen.md` 中对应类型的提示词，用户在 ChatGPT / DALL-E 3 生成后放入 `images/` |
| `claude-code` | 输出提示词 + 命名规范，用户手动生图后 agent 自动更新 HTML src |
| `codex` | **直接调用 GPT-Image 2.0**，生成后落盘 `images/{slot}.png`，自动更新 HTML |

### 校验（Step 4）

| ENV | 做法 |
|---|---|
| `claude` | 输出 checklist.md 速查表，提示用户在浏览器手动打开校验 |
| `claude-code` / `codex` | 运行 grep 自检命令，打开浏览器预览 |

---

## 图片占位机制（跨环境协作）

Claude 生成 HTML 时在 `<figure>` 上打 `data-image-slot` 标记：

```html
<figure class="frame-img r-16x10" data-image-slot="03-arch-diagram-16x10">
  <img src="images/03-arch-diagram.png" alt="[待生成]" style="opacity:0.15">
</figure>
```

Codex 稍后读 `data-image-slot` 决定生成什么图、落盘路径、更新哪个 `img src`。  
Claude 环境：用户手动替换图片，删除 `data-image-slot` 和 `style="opacity:0.15"`。

---

## Codex 特有交互模式

Codex 有图片生成能力但没有持续对话机制，一次对话内高效工作：

1. **主动问图**：deck 初稿完成后立即询问：
   > 要不要为这份 PPT 生成几张配图？可以做：纪实照片 / 信息图 / 流程图 / 截图美化 / 多图拼贴

2. **一次决策**：用户确认后，一次性问清所有需要，然后批量生成，不逐张确认

3. **假设合理值**：用户无明确偏好时，根据页面内容自动选类型，生成后汇报选择

4. **批量落盘**：所有图片按命名规范存入 `images/`，HTML src 自动更新，最后汇报一句：「已生成 N 张配图并插入页面」

---

## 共享流程（三环境完全一致）

- narrative.md 的 7 问澄清逻辑
- 主题节奏规划
- 布局骨架选择（deck-layouts.md）
- data-anim / data-animate 标记方式
- checklist.md 自检逻辑
- 最终 HTML / PPTX 结构和 token 使用
