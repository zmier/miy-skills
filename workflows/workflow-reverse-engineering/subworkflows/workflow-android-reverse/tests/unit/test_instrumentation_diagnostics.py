from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_instrumentation_skill_handles_modern_linker_and_noninteractive_frida() -> None:
    # GIVEN：Android 10+ 与非交互 Frida CLI 会改变 so 观察链的失败形态。
    skill = (
        ROOT
        / "skills"
        / "diagnose-android-instrumentation"
        / "SKILL.md"
    ).read_text(encoding="utf-8")

    # WHEN：需要确认 so 加载。
    # THEN：Skill 应要求先枚举 linker 导出，并保持 Frida stdin 存活。
    assert "__loader_android_dlopen_ext" in skill
    assert "__loader_dlopen" in skill
    assert "stdin" in skill
    assert "not-reproduced" in skill


def test_instrumentation_skill_does_not_overclaim_antifrida_when_red_is_absent() -> None:
    # GIVEN：课程 Red 可能因为设备、版本、服务端状态不同而未复现。
    skill = (
        ROOT
        / "skills"
        / "diagnose-android-instrumentation"
        / "SKILL.md"
    ).read_text(encoding="utf-8")

    # WHEN：空脚本 attach/spawn 稳定。
    # THEN：结论应是观察链恢复，而不是宣称已经绕过检测。
    assert "Red 未复现，观察链已恢复" in skill
    assert "不是“反调试已解决”" in skill
