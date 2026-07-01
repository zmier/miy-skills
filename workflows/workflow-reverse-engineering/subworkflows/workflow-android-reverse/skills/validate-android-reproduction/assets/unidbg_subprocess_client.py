#!/usr/bin/env python3
"""Call a TASK-local Unidbg Java wrapper and parse the last stdout line."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from pathlib import Path
from typing import Any


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Unidbg Java wrapper once.")
    parser.add_argument("--cmd", nargs="+", required=True, help="Java command before business input.")
    parser.add_argument("--input", required=True, help="Business input passed as the final Java argument.")
    parser.add_argument("--cwd", help="Working directory for the Java command.")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output", help="Optional JSON output path.")
    parser.add_argument("--save-raw", action="store_true", help="Include raw stdout/stderr in output JSON.")
    args = parser.parse_args()

    command = list(args.cmd) + [args.input]
    started = time.time()
    proc = subprocess.run(
        command,
        cwd=args.cwd,
        text=True,
        capture_output=True,
        timeout=args.timeout,
        check=False,
    )
    elapsed_ms = int((time.time() - started) * 1000)
    stdout_lines = proc.stdout.splitlines()
    business_result = stdout_lines[-1] if stdout_lines else ""

    result: dict[str, Any] = {
        "ok": proc.returncode == 0,
        "route": "unidbg-subprocess",
        "status": "unit-passed" if proc.returncode == 0 else "unit-failed",
        "returncode": proc.returncode,
        "elapsed_ms": elapsed_ms,
        "business_result": business_result,
        "business_result_sha256": sha256_text(business_result),
        "stdout_line_count": len(stdout_lines),
        "stderr_sha256": sha256_text(proc.stderr),
    }
    if args.save_raw:
        result["raw"] = {
            "command": command,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
