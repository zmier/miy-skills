#!/usr/bin/env python3
"""List or remove DrawLine XML annotations with backup."""

from __future__ import annotations

import argparse
import shutil
import time
import xml.etree.ElementTree as ET
from pathlib import Path


CONTAINER_DATA = Path.home() / "Library/Containers/cn.com.10jqka.macstock/Data"


def find_account_dir(base: Path, account_dir: str | None) -> Path:
    if account_dir:
        path = base / account_dir
        if not path.exists():
            raise SystemExit(f"account_dir_not_found={path}")
        return path
    candidates = sorted(p for p in base.glob("mx_*") if (p / "DrawLine_New").exists())
    if len(candidates) != 1:
        raise SystemExit(f"account_dir_ambiguous={','.join(str(p) for p in candidates)}")
    return candidates[0]


def xml_path(args: argparse.Namespace) -> Path:
    base = Path(args.container_data).expanduser()
    account = find_account_dir(base, args.account_dir)
    return account / "DrawLine_New" / f"{args.market_code}_{args.stock_code}" / f"{args.period_code}_{args.suffix}.xml"


def load_xml(path: Path) -> ET.Element:
    data = path.read_bytes()
    for enc in ("gb2312", "gb18030", "utf-8"):
        try:
            return ET.fromstring(data.decode(enc))
        except Exception:
            continue
    raise SystemExit(f"xml_decode_failed={path}")


def indent(elem: ET.Element, level: int = 0) -> None:
    pad = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = pad + "  "
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = pad
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = pad


def write_xml(path: Path, root: ET.Element) -> Path:
    backup = path.with_suffix(path.suffix + f".bak-{time.strftime('%Y%m%d-%H%M%S')}")
    shutil.copy2(path, backup)
    indent(root)
    body = ET.tostring(root, encoding="unicode", short_empty_elements=False)
    path.write_bytes(('<?xml version="1.0" encoding="GB2312"?>\n' + body).encode("gb2312"))
    return backup


def text_preview(value: str) -> str:
    return value.replace("\r", "\\r").replace("\n", "\\n")


def point_date(point: dict[str, str]) -> str:
    x_time = point.get("XTime", "")
    if x_time and x_time != "0":
        return x_time
    return point.get("XData", "")


def point_summary(point: dict[str, str]) -> str:
    pieces = [
        f"date={point_date(point)}",
        f"xdata={point.get('XData', '')}",
        f"xtime={point.get('XTime', '')}",
        f"y={point.get('YData', '')}",
        f"open={point.get('OpenPrice', '')}",
    ]
    return ", ".join(pieces)


def non_empty_points(line: ET.Element) -> list[dict[str, str]]:
    return [point.attrib for point in line.findall("KeyPoint") if point.attrib]


def list_annotations(root: ET.Element, verbose: bool) -> None:
    lines = root.findall("DrawLine")
    print(f"drawline_count={len(lines)}")
    for idx, line in enumerate(lines, 1):
        points = non_empty_points(line)
        print(
            f"{idx}\tLineName={line.attrib.get('LineName')}\t"
            f"LineType={line.attrib.get('LineType')}\t"
            f"Option={line.attrib.get('Option')}\t"
            f"Color={line.attrib.get('Color')}\t"
            f"Width={line.attrib.get('Width')}\t"
            f"TextContent={text_preview(line.attrib.get('TextContent', ''))!r}\t"
            f"PointCount={len(points)}"
        )
        for point_idx, point in enumerate(points, 1):
            if verbose:
                print(f"  P{point_idx}\t{point}")
            else:
                print(f"  P{point_idx}\t{point_summary(point)}")


def remove_by_text(root: ET.Element, text: str) -> int:
    removed = 0
    for line in list(root.findall("DrawLine")):
        if text in line.attrib.get("TextContent", ""):
            root.remove(line)
            removed += 1
    return removed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["list", "remove-text"])
    parser.add_argument("--container-data", default=str(CONTAINER_DATA))
    parser.add_argument("--account-dir")
    parser.add_argument("--market-code", required=True)
    parser.add_argument("--stock-code", required=True)
    parser.add_argument("--period-code", default="16384")
    parser.add_argument("--suffix", default="C09C8")
    parser.add_argument("--text")
    parser.add_argument("--verbose", action="store_true", help="Print raw KeyPoint dictionaries when listing.")
    parser.add_argument("--write", action="store_true", help="Actually mutate file. Default is dry-run for remove.")
    args = parser.parse_args()

    path = xml_path(args)
    if not path.exists():
        raise SystemExit(f"xml_not_found={path}")
    root = load_xml(path)
    print(f"target={path}")

    if args.command == "list":
        list_annotations(root, args.verbose)
        return 0

    if not args.text:
        raise SystemExit("--text is required for remove-text")
    removed = remove_by_text(root, args.text)
    print(f"removed={removed}")
    print(f"mode={'write' if args.write else 'dry-run'}")
    if args.write and removed:
        backup = write_xml(path, root)
        print(f"backup={backup}")
        print(f"wrote={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
