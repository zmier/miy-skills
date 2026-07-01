# <TYPE>: <short title>

## Summary

<一句话说明问题和影响。>

## Metadata

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Reporter | <calling skill / workflow / task> |
| Target | <target skill / workflow path> |
| Type | BUG / REQ / DOC / REG |
| Severity | P0 / P1 / P2 / P3 |
| Evidence status | complete / partial / needs-repro |

## Environment

| Field | Value |
|---|---|
| Working directory | <path> |
| Command / tool | <command or tool> |
| Input | <input path or query> |
| Output path | <output path> |

## Reproduction

```bash
<minimal command if available>
```

## Expected Behavior

<应当发生什么。>

## Actual Behavior

<实际发生什么。>

## Evidence

- <path / log / screenshot / output>

## Downstream Impact

<调用方为什么无法继续，或者会造成什么误判。>

## Suspected Area

| File / Module | Why suspicious |
|---|---|
| <path> | <reason> |

## Regression Requirement

<修复后应该如何验证。明确 pass 标准。>

## Acceptance Criteria

- [ ] <criterion>
- [ ] <criterion>
- [ ] <criterion>
