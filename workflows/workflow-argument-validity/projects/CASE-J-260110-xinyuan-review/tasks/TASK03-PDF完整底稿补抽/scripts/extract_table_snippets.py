from __future__ import annotations

from pathlib import Path


TASK_DIR = Path("/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK03-PDF完整底稿补抽")
TEXT_PATH = TASK_DIR / "outputs" / "pdf-pages-text.md"
OUT_PATH = TASK_DIR / "outputs" / "table-text-snippets.md"

KEYWORDS = [
    "表 2", "表 3", "表 4", "表 5", "表 6", "表 7", "表 8", "表 9",
    "表 10", "表 11", "表 12", "表 13", "表 14", "表 15", "表 16", "表 17", "表 18",
    "Peerdumy", "POST", "CAR", "KV", "标准误", "聚类", "注：", "***", "**", "*",
]


def main() -> None:
    text = TEXT_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    hit_indexes: set[int] = set()
    for i, line in enumerate(lines):
        if any(k in line for k in KEYWORDS):
            for j in range(max(0, i - 5), min(len(lines), i + 9)):
                hit_indexes.add(j)

    parts = ["# Table Text Snippets", "", "从 `pdf-pages-text.md` 中按表格/系数关键词抽取的上下文片段。该文件不是视觉核验表格，使用精确数值前仍需回 PDF 复核。", ""]
    last = -10
    for idx in sorted(hit_indexes):
        if idx > last + 1:
            parts.append("\n---\n")
        parts.append(f"{idx + 1}: {lines[idx]}")
        last = idx

    OUT_PATH.write_text("\n".join(parts) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
