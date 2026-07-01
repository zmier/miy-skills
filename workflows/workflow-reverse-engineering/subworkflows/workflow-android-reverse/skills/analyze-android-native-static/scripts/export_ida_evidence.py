from __future__ import annotations

import json
import traceback
from pathlib import Path

import ida_auto
import ida_bytes
import ida_funcs
import ida_hexrays
import ida_idaapi
import ida_idp
import ida_kernwin
import ida_lines
import ida_name
import ida_pro
import ida_ua
import idautils
import idc


def strip_tags(text: str) -> str:
    return ida_lines.tag_remove(text)


def ensure_thumb_function(address: int) -> bool:
    idc.split_sreg_range(address, "T", 1, idc.SR_user)
    if ida_funcs.get_func(address) is not None:
        return True
    ida_bytes.del_items(address, ida_bytes.DELIT_SIMPLE, 2)
    ida_ua.create_insn(address)
    return bool(ida_funcs.add_func(address, ida_idaapi.BADADDR))


def disassemble(start: int, count: int) -> list[dict[str, str]]:
    rows = []
    address = start
    for _ in range(count):
        line = idc.generate_disasm_line(address, 0)
        if not line:
            break
        rows.append({"address": hex(address), "text": strip_tags(line)})
        next_address = idc.next_head(address)
        if next_address == ida_idaapi.BADADDR or next_address <= address:
            break
        address = next_address
    return rows


def decompile(address: int) -> dict[str, object]:
    function = ida_funcs.get_func(address)
    if function is None:
        return {"success": False, "error": "function-not-found"}
    try:
        cfunc = ida_hexrays.decompile(function.start_ea)
        if cfunc is None:
            return {"success": False, "error": "decompile-returned-none"}
        return {
            "success": True,
            "function_start": hex(function.start_ea),
            "function_end": hex(function.end_ea),
            "pseudocode": str(cfunc),
        }
    except Exception as exc:
        return {"success": False, "error": repr(exc)}


def code_xrefs_to(address: int) -> list[dict[str, str]]:
    rows = []
    for xref in idautils.XrefsTo(address, 0):
        if not xref.iscode:
            continue
        function = ida_funcs.get_func(xref.frm)
        rows.append(
            {
                "from": hex(xref.frm),
                "function": ida_name.get_name(
                    function.start_ea if function else xref.frm
                ),
            }
        )
    return rows


def main() -> None:
    if len(idc.ARGV) < 3:
        raise RuntimeError("usage: export_ida_evidence.py TARGETS_JSON OUTPUT_JSON")

    targets_path = Path(idc.ARGV[1]).resolve()
    output_path = Path(idc.ARGV[2]).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    ida_auto.auto_wait()
    ida_hexrays.init_hexrays_plugin()
    targets = json.loads(targets_path.read_text(encoding="utf-8"))
    records = []
    thumb = "thumb" in targets.get("architecture", "").lower()

    for item in targets["functions"]:
        address = int(str(item["address"]), 0) & ~1
        available = ensure_thumb_function(address) if thumb else True
        if not thumb and ida_funcs.get_func(address) is None:
            available = bool(ida_funcs.add_func(address, ida_idaapi.BADADDR))
        ida_auto.auto_wait()
        records.append(
            {
                **item,
                "normalized_address": hex(address),
                "thumb": thumb,
                "function_available": available,
                "disassembly": disassemble(
                    address, int(item.get("instruction_count", 80))
                ),
                "decompilation": decompile(address),
                "code_xrefs_to": code_xrefs_to(address),
            }
        )

    output_path.write_text(
        json.dumps(
            {
                "ida_version": ida_kernwin.get_kernel_version(),
                "input_file": idc.get_input_file_path(),
                "processor": ida_idp.get_idp_name(),
                "targets": records,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    ida_pro.qexit(0)


try:
    main()
except Exception:
    traceback.print_exc()
    ida_pro.qexit(1)
