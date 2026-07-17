#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import requests
except ModuleNotFoundError as exc:
    requests = None  # type: ignore[assignment]
    REQUESTS_IMPORT_ERROR = exc
else:
    REQUESTS_IMPORT_ERROR = None


API_ROOT = "https://upload.chaojiying.net/Upload"
PROCESSING_URL = f"{API_ROOT}/Processing.php"
REPORT_ERROR_URL = f"{API_ROOT}/ReportError.php"
GET_SCORE_URL = f"{API_ROOT}/GetScore.php"
MAX_IMAGE_BYTES = 2 * 1024 * 1024
DEFAULT_CODETYPE = "1902"

PASSWORD_MD5_RE = re.compile(r"^[a-f0-9]{32}$")
CODETYPE_RE = re.compile(r"^\d+$")
IMAGE_MAGIC = {
    b"\xff\xd8\xff": "jpg",
    b"BM": "bmp",
    b"\x89PNG\r\n\x1a\n": "png",
}


class ChaojiyingCliError(RuntimeError):
    """User-facing error for this CLI."""


def md5_lower(value: str) -> str:
    return hashlib.md5(value.encode("utf-8")).hexdigest()


def strip_data_url(value: str) -> str:
    if "," in value and value.lstrip().lower().startswith("data:"):
        return value.split(",", 1)[1]
    return value


def validate_image_bytes(image_bytes: bytes) -> str:
    if not image_bytes:
        raise ChaojiyingCliError("image is empty")
    if len(image_bytes) > MAX_IMAGE_BYTES:
        raise ChaojiyingCliError("image exceeds the 2 MiB API limit")
    for magic, image_type in IMAGE_MAGIC.items():
        if image_bytes.startswith(magic):
            return image_type
    raise ChaojiyingCliError("unsupported image magic; use bmp, jpg/jpeg, or png")


def read_image(path_text: str) -> tuple[str, bytes]:
    path = Path(path_text)
    if not path.is_file():
        raise ChaojiyingCliError(f"image path is not a file: {path}")
    image_bytes = path.read_bytes()
    validate_image_bytes(image_bytes)
    return path.name, image_bytes


def read_base64_image(path_text: str) -> str:
    path = Path(path_text)
    if not path.is_file():
        raise ChaojiyingCliError(f"base64 path is not a file: {path}")
    encoded = strip_data_url(path.read_text(encoding="utf-8").strip())
    try:
        decoded = base64.b64decode(encoded, validate=True)
    except Exception as exc:  # noqa: BLE001 - argparse-facing validation path.
        raise ChaojiyingCliError("file_base64 is not valid base64") from exc
    validate_image_bytes(decoded)
    return encoded


def env_or_arg(value: str | None, env_name: str) -> str | None:
    return value if value is not None else os.environ.get(env_name)


def parse_env_file(path_text: str) -> dict[str, str]:
    path = Path(path_text)
    if not path.is_file():
        raise ChaojiyingCliError(f"env file is not a file: {path}")
    values: dict[str, str] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            raise ChaojiyingCliError(f"invalid env line {line_number}: missing '='")
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if not key:
            raise ChaojiyingCliError(f"invalid env line {line_number}: empty key")
        values[key] = value
    return values


def load_env_file(path_text: str) -> None:
    for key, value in parse_env_file(path_text).items():
        os.environ.setdefault(key, value)


def configured_source(
    args: argparse.Namespace,
    arg_name: str,
    env_name: str,
    env_values: dict[str, str] | None = None,
) -> str | None:
    if getattr(args, arg_name, None):
        return f"--{arg_name.replace('_', '-')}"
    if env_values and env_values.get(env_name):
        return f"env-file:{env_name}"
    if os.environ.get(env_name):
        return env_name
    return None


def env_or_arg_for_preflight(
    args: argparse.Namespace,
    arg_name: str,
    env_name: str,
    env_values: dict[str, str],
) -> str | None:
    value = getattr(args, arg_name, None)
    if value is not None:
        return value
    if env_values.get(env_name):
        return env_values[env_name]
    return os.environ.get(env_name)


