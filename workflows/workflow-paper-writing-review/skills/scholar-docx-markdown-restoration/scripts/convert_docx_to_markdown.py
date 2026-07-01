#!/usr/bin/env python3
"""
Convert a scholarly DOCX manuscript to raw Markdown plus media assets.

This script is intentionally light: it performs reproducible extraction and
basic inventory only. Restoration, paragraph indexing, and QC remain workflow
steps governed by SKILL.md.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile


def run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit(proc.returncode)


def docx_inventory(docx: Path) -> dict[str, object]:
    with ZipFile(docx) as zf:
        names = zf.namelist()
        document_xml = zf.read("word/document.xml").decode("utf-8", errors="ignore")
        media = [name for name in names if name.startswith("word/media/")]
        return {
            "docx": str(docx),
            "paragraph_xml_count": document_xml.count("<w:p"),
            "table_xml_count": document_xml.count("<w:tbl"),
            "media_count": len(media),
            "media_files": media,
            "has_footnotes": "word/footnotes.xml" in names,
            "has_endnotes": "word/endnotes.xml" in names,
            "has_comments": "word/comments.xml" in names,
        }


def should_number_block(block: str) -> bool:
    stripped = block.strip()
    if not stripped:
        return False
    plain = re.sub(r"<[^>]+>", "", stripped)
    plain = re.sub(r"[*_`\\]", "", plain).strip()
    plain_lower = plain.lower()
    if plain_lower.startswith("fiber-shaped,"):
        return False
    if plain_lower.startswith(("keywords:", "corresponding author:")):
        return False
    if re.match(r"^\d+\s+[A-Z][A-Za-z ,:/()-]+$", plain):
        return False
    if re.match(r"^\d+\.\d+\s+", plain):
        return False
    if re.match(r"^fig\.?\s*\d+", plain_lower):
        return False
    if plain_lower in {
        "credit authorship contribution statement",
        "declaration of competing interest",
        "acknowledgements",
        "acknowledgments",
        "data availability",
        "reference",
        "references",
    }:
        return False
    if re.match(r"^\[\d+\]", plain):
        return False
    if re.match(r"^<sup>\d+</sup>", stripped):
        return False
    if "corresponding author" in plain_lower and "@" in plain_lower:
        return False
    if re.search(r"<img\b", stripped):
        return False
    if stripped.startswith("#"):
        return False
    if stripped.startswith("![](") or stripped.startswith("!["):
        return False
    if stripped.startswith("[^") and "]:" in stripped.splitlines()[0]:
        return False
    if stripped.startswith("|"):
        return False
    if stripped.startswith("```"):
        return False
    if stripped.startswith("$$"):
        return False
    if re.match(r"^[-*+]\s+", stripped):
        return False
    if re.match(r"^\d+[.)]\s+", stripped):
        return False
    if stripped.lower().startswith(("references", "acknowledg", "funding", "data availability", "conflict of interest")):
        return False
    return True


def add_paragraph_indices(raw_markdown: str) -> tuple[str, int]:
    blocks = re.split(r"\n\s*\n", raw_markdown.strip())
    numbered: list[str] = []
    para_id = 0
    back_matter = False
    before_abstract = True
    for block in blocks:
        clean = block.strip()
        plain = re.sub(r"<[^>]+>", "", clean)
        plain = re.sub(r"[*_`\\]", "", plain).strip().lower()
        is_abstract = plain.startswith("abstract:")
        if is_abstract:
            before_abstract = False
        if plain in {
            "credit authorship contribution statement",
            "declaration of competing interest",
            "acknowledgements",
            "acknowledgments",
            "data availability",
            "reference",
            "references",
        }:
            back_matter = True
        if (not before_abstract) and (not back_matter) and should_number_block(clean):
            para_id += 1
            numbered.append(f"[para {para_id}] {clean}")
        else:
            numbered.append(clean)
    return "\n\n".join(numbered).rstrip() + "\n", para_id


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--outdir", type=Path, default=Path("outputs"))
    parser.add_argument("--pandoc", default="pandoc")
    args = parser.parse_args()

    docx = args.docx.expanduser().resolve()
    outdir = args.outdir.expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    media_dir = outdir / "media"
    raw_md = outdir / "manuscript_raw.md"
    restored_md = outdir / "manuscript_restored.md"
    inventory_json = outdir / "docx-inventory.json"

    info = docx_inventory(docx)
    inventory_json.write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")

    cmd = [
        args.pandoc,
        "--from=docx",
        "--to=gfm",
        "--wrap=none",
        f"--extract-media={media_dir}",
        str(docx),
        "-o",
        str(raw_md),
    ]
    run(cmd)

    raw_text = raw_md.read_text(encoding="utf-8")
    restored_text, para_count = add_paragraph_indices(raw_text)
    restored_md.write_text(restored_text, encoding="utf-8")

    print(json.dumps({
        "raw_markdown": str(raw_md),
        "restored_markdown_initial": str(restored_md),
        "paragraph_count_initial": para_count,
        "media_dir": str(media_dir),
        "inventory": str(inventory_json),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
