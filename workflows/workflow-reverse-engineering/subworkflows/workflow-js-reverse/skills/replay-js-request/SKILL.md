---
name: replay-js-request
description: Use when a JS reverse task has already located or suspected a request parameter algorithm, and Codex needs to reproduce the target web request end to end with real endpoint first, evidence ledger, Python/Node/execjs bridge, response oracle, and explicit red/green boundaries. Trigger for JS sign/analysis/token replay, small web protocol recovery, real endpoint verification, or converting course JS/Python request code into a reproducible TASK.
---

# Replay JS Request

Use this skill after `find-crypto-entry` has identified a candidate parameter algorithm, or when course material already gives a JS function plus a Python/Node request wrapper.

This is the JS subworkflow's request construction ledger skill. Treat the target URL/method/query/body/headers/cookies/response as the main axis; algorithms, webpack modules, WASM exports, browser hooks, and miniapp request samples are evidence sources for filling fields on that axis.

## Procedure

1. Define the request contract:
   - method, URL, query/body keys, header keys, cookie/session dependency;
   - target generated fields such as `sign`, `analysis`, `token`, `m`, `data`.
   - for header signing, include the canonical string and body serialization form.
2. Locate the generation entry:
   - read JS function name, inputs, constants, timestamp/random dependencies;
   - classify whether it is sync JS, Promise JS, browser-only JS, or bundle module.
3. Choose execution bridge:
   - sync pure JS -> Python `execjs` or Node CLI;
   - Promise JS -> Node subprocess or Express wrapper;
   - browser-only JS -> Playwright/browser runtime.
4. Build request from evidence, not guesses:
   - record param keys and generated-field preview/length;
   - keep cookies/session as task-local inputs when needed;
   - do not move target-specific secrets into the generic Skill.
   - for POST JSON, lock `JSON.stringify`/`json.dumps` separators if `Content-Md5` participates in signing.
5. Verify against the real endpoint first when the target environment is available:
   - save status code, content-type, JSON top-level keys, business code/message;
   - if service rejects due to session/fingerprint/rate limit, mark the real service branch red instead of replacing it with mock Green.
   - if direct replay times out, check bootstrap endpoints, session cookies, and visited/verification APIs before blaming the crypto.
6. Only use fixture/oracle fallback when real access is unavailable:
   - label it `structural-green`, not full replay Green;
   - explain the missing external condition.

## Green Rules

Use separate flags:

- `algorithmOk`: generated field is non-empty and shape matches expectation.
- `requestConstructedOk`: URL/method/params/body/headers are complete.
- `realEndpointReachedOk`: HTTP request reaches the target and returns a status.
- `realJsonOk` or `responseOracleOk`: response is parseable or matches known oracle.
- `canonicalOk`: request signing string is explicit and matches generated headers.
- `stageGreen`: only true when the task-defined endpoint criterion passes.

Never collapse these into one vague “success”; the split is what tells the next task where the real red light is.

## Bootstrap / Session Gate

Some sites require a preflight request before the encrypted API works. Record:

- bootstrap URL;
- cookies/session values obtained;
- whether the same encrypted request fails without bootstrap;
- whether the bootstrap path is part of the minimal replay.
- dynamic crypto material extracted from bootstrap, such as AES key, IV, timestamp, key id, version, or RSA key material.
- whether request encryption and response decryption must share the same bootstrap context.

For signer-gated + decode-gated protocols, split replay into:

1. bootstrap material;
2. request envelope generation;
3. real endpoint POST/GET;
4. response decrypt;
5. business-shape oracle.

AI-generated or course-provided wrappers can be used as a parallel implementation, but they become evidence only after endpoint/UAT verification.

## Output Files

For a task, prefer:

```text
TASKxx-说明.md
evidence-ledger.md
run.py or run.js
outputs/taskxx-*-result.json
tests/uat/test_taskxx_outputs.py
log.md
```

## Provenance

Course scripts and target-specific cookies belong in the task or course material path. The workflow should store only the reusable replay method, evidence schema, and failure taxonomy.
