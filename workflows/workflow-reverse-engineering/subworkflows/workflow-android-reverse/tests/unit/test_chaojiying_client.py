from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "skills"
    / "handle-interactive-verification"
    / "scripts"
    / "chaojiying_client.py"
)
SPEC = importlib.util.spec_from_file_location("chaojiying_client", SCRIPT)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def write_jpeg_fixture(path: Path) -> None:
    path.write_bytes(b"\xff\xd8\xff\xe0fixture\xff\xd9")


def set_credentials(monkeypatch) -> None:
    monkeypatch.setenv("CHAOJIYING_USER", "demo-user")
    monkeypatch.setenv("CHAOJIYING_PASS", "demo-pass")
    monkeypatch.setenv("CHAOJIYING_SOFT_ID", "123456")


def clear_credentials(monkeypatch) -> None:
    for key in [
        "CHAOJIYING_USER",
        "CHAOJIYING_PASS",
        "CHAOJIYING_PASS2",
        "CHAOJIYING_SOFT_ID",
        "CHAOJIYING_CODETYPE",
    ]:
        monkeypatch.delenv(key, raising=False)


def test_preflight_reports_ready_without_network(monkeypatch, capsys) -> None:
    set_credentials(monkeypatch)

    def fail_post(*args, **kwargs):
        raise AssertionError("preflight must not contact Chaojiying")

    monkeypatch.setattr(module.requests, "post", fail_post)

    status = module.main(["preflight", "--no-network", "--json"])

    assert status == 0
    raw_output = capsys.readouterr().out
    output = json.loads(raw_output)
    assert output["status"] == "ready"
    assert output["ready"] is True
    assert output["manual_fallback"] is False
    assert output["network"]["attempted"] is False
    assert "demo-pass" not in raw_output
    assert hashlib.md5(b"demo-pass").hexdigest() not in raw_output


def test_preflight_treats_softid_as_optional(tmp_path, monkeypatch, capsys) -> None:
    clear_credentials(monkeypatch)
    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "\n".join(
            [
                "CHAOJIYING_USER=file-user",
                f"CHAOJIYING_PASS2={hashlib.md5(b'file-pass').hexdigest()}",
                "CHAOJIYING_CODETYPE=1902",
            ]
        ),
        encoding="utf-8",
    )

    status = module.main(
        ["preflight", "--env-file", str(env_file), "--no-network", "--json"]
    )

    assert status == 0
    output = json.loads(capsys.readouterr().out)
    assert output["status"] == "ready"
    softid_check = next(
        check for check in output["checks"] if check["name"] == "credentials.softid"
    )
    assert softid_check["ok"] is True
    assert softid_check["source"] == "optional_missing"


def test_preflight_reports_missing_credentials(monkeypatch, capsys) -> None:
    clear_credentials(monkeypatch)

    status = module.main(["preflight", "--no-network", "--json"])

    assert status == 1
    output = json.loads(capsys.readouterr().out)
    assert output["status"] == "missing_credentials"
    assert output["ready"] is False
    assert output["manual_fallback"] is True
    assert "CHAOJIYING_USER/--user" in output["missing_credentials"]
    assert output["network"]["attempted"] is False


def test_preflight_reports_missing_dependency_without_traceback(monkeypatch, capsys) -> None:
    set_credentials(monkeypatch)
    monkeypatch.setattr(module, "requests", None)
    monkeypatch.setattr(
        module,
        "REQUESTS_IMPORT_ERROR",
        ModuleNotFoundError("No module named 'requests'"),
    )

    status = module.main(["preflight", "--no-network", "--json"])

    captured = capsys.readouterr()
    assert status == 1
    assert "Traceback" not in captured.err
    output = json.loads(captured.out)
    assert output["status"] == "missing_dependency"
    assert output["ready"] is False
    assert output["network"]["attempted"] is False


def test_preflight_reports_invalid_env_shape(tmp_path, monkeypatch, capsys) -> None:
    clear_credentials(monkeypatch)
    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "\n".join(
            [
                "CHAOJIYING_USER=file-user",
                "CHAOJIYING_PASS2=NOT_A_LOWERCASE_MD5",
                "CHAOJIYING_SOFT_ID=file-softid",
            ]
        ),
        encoding="utf-8",
    )

    status = module.main(
        ["preflight", "--env-file", str(env_file), "--no-network", "--json"]
    )

    assert status == 1
    output = json.loads(capsys.readouterr().out)
    assert output["status"] == "invalid_env_shape"
    assert output["ready"] is False


def test_recognize_refuses_network_without_authorized_ack(tmp_path, monkeypatch) -> None:
    set_credentials(monkeypatch)
    image = tmp_path / "captcha.jpg"
    write_jpeg_fixture(image)

    status = module.main(
        [
            "recognize",
            "--image",
            str(image),
            "--codetype",
            "1902",
        ]
    )

    assert status == 1


