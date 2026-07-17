#!/usr/bin/env python3
"""Scan local file timestamps and classify daily activity by project/task."""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


EXCLUDED_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".cache"}
ACTIVITY_EXTS = {
    ".md", ".txt", ".doc", ".docx", ".pdf", ".rtf", ".tex", ".qmd", ".ppt", ".pptx",
    ".xls", ".xlsx", ".csv", ".tsv", ".json", ".yaml", ".yml", ".html", ".htm",
    ".ipynb", ".py", ".sh", ".swift", ".plist",
}
DOC_EXTS = {".md", ".txt", ".doc", ".docx", ".pdf", ".rtf", ".tex", ".qmd", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".tsv", ".json", ".yaml", ".yml", ".html", ".htm", ".ipynb"}


def local_day(ts: float, tz: ZoneInfo) -> date:
    return datetime.fromtimestamp(ts, tz).date()


def local_hour(ts: float, tz: ZoneInfo) -> int:
    return datetime.fromtimestamp(ts, tz).hour


def project_and_task(rel: Path) -> tuple[str, str | None]:
    parts = rel.parts
    if len(parts) >= 3 and parts[0] == "03 Projects":
        project = parts[1]
    else:
        project = "项目外/未归属项目"
    task = None
    if project != "项目外/未归属项目":
        for i, part in enumerate(parts[:-1]):
            if part == "tasks":
                task = parts[i + 1]
                break
    return project, task


def unassigned_topic(rel: Path) -> str:
    """Infer a cautious topic from path structure without reading file contents."""
    parts = rel.parts
    if not parts:
        return "其他"
    if parts[0] == "00 信息":
        if len(parts) >= 4 and parts[1] == "miy-skills":
            return f"技能/工作流维护：{parts[3]}"
        if len(parts) >= 3 and parts[1] == "工具":
            return f"工具维护：{parts[2]}"
        return f"00 信息/{parts[1]}" if len(parts) >= 2 else "00 信息"
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return parts[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--timezone", default="Asia/Shanghai")
    ap.add_argument("--max-samples", type=int, default=5)
    ap.add_argument("--include-files", action="store_true", help="include every matching file record")
    args = ap.parse_args()

    target = date.fromisoformat(args.date)
    tz = ZoneInfo(args.timezone)
    root = Path(args.root).expanduser().resolve()
    records: list[dict] = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for filename in filenames:
            path = Path(dirpath) / filename
            if path.suffix.lower() not in ACTIVITY_EXTS:
                continue
            try:
                st = path.stat()
            except OSError:
                continue
            created = local_day(getattr(st, "st_birthtime", st.st_ctime), tz) == target
            modified = local_day(st.st_mtime, tz) == target
            if not (created or modified):
                continue
            rel = path.relative_to(root)
            project, task = project_and_task(rel)
            topic = unassigned_topic(rel) if project == "项目外/未归属项目" else None
            records.append({
                "path": str(rel),
                "extension": path.suffix.lower(),
                "is_markdown": path.suffix.lower() == ".md",
                "created": created,
                "modified": modified,
                "hour": local_hour(st.st_mtime, tz) if modified else None,
                "project": project,
                "task": task,
                "topic": topic,
            })

    def count(predicate) -> int:
        return sum(1 for r in records if predicate(r))

    markdown = [r for r in records if r["is_markdown"]]
    modified = [r for r in records if r["modified"]]
    created = [r for r in records if r["created"]]
    both = [r for r in records if r["created"] and r["modified"]]
    by_project: dict[str, dict] = {}
    for project in sorted({r["project"] for r in records}):
        rows = [r for r in records if r["project"] == project]
        by_project[project] = {
            "files": len(rows),
            "markdown_created": count(lambda r, p=project: r["project"] == p and r["is_markdown"] and r["created"]),
            "markdown_modified": count(lambda r, p=project: r["project"] == p and r["is_markdown"] and r["modified"]),
            "tasks": dict(sorted(Counter(r["task"] for r in rows if r["task"]).items())),
            "topics": dict(sorted(Counter(r["topic"] for r in rows if r["topic"]).items())),
        }

    hourly: dict[str, dict] = {}
    for hour in sorted({r["hour"] for r in modified if r["hour"] is not None}):
        rows = [r for r in modified if r["hour"] == hour]
        groups = Counter((r["project"], r["task"] or r["topic"] or "项目级/其他") for r in rows)
        samples = defaultdict(list)
        for r in rows:
            key = f'{r["project"]}｜{r["task"] or r["topic"] or "项目级/其他"}'
            if len(samples[key]) < args.max_samples:
                samples[key].append(r["path"])
        hourly[f"{hour:02d}:00-{hour:02d}:59"] = {
            "files": len(rows),
            "groups": [{"project": p, "label": t, "files": n} for (p, t), n in sorted(groups.items())],
            "samples": dict(samples),
        }

    output = {
        "date": args.date,
        "timezone": args.timezone,
        "root": str(root),
        "counts": {
            "all_activity_files": len(records),
            "created_files": len(created),
            "modified_files": len(modified),
            "created_and_modified_files": len(both),
            "created_only_files": count(lambda r: r["created"] and not r["modified"]),
            "modified_only_files": count(lambda r: r["modified"] and not r["created"]),
            "markdown_created": sum(r["is_markdown"] for r in created),
            "markdown_modified": sum(r["is_markdown"] for r in modified),
            "markdown_created_and_modified": sum(r["is_markdown"] for r in both),
        },
        "projects": by_project,
        "hourly_modified_activity": hourly,
    }
    if args.include_files:
        output["files"] = records
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
