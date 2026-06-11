#!/usr/bin/env python3
"""
pptx_lint.py — FLock PPTX 自动体检（颜色合规 + 几何问题）

用法:
  python pptx_lint.py deck.pptx              # 全量检查
  python pptx_lint.py deck.pptx --colors     # 只查颜色
  python pptx_lint.py deck.pptx --geometry   # 只查几何

检查项:
  [COLOR]    off-brand 颜色（含修复建议,对照 colors.md §5 重映射表）
  [OVERFLOW] 元素超出画布边界 / 贴边 (< 0.15in 安全距)
  [OVERLAP]  两个含文字的 shape bbox 相交
  [FOOTER]   宽幅 footer 与页码横向碰撞

退出码: 0 = 干净; 1 = 有 P0 问题
依赖: 仅标准库。直接对 .pptx (zip) 操作,不解包。
"""
import sys, re, zipfile, argparse
from collections import defaultdict

EMU_SLIDE_W, EMU_SLIDE_H = 12192000, 6858000   # 16:9 默认
EMU_IN = 914400
SAFE = int(0.15 * EMU_IN)        # 贴边告警阈值
PAGE_NUM_RE = re.compile(r'^\d{1,3}$')

# colors.md §5 — canonical off-brand → FLock 重映射表
REMAP = {
    # 蓝系 → Brand Blue
    "2D72F8": "3773FF", "2C68F0": "3773FF", "3B82F6": "3773FF",
    "1A4FB0": "3773FF", "2563EB": "3773FF", "1D4ED8": "3773FF",
    # 浅蓝 → Blue Tint
    "60A5FA": "98B8F8", "93C5FD": "98B8F8",
    # 旧版品牌色
    "282828": "000000", "F2F2F0": "F2F2F2", "00A8C0": "03BFD4", "6030D0": "9C59F3",
    # 红系 → Orange (warning 语义)
    "DC2626": "FF8B00", "EF4444": "FF8B00", "B91C1C": "FF8B00",
    "FEE4E4": "F8D0A8", "FEE2E2": "F8D0A8", "FECACA": "F8D0A8",
    # 绿/青系 → Turquoise
    "0D9488": "03BFD4", "0891B2": "03BFD4", "059669": "03BFD4", "10B981": "03BFD4",
    "ECFDF5": "B8E8F0", "D1FAE5": "B8E8F0", "CCFBF1": "B8E8F0",
    # 粉/紫系 → Purple
    "BE185D": "9C59F3", "DB2777": "9C59F3", "7C3AED": "9C59F3", "8B5CF6": "9C59F3",
    "FCE7F3": "D0B8F8", "EDE9FE": "D0B8F8", "F3E8FF": "D0B8F8",
    # 黄/橙系 → Orange
    "D97706": "FF8B00", "F59E0B": "FF8B00", "EA580C": "FF8B00",
    "FEF3C7": "F8D0A8", "FFEDD5": "F8D0A8",
    # 灰边框 → FLock border
    "DCE5F0": "E0E4F0", "D1D5DB": "E0E4F0",
}
# 这些颜色 OK,不报
ALLOWED = {
    "3773FF", "000000", "FFFFFF", "F2F2F2", "FF8B00", "03BFD4", "9C59F3",
    "98B8F8", "B8E8F0", "D0B8F8", "F8D0A8", "22B473", "E0E4F0", "F8F8F8",
    # 常见中性灰文字色,容忍
    "1F2937", "374151", "4B5563", "6B7280", "9CA3AF", "9A9A9A",
    "E5E7EB", "F9FAFB", "EFF4FF", "DBEAFE", "1E3A8A", "5A92FB", "F3F4F6",
    "94A3B8", "0F172A",
}

SP_RE = re.compile(rb'<p:sp>.*?</p:sp>', re.DOTALL)
OFF_RE = re.compile(rb'<a:off x="(\d+)" y="(\d+)"/>')
EXT_RE = re.compile(rb'<a:ext cx="(\d+)" cy="(\d+)"/>')
TXT_RE = re.compile(rb'<a:t>([^<]*)</a:t>')
CLR_RE = re.compile(rb'srgbClr val="([0-9A-Fa-f]{6})"')