def test_recognize_posts_pass2_and_single_image(tmp_path, monkeypatch, capsys) -> None:
    set_credentials(monkeypatch)
    image = tmp_path / "captcha.jpg"
    write_jpeg_fixture(image)
    calls = []

    class FakeResponse:
        def json(self):
            return {
                "err_no": 0,
                "err_str": "OK",
                "pic_id": "9160109360600112681",
                "pic_str": "8vka",
                "md5": "35d5c7f6f53223fbdc5b72783db0c2c0",
            }

    def fake_post(url, *, data, files, timeout):
        calls.append({"url": url, "data": data, "files": files, "timeout": timeout})
        return FakeResponse()

    monkeypatch.setattr(module.requests, "post", fake_post)

    status = module.main(
        [
            "recognize",
            "--image",
            str(image),
            "--codetype",
            "1902",
            "--ack-authorized",
        ]
    )

    assert status == 0
    assert len(calls) == 1
    call = calls[0]
    assert call["url"] == module.PROCESSING_URL
    assert call["data"]["user"] == "demo-user"
    assert call["data"]["pass2"] == hashlib.md5(b"demo-pass").hexdigest()
    assert "pass" not in call["data"]
    assert call["data"]["softid"] == "123456"
    assert call["data"]["codetype"] == "1902"
    assert sorted(call["files"]) == ["userfile"]

    output = json.loads(capsys.readouterr().out)
    assert output["pic_str"] == "8vka"


def test_recognize_defaults_codetype_to_1902(tmp_path, monkeypatch) -> None:
    set_credentials(monkeypatch)
    monkeypatch.delenv("CHAOJIYING_CODETYPE", raising=False)
    image = tmp_path / "captcha.jpg"
    write_jpeg_fixture(image)
    calls = []

    class FakeResponse:
        def json(self):
            return {"err_no": 0, "err_str": "OK", "pic_id": "p", "pic_str": "a1b2"}

    def fake_post(url, *, data, files, timeout):
        calls.append({"url": url, "data": data, "files": files, "timeout": timeout})
        return FakeResponse()

    monkeypatch.setattr(module.requests, "post", fake_post)

    status = module.main(
        [
            "recognize",
            "--image",
            str(image),
            "--ack-authorized",
        ]
    )

    assert status == 0
    assert calls[0]["data"]["codetype"] == "1902"


def test_report_error_requires_wrong_result_confirmation(monkeypatch) -> None:
    set_credentials(monkeypatch)

    status = module.main(
        [
            "report-error",
            "--pic-id",
            "9160109360600112681",
            "--ack-authorized",
        ]
    )

    assert status == 1


def test_score_uses_score_endpoint_without_softid(monkeypatch) -> None:
    set_credentials(monkeypatch)
    calls = []

    class FakeResponse:
        def json(self):
            return {"err_no": 0, "err_str": "OK", "tifen": 10, "tifen_lock": 0}

    def fake_post(url, *, data, files, timeout):
        calls.append({"url": url, "data": data, "files": files, "timeout": timeout})
        return FakeResponse()

    monkeypatch.setattr(module.requests, "post", fake_post)

    status = module.main(["score"])

    assert status == 0
    assert len(calls) == 1
    assert calls[0]["url"] == module.GET_SCORE_URL
    assert "softid" not in calls[0]["data"]
    assert calls[0]["files"] is None


def test_score_can_load_credentials_from_env_file(tmp_path, monkeypatch) -> None:
    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "\n".join(
            [
                "CHAOJIYING_USER=file-user",
                "CHAOJIYING_PASS=file-pass",
                "CHAOJIYING_SOFT_ID=file-softid",
            ]
        ),
        encoding="utf-8",
    )
    for key in ["CHAOJIYING_USER", "CHAOJIYING_PASS", "CHAOJIYING_PASS2"]:
        monkeypatch.delenv(key, raising=False)
    calls = []

    class FakeResponse:
        def json(self):
            return {"err_no": 0, "err_str": "OK", "tifen": 10, "tifen_lock": 0}

    def fake_post(url, *, data, files, timeout):
        calls.append({"url": url, "data": data, "files": files, "timeout": timeout})
        return FakeResponse()

    monkeypatch.setattr(module.requests, "post", fake_post)

    status = module.main(["score", "--env-file", str(env_file)])

    assert status == 0
    assert calls[0]["data"]["user"] == "file-user"
    assert calls[0]["data"]["pass2"] == hashlib.md5(b"file-pass").hexdigest()


def test_skill_documents_chaojiying_cli_inputs() -> None:
    skill = (ROOT / "skills/handle-interactive-verification/SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "## 超级鹰脚本用法" in skill
    assert "--env-file" in skill
    assert "--image" in skill
    assert "--image-base64-file" in skill
    assert "--codetype" in skill
    assert "--ack-authorized" in skill
    assert "preflight" in skill
    assert "--no-network" in skill
    assert "--json" in skill
    assert "默认使用 `1902`" in skill
    assert "report-error" in skill
    assert "score" in skill
