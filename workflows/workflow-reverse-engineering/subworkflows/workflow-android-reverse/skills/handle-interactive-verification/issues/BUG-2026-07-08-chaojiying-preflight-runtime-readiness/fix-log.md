# Fix Log

## Date

2026-07-08

## Modified Files

- `skills/handle-interactive-verification/scripts/chaojiying_client.py`
  - Added `preflight --no-network --json`.
  - Made `requests` an optional import so missing dependency is reported as structured readiness JSON instead of import traceback.
  - Added readiness statuses: `ready`, `missing_credentials`, `missing_dependency`, `invalid_env_shape`.
  - Ensured preflight does not mutate `os.environ` and never calls the Chaojiying HTTP endpoints.
  - Accepted `score --env-file ... --ack-authorized` for the optional UAT command shape; `score` still submits no CAPTCHA image.
  - Set the script executable for direct CLI use when the project virtualenv is active.
- `skills/handle-interactive-verification/SKILL.md`
  - Documented mandatory Chaojiying preflight before any automatic recognition attempt.
  - Documented preflight inputs, output status contract, and manual fallback mapping.
- `tests/unit/test_chaojiying_client.py`
  - Added coverage for ready, missing credentials, missing dependency, invalid env shape, no-network behavior, and no secret leakage in preflight output.
  - Added coverage that `softid` is optional, matching Chaojiying HTTP docs.
- `skills/handle-interactive-verification/.env.local`
  - Created as a local ignored credential file with `CHAOJIYING_USER`, `CHAOJIYING_PASS2`, and `CHAOJIYING_CODETYPE=1902`.
  - Stored `PASS2` only; plaintext password was not written.
  - Set file mode to `600`.

## Reproduction

Credential readiness check:

```bash
test -f "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" && printf present || printf missing
```

Result:

```text
present
```

The original failure mode was a default `python3` import traceback before the caller could classify readiness.

## Regression

Static compile:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m py_compile skills/handle-interactive-verification/scripts/chaojiying_client.py
```

Result: PASS.

Unit / contract tests:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest tests/unit/test_chaojiying_client.py tests/unit/test_skill_contracts.py
```

Result:

```text
22 passed in 0.09s
```

Ready-path no-network smoke with dummy credentials and the project venv:

```bash
CHAOJIYING_USER=uat-user CHAOJIYING_PASS=uat-pass CHAOJIYING_SOFT_ID=uat-softid \
PYTHONDONTWRITEBYTECODE=1 \
"/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python" \
"/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
preflight --no-network --json
```

Result:

```text
exit code: 0
status: ready
network.attempted: false
dependency.requests: ok
credentials: present by source only; no secret values printed
```

## UAT / Acceptance Run

Required UAT command from the issue, run from `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究`:

```bash
python3 "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
  preflight \
  --env-file "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
  --no-network \
  --json
```

Result:

```text
exit code: 1
status: missing_dependency
ready: false
manual_fallback: true
env_file.status: loaded
dependency.requests.ok: false
missing_credentials: none
network.attempted: false
```

Pass / fail: PASS. The run returned non-zero structured JSON, did not print a traceback, did not print secret values, and gave callers a direct `manual_fallback` signal.

Project-venv no-network UAT using the same `.env.local`:

```bash
"/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python" \
"/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
preflight \
--env-file "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
--no-network \
--json
```

Result:

```text
exit code: 0
status: ready
ready: true
manual_fallback: false
env_file.status: loaded
dependency.requests.ok: true
credentials.softid.source: optional_missing
network.attempted: false
```

Real-service score UAT, run after the user asked whether direct invocation is available:

```bash
"/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python" \
"/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
score \
--env-file "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
--ack-authorized
```

Result:

```text
exit code: 0
err_no: 0
err_str: OK
tifen: 1000
tifen_lock: 0
tifen_zeng: 1000
```

Pass / fail: PASS. The configured credentials, pass2 hashing/storage path, network route, and Chaojiying score endpoint are usable. No CAPTCHA image was uploaded.

## Acceptance Criteria

- [x] `SKILL.md` documents a mandatory Chaojiying preflight before attempting automatic recognition.
- [x] `chaojiying_client.py` reports missing dependency and missing credential states without an import traceback.
- [x] Preflight output is structured enough for callers such as `$resset-download` to choose manual fallback immediately.
- [x] No CAPTCHA result, password, pass2, or token is written to logs.
- [x] `fix-log.md` records UAT commands, outputs, pass/fail status, and residual risk.

## Residual Risk

- Default `python3` still lacks `requests` in the observed environment. This is now an explicit `missing_dependency` readiness state; use the project `.venv` or manual fallback.
- Real Chaojiying score UAT passed. Full recognition remains untested until a single authorized CAPTCHA image is available; run only after `preflight` returns `ready`.
