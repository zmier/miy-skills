from __future__ import annotations

import importlib.util
import os
from pathlib import Path

from mitmproxy import http


ROOT = Path(__file__).resolve().parents[2]
ADDON = (
    ROOT
    / "skills"
    / "process-android-traffic"
    / "scripts"
    / "target_capture_addon.py"
)
os.environ.setdefault("MITM_EVENT_FILE", "/tmp/mitm-addon-test.jsonl")
SPEC = importlib.util.spec_from_file_location("target_capture_addon", ADDON)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def test_header_values_are_never_exported() -> None:
    # GIVEN：请求头含 Cookie、Token 和带邮箱的 User-Agent。
    headers = http.Headers(
        cookie="session=secret",
        authorization="Bearer secret",
        **{"user-agent": "agent user@example.com"},
    )

    # WHEN：生成可导出的头部信息。
    result = module.header_names(headers)

    # THEN：只保留字段名，不出现任何字段值。
    assert result == ["authorization", "cookie", "user-agent"]
    assert "secret" not in repr(result)
    assert "example.com" not in repr(result)


def test_query_keys_support_mitmproxy_multidict_view() -> None:
    # GIVEN：真实 mitmproxy Request 使用 MultiDictView 表示重复查询参数。
    flow = http.HTTPFlow(
        None,
        None,
    )
    flow.request = http.Request.make(
        "GET",
        "https://example.com/?aid=1&aid=2&cid=",
    )

    # WHEN：提取查询参数结构。
    result = module.query_keys(flow)

    # THEN：只保留去重后的字段名，不泄漏参数值。
    assert result == ["aid", "cid"]
    assert "1" not in repr(result)
    assert "2" not in repr(result)


def test_target_path_root_matches_absolute_proxy_form() -> None:
    # GIVEN：HTTP 正向代理明文请求可能以 absolute-form 保存 path。
    flow = http.HTTPFlow(None, None)
    flow.request = http.Request.make(
        "GET",
        "http://example.com/generate_204",
    )
    flow.request.path = "http://example.com/generate_204"

    # WHEN：目标路径为根路径。
    old_target_path = module.TARGET_PATH
    module.TARGET_PATH = "/"
    try:
        result = module.matches(flow)
    finally:
        module.TARGET_PATH = old_target_path

    # THEN：不应误过滤基础连通性探针。
    assert result is True


def test_normalized_path_removes_absolute_url_origin() -> None:
    # GIVEN：mitmproxy 记录了 absolute-form URL。
    path = "http://example.com/a/b?token=secret"

    # WHEN：归一化路径。
    result = module.normalized_path(path)

    # THEN：只保留路径结构，便于过滤和导出。
    assert result == "/a/b"
