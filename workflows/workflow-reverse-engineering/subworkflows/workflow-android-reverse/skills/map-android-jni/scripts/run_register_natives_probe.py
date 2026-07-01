from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import frida


def main() -> None:
    parser = argparse.ArgumentParser(description="冷启动捕获目标类的 RegisterNatives 映射")
    parser.add_argument("--package", required=True)
    parser.add_argument("--class-name", required=True)
    parser.add_argument("--seconds", type=float, default=12)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    template = (
        Path(__file__).resolve().parents[1]
        / "assets"
        / "register-natives-probe.js"
    ).read_text(encoding="utf-8")
    source = template.replace("__TARGET_CLASS__", args.class_name)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    device = frida.get_usb_device(timeout=10)
    pid = device.spawn([args.package])
    session = device.attach(pid)
    script = session.create_script(source)

    with args.output.open("w", encoding="utf-8") as stream:
        def on_message(message: dict, data: bytes | None) -> None:
            record = {
                "host_timestamp": time.time(),
                "message": message,
                "data_hex": data.hex() if data else None,
            }
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
            payload = message.get("payload", {})
            if payload.get("event") in {"jni-mapping", "error"}:
                print(json.dumps(payload, ensure_ascii=False))

        script.on("message", on_message)
        script.load()
        device.resume(pid)
        time.sleep(args.seconds)

    session.detach()


if __name__ == "__main__":
    main()
