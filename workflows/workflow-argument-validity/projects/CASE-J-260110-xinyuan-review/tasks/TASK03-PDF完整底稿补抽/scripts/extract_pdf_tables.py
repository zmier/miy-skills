from __future__ import annotations

import re
from pathlib import Path

import pdfplumber


PDF_PATH = Path("/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.pdf")
TASK_DIR = Path("/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK03-PDF完整底稿补抽")
OUT_DIR = TASK_DIR / "outputs"
TABLE_DIR = OUT_DIR / "tables"


def clean_cell(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    text = text.replace("\n", "<br>")
    text = re.sub(r"\s+", " ", text).strip()
    return text.replace("|", "\\|")


def to_markdown_table(rows: list[list[object]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    normalized = [list(row) + [""] * (width - len(row)) for row in rows]
    header = [clean_cell(cell) or f"col{i+1}" for i, cell in enumerate(normalized[0])]
    body = normalized[1:]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(clean_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def likely_caption(lines: list[str], table_index: int) -> str:
    table_pat = re.compile(r"(表|Table)\s*[\d一二三四五六七八九十]+")
    for line in lines:
        if table_pat.search(line):
            return line.strip()
    return f"table-{table_index:02d}"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)

    page_text_parts: list[str] = ["# PDF Pages Text\n"]
    inventory_rows = [
        "| table_id | pdf_page | caption_candidate | rows | cols | output | status |",
        "|---|---:|---|---:|---:|---|---|",
    ]
    qc_rows = [
        "# Restoration QC\n",
        "## Source\n",
        f"- PDF: `{PDF_PATH}`",
        "- extractor: `pdfplumber`",
        "",
        "## Table Extraction Notes\n",
        "| item | status | note |",
        "|---|---|---|",
    ]

    table_counter = 0
    with pdfplumber.open(str(PDF_PATH)) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            page_text_parts.append(f"\n## PDF Page {page_number}\n\n```text\n{text}\n```\n")

            tables = page.extract_tables() or []
            if not tables:
                continue

            caption = likely_caption(lines, table_counter + 1)
            for table in tables:
                if not table or len(table) < 2:
                    continue
                table_counter += 1
                rows = len(table)
                cols = max(len(row) for row in table)
                safe_caption = re.sub(r"[^0-9A-Za-z一-龥_-]+", "-", caption)[:40].strip("-") or f"table-{table_counter:02d}"
                table_file = TABLE_DIR / f"table-{table_counter:02d}-p{page_number}-{safe_caption}.md"
                md = [
                    f"# Table {table_counter:02d}",
                    "",
                    f"- pdf_page: {page_number}",
                    f"- caption_candidate: {caption}",
                    f"- extraction_status: needs-table-visual-qc",
                    "",
                    to_markdown_table(table),
                    "",
                ]
                table_file.write_text("\n".join(md), encoding="utf-8")
                inventory_rows.append(
                    f"| T{table_counter:02d} | {page_number} | {clean_cell(caption)} | {rows} | {cols} | `{table_file.relative_to(OUT_DIR)}` | needs-table-visual-qc |"
                )
                qc_rows.append(
                    f"| T{table_counter:02d} | needs-table-visual-qc | pdfplumber extracted {rows} rows x {cols} cols on page {page_number}; compare against PDF before using exact values. |"
                )

    (OUT_DIR / "pdf-pages-text.md").write_text("\n".join(page_text_parts), encoding="utf-8")
    (OUT_DIR / "pdf-table-inventory.md").write_text("# PDF Table Inventory\n\n" + "\n".join(inventory_rows) + "\n", encoding="utf-8")
    qc_rows.append(f"| total_tables | info | extracted {table_counter} candidate tables. |")
    (OUT_DIR / "restoration-qc.md").write_text("\n".join(qc_rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
