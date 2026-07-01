---
name: reproduce-js-crypto
description: Use when a JS reverse task needs to reproduce digest, HMAC, symmetric, asymmetric, or custom JavaScript cryptographic parameters and cross-check outputs between JavaScript and Python before request replay. Trigger for MD5, SHA, HMAC, AES, DES, RSA, SM algorithms, sign/code/token generation, timestamp coupling, salt/secret discovery, encoding differences, and JS/Python parity validation.
---

# Reproduce JS Crypto

Use this skill after locating an algorithm entry with `find-crypto-entry`, or when course material already provides a candidate algorithm implementation.

This skill is field-level, not the workflow endpoint. Its job is to explain and verify how one dynamic field is generated, then hand the result back to the request construction ledger in `replay-js-request`.

## Core Workflow

1. Identify the target field:
   - common names: `sign`, `token`, `code`, `analysis`, `m`, `data`, `password`;
   - record where it appears: query, body, header, cookie, response decode.
2. Recover the algorithm contract:
   - algorithm family: digest, HMAC, symmetric, asymmetric, national crypto, modified/custom;
   - input fields and order;
   - salt/secret/key/iv/public key;
   - timestamp/random dependencies;
   - encoding: UTF-8, hex, base64, URL encoding, CryptoJS WordArray.
   - canonical string: exact method/path/body/header order when signing requests.
   - for symmetric crypto: mode, padding, key, iv/nonce, plaintext/ciphertext encoding.
3. Build JS/Python parity:
   - compute with the original JS or a minimal extracted JS function;
   - compute independently in Python when the algorithm is standard;
   - compare exact output, length, and alphabet.
4. Preserve coupling:
   - if a timestamp/random value is used to generate the field, pass the same value into the final request;
   - do not call `Date.now()` separately in JS and Python unless that is the target behavior.
5. Hand off to `replay-js-request`:
   - only after algorithm output is stable;
   - record endpoint response as a separate Green from algorithm parity.
6. For encrypted responses:
   - record response ciphertext encoding;
   - decrypt to plaintext;
   - parse plaintext and verify business keys.

## Digest/HMAC Baseline

For standard algorithms, use a known tiny input such as `"1"`:

- MD5 output is 32 hex chars.
- SHA1/SHA224/SHA256/SHA384/SHA512 lengths are 40/56/64/96/128 hex chars.
- HMAC output length follows the digest algorithm, but requires a key.

## Request Signature Pattern

For header signatures such as `x-signature`, write the canonical string explicitly before testing:

```text
METHOD_UPPER
/path?query
header-a:value
header-b:value
body-md5:value
```

Verify:

- method case;
- path/query exactly as signed, including query order;
- body serialization separators and key order;
- final newline;
- HMAC key and output casing.

## Symmetric Crypto Pattern

For DES/AES/SM4-like tasks, create a crypto contract before coding:

```text
algorithm = DES/AES/SM4
mode = CBC/ECB/CTR/GCM/...
padding = PKCS7/PKCS5/NoPadding/...
key = ...
iv/nonce = ...
plaintext encoding = utf8/json/hex/base64
ciphertext encoding = hex/base64/url-safe-base64
```

Make JS and Python use the same contract. If course samples use different modes, treat them as demonstrations and build a parity fixture with one explicit mode.

## Response Decrypt Pattern

For APIs that return encrypted bodies:

1. Keep the raw response preview.
2. Identify ciphertext encoding: base64, hex, URL-safe base64, JSON field.
3. Apply the crypto contract.
4. Parse plaintext as JSON or text.
5. Use business-shape Green such as top-level keys or list length.

If the endpoint returns 403/401/anti-bot HTML, record that as an endpoint red light. Do not replace it with a local fixture unless the task is explicitly structural-only.

## Asymmetric And Modified Algorithms

For RSA-like tasks:

- record public/private key format: PKCS1, PKCS8, PEM, modulus/exponent;
- verify encrypt/decrypt roundtrip before request replay;
- expect ciphertext to vary when padding is random.

For hybrid request crypto:

- identify which part is RSA/envelope encryption;
- identify which part is digest signature;
- identify which part is response AES/DES decrypt;
- verify each part separately, then verify the whole endpoint.
- for bootstrap-driven protocols, record where key/iv/timestamp/version/RSA material comes from before generating any request field.
- for custom post-processing such as printable-character shifting, keep it as a named transform after the standard primitive instead of pretending it is part of RSA/AES.

For SM-family web protocols:

- identify whether SM2/SM3/SM4 is used by name and by actual primitive call;
- record `encData`, `signData`, `encType`, `signType`, `appCode`, `timestamp` separately;
- keep dynamic headers such as `x-tif-nonce`, `x-tif-signature`, `x-tif-timestamp` coupled with the generated body;
- decrypt the response and verify business keys, not only HTTP status.
- for SM3/SM4 parity, prefer a fixed contract first: plaintext, key, iv, mode, padding, ciphertext encoding;
- for encrypted API responses, decrypt the same ciphertext through both original JS helper and Python `gmssl` when feasible, then compare plaintext exactly before parsing business JSON.

For modified algorithms:

- do not trust variable names such as `aes` or `rsa`;
- inspect whether the code actually calls standard crypto primitives;
- create encode/decode roundtrip tests because ciphertext may include random salt/string segments;
- only call it standard crypto when the contract matches a known algorithm.

When using course JS libraries, check package export shape. Some packages expose `default` or named exports instead of a direct CommonJS constructor.

If a supposed standard algorithm does not match the known baseline, treat it as:

- wrong input/encoding;
- missing salt/secret;
- modified algorithm;
- browser/runtime state dependency.

## Green Rules

Use separate flags:

- `digestParityOk` / `cryptoParityOk`: JS and Python outputs match.
- `fieldShapeOk`: generated field matches expected length/alphabet.
- `canonicalOk`: signed string contains the exact method/path/header/body components.
- `desParityOk` / `symmetricParityOk`: JS and Python ciphertext match under the same contract.
- `timestampCouplingOk`: dynamic values are reused consistently.
- `requestReplayOk`: real endpoint or oracle accepts the generated field.
- `responseDecryptOk`: encrypted response decrypts and parses.
- `jsPythonDecryptSameOk`: original JS helper and Python port decrypt the same ciphertext to identical plaintext.
- `businessShapeOk`: decrypted payload contains expected business structure.
- `modifiedRoundtripOk`: custom encode/decode returns equivalent payload.
- `bootstrapMaterialOk`: dynamic material is extracted and bound to the same request/response cycle.
- `requestEnvelopeOk`: all encrypted/signature envelope fields are present and have expected shape.

Do not call an algorithm “reversed” until both parity and a request/response oracle pass, unless the task explicitly defines a structural-only Green.
