from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_workflow_has_tdd_regression_reference() -> None:
    reference = read("references/tdd-regression-test-system.md")
    workflow = read("SKILL.md")

    assert "三圈测试" in reference
    assert "Workflow" in reference
    assert "Miku" in reference
    assert "TASK" in reference
    assert "Unit" in reference
    assert "E2E" in reference
    assert "UAT" in reference
    assert "gnirehtet" in reference
    assert "runtime crash sentinel" in reference
    assert "不把真实 raw 响应放进 workflow tests" in reference
    assert "真实项目反哺" in workflow


def test_tests_readme_keeps_task_boundary_clear() -> None:
    readme = read("tests/README.md")

    assert "不连真机" in readme
    assert "默认不发送真实业务请求" in readme
    assert "Manual UAT" in readme
    assert "TASK27-回答详情请求池与采集调度" in readme