def auth_payload(args: argparse.Namespace, *, include_softid: bool) -> dict[str, str]:
    user = env_or_arg(getattr(args, "user", None), "CHAOJIYING_USER")
    password_md5 = env_or_arg(getattr(args, "pass2", None), "CHAOJIYING_PASS2")
    password_plain = env_or_arg(getattr(args, "password", None), "CHAOJIYING_PASS")
    softid = env_or_arg(getattr(args, "softid", None), "CHAOJIYING_SOFT_ID")

    if not user:
        raise ChaojiyingCliError("missing user; set CHAOJIYING_USER or pass --user")
    if password_md5:
        if not PASSWORD_MD5_RE.fullmatch(password_md5):
            raise ChaojiyingCliError("pass2 must be a 32-character lowercase md5 hex")
        pass2 = password_md5
    elif password_plain:
        pass2 = md5_lower(password_plain)
    else:
        raise ChaojiyingCliError(
            "missing password; set CHAOJIYING_PASS2 or CHAOJIYING_PASS"
        )

    payload = {"user": user, "pass2": pass2}
    if include_softid and softid:
        payload["softid"] = softid
    return payload


def post_json(
    url: str,
    *,
    data: dict[str, str],
    files: dict[str, tuple[str, bytes]] | None,
    timeout: float,
) -> dict[str, Any]:
    if requests is None:
        raise ChaojiyingCliError(
            "missing dependency: requests; install project dependencies or use manual fallback"
        )
    try:
        response = requests.post(url, data=data, files=files, timeout=timeout)
    except requests.RequestException as exc:
        raise ChaojiyingCliError(f"request failed: {exc}") from exc

    try:
        parsed = response.json()
    except ValueError as exc:
        raise ChaojiyingCliError("response is not valid JSON") from exc
    if not isinstance(parsed, dict):
        raise ChaojiyingCliError("response JSON is not an object")
    return parsed


def print_json(payload: dict[str, Any], *, redact_result: bool) -> None:
    output = dict(payload)
    if redact_result and "pic_str" in output:
        output["pic_str"] = "<redacted>"
    print(json.dumps(output, ensure_ascii=False, sort_keys=True))


def require_ack(args: argparse.Namespace) -> None:
    if getattr(args, "dry_run", False):
        return
    if not getattr(args, "ack_authorized", False):
        raise ChaojiyingCliError(
            "refusing third-party verification call without --ack-authorized"
        )


def recognize(args: argparse.Namespace) -> dict[str, Any]:
    require_ack(args)
    codetype = env_or_arg(args.codetype, "CHAOJIYING_CODETYPE") or DEFAULT_CODETYPE

    data = auth_payload(args, include_softid=True)
    data["codetype"] = codetype
    if args.str_debug:
        data["str_debug"] = args.str_debug

    files: dict[str, tuple[str, bytes]] | None = None
    if args.image:
        filename, image_bytes = read_image(args.image)
        files = {"userfile": (filename, image_bytes)}
        image_hint: dict[str, Any] = {
            "image_bytes": len(image_bytes),
            "upload": "userfile",
        }
    else:
        encoded = read_base64_image(args.image_base64_file)
        data["file_base64"] = encoded
        image_hint = {
            "image_bytes": len(base64.b64decode(encoded)),
            "upload": "file_base64",
        }

    if args.dry_run:
        return {
            "dry_run": True,
            "endpoint": PROCESSING_URL,
            "fields": sorted(k for k in data if k not in {"pass2", "file_base64"}),
            **image_hint,
        }
    return post_json(PROCESSING_URL, data=data, files=files, timeout=args.timeout)


def report_error(args: argparse.Namespace) -> dict[str, Any]:
    require_ack(args)
    if not args.confirm_wrong_result and not args.dry_run:
        raise ChaojiyingCliError(
            "ReportError requires --confirm-wrong-result; only report proven wrong results"
        )

    data = auth_payload(args, include_softid=True)
    data["id"] = args.pic_id
    if args.dry_run:
        return {
            "dry_run": True,
            "endpoint": REPORT_ERROR_URL,
            "fields": sorted(k for k in data if k != "pass2"),
        }
    return post_json(REPORT_ERROR_URL, data=data, files=None, timeout=args.timeout)