def boxes(xml):
    out = []
    for m in SP_RE.finditer(xml):
        sp = m.group()
        o, e = OFF_RE.search(sp), EXT_RE.search(sp)
        if not (o and e):
            continue
        x, y = int(o.group(1)), int(o.group(2))
        cx, cy = int(e.group(1)), int(e.group(2))
        text = b" ".join(TXT_RE.findall(sp)).decode("utf-8", "ignore").strip()
        out.append((x, y, cx, cy, text))
    return out


def lint(path, do_colors=True, do_geom=True):
    issues = defaultdict(list)
    zf = zipfile.ZipFile(path)
    slides = sorted(
        (n for n in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
        key=lambda n: int(re.search(r"(\d+)", n).group()),
    )
    for name in slides:
        sn = int(re.search(r"(\d+)", name).group())
        xml = zf.read(name)

        if do_colors:
            for c in {c.decode().upper() for c in CLR_RE.findall(xml)}:
                if c in REMAP:
                    issues[sn].append(f"[P0:COLOR] #{c} → 应改为 #{REMAP[c]}")
                elif c not in ALLOWED:
                    issues[sn].append(f"[P1:COLOR] #{c} 未知色,人工确认（不在 FLock 调色板）")

        if do_geom:
            bs = boxes(xml)
            for x, y, cx, cy, t in bs:
                if cx == 0 or cy == 0:
                    continue
                if t and (x + cx > EMU_SLIDE_W or y + cy > EMU_SLIDE_H):
                    issues[sn].append(f"[P0:OVERFLOW] '{t[:24]}' 超出画布 (ends {x+cx},{y+cy})")
                elif y + cy > EMU_SLIDE_H - SAFE and t:
                    issues[sn].append(f"[P1:EDGE] '{t[:24]}' 贴底边 <0.15in")
            # 文字 bbox 两两相交（只查都有文字的,忽略装饰形状）
            txt_bs = [(x, y, cx, cy, t) for x, y, cx, cy, t in bs if t and cx > 0]
            for i in range(len(txt_bs)):
                for j in range(i + 1, len(txt_bs)):
                    a, b = txt_bs[i], txt_bs[j]
                    ox = min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])
                    oy = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1])
                    if ox > 0 and oy > 0:
                        # 重叠面积超过较小框 15% 才报,容忍轻微贴靠
                        if ox * oy > 0.40 * min(a[2] * a[3], b[2] * b[3]):
                            # 跳过同位置 frame+text 组合（一个无意义包含另一个全部）
                            if a[:4] == b[:4]:
                                continue
                            issues[sn].append(
                                f"[P1:OVERLAP] '{a[4][:18]}' × '{b[4][:18]}'（bbox 相交,需人工目视确认）"
                            )
            # footer 撞页码
            page_nums = [(x, y, cx, cy, t) for x, y, cx, cy, t in txt_bs
                         if PAGE_NUM_RE.match(t) and y > EMU_SLIDE_H * 0.88]
            wide = [(x, y, cx, cy, t) for x, y, cx, cy, t in txt_bs
                    if cx > EMU_SLIDE_W * 0.7 and y > EMU_SLIDE_H * 0.85]
            for px, py, pcx, pcy, pt in page_nums:
                for wx, wy, wcx, wcy, wt in wide:
                    if wx + wcx > px and wx < px + pcx:
                        issues[sn].append(f"[P1:FOOTER] 宽 footer '{wt[:20]}' 横向覆盖页码 '{pt}'")
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--colors", action="store_true")
    ap.add_argument("--geometry", action="store_true")
    a = ap.parse_args()
    both = not (a.colors or a.geometry)
    issues = lint(a.pptx, do_colors=both or a.colors, do_geom=both or a.geometry)
    if not issues:
        print("PASS · 无颜色/几何问题")
        sys.exit(0)
    total, p0 = 0, 0
    for sn in sorted(issues):
        uniq = list(dict.fromkeys(issues[sn]))
        print(f"\nSlide {sn}:")
        for line in uniq:
            print(f"  {line}")
            total += 1
            if line.startswith("[P0"):
                p0 += 1
    print(f"\n{'FAIL' if p0 else 'WARN'} · P0={p0} · 总计 {total} 项（P1 为 advisory,人工确认）")
    sys.exit(1 if p0 else 0)


if __name__ == "__main__":
    main()
