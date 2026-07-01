from __future__ import annotations

import hashlib
import json
import os
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlsplit

from mitmproxy import http


TARGET_HOST = os.environ.get("MITM_TARGET_HOST", "")
TARGET_PATH = os.environ.get("MITM_TARGET_PATH", "/")
EVENT_FILE = Path(os.environ["MITM_EVENT_FILE"])


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def matches(flow: http.HTTPFlow) -> bool:
    host_ok = not TARGET_HOST or flow.request.pretty_host == TARGET_HOST
    if not host_ok:
        return False
    if not TARGET_PATH or TARGET_PATH == "/":
        return True
    return normalized_path(flow.request.path).startswith(TARGET_PATH)


def normalized_path(path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        parsed = urlsplit(path)
        return parsed.path or "/"
    return path


def header_names(headers: http.Headers) -> list[str]:
    return sorted({key.lower() for key, _ in headers.items(multi=True)})


def query_keys(flow: http.HTTPFlow) -> list[str]:
    return sorted(flow.request.query.keys())


def append(record: dict[str, object]) -> None:
    EVENT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with EVENT_FILE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def request(flow: http.HTTPFlow) -> None:
    if not matches(flow):
        return
    body = flow.request.raw_content or b""
    append(
        {
            "event": "request",
            "captured_at": datetime.now(UTC).isoformat(),
            "flow_id": flow.id,
            "method": flow.request.method,
            "scheme": flow.request.scheme,
            "host": flow.request.pretty_host,
            "path": normalized_path(flow.request.path).split("?", 1)[0],
            "query_keys": query_keys(flow),
            "header_names": header_names(flow.request.headers),
            "body_length": len(body),
            "body_sha256": digest(body),
        }
    )


def response(flow: http.HTTPFlow) -> None:
    if not matches(flow) or flow.response is None:
        return
    body = flow.response.raw_content or b""
    append(
        {
            "event": "response",
            "captured_at": datetime.now(UTC).isoformat(),
            "flow_id": flow.id,
            "status_code": flow.response.status_code,
            "header_names": header_names(flow.response.headers),
            "body_length": len(body),
            "body_sha256": digest(body),
        }
    )


def error(flow: http.HTTPFlow) -> None:
    if not matches(flow) or flow.error is None:
        return
    append(
        {
            "event": "error",
            "captured_at": datetime.now(UTC).isoformat(),
            "flow_id": flow.id,
            "method": flow.request.method,
            "scheme": flow.request.scheme,
            "host": flow.request.pretty_host,
            "path": normalized_path(flow.request.path).split("?", 1)[0],
            "error": str(flow.error),
        }
    )
