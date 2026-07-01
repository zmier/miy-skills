from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import frida


def main() -> None:
    parser = argparse.ArgumentParser(description="按模块偏移捕获 Native 缓冲区")
    parser.add_argument("--package", required=True)
    parser.add_argument("--module", required=True)
    parser.add_argument("--offset", required=True)
    parser.add_argument("--caller-offset", action="append", default=[])
    parser.add_argument("--buffer-arg", type=int, default=1)
    parser.add_argument("--length-arg", type=int, default=2)
    parser.add_argument("--max-bytes", type=int, default=1_048_576)
    parser.add_argument("--seconds", type=float, default=15)
    parser.add_argument("--thumb", action="store_true")
    parser.add_argument("--spawn", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    config = {
        "module": args.module,
        "offset": args.offset,
        "caller_offsets": args.caller_offset,
        "buffer_arg": args.buffer_arg,
        "length_arg": args.length_arg,
        "max_bytes": args.max_bytes,
        "thumb": args.thumb,
    }
    template = (
        Path(__file__).resolve().parents[1] / "assets" / "native-buffer-probe.js"
    ).read_text(encoding="utf-8")
    source = template.replace("__CONFIG_JSON__", json.dumps(config))
    args.output.parent.mkdir(parents=True, exist_ok=True)

    device = frida.get_usb_device(timeout=10)
    if args.spawn:
        pid = device.spawn([args.package])
    else:
        app = next(
            app
            for app in device.enumerate_applications()
            if app.identifier == args.package
        )
        if app.pid == 0:
            raise SystemExit("目标 App 未运行；请先启动或使用 --spawn")
        pid = app.pid

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
            if message.get("type") == "send":
                print(json.dumps(message["payload"], ensure_ascii=False))

        script.on("message", on_message)
        script.load()
        if args.spawn:
            device.resume(pid)
        time.sleep(args.seconds)

    session.detach()


if __name__ == "__main__":
    main()
