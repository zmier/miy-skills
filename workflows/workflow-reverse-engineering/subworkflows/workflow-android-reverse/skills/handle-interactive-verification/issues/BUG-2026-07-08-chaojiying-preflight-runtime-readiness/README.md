# BUG: Chaojiying preflight does not expose runtime readiness

## Summary

`handle-interactive-verification` documents a Chaojiying single-challenge route, but the caller currently discovers missing credentials and missing Python dependencies only at task runtime, which blocks automatic CAPTCHA handoff and can be misclassified as OCR failure.

Resolved on 2026-07-08: the skill now exposes a no-network `preflight` status contract, local `.env.local` credentials are configured with `PASS2`, project-venv preflight returns `ready`, and real-service `score` UAT returns `err_no=0`.

## Metadata

| Field | Value |
|---|---|
| Date | 2026-07-08 |
| Reporter | TASK04-external-fund-data-inventory / RESSET direct interface forward test |
| Target | `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification` |
| Type | BUG |
| Severity | P2 |
| Evidence status | complete |
| Status | fixed |
| Fix log | `fix-log.md` |

## Environment

| Field | Value |
|---|---|
| Working directory | `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究` |
| Command / tool | `scripts/chaojiying_client.py` via default `python3` |
| Input | RESSET CAPTCHA forward test; no image submitted yet |
| Output path | this issue |

## Reproduction

Credential readiness check:

```bash
test -f "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
  && echo "present" || echo "missing"
```

Observed:

```text
missing
```

Dry-run script check:

```bash
python3 "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
  --env-file "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
  --dry-run \
  score
```

Observed:

```text
Traceback (most recent call last):
  File ".../scripts/chaojiying_client.py", line 14, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```

## Expected Behavior

The skill should provide a clear preflight path before a caller reaches a real CAPTCHA challenge:

- report whether `.env.local` or equivalent environment variables are present;
- report whether required Python dependencies such as `requests` are importable;
- avoid contacting Chaojiying during preflight;
- return a machine-readable status such as `ready`, `missing_credentials`, `missing_dependency`, or `needs_manual_fallback`;
- tell callers to use manual handoff when Chaojiying is not ready.

## Actual Behavior

The RESSET caller had to discover readiness ad hoc:

- `.env.local` was absent;
- the documented script cannot even run a dry-run under default `python3` because `requests` is missing;
- no single preflight command or status contract distinguishes missing credentials from missing dependency or OCR/service failure.

No CAPTCHA image was sent to Chaojiying, and no third-party API call was made in this reproduction.

## Resolution

Fixed in:

- `skills/handle-interactive-verification/scripts/chaojiying_client.py`
- `skills/handle-interactive-verification/SKILL.md`
- `tests/unit/test_chaojiying_client.py`
- `skills/handle-interactive-verification/.env.local`
- `skills/handle-interactive-verification/issues/BUG-2026-07-08-chaojiying-preflight-runtime-readiness/fix-log.md`

Current behavior:

- `preflight --no-network --json` returns one of `ready`, `missing_credentials`, `missing_dependency`, or `invalid_env_shape`.
- Missing `requests` is reported as structured JSON instead of import traceback.
- `.env.local` is present, uses `CHAOJIYING_PASS2`, and does not store the plaintext password.
- `softid` is treated as optional, matching Chaojiying HTTP docs.
- Real-service `score` UAT passed; no CAPTCHA image was uploaded.

## Evidence

- `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK04-external-fund-data-inventory/logs/log.md`
- Terminal output from 2026-07-08 RESSET direct POST forward-test setup:
  - `chaojiying_env=missing`
  - `ModuleNotFoundError: No module named 'requests'`
- Target skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/SKILL.md`
- Target script: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py`

## Downstream Impact

RESSET automation expects `default Chaojiying, failure manual`. Without a deterministic preflight, the caller may pause only after reaching the CAPTCHA gate, confuse infrastructure readiness with CAPTCHA recognition failure, or wait for an automatic route that cannot run. Manual fallback exists, so this is not P1, but it causes unnecessary interruption and unclear status.

## Suspected Area

| File / Module | Why suspicious |
|---|---|
| `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/SKILL.md` | Documents Chaojiying usage but does not define a required preflight command/status contract for callers. |
| `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py` | Imports `requests` before argument handling, so even dry-run/helpful readiness checks fail if dependency is missing. |
| `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.example` | Credential template exists, but callers need a health-check that verifies `.env.local` or environment variables without exposing secrets. |

## Regression Requirement

Add a no-network preflight path and document it in `SKILL.md`. The preflight must pass with no CAPTCHA image and no third-party call. It should classify:

```text
ready
missing_credentials
missing_dependency
invalid_env_shape
```

The script should not fail at module import before it can produce a structured readiness result.

## UAT / Acceptance Run

Required after fix because this issue affects a real browser/database workflow and a human fallback boundary.

Run from any working directory:

```bash
python3 "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
  preflight \
  --env-file "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
  --no-network \
  --json
```

Pass standard:

```text
exit code 0 for ready;
non-zero but structured JSON for missing_credentials or missing_dependency;
no third-party HTTP request;
no secret values printed;
caller can map non-ready status to manual fallback.
```

Optional real-service UAT, only when credentials are intentionally configured and user authorizes a single check:

```bash
python3 "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py" \
  score \
  --env-file "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local" \
  --ack-authorized
```

Pass standard:

```text
returns account score or a structured service/auth error;
does not print credentials;
does not require a CAPTCHA image.
```

Executed fixed-state results:

```text
default python3 preflight:
  exit code: 1
  status: missing_dependency
  env_file.status: loaded
  missing_credentials: none
  network.attempted: false

project .venv preflight:
  exit code: 0
  status: ready
  network.attempted: false

real-service score UAT:
  exit code: 0
  err_no: 0
  err_str: OK
  tifen: 1000
  tifen_lock: 0
  tifen_zeng: 1000
```

Detailed commands and residual risk are recorded in `fix-log.md`.

## Acceptance Criteria

- [x] `SKILL.md` documents a mandatory Chaojiying preflight before attempting automatic recognition.
- [x] `chaojiying_client.py` can report missing dependency and missing credential states without an import traceback.
- [x] Preflight output is structured enough for callers such as `$resset-download` to choose manual fallback immediately.
- [x] No CAPTCHA result, password, pass2, or token is written to logs.
- [x] A `fix-log.md` records UAT commands, outputs, pass/fail status, and residual risk.
