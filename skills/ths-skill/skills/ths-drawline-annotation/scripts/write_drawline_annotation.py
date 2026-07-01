#!/usr/bin/env python3
"""Append a DrawLine annotation XML entry with backup and dry-run support."""

from __future__ import annotations

import argparse
import shutil
import time
import xml.etree.ElementTree as ET
from pathlib import Path


CONTAINER_DATA = Path.home() / "Library/Containers/cn.com.10jqka.macstock/Data"
TYPE_PRESETS = {
    "text": {"LineName": "文字工具", "LineType": "67", "Option": "0010", "Color": 44794, "points": 2},
    "note": {"LineName": "标注", "LineType": "68", "Option": "0010", "Color": 0, "points": 2},
    "hline": {"LineName": "水平线", "LineType": "54", "Option": "0000", "Color": 44794, "points": 1},
    "rect": {"LineName": "矩形", "LineType": "20", "Option": "0010", "Color": 44794, "points": 2},
    "up-arrow": {"LineName": "上涨箭头", "LineType": "21", "Option": "0000", "Color": 0, "points": 1},
    "down-arrow": {"LineName": "下跌箭头", "LineType": "40", "Option": "0000", "Color": 16724740, "points": 1},
}


def find_account_dir(base: Path, account_dir: str | None) -> Path:
    if account_dir:
        path = base / account_dir
        if not path.exists():
            raise SystemExit(f"account_dir_not_found={path}")
        return path
    candidates = sorted(base.glob("mx_*"))
    candidates = [p for p in candidates if (p / "DrawLine_New").exists()]
    if len(candidates) != 1:
        raise SystemExit(f"account_dir_ambiguous={','.join(str(p) for p in candidates)}")
    return candidates[0]


def load_or_create(path: Path) -> ET.Element:
    if not path.exists():
        return ET.Element("DrawLineData")
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


def drawline_attrs(args: argparse.Namespace, preset: dict) -> dict[str, str]:
    text = args.text or ""
    if text and not text.endswith("\\r\\n\\r\\n"):
        text = text + "\\r\\n\\r\\n"
    return {
        "Option": args.option or preset["Option"],
        "WordClr": str(args.word_color),
        "LineName": args.line_name or preset["LineName"],
        "Show": "1",
        "TextContent": text,
        "Color": str(args.color if args.color is not None else preset["Color"]),
        "WordInfo": str(args.word_info),
        "Width": f"{args.width:.6f}",
        "LineType": str(args.line_type or preset["LineType"]),
        "BKColor": str(args.background_color),
    }


def point_attrs(open_price: float, x_data: str, y_data: float, x_time: str) -> dict[str, str]:
    return {
        "OpenPrice": f"{open_price:.6f}",
        "XData": x_data,
        "YDataType": "20480",
        "YData": f"{y_data:.6f}",
        "XTime": x_time,
        "Active": "1",
    }


def resolve_second_xdata(args: argparse.Namespace) -> str:
    if args.second_xdata is not None:
        return args.second_xdata
    if not args.second_date or args.second_date == args.date:
        return "0"
    raise SystemExit(
        "second_xdata_required_for_cross_date_shape="
        f"kind:{args.kind},date:{args.date},second_date:{args.second_date}"
    )


def validate_args(args: argparse.Namespace, preset: dict) -> None:
    if args.kind in {"text", "note"} and not args.text:
        raise SystemExit(f"text_required_for_kind={args.kind}")
    if preset["points"] < 2:
        return
    if args.kind == "text":
        return
    missing = []
    if not args.second_date:
        missing.append("--second-date")
    if args.second_price is None:
        missing.append("--second-price")
    if missing:
        raise SystemExit(f"missing_required_for_kind_{args.kind}={','.join(missing)}")


def append_annotation(root: ET.Element, args: argparse.Namespace) -> ET.Element:
    preset = TYPE_PRESETS[args.kind]
    validate_args(args, preset)
    dl = ET.SubElement(root, "DrawLine", drawline_attrs(args, preset))
    ET.SubElement(dl, "KeyPoint", point_attrs(args.open_price, args.date, args.price, "0"))
    if preset["points"] >= 2:
        second_date = args.second_date or args.date
        second_price = args.second_price if args.second_price is not None else args.price
        second_open_price = args.second_open_price if args.second_open_price is not None else args.open_price
        ET.SubElement(
            dl,
            "KeyPoint",
            point_attrs(
                second_open_price,
                resolve_second_xdata(args),
                second_price,
                second_date,
            ),
        )
    return dl


def xml_bytes(root: ET.Element) -> bytes:
    indent(root)
    body = ET.tostring(root, encoding="unicode", short_empty_elements=False)
    return ('<?xml version="1.0" encoding="GB2312"?>\n' + body).encode("gb2312")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--container-data", default=str(CONTAINER_DATA))
    parser.add_argument("--account-dir")
    parser.add_argument("--market-code", required=True)
    parser.add_argument("--stock-code", required=True)
    parser.add_argument("--period-code", default="16384")
    parser.add_argument("--suffix", default="C09C8")
    parser.add_argument("--kind", choices=sorted(TYPE_PRESETS), default="text")
    parser.add_argument("--text")
    parser.add_argument("--date", "--anchor-date", dest="date", required=True, help="Anchor date, e.g. 20260513")
    parser.add_argument("--price", "--anchor-price", dest="price", type=float, required=True)
    parser.add_argument("--open-price", "--anchor-open-price", dest="open_price", type=float, required=True)
    parser.add_argument("--second-date", "--end-date", "--box-date", dest="second_date")
    parser.add_argument("--second-xdata", "--end-xdata", "--box-xdata", dest="second_xdata")
    parser.add_argument("--second-price", type=float)
    parser.add_argument("--end-price", "--box-price", dest="second_price", type=float)
    parser.add_argument("--second-open-price", type=float)
    parser.add_argument("--end-open-price", "--box-open-price", dest="second_open_price", type=float)
    parser.add_argument("--color", type=int)
    parser.add_argument("--word-color", type=int, default=255)
    parser.add_argument("--background-color", type=int, default=5250560)
    parser.add_argument("--word-info", type=int, default=1310720)
    parser.add_argument("--width", type=float, default=1.0)
    parser.add_argument("--line-name")
    parser.add_argument("--line-type", type=int)
    parser.add_argument("--option")
    parser.add_argument("--write", action="store_true", help="Actually write file. Default is dry-run.")
    args = parser.parse_args()

    base = Path(args.container_data).expanduser()
    account = find_account_dir(base, args.account_dir)
    out_dir = account / "DrawLine_New" / f"{args.market_code}_{args.stock_code}"
    out_file = out_dir / f"{args.period_code}_{args.suffix}.xml"
    root = load_or_create(out_file)
    new_entry = append_annotation(root, args)
    data = xml_bytes(root)

    print(f"target={out_file}")
    print(f"mode={'write' if args.write else 'dry-run'}")
    print(f"entry={ET.tostring(new_entry, encoding='unicode', short_empty_elements=False)}")
    if not args.write:
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)
    if out_file.exists():
        backup = out_file.with_suffix(out_file.suffix + f".bak-{time.strftime('%Y%m%d-%H%M%S')}")
        shutil.copy2(out_file, backup)
        print(f"backup={backup}")
    out_file.write_bytes(data)
    print(f"wrote={out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
