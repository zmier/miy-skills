#!/usr/bin/env python3
"""Build a restored manuscript draft with table transclusions.

This script intentionally keeps the table restoration conservative:
it preserves raw PDF table text, adds a readable row-level Markdown
reconstruction, and marks complex tables for visual QC.
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path


TASK = Path(__file__).resolve().parents[1]
CASE = TASK.parents[1]
SOURCE_MD = Path("/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.md")
SOURCE_PDF = Path("/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.pdf")
PDF_TEXT = CASE / "tasks" / "TASK03-PDF完整底稿补抽" / "outputs" / "pdf-pages-text.md"

OUT = TASK / "outputs"
TABLE_DIR = OUT / "tables-restored"
LOGS = TASK / "logs"


TABLE_META = {
    1: ("变量定义表", [8], "readable-md-source; page-level-visual-checked"),
    2: ("描述性统计结果", [9], "restored-from-pdf-text; page-level-visual-checked"),
    3: ("事前趋势检验结果", [10], "restored-from-pdf-text; page-level-visual-checked"),
    4: ("多元回归分析结果", [11], "restored-from-pdf-text; page-level-visual-checked"),
    5: ("堆叠 DID 估计", [12], "restored-from-pdf-text; page-level-visual-checked"),
    6: ("匹配回归的结果", [14, 15], "restored-from-pdf-text; cross-page; page-level-visual-checked"),
    7: ("排除共同决定因素干扰的检验", [15, 16], "restored-from-pdf-text; cross-page; page-level-visual-checked"),
    8: ("Oster 检验结果", [16], "restored-from-pdf-text; page-level-visual-checked"),
    9: ("替换变量衡量方式的检验", [17], "restored-from-pdf-text; page-level-visual-checked"),
    10: ("事件公司主动披露违规的短期市场反应", [18], "restored-from-pdf-text; page-level-visual-checked"),
    11: ("基于声誉竞争机制的检验结果", [19, 20], "restored-from-pdf-text; cross-page; page-level-visual-checked; author-prose-conflict"),
    12: ("基于市场压力机制的检验结果", [21], "restored-from-pdf-text; page-level-visual-checked"),
    13: ("基于信息传导机制的检验结果", [22, 23], "restored-from-pdf-text; cross-page; page-level-visual-checked"),
    14: ("基于事件公司行业地位的检验结果", [24, 25], "restored-from-pdf-text; cross-page; page-level-visual-checked"),
    15: ("基于事件公司披露违规主动性的检验结果", [26], "restored-from-pdf-text; page-level-visual-checked"),
    16: ("基于事件公司违规严重程度的检验结果", [27, 28], "restored-from-pdf-text; cross-page; page-level-visual-checked"),
    17: ("基于公司外部融资依赖度的检验结果", [29], "restored-from-pdf-text; page-level-visual-checked"),
    18: ("基于行业竞争程度的检验结果", [30, 31], "restored-from-pdf-text; cross-page; page-level-visual-checked"),
}

VISUAL_QC_NOTES = {
    1: "page-level checked; existing Markdown table retained; cell-level PDF audit not repeated",
    2: "page-level checked; table present on page 9; raw text matches visible table structure",
    3: "page-level checked; table present on page 10; key event-study rows visible",
    4: "page-level checked; table present on page 11; main DID coefficient visible",
    5: "page-level checked; table present on page 12; stack DID coefficient visible",
    6: "cross-page boundary checked on pages 14-15; table tail continues on page 15",
    7: "cross-page boundary checked on pages 15-16; table starts below table 6 tail",
    8: "page-level checked; compact Oster table visible on page 16",
    9: "page-level checked; table present on page 17",
    10: "page-level checked; CAR table visible on page 18",
    11: "cross-page visual checked on pages 19-20; PDF table shows PosCAR[-10,10] is -0.0028 and NegCAR[-10,10] is -0.0168***, which conflicts with author prose",
    12: "page-level checked; market pressure table visible on page 21",
    13: "cross-page/page-level checked on pages 22-23; table appears on page 23 after mechanism prose",
    14: "cross-page boundary checked on pages 24-25; table starts page 24 and continues page 25",
    15: "page-level checked; table visible on page 26",
    16: "cross-page boundary checked on pages 27-28; table starts page 27 and continues page 28",
    17: "page-level checked; table visible on page 29",
    18: "cross-page boundary checked on pages 30-31; table starts page 30 and continues page 31",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def clean_annotation_markup(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"%%.*?%%", "", text, flags=re.S)
    text = re.sub(r"<mark[^>]*>", "", text)
    text = text.replace("</mark>", "")
    text = text.replace("==", "")
    text = re.sub(r"\[\^[^\]]+\]", "", text)
    text = re.sub(r"(表\s*1[： ]变量定义表)\n\n\|.*?(?=\n###|\n##|\Z)", r"\1\n", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def split_pdf_pages(pdf_text: str) -> dict[int, str]:
    pages: dict[int, str] = {}
    matches = list(re.finditer(r"^## PDF Page (\d+)\n\n```text\n", pdf_text, flags=re.M))
    for i, match in enumerate(matches):
        page = int(match.group(1))
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(pdf_text)
        chunk = pdf_text[start:end]
        chunk = re.sub(r"\n```\s*$", "", chunk.strip())
        pages[page] = chunk.strip()
    return pages


def find_table_block_from_pages(pages: dict[int, str], table_no: int) -> str:
    title = TABLE_META[table_no][0]
    caption = f"表 {table_no} {title}"
    page_numbers = TABLE_META[table_no][1]
    merged = "\n".join(pages.get(page, "") for page in page_numbers)
    if table_no == 1:
        source = read(SOURCE_MD)
        source = re.sub(r"%%.*?%%", "", source, flags=re.S)
        source = re.sub(r"<mark[^>]*>", "", source)
        source = source.replace("</mark>", "").replace("==", "")
        source = re.sub(r"\[\^[^\]]+\]", "", source)
        m = re.search(r"表 1[： ]变量定义表\n\n(?P<table>\|.*?)(?:\n###|\n##|\Z)", source, flags=re.S)
        if m:
            return "表 1 变量定义表\n" + m.group("table").strip()
    pos = merged.find(caption)
    if pos < 0:
        pos = merged.find(f"表 {table_no} ")
    if pos < 0:
        return merged.strip()
    block = merged[pos:].strip()

    stop_patterns = [
        r"\n[一二三四五六七八九十]+、",
        r"\n（[一二三四五六七八九十]+）",
        r"\n\d+\.\s",
        r"\n本文",
        r"\n进一步",
        r"\n同时",
        r"\n最后",
        r"\n此外",
        r"\n为",
        r"\n基于",
    ]
    # Keep table notes, but remove obvious prose after the table.
    for pattern in stop_patterns:
        m = re.search(pattern, block[20:])
        if m:
            candidate = block[: 20 + m.start()].strip()
            if len(candidate.splitlines()) >= 5:
                block = candidate
                break
    return block.strip()


def markdown_row_reconstruction(raw: str) -> str:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    md_table_lines = [line for line in lines if line.startswith("|")]
    if len(md_table_lines) >= 2:
        return "\n".join(md_table_lines)
    rows = []
    for line in lines:
        if line.startswith("表 "):
            continue
        parts = re.split(r"\s{2,}|\t+", line)
        if len(parts) == 1:
            pieces = line.split()
            if len(pieces) > 1 and re.search(r"[-+]?\d", pieces[-1]):
                parts = [" ".join(pieces[:-1]), pieces[-1]]
            else:
                parts = [line]
        rows.append(parts)
    max_cols = max((len(row) for row in rows), default=1)
    max_cols = min(max_cols, 8)
    header = ["row"] + [f"col{i}" for i in range(1, max_cols)]
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * max_cols) + " |"]
    for row in rows:
        row = row[:max_cols] + [""] * (max_cols - len(row))
        out.append("| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |")
    return "\n".join(out)


def write_tables(pages: dict[int, str]) -> list[str]:
    inventory = ["# Figures / Tables Inventory", ""]
    insertion = ["# Table Insertion Map", ""]
    for no, (title, page_numbers, status) in TABLE_META.items():
        raw = find_table_block_from_pages(pages, no)
        table_file = TABLE_DIR / f"table-{no:02d}.md"
        pdf_pages = ", ".join(str(p) for p in page_numbers)
        table_md = "\n".join(
            [
                f"# 表 {no} {title}",
                "",
                f"- source_pdf_pages: {pdf_pages}",
                f"- extraction_status: {status}",
                f"- visual_qc_status: page-level visual checked on 2026-06-20",
                f"- visual_qc_note: {VISUAL_QC_NOTES[no]}",
                f"- page_images: {', '.join(f'../page-images/page-{p:02d}.png' for p in page_numbers)}",
                "- restoration_note: 由 PDF 页文本抽取并重建；复杂表格需对照 PDF 视觉复核。",
                "",
                "## Markdown reconstruction",
                "",
                markdown_row_reconstruction(raw),
                "",
                "## Raw PDF table text",
                "",
                "```text",
                raw,
                "```",
                "",
            ]
        )
        write(table_file, table_md)
        inventory.append(f"- 表 {no}：{title}；PDF page {pdf_pages}；status `{status}`；`tables-restored/table-{no:02d}.md`")
        insertion.append(f"- 表 {no}：`![[tables-restored/table-{no:02d}.md]]`")
    write(OUT / "figures-tables-inventory.md", "\n".join(inventory) + "\n")
    write(OUT / "table-insertion-map.md", "\n".join(insertion) + "\n")
    return inventory


def insert_table_transclusions(text: str) -> str:
    for no in sorted(TABLE_META):
        title = TABLE_META[no][0]
        transclusion = f"\n\n![[tables-restored/table-{no:02d}.md]]\n"
        pattern = rf"(表\s*{no}(?:[： ]{re.escape(title)})?)"
        if re.search(pattern, text):
            text = re.sub(pattern, rf"\1{transclusion}", text, count=1)
        else:
            text += f"\n\n## 表 {no} {title}\n{transclusion}\n"
    return text


def build_pdf_page_backup(pdf_text: str) -> str:
    out = [
        "# PDF 页文本备份",
        "",
        f"- source_pdf: `{SOURCE_PDF}`",
        "- note: 这是 TASK03 pdfplumber 页文本的整理备份，用于回查原始抽取；主读稿见 `manuscript_restored_with_tables.md`。",
        "",
        "## 表格文件入口",
        "",
    ]
    for no, (title, _, _) in TABLE_META.items():
        out.append(f"- 表 {no} {title}: ![[tables-restored/table-{no:02d}.md]]")
    out.extend(["", "## Raw Page Text", "", pdf_text.strip(), ""])
    return "\n".join(out)


def build_qc() -> str:
    risky = ", ".join(f"表 {no}" for no, meta in TABLE_META.items() if "needs-table-visual-qc" in meta[2] or "cross-page" in meta[2])
    return f"""# Restoration QC

