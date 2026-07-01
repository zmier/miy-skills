# Pass / Fail

## Summary

Overall result: PASS after manual verification

CNKI was not rerun in this test because the 2026-06-20 executed-search smoke test already confirmed CNKI execution. This run tests WoS only.

## WoS Handoff Probe

Result: PARTIAL

Command:

```bash
cd /Users/narra/Documents/alib/Writer/.pytools/scholar-kit
WOS_MANUAL_CONFIRM_TIMEOUT_MS=5000 poetry run python3 \
  skills/scholar-kit-wos-search/scripts/wos_fetch.py \
  --query 'TS=("digital governance")' \
  --mode browser \
  --browser-stage handoff \
  --output '.../outputs/wos_handoff_probe_timeout.json'
```

Observed:

- Output JSON was written.
- Status: `browser_handoff_ready`.
- Current page: `https://www.webofscience.com/wos/woscc/advanced-search`.
- Page title: `Advanced search - Web of Science Core Collection`.
- `manual_checkpoint.confirmed=false` after the short callback timeout.

Interpretation:

The shared-browser WoS entry is available, but this does not prove result retrieval.

## WoS Results Probe

Initial short-timeout result: FAIL / OBSERVABILITY ISSUE

Command:

```bash
cd /Users/narra/Documents/alib/Writer/.pytools/scholar-kit
WOS_MANUAL_CONFIRM_TIMEOUT_MS=5000 poetry run python3 \
  skills/scholar-kit-wos-search/scripts/wos_fetch.py \
  --query 'TS=("digital governance")' \
  --mode browser \
  --browser-stage results \
  --output '.../outputs/wos_results_probe_timeout.json'
```

Observed terminal output:

```text
WoS 查询提交后既未进入 summary URL，也未识别到 zero result；当前返回保守失败。
WoS manual checkpoint callback timed out after 5000ms; falling back to stdin if available
manual confirmation could not use callback and stdin is unavailable
```

Observed file state:

- `wos_results_probe_timeout.json` was not written.
- The process remained running and had to be manually terminated.
- User-side observation: Chrome did not appear to require verification.

Interpretation:

The short-timeout run exposed an observability issue: while waiting for slow WoS verification / page readiness, the script did not write an intermediate machine-readable waiting status.

## WoS Results Probe After Verification

Result: PASS

Command:

```bash
cd /Users/narra/Documents/alib/Writer/.pytools/scholar-kit
WOS_MANUAL_CONFIRM_TIMEOUT_MS=180000 poetry run python3 \
  skills/scholar-kit-wos-search/scripts/wos_fetch.py \
  --query 'TS=("digital governance")' \
  --mode browser \
  --browser-stage results \
  --output '.../outputs/wos_results_probe_after_verification.json'
```

Observed:

- Output JSON was written.
- Status: `browser_results_ready`.
- Result URL: `https://www.webofscience.com/wos/woscc/summary/03f4b191-a4ad-40fd-8d5f-10cc68989880-01ba6e795d/relevance/1`.
- Result title: `TS=("digital governance") – 1,468 – Web of Science Core Collection`.
- Result count: `1468`.
- Candidate count: `50`.

Interpretation:

WoS executed-search capability is confirmed after manual verification / longer wait.

## Bug Ticket

Filed as an observability / waiting-state improvement at:

- `/Users/narra/Documents/alib/Writer/.pytools/scholar-kit/skills/scholar-kit-wos-search/issues/BUG-2026-06-21-wos-results-probe-stalls/README.md`

## Regression Standard After Fix

This test now passes for execution. The remaining improvement is that `browser-stage results` should write an intermediate output JSON with one of:

- `completed`
- `zero_result_confirmed`
- `awaiting_manual_confirmation`
- `failed_with_reason`

It must not:

- report `status=scaffold` as execution;
- stop at handoff and claim WoS retrieval passed;
- hang without writing status during slow verification / page readiness.