def score(args: argparse.Namespace) -> dict[str, Any]:
    data = auth_payload(args, include_softid=False)
    if args.dry_run:
        return {
            "dry_run": True,
            "endpoint": GET_SCORE_URL,
            "fields": sorted(k for k in data if k != "pass2"),
        }
    return post_json(GET_SCORE_URL, data=data, files=None, timeout=args.timeout)


def load_env_for_preflight(args: argparse.Namespace) -> tuple[dict[str, Any], bool, dict[str, str]]:
    if not args.env_file:
        return {"name": "env_file", "ok": False, "status": "not_provided"}, False, {}

    path = Path(args.env_file)
    if not path.is_file():
        return {
            "name": "env_file",
            "ok": False,
            "path": str(path),
            "status": "missing",
        }, False, {}

    try:
        values = parse_env_file(args.env_file)
    except ChaojiyingCliError as exc:
        return {
            "name": "env_file",
            "ok": False,
            "error": str(exc),
            "path": str(path),
            "status": "invalid_env_shape",
        }, True, {}
    return {
        "name": "env_file",
        "ok": True,
        "keys": sorted(k for k in values if k.startswith("CHAOJIYING_")),
        "path": str(path),
        "status": "loaded",
    }, False, values


def preflight(args: argparse.Namespace) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    missing_credentials: list[str] = []
    invalid_env: list[str] = []

    env_file_check, env_file_invalid, env_values = load_env_for_preflight(args)
    checks.append(env_file_check)
    if env_file_invalid:
        invalid_env.append("env_file")

    python_ok = (3, 12) <= sys.version_info[:2] < (3, 14)
    checks.append(
        {
            "name": "python_runtime",
            "ok": python_ok,
            "required": ">=3.12,<3.14",
            "version": sys.version.split()[0],
        }
    )

    requests_ok = requests is not None
    checks.append(
        {
            "name": "dependency.requests",
            "ok": requests_ok,
            "detail": (
                f"requests {getattr(requests, '__version__', 'unknown')}"
                if requests_ok
                else str(REQUESTS_IMPORT_ERROR or "requests is not importable")
            ),
        }
    )

    user_source = configured_source(args, "user", "CHAOJIYING_USER", env_values)
    checks.append(
        {
            "name": "credentials.user",
            "ok": user_source is not None,
            "source": user_source or "missing",
        }
    )
    if user_source is None:
        missing_credentials.append("CHAOJIYING_USER/--user")

    pass2 = env_or_arg_for_preflight(args, "pass2", "CHAOJIYING_PASS2", env_values)
    password = env_or_arg_for_preflight(args, "password", "CHAOJIYING_PASS", env_values)
    pass2_source = configured_source(args, "pass2", "CHAOJIYING_PASS2", env_values)
    password_source = configured_source(args, "password", "CHAOJIYING_PASS", env_values)
    if pass2:
        password_ok = bool(PASSWORD_MD5_RE.fullmatch(pass2))
        password_source_label = pass2_source
        if not password_ok:
            invalid_env.append("CHAOJIYING_PASS2/--pass2")
    elif password:
        password_ok = True
        password_source_label = password_source
    else:
        password_ok = False
        password_source_label = None
        missing_credentials.append("CHAOJIYING_PASS2 or CHAOJIYING_PASS")
    checks.append(
        {
            "name": "credentials.password",
            "ok": password_ok,
            "source": password_source_label or "missing",
        }
    )

    softid_source = configured_source(args, "softid", "CHAOJIYING_SOFT_ID", env_values)
    checks.append(
        {
            "name": "credentials.softid",
            "ok": True,
            "source": softid_source or "optional_missing",
        }
    )

    codetype = (
        env_or_arg_for_preflight(args, "codetype", "CHAOJIYING_CODETYPE", env_values)
        or DEFAULT_CODETYPE
    )
    codetype_ok = bool(CODETYPE_RE.fullmatch(codetype))
    if not codetype_ok:
        invalid_env.append("CHAOJIYING_CODETYPE/--codetype")
    checks.append(
        {
            "name": "codetype",
            "ok": codetype_ok,
            "source": configured_source(args, "codetype", "CHAOJIYING_CODETYPE", env_values)
            or "default",
            "value": codetype,
        }
    )

    if invalid_env:
        status = "invalid_env_shape"
    elif not python_ok or not requests_ok:
        status = "missing_dependency"
    elif missing_credentials:
        status = "missing_credentials"
    else:
        status = "ready"

    return {
        "checks": checks,
        "manual_fallback": status != "ready",
        "missing_credentials": missing_credentials,
        "network": {
            "allowed": False,
            "attempted": False,
            "mode": "no-network",
        },
        "next_action": "use_manual_handoff" if status != "ready" else "chaojiying_ready",
        "ready": status == "ready",
        "status": status,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Low-frequency, authorized Chaojiying client for interactive "
            "verification fixtures. Do not use for bulk bypass."
        )
    )
    parser.add_argument("--user", help="Chaojiying account; prefer CHAOJIYING_USER")
    parser.add_argument("--password", help="Plain password; prefer CHAOJIYING_PASS")
    parser.add_argument(
        "--pass2",
        help="Lowercase md5 password; prefer CHAOJIYING_PASS2",
    )
    parser.add_argument("--softid", help="Software ID; prefer CHAOJIYING_SOFT_ID")
    parser.add_argument("--env-file", help="Load credentials from an ignored local env file")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs without network",
    )
    parser.add_argument(
        "--redact-result",
        action="store_true",
        help="Redact pic_str in stdout",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    preflight_parser = subparsers.add_parser(
        "preflight",
        help="Report local Chaojiying runtime readiness without network",
    )
    preflight_parser.add_argument("--user", help="Chaojiying account")
    preflight_parser.add_argument("--password", help="Plain password")
    preflight_parser.add_argument("--pass2", help="Lowercase md5 password")
    preflight_parser.add_argument("--softid", help="Software ID")
    preflight_parser.add_argument("--env-file", help="Load an ignored local env file")
    preflight_parser.add_argument(
        "--codetype",
        default=None,
        help="Recognition type. Defaults to CHAOJIYING_CODETYPE or 1902.",
    )
    preflight_parser.add_argument(
        "--no-network",
        action="store_true",
        help="Document that preflight must not contact Chaojiying",
    )
    preflight_parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON; preflight always uses JSON output",
    )
    preflight_parser.set_defaults(func=preflight)

    recognize_parser = subparsers.add_parser("recognize", help="Upload one image")
    image_group = recognize_parser.add_mutually_exclusive_group(required=True)
    image_group.add_argument("--image", help="Path to one bmp/jpg/jpeg/png image")
    image_group.add_argument(
        "--image-base64-file",
        help="Path to a text file containing one base64 image",
    )
    recognize_parser.add_argument(
        "--codetype",
        default=None,
        help=(
            "Recognition type. Defaults to CHAOJIYING_CODETYPE or 1902 "
            "(4-6 alphanumeric chars)."
        ),
    )
    recognize_parser.add_argument("--str-debug", help="Optional API str_debug value")
    recognize_parser.add_argument(
        "--ack-authorized",
        action="store_true",
        help="Acknowledge this is a single authorized challenge",
    )
    recognize_parser.set_defaults(func=recognize)

    report_parser = subparsers.add_parser("report-error", help="Report one wrong result")
    report_parser.add_argument(
        "--pic-id",
        required=True,
        help="pic_id returned by recognize",
    )
    report_parser.add_argument(
        "--confirm-wrong-result",
        action="store_true",
        help="Confirm the result is proven wrong and still eligible for report",
    )
    report_parser.add_argument(
        "--ack-authorized",
        action="store_true",
        help="Acknowledge this is a single authorized challenge",
    )
    report_parser.set_defaults(func=report_error)

    score_parser = subparsers.add_parser("score", help="Query account score")
    score_parser.add_argument("--env-file", help="Load credentials from an ignored local env file")
    score_parser.add_argument(
        "--ack-authorized",
        action="store_true",
        help="Accepted for UAT symmetry; score submits no CAPTCHA image",
    )
    score_parser.set_defaults(func=score)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.env_file and args.command != "preflight":
            load_env_file(args.env_file)
        result = args.func(args)
    except ChaojiyingCliError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print_json(result, redact_result=args.redact_result)
    if args.command == "preflight":
        return 0 if result["status"] == "ready" else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
