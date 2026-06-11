# Fix · 修复现有 Deliverable（保内容,改视觉）

**读本文件的时机**：用户要求修复/优化一份**已存在**的 deliverable —— 排版问题、品牌色归一、对齐溢出 —— 但**内容文字不动**。
触发语：「布局优化」「修排版」「fix this deck」「brand-normalize」「把这份套成 FLock 品牌」「修一下重叠/溢出」。

```
audit  →  只评估,输出整改清单,不改文件
fix    →  audit + 执行修复,内容 1:1 保留,只改视觉      ← 本文件
生成    →  从零做新 deliverable
```

**fix 的铁律：全部文字内容零修改。** 文案精简/改写需要用户单独授权。

---

## 修复流程（PPTX）

```
Step 1   备份 + 解包
         cp deck.pptx deck.bak.pptx
         python -m office.unpack deck.pptx unpacked/

Step 2   机器体检（先跑脚本,再人工看图）
         python scripts/pptx_lint.py deck.pptx
         → P0:COLOR / P0:OVERFLOW 必须修
         → P1:OVERLAP / P1:FOOTER / P1:EDGE 渲染成图人工确认

Step 3   渲染现状图,逐页目视
         soffice --headless --convert-to pdf deck.pptx
         pdftoppm -jpeg -r 90 deck.pdf orig
         结合 lint 输出定位真问题（bbox 相交 ≠ 视觉重叠,必须看图）

Step 4   颜色归一（批量,sed 安全区操作）
         对照 colors.md §5 重映射表,sed 只替换 srgbClr 属性值:
         sed -i 's/val="2D72F8"/val="3773FF"/g' ppt/slides/*.xml
         ⚠ sed 仅限属性值替换;结构性 XML 编辑必须用 Edit 工具（见 pptx.md）

Step 5   几何修复（逐个,Python 定点）
         解析 <p:sp> 的 off/ext,按问题类型处理:
         | 问题 | 标准手法 |
         |---|---|
         | 文本框撞相邻元素 | 缩 cx + 增 cy（让文字换行而不是越界） |
         | 元素压住文字 | 移动到对称/留白位置,保持构图平衡 |
         | 空白占位框 | 删除整个 <p:sp> 块（含容器） |
         | 卡片贴底边 | 整组上移 + 收紧 cy,保 ≥0.3in 底距 |
         | footer 撞页码 | 缩 footer cx 到页码 x - 0.1in |
         同一组元素(frame+text 同坐标)必须一起移动。

Step 6   重打包 + 双重验证
         python -m office.pack unpacked/ fixed.pptx
         python scripts/pptx_lint.py fixed.pptx        # P0 必须归零
         soffice → pdftoppm → 逐页目视对比修复前后

Step 7   交付 + 写 log
         按 project-memory.md 追加 .flock/log.json 条目,
         deliverable 字段记 "PPTX-fix",brief 写明修了什么。
```

## 修复流程（HTML deck）

```
Step 1   备份 index.html
Step 2   跑 SKILL.md Iron Rules grep + checklist §flock P0 的全部 grep
Step 3   浏览器渲染截图,逐页目视
Step 4   颜色:直接替换 hex → var(--flock-*) token（不是 hex → hex）
Step 5   布局:改 CSS,优先 grid/flex 参数,不动 DOM 文字节点
Step 6   重跑 grep + 目视,P0 归零后交付
```

---

## 常用 EMU 速查（16:9 PPTX 几何修复必备）

```
画布           12192000 × 6858000 EMU
1 inch         914400 EMU
0.5in 顶距     457200       （action title baseline）
0.3in 底距     274320       （source line / 最小底边距）
安全边距       ≥137160 (0.15in),推荐 ≥274320 (0.3in)
```

判断公式：元素 `y + cy > 6858000 - 274320` → 贴底,需上移或收紧。

---

## fix 不做的事

- ❌ 改写/精简/增删任何文字（包括标点、术语统一）→ 需用户单独授权
- ❌ 增删 slide
- ❌ 换版式结构（那是 redesign,另一个任务）
- ❌ 跳过 Step 6 验证直接交付 —— 修一处常引发另一处回归,lint + 目视双查不可省
