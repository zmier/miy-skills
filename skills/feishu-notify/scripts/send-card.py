#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def find_alib_root() -> Path:
    if os.getenv("ALIB_SOURCE"):
        return Path(os.environ["ALIB_SOURCE"]).expanduser().resolve()

    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        candidate = parent / "Writer" / ".pytools" / "scholar-kit" / "src"
        if candidate.exists():
            return parent
    raise SystemExit("未找到 alib 根目录；请设置 ALIB_SOURCE。")


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a Feishu interactive card.")
    parser.add_argument("title", help="卡片标题")
    parser.add_argument("message", help="卡片正文，支持飞书 lark_md")
    parser.add_argument("--button-text", default="收到", help="按钮文案")
    parser.add_argument("--reply-text", default=None, help="点击按钮后自动回复的文本")
    parser.add_argument("--action-name", default="acknowledge", help="按钮 action 名称")
    parser.add_argument("--action-json", default=None, help="附加 action JSON 对象")
    parser.add_argument("--user-id", default=None, help="覆盖 FEISHU_USER_ID")
    parser.add_argument("--open-id", default=None, help="使用 open_id 接收")
    parser.add_argument("--chat-id", default=None, help="发送到群聊 chat_id")
    args = parser.parse_args()

    alib_root = find_alib_root()
    src_dir = alib_root / "Writer" / ".pytools" / "scholar-kit" / "src"
    sys.path.insert(0, str(src_dir))

    from scholar_kit.utils.notify import feishu_notify

    action_value = None
    if args.action_json:
        try:
            action_value = json.loads(args.action_json)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"--action-json 不是合法 JSON：{exc}") from exc
        if not isinstance(action_value, dict):
            raise SystemExit("--action-json 必须是 JSON object。")

    ok = feishu_notify(
        text=args.message,
        title=args.title,
        button_text=args.button_text,
        reply_text=args.reply_text,
        action_name=args.action_name,
        action_value=action_value,
        user_id=args.user_id,
        open_id=args.open_id,
        chat_id=args.chat_id,
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
