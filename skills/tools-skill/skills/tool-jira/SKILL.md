---
name: tool-jira
description: 为 Skill / workflow / 本地工具链创建 Markdown Jira / issue。用于跨 Skill 报 bug、记录契约缺口、状态不可观测、复现命令、证据路径、修复验收标准和回归要求。
---

# Tool Jira

把发现的问题写成可复现、可修复、可回归的 Markdown issue。

## 输入

尽量收集：

- 问题发生时的调用方 workflow / Skill；
- 被报问题的目标 Skill / workflow / 工具链路径；
- 复现命令或触发步骤；
- 预期行为；
- 实际行为；
- 输出文件、日志、截图、状态文件、终端关键输出；
- 下游影响；
- 是否已有回归 fixture / run。

信息不全也可以报，但必须标 `evidence_status: partial`。

## Issue 放置位置

优先放到被报问题对象自己的目录下：

```text
target-skill-or-workflow/
└── issues/
    └── BUG-YYYY-MM-DD-short-title/
        └── README.md
```

如果不是 bug，而是能力需求或契约改进：

```text
target-skill-or-workflow/
└── issues/
    └── REQ-YYYY-MM-DD-short-title/
        └── README.md
```

如果问题跨多个 Skill，放到最近的共同父 workflow / 复合 Skill 下，并在 issue 中列出 affected skills。

## Issue 类型

| Prefix | 用途 |
|---|---|
| `BUG` | 明确行为错误、脚本异常、契约未履行、状态不可判定 |
| `REQ` | 新能力、增强请求、契约补强 |
| `DOC` | 文档与真实行为不一致 |
| `REG` | 回归测试缺失或回归失败 |

## README.md 模板

创建 issue 时使用以下结构。没有的信息写 `unknown`，不要编造。

```markdown
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

或：

```text
1. <step>
2. <step>
3. <step>
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

## UAT / Acceptance Run

<必须写明修复后是否需要 UAT。若 issue 涉及真实外部系统、浏览器链路、人工接管、数据完整性、下游流程可用性或历史复现命令，则必须给出可执行 UAT 命令 / 步骤、输出路径和 pass / fail 标准。若暂时不能执行，写明阻塞原因、替代验证和后续补跑条件。>

## Acceptance Criteria

- [ ] <criterion>
- [ ] <criterion>
- [ ] <criterion>
```

## 严重度

| Severity | 判断 |
|---|---|
| P0 | 数据破坏、安全风险、会导致严重错误结论 |
| P1 | 主流程阻塞，无法可靠完成任务 |
| P2 | 有 workaround，但会造成误判、等待、重复劳动或回归不可判定 |
| P3 | 文档、可观测性、可维护性改进 |

## 写作规则

- 用事实和证据路径说话。
- 区分 `route-only`、`executed-capability`、`scaffold`、`handoff`、`completed`。
- 不把等待人工、验证码、登录、真零结果、技术失败混写。
- 不要求修复方读当前对话才能理解 issue。
- 如果 issue 来自回归测试，必须写 run 路径和 pass / fail 标准。
- 修复方不能只用静态检查或单元测试关闭 issue；必须执行 issue 中定义的 UAT / Acceptance Run，或在 `fix-log.md` 中明确记录无法执行 UAT 的阻塞原因、替代验证和补跑条件。
- UAT 结果必须写入 `fix-log.md`：包括命令 / 步骤、输出路径、关键指标、pass / fail 判定和残余风险。

## 修复方使用方式

修复目标 Skill 时，应先读取：

1. 目标 Skill 的 `SKILL.md`；
2. 对应 `issues/.../README.md`；
3. issue 中列出的证据文件；
4. 若涉及回归，读取 `workflow-tao/references/regression-test-protocol.md` 或 issue 指定的回归协议。

修复后在 issue 中追加或创建 `fix-log.md`，记录：

- 修改了哪些文件；
- 如何复现；
- 跑了哪些回归；
- 跑了哪些 UAT / acceptance run；
- UAT 是否达到 issue 的 Acceptance Criteria；
- 结果是否通过；
- 残余风险。
