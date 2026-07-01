# Pass / Fail

## Summary

Overall result: PARTIAL

The original `external-evidence-routing-mini` test only verified route selection. It did not execute WoS or CNKI. This executed-search smoke test was added to check the actual database/tool chain.

## CNKI

Result: PASS

Command executed:

```bash
cd /Users/narra/Documents/alib/Writer/.pytools/scholar-kit
poetry run abstract-cli cnki-fetch \
  --expression "TI='数字治理'" \
  --limit 3 \
  --output ".../executed-search-smoke/outputs/cnki_probe.json"
```

Observed:

- `cnki_probe.json` was written.
- `cnki_run_status.json` reports `status=completed`.
- `result_count=3`.
- `awaiting_human_verification=false`.
- A CNKI debug artifact was written under `outputs/artifacts/`.

Conclusion:

CNKI execution is confirmed for this minimal query.

## WoS

Result: PARTIAL / NOT YET EXECUTED TO RESULTS

Three WoS checks were attempted:

1. Default `wos_fetch.py` mode:
   - Output: `wos_probe.json`
   - Status: `scaffold`
   - Interpretation: not a real executed search.

2. Browser `results` mode:
   - Command entered `wait_for_manual_confirmation`.
   - It did not write `wos_browser_probe.json` before manual interruption.
   - Interpretation: the browser flow reached a human-confirmation point, but this is not a completed result search and did not produce a machine-readable waiting-state file.

3. Browser `handoff` mode:
   - Output: `wos_handoff_probe.json`
   - Status: `browser_handoff_ready`
   - Current page: `https://www.webofscience.com/wos/woscc/advanced-search`
   - Page title: `Advanced search - Web of Science Core Collection`
   - Interpretation: WoS browser entry and shared-browser handoff are available, but result-page search execution is not confirmed.

Conclusion:

WoS should not be marked PASS for executed-search capability yet. It is currently confirmed only up to browser handoff. The WoS child skill or test harness needs a machine-readable waiting status such as `awaiting_human_confirmation`, or a bounded results-mode smoke test that can complete after manual confirmation.

## Regression Lesson

- Route-only tests must be named and reported as route-only.
- Executed-search tests must require real database/tool execution, or a machine-readable waiting/blocked state.
- A file with `status=scaffold` is not evidence of search execution.
- A browser opened to WoS advanced search is not evidence of WoS result retrieval.