- date: {date.today().isoformat()}
- source_pdf: `{SOURCE_PDF}`
- readable_markdown_source: `{SOURCE_MD}`
- pdf_page_text_source: `{PDF_TEXT}`
- skill: `scholar-pdf-markdown-restoration`

## 本轮完成

- 已生成带表格嵌入的主底稿：`outputs/manuscript_restored_with_tables.md`
- 已生成 PDF 页文本备份：`outputs/manuscript_pdf_page_text_with_tables.md`
- 已生成表 1 至表 18 的独立表格文件：`outputs/tables-restored/table-01.md` 至 `table-18.md`
- 主底稿中已加入 Obsidian transclusion：`![[tables-restored/table-XX.md]]`
- 已清理现有 Markdown 中的讨论批注、高亮标记和脚注式疑问标记。
- 本轮未拆分 `sections-restored/`：现有主稿章节结构已经清楚，且后续任务需要完整上下文抽取论证树；因此优先保留单文件主底稿。

## 表格还原状态

- 表 1 使用现有 Markdown 表格并保留 PDF QC 标记。
- 表 2 至表 18 使用 TASK03 PDF 页文本抽取结果恢复。
- 已补做表格页图像渲染和页面级视觉复核：`outputs/page-images/page-08.png` 至 `page-31.png`
- 已补做两张表格页总览：`outputs/page-images/contact-08-19.png`、`outputs/page-images/contact-20-31.png`
- 跨页表与版式风险表已做跨页边界视觉确认：{risky}
- 表 11 发现作者正文解释与 PDF 表格本身疑似不一致：正文说三组 PosCAR 显著、NegCAR 不显著；PDF 表格第三列显示 `Peerdumy_PosCAR[-10,10]×POST = -0.0028` 不显著，而 `Peerdumy_NegCAR[-10,10]×POST = -0.0168***` 显著。

