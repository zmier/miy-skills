from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_orchestrator_requires_red_reproduction_before_fix_story() -> None:
    skill = read("skills/android-request-reproduction/SKILL.md")
    routing = read("skills/android-request-reproduction/references/routing.md")
    statuses = read("skills/android-request-reproduction/references/acceptance-statuses.md")

    assert "Red" in skill
    assert "not-reproduced" in skill
    assert "先在当前设备、版本、网络和同一动作窗口复现" in routing
    assert "不要把备用实验写成故障修复" in statuses


def test_acceptance_template_supports_scoped_and_boundary_statuses() -> None:
    template = read("skills/android-request-reproduction/assets/acceptance-contract-template.md")

    assert "S-RED-01" in template
    assert "not-reproduced" in template
    assert "blocked-by-boundary" in template
    assert "passed-with-scope" in template


def test_capture_skill_requires_cleanup_and_red_not_reproduced_state() -> None:
    skill = read("skills/capture-android-traffic/SKILL.md")
    evidence = read("skills/capture-android-traffic/references/evidence-contract.md")

    assert "停止采集后必须验证恢复" in skill
    assert "用户 VPN" in skill
    assert "not-reproduced" in skill
    assert "passed-with-scope" in evidence


def test_rpc_corpus_skill_preserves_long_running_frida_harvest_guardrails() -> None:
    # GIVEN：App 内 Frida RPC 单次可用，不代表批量语料采集可长跑。
    skill = read("skills/build-android-rpc-data-corpus/SKILL.md")
    policy = read("skills/build-android-rpc-data-corpus/references/batch-safety-policy.md")
    lifecycle = read("skills/export-frida-rpc/references/rpc-lifecycle.md")
    diagnostics = read("skills/diagnose-android-instrumentation/SKILL.md")
    workflow = read("SKILL.md")

    # WHEN：真实探索项目暴露 TTY/session/服务端窗口问题。
    # THEN：Workflow 应保留通用护栏，不把个案过程硬编码进 Skill。
    assert "Frida RPC 长跑采集" in policy
    assert "真实 Terminal TTY" in policy
    assert "单实体隔离" in policy
    assert "batch-summary" in policy
    assert "全局 summary/report" in policy
    assert "单次 RPC Green 不等于批量 Green" in lifecycle
    assert "script has been destroyed" in lifecycle
    assert "非交互后台、TTY/stdin、USB 抖动或 session 生命周期" in diagnostics
    assert "服务端分页窗口" in workflow
    assert "具体账号、offset、业务 ID" in workflow
    assert "真实 TTY/伪终端" in skill


def test_xposed_p1_sop_preserves_module_loaded_gate() -> None:
    # GIVEN：A5/R4-X 服务化路线不能从 Frida 直接跳到业务 action。
    skill = read("skills/xposed-sekiro-runtime-dispatch/SKILL.md")
    sop = read("skills/xposed-sekiro-runtime-dispatch/references/xposed-lsposed-p1-sop.md")
    workflow = read("SKILL.md")
    provenance = read("references/field-provenance.md")

    # WHEN：真实 P1 跑通 LSPosed module-loaded smoke。
    # THEN：Workflow 应保留先 module-loaded，再 action server 的通用门禁。
    assert "P1 Xposed/LSPosed smoke" in skill
    assert "module-loaded" in sop
    assert "classloader-ready" in sop
    assert "xposedscope" in sop
    assert "不要优先手写" in skill
    assert "ProcessRouter" in skill
    assert "P1 Green 不等于业务 Green" in workflow
    assert "TASK34 - Xposed/LSPosed P1 module-loaded" in provenance


def test_xposed_build_uses_workflow_pinned_toolchain() -> None:
    # GIVEN：A5/Xposed TASK 构建时，系统 PATH 可能没有 gradle。
    workflow = read("SKILL.md")

    # THEN：总编排应明确优先使用 workflow 自带 Gradle/JDK，不让 TASK 到处找系统工具。
    assert "workflow 固定工具链" in workflow
    assert "tools/gradle-8.7/bin/gradle" in workflow
    assert "tools/jdk17/Contents/Home" in workflow
    assert "不要因为 `gradle` 不在系统 PATH" in workflow


