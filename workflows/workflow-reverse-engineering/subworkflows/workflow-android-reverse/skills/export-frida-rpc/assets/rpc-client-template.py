#!/usr/bin/env python3
"""Minimal Frida RPC client template.

This template is for authorized Android research tasks. It deliberately avoids
hard-coded PIDs, package names, hosts, headers, tokens, and business values.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import frida


def load_input(args: argparse.Namespace) -> Any:
    if args.input_file:
        return json.loads(Path(args.input_file).read_text(encoding="utf-8"))
    if args.input_json:
        return json.loads(args.input_json)
    return {}


def attach_session(device: frida.core.Device, args: argparse.Namespace) -> frida.core.Session:
    if args.spawn:
        if not args.package:
            raise SystemExit("--spawn requires --package")
        pid = device.spawn([args.package])
        session = device.attach(pid)
        device.resume(pid)
        time.sleep(args.resume_wait)
        return session
    if args.pid is not None:
        return device.attach(args.pid)
    if args.package:
        return device.attach(args.package)
    raise SystemExit("Provide --package or --pid")


def on_message(message: dict[str, Any], data: bytes | None) -> None:
    payload = {"type": message.get("type"), "payload": message.get("payload")}
    if message.get("type") == "error":
        payload["stack"] = message.get("stack")
    print(json.dumps(payload, ensure_ascii=False), file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Call a Frida RPC export once.")
    parser.add_argument("--package", help="Android package/process name for attach or spawn.")
    parser.add_argument("--pid", type=int, help="PID fallback when package attach fails.")
    parser.add_argument("--spawn", action="store_true", help="Spawn the package before loading the agent.")
    parser.add_argument("--agent", required=True, help="Path to Frida JS agent.")
    parser.add_argument("--method", default="compute", help="rpc.exports method name.")
    parser.add_argument("--input-json", help="JSON string passed to the RPC method.")
    parser.add_argument("--input-file", help="JSON file passed to the RPC method.")
    parser.add_argument("--output", help="Optional output JSON path.")
    parser.add_argument("--resume-wait", type=float, default=1.0, help="Seconds to wait after spawn resume.")
    args = parser.parse_args()

    request = load_input(args)
    started = time.time()
    device = frida.get_usb_device(timeout=5)
    session = attach_session(device, args)

    try:
        agent_source = Path(args.agent).read_text(encoding="utf-8")
        script = session.create_script(agent_source)
        script.on("message", on_message)
        script.load()

        ping = script.exports_sync.ping()
        method = getattr(script.exports_sync, args.method)
        value = method(request)
        elapsed_ms = int((time.time() - started) * 1000)
        result = {
            "ok": True,
            "route": "frida-rpc",
            "status": "rpc-call-passed",
            "method": args.method,
            "elapsed_ms": elapsed_ms,
            "ping": ping,
            "result": value,
        }
    except Exception as exc:  # noqa: BLE001 - template should preserve runtime errors.
        result = {
            "ok": False,
            "route": "frida-rpc",
            "status": "rpc-call-failed",
            "error": str(exc),
        }
    finally:
        try:
            session.detach()
        except Exception:
            pass

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
