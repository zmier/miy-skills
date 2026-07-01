from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_https_mitm_diagnosis_is_routable_from_capture_skill() -> None:
    skill = read("skills/capture-android-traffic/SKILL.md")
    reference = read("skills/capture-android-traffic/references/https-mitm-diagnosis.md")

    assert "https-mitm-diagnosis.md" in skill
    assert "Trust anchor for certification path not found" in reference
    assert "tls-mitm-red" in reference
    assert "PARTIAL_CONNECTIVITY" in reference


def test_trace_java_has_day15_request_boundary_templates() -> None:
    skill = read("skills/trace-android-java/SKILL.md")
    reference = read("skills/trace-android-java/references/request-boundary-probes.md")
    okhttp = read("skills/trace-android-java/assets/okhttp-interceptor-probe.js")
    mapping = read("skills/trace-android-java/assets/map-put-probe.js")
    base64 = read("skills/trace-android-java/assets/base64-probe.js")

    assert "request-boundary-probes.md" in skill
    assert "OkHttp" in reference
    assert "Map/TreeMap" in reference
    assert "addInterceptor" in okhttp
    assert "TreeMap" in mapping
    assert "Base64" in base64


def test_g2_rejection_taxonomy_covers_406_and_cloudwaf() -> None:
    skill = read("skills/android-request-reproduction/SKILL.md")
    routing = read("skills/android-request-reproduction/references/routing.md")
    taxonomy = read("skills/android-request-reproduction/references/g2-rejection-taxonomy.md")

    assert "g2-rejection-taxonomy.md" in skill
    assert "g2-rejection-taxonomy.md" in routing
    assert "406" in taxonomy
    assert "418" in taxonomy
    assert "CloudWAF" in taxonomy


def test_course_case_migration_skill_exists_and_is_registered() -> None:
    skill = read("skills/extract-course-case-workflow/SKILL.md")
    registry = read("skills/android-request-reproduction/references/capability-registry.md")

    assert "integrate-now" in skill
    assert "case-evidence" in skill
    assert "defer" in skill
    assert "extract-course-case-workflow" in registry