def test_xposed_p3_sop_preserves_single_action_oracle_and_business_ok_boundary() -> None:
    # GIVEN：Frida RPC 已证明一个业务 RPC 可用，但 Xposed 服务化仍需重新验收。
    skill = read("skills/xposed-sekiro-runtime-dispatch/SKILL.md")
    workflow = read("SKILL.md")
    provenance = read("references/field-provenance.md")

    # WHEN：真实 P3 跑通首个 Xposed allowlist action。
    # THEN：Workflow 应保留单 action smoke、Frida oracle 和成功语义分层。
    assert "P3 单 Action 业务 Smoke" in skill
    assert "Frida oracle" in skill
    assert "默认 dry-run" in skill
    assert "real=1" in skill
    assert "transportOk" in skill
    assert "businessOk" in skill
    assert "单 action 低频 smoke" in workflow
    assert "App ClassLoader / RPC proxy / requestData / business-ok 四层排错" in workflow
    assert "transport 成功但业务 `success=false`" in workflow
    assert "TASK34-03 - A5/Xposed 首个真实业务 action P3 smoke" in provenance
    assert "forward-test-green for one P3 action" in provenance


def test_xposed_templates_preserve_runtime_service_guardrails() -> None:
    # GIVEN：模板是后续 TASK 复制的起点，必须自带 P1/P2/P3 护栏。
    entry = read("skills/xposed-sekiro-runtime-dispatch/assets/XposedSekiroEntryTemplate.java")
    handler = read("skills/xposed-sekiro-runtime-dispatch/assets/SekiroActionHandlerTemplate.java")
    contract = read("skills/xposed-sekiro-runtime-dispatch/references/xposed-sekiro-contract.md")

    # WHEN：检查 Xposed/Sekiro 模板与契约。
    # THEN：它们应默认具备进程路由、dry-run、异常兜底和业务成功分层。
    assert "TARGET_PROCESS" in entry
    assert "module-loaded" in entry
    assert "classloader-ready" in entry
    assert "action-server-skip" in entry
    assert "dryRun" in handler
    assert "real" in handler
    assert "Throwable" in handler
    assert "transportOk" in handler
    assert "businessOk" in handler
    assert "sensitiveHeadersReturned" in handler
    assert "process-routed" in contract
    assert "single-action-smoke-passed" in contract
    assert "business-failed-handled" in contract


def test_xposed_p4_p6_preserve_long_run_production_gates() -> None:
    # GIVEN：P3 单 action smoke 已通过，但仍不能代表请求池和长跑可用。
    skill = read("skills/xposed-sekiro-runtime-dispatch/SKILL.md")
    contract = read("skills/xposed-sekiro-runtime-dispatch/references/xposed-sekiro-contract.md")
    workflow = read("SKILL.md")
    provenance = read("references/field-provenance.md")

    # WHEN：真实项目进入 P4/P5/P6。
    # THEN：Workflow 应保留 transport adapter、高危状态变更和长跑状态机三层门禁。
    assert "P4 请求池 Transport 接入" in skill
    assert "XposedActionTransport" in skill
    assert "workerStatusMachineUnchanged=true" in skill
    assert "P5 受控状态变更 Action" in skill
    assert "prepare 与 execute 分离" in skill
    assert "recentRedEvidence" in skill
    assert "post-smoke" in skill
    assert "P6 生产长跑状态机" in skill
    assert "真实 worker 进程 / 最近 DB 推进 / action server health" in skill
    assert "P4 request-pool adapter" in workflow
    assert "P5 supervised state-changing action" in workflow
    assert "P6 production long-run" in workflow
    assert "dashboardReadsLiveEvidenceBeforeHistoricalError=true" in workflow
    assert "request-pool-adapted" in contract
    assert "state-changing-action-executed" in contract
    assert "long-run-supervised" in contract
    assert "TASK34-05/P4 - Xposed transport 接入请求池" in provenance
    assert "TASK34-P5 - Xposed 内部受控状态变更 Action" in provenance
    assert "TASK34-P6 - Xposed transport 受监督长跑状态机" in provenance


def test_interactive_verification_slider_topic_preserves_recovery_state_machine() -> None:
    # GIVEN：长跑采集可能遇到服务端交互验证或 native/H5 滑块。
    workflow = read("SKILL.md")
    provenance = read("references/field-provenance.md")

    # THEN：总编排应把滑块作为独立 Red，而不是普通请求失败或 session 问题。
    assert "交互验证与滑块处理" in workflow
    assert "H5/WebView 滑块" in workflow
    assert "native View 滑块" in workflow
    assert "服务端返回验证态，但前台暂未出现可操作页面" in workflow
    assert "ADB swipe / tap / input 先证明人工动作可被机器复现" in workflow
    assert "Xposed App 内 `MotionEvent`" in workflow
    assert "detected -> notify human" in workflow
    assert "solve ok -> clear local interactive waiting / cooldown -> post-smoke -> continue" in workflow
    assert "interactive verification returned by business RPC" in workflow
    assert "manual UAT: 真实滑块出现后" in workflow
    assert "TASK35 - 交互验证与 native 滑块处理" in provenance
    assert "slider_status" in provenance
    assert "solve_slider" in provenance
    assert "new-case forward-test-pending" in provenance
