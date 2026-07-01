from __future__ import annotations

import argparse
import hashlib
import json
import plistlib
import shutil
import subprocess
import time
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_targets(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not payload.get("functions"):
        raise SystemExit("targets JSON must contain at least one function")
    for item in payload["functions"]:
        int(str(item["address"]), 0)
    return payload


def ida_version(ida_app: Path) -> str:
    info = ida_app / "Contents/Info.plist"
    if not info.is_file():
        return "unknown"
    with info.open("rb") as stream:
        payload = plistlib.load(stream)
    return str(payload.get("CFBundleShortVersionString", "unknown"))


def select_ida_binary(ida_app: Path) -> Path:
    for name in ("idat", "idat64"):
        binary = ida_app / "Contents/MacOS" / name
        if binary.is_file():
            return binary
    raise SystemExit(f"IDA batch binary not found under {ida_app}")


def resolve_llvm_objdump(explicit: Path | None) -> Path:
    candidates = [
        explicit,
        Path("/opt/homebrew/opt/llvm/bin/llvm-objdump"),
        Path("/usr/local/opt/llvm/bin/llvm-objdump"),
    ]
    command = shutil.which("llvm-objdump")
    if command:
        candidates.append(Path(command))
    for candidate in candidates:
        if candidate and candidate.is_file():
            return candidate.resolve()
    raise SystemExit("llvm-objdump not found")


def run_ida(args: argparse.Namespace) -> dict:
    ida_app = args.ida_app.resolve()
    ida_binary = select_ida_binary(ida_app)
    evidence = args.output_dir / "ida-evidence.json"
    database = args.output_dir / f"{args.binary.stem}.i64"
    log = args.output_dir / "ida-batch.log"
    if args.force:
        evidence.unlink(missing_ok=True)
        database.unlink(missing_ok=True)
        log.unlink(missing_ok=True)
        for suffix in (".id0", ".id1", ".id2", ".nam", ".til"):
            (args.output_dir / f"{args.binary.stem}{suffix}").unlink(missing_ok=True)

    script_args = f'"{args.ida_script}" "{args.targets}" "{evidence}"'
    command = [
        str(ida_binary),
        "-A",
        f"-L{log}",
        f"-o{database}",
        f"-S{script_args}",
        str(args.binary),
    ]
    started = time.time()
    result = subprocess.run(
        command,
        cwd=args.output_dir,
        capture_output=True,
        text=True,
        timeout=args.timeout,
        check=False,
    )
    return {
        "adapter": "ida-idapython",
        "ida_app": str(ida_app),
        "ida_version": ida_version(ida_app),
        "ida_binary": str(ida_binary),
        "command": command,
        "return_code": result.returncode,
        "elapsed_seconds": round(time.time() - started, 3),
        "success": result.returncode == 0 and evidence.is_file(),
        "evidence": str(evidence),
        "database": str(database),
        "log": str(log),
        "stdout": result.stdout[-4000:],
        "stderr": result.stderr[-4000:],
    }


def run_objdump(args: argparse.Namespace, targets: dict) -> dict:
    tool = resolve_llvm_objdump(args.llvm_objdump)
    output = args.output_dir / "objdump-thumb.txt"
    records = []
    chunks = []
    for item in targets["functions"]:
        address = int(str(item["address"]), 0) & ~1
        size = int(item.get("window", 128))
        command = [
            str(tool),
            "--disassemble",
            "--triple=thumbv7-none-linux-android",
            f"--start-address={hex(address)}",
            f"--stop-address={hex(address + size)}",
            str(args.binary),
        ]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=args.timeout,
            check=False,
        )
        records.append(
            {
                "name": item.get("name"),
                "address": item["address"],
                "command": command,
                "return_code": result.returncode,
            }
        )
        chunks.append(
            f"===== {item.get('name', item['address'])} @ {item['address']} =====\n"
            f"{result.stdout}{result.stderr}"
        )
    output.write_text("\n".join(chunks), encoding="utf-8")
    return {
        "adapter": "llvm-objdump",
        "tool": str(tool),
        "success": all(item["return_code"] == 0 for item in records),
        "records": records,
        "disassembly": str(output),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run IDA, LLVM objdump, or both for Android Native static analysis."
    )
    parser.add_argument("--route", choices=["ida", "objdump", "cross"], required=True)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--ida-app",
        type=Path,
        default=Path("/Applications/IDA Professional 9.3.app"),
    )
    parser.add_argument("--ida-script", type=Path)
    parser.add_argument("--llvm-objdump", type=Path)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    args.binary = args.binary.resolve()
    args.targets = args.targets.resolve()
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    targets = read_targets(args.targets)
    if args.ida_script:
        args.ida_script = args.ida_script.resolve()
    elif args.route in {"ida", "cross"}:
        args.ida_script = Path(__file__).with_name("export_ida_evidence.py").resolve()

    manifest = {
        "generated_at": int(time.time()),
        "route": args.route,
        "binary": str(args.binary),
        "binary_sha256": sha256(args.binary),
        "targets": targets,
        "adapters": [],
    }
    if args.route in {"ida", "cross"}:
        manifest["adapters"].append(run_ida(args))
    if args.route in {"objdump", "cross"}:
        manifest["adapters"].append(run_objdump(args, targets))
    manifest["success"] = all(item["success"] for item in manifest["adapters"])

    manifest_path = args.output_dir / "static-analysis-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    if not manifest["success"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
