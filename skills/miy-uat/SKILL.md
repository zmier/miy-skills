---
name: miy-uat
description: UAT 与 subAgent 验收防作弊 Skill。用于设计黑箱/灰箱验收、subAgent UAT prompt、技能/工作流改动回归测试、避免把预期答案/修复意图/已知 bug 泄露给验证者，并区分真实泛化能力与照题干复现。适用于用户要求做 UAT、开 subAgent 验证、测试 Skill 是否生效、检查 workflow 是否复发旧错误、或质疑测试 prompt 是否作弊时。
---

# Miy UAT

## Core Principle

UAT 的目标是验证被测对象能否在真实使用条件下自然产出正确行为，不是验证另一个 Agent 是否会照着提示复述标准答案。

```text
测 Skill，就不要把 Skill 应该产出的关键结构写进测试 prompt。
测修复，就不要把 bug、fix、预期输出和你自己的结论泄露给验证者。
测理解，就不要把答案拆成步骤交给验证者照做。
```

## UAT Types

| 类型 | 何时使用 | 给 subAgent 什么 |
|---|---|---|
| black-box | 验证真实用户入口是否自然工作 | 用户任务、被测 Skill 路径、原始材料 |
| gray-box | 验证特定接口/模板是否生效 | 被测 Skill/模板、原始材料、产物要求 |
| white-box | 验证某个修复点是否覆盖 | 可说明改动范围，但仍避免给标准答案 |

默认优先使用 black-box 或 gray-box。只有在做代码审查、补丁覆盖或回归诊断时才使用 white-box。

## Anti-Cheating Rules

禁止在 UAT prompt 中泄露：

- 预期最终答案；
- 你已经发现的具体正确结构；
- 旧 bug 的精确表现，除非目标是 white-box 回归；
- 修复方案；
- 需要出现的关键词列表；
- 评价标准中会让 subAgent 反向构造答案的细节。

允许提供：

- 被测 Skill 路径；
- 原始输入材料；
- 真实用户任务；
- 输出格式的外壳，例如“给出你会返回给用户的内容”；
- 禁止改文件、禁止参考已有产物等隔离规则；
- 如果是 gray-box，可要求“按 Skill 自己的要求执行”，但不要替 Skill 展开要求。

## Prompt Pattern

推荐 black-box prompt：

```text
请读取 <Skill> 和 <raw material>。
假设用户提出如下任务：<真实用户请求>。
请按 Skill 的要求执行第一轮输出。
不要参考已有产物，不要修改文件。
输出你会返回给用户的内容，以及你会写入的文件草案/提纲草案。
```

不合格 prompt：

```text
请先识别 A01 是 P1 且 P2，再拆 Bx/By，并输出 proxy bridge、warrant、evidence。
```

这不是 UAT，而是把标准答案结构写进题干。

## Evaluation After SubAgent Returns

主 Agent 在 subAgent 返回后再使用隐藏验收标准评估：

```text
expected_behavior:
actual_behavior:
pass_fail:
where_it_generalized:
where_it only followed prompt:
regression_risk:
next_patch:
```

验收标准可以来自先前讨论，但不要提前给 subAgent。

## Isolation Rules

- 明确要求 subAgent 不要读取现有 expected output、discussion outline、golden answer 或主 Agent 的分析记录。
- 如果必须读取日志，只能读取 Skill 要求的日志；不要读取含有本次标准答案的 case log。
- 对技能 UAT，优先让 subAgent 读取 Skill + 原始材料，而不是读取已经按新规则生成的产物。
- 对代码/文档改动 UAT，subAgent 可以读 diff，但不要读主 Agent 的“为什么这么改”的解释，除非是 white-box review。

## Reporting

最终报告应区分：

```text
SubAgent raw result:
Main Agent evaluation:
Whether the UAT was clean:
Any leakage found:
Patch needed:
```

抽取类 / 生成类 UAT 必须同时保存两个本地记录：

```text
raw output:
  subAgent 原始返回；
  包括它会返回给用户的内容，以及它会写入的文件草案；
  不夹杂主 Agent 的事后评价。

evaluation:
  主 Agent 的隐藏标准评估；
  包括 expected_behavior、actual_behavior、pass_fail、regression_risk、next_patch。
```

不得只保存 evaluation。否则用户无法验收“被测对象到底产出了什么”，UAT 证据链不完整。

推荐文件命名：

```text
logs/<date>-UAT-<case>-raw-output.md
logs/<date>-UAT-<case>-evaluation.md
```

如果发现 prompt 泄题，应明确标记：

```text
UAT invalid due to prompt leakage.
```

然后重跑更干净的 UAT。
