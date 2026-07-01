---
name: deobfuscate-js-control-flow
description: Use when JS reverse engineering is blocked by async stack, Promise callbacks, dispatcher functions, switch-based invocation, generator/runtime wrappers, or control-flow-flattened code, and Codex needs to locate the real crypto/request entry before replay. Trigger for async stack analysis, control flow, dispatcher, _invoke, d(e,t,n), regenerator-like runtime, and entry hidden behind Promise.then.
---

# Deobfuscate JS Control Flow

Use this skill before `find-crypto-entry` when the code shape hides the real entry behind async or dispatcher layers.

## Procedure

1. Identify the wrapper:
   - Promise chain: `Promise.resolve(x).then(success, fail)`;
   - generator/runtime wrapper: `d(e,t,n)`, `dispatchException`, `delegate`;
   - dispatcher: `_invoke(name, ...)`, switch/case, table lookup.
2. Find the real payload edge:
   - request builder;
   - crypto call;
   - `param/sign/data` assignment;
   - axios/fetch/XHR invocation.
   - bootstrap material extraction, such as inline keys, dynamic config, session seed, or public/private key material.
3. Create a small executable fixture:
   - prove dispatcher routes to real functions;
   - record input/output of one branch.
4. Hand off:
   - to `find-crypto-entry` once the real function is identified;
   - to `reproduce-js-crypto` once the algorithm contract is known.
   - to `replay-js-request` only after request envelope and response oracle are explicit.

## Obfuscation To Protocol

For OB/control-flow/string-array targets, pretty printed code is only a reading aid. The task is not Green until the execution edge reaches a verifiable protocol stage.

Use this four-stage ledger for comprehensive cases:

- `bootstrapMaterialOk`: dynamic material such as keys, iv, timestamp, session seed, or RSA material is extracted.
- `requestEnvelopeOk`: encrypted body/header fields are generated with expected keys and shapes.
- `responseDecryptOk`: encrypted response field is decrypted and parsed.
- `businessShapeOk`: decrypted payload contains expected business structure such as list length, total count, or item names.

If only the first two stages pass, mark it as partial protocol recovery. Do not call it complete deobfuscation.

## Green Rules

- `controlFlowEvidenceOk`: wrapper and entry edge are documented.
- `fixtureOk`: a minimal dispatcher/async fixture runs.
- `entryLocatedOk`: target function or request builder is named.
- `protocolStageOk`: comprehensive obfuscation cases pass the stage ledger above.

Do not treat pretty-printed code as deobfuscated until the execution edge is clear.