## 未完成 / 风险

- 本轮已做页面级视觉复核，但未做每个单元格的人工录入式全量校对。
- 当前 Markdown 表格重建是 row-level readable reconstruction；复杂回归表的精确列对齐仍以 PDF page image 和 `Raw PDF table text` 为准。
- 图像/图 1、图 2尚未做精准裁剪，仅在 PDF 页文本中保留文字线索。
- 该底稿适合进入论证树抽取和证据定位；若用于正式审稿逐句引用，建议先对关键表格做视觉复核。
"""


def build_visual_qc() -> str:
    rows = [
        "# Table Visual QC",
        "",
        "- date: 2026-06-20",
        "- scope: 表 1 至表 18 的页面级视觉复核；跨页表做边界确认；关键风险表 11 做重点核验。",
        "- limitation: 不是逐单元格人工录入式校对；复杂回归表的精确列对齐仍应回查 PDF page image。",
        "",
        "| table | pdf pages | visual status | note |",
        "|---|---:|---|---|",
    ]
    for no, (title, page_numbers, _status) in TABLE_META.items():
        pages = ", ".join(str(p) for p in page_numbers)
        rows.append(f"| 表 {no} {title} | {pages} | page-level checked | {VISUAL_QC_NOTES[no]} |")
    rows.extend(
        [
            "",
            "## Key Finding",
            "",
            "表 11 是本轮视觉复核发现的高价值问题：PDF 表格第三列显示 `Peerdumy_PosCAR[-10,10]×POST = -0.0028`，而 `Peerdumy_NegCAR[-10,10]×POST = -0.0168***`。这与作者正文声称 `PosCAR` 三组均显著、`NegCAR` 三组均不显著不一致。后续论证树与审稿 issue 应把它作为“机制证据与文字叙事不一致”的候选问题。",
            "",
        ]
    )
    return "\n".join(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    source = clean_annotation_markup(read(SOURCE_MD))
    pdf_text = read(PDF_TEXT)
    pages = split_pdf_pages(pdf_text)
    write_tables(pages)
    restored = insert_table_transclusions(source)
    front = [
        "---",
        f"source_pdf: \"{SOURCE_PDF}\"",
        "restoration_task: TASK05-PDF手稿完整Markdown还原",
        "table_policy: tables are transcluded from outputs/tables-restored/table-XX.md",
        "---",
        "",
    ]
    write(OUT / "manuscript_restored_with_tables.md", "\n".join(front) + restored)
    write(OUT / "manuscript_pdf_page_text_with_tables.md", build_pdf_page_backup(pdf_text))
    write(LOGS / "table-visual-qc.md", build_visual_qc())
    write(LOGS / "restoration-qc.md", build_qc())


if __name__ == "__main__":
    main()
