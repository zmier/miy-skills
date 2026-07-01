---
name: tools-skill
description: 工具型复合 Skill。用于维护 Skill / workflow 生态中的工程协作事项，例如给其他 Skill 报 bug、创建 markdown Jira、记录复现证据、请求修复和回归验证。当前子 Skill：tool-jira。
---

# Tools Skill

这是一个工具型复合 Skill，用来承载 Skill / workflow 生态的工程维护能力。

当前只包含一个子 Skill：

- `tool-jira`：给 Skill / workflow / 工具链创建 Markdown issue / Jira。

## 何时使用

当当前任务发现另一个 Skill / workflow / 工具链存在以下问题时，使用本 Skill，并路由到 `tool-jira`：

- 行为与 `SKILL.md` 或 references 中的契约不一致；
- 应该输出状态、日志、结果或 QC，但没有输出；
- route-only 被误当作 executed-capability；
- 外部工具、浏览器、数据库、视觉、OCR、脚本执行状态不可观测；
- 上游 workflow 无法判断下游 Skill 是成功、失败、等待人工、真零结果还是技术故障；
- 需要把一次问题沉淀成可复现、可修复、可回归的 Markdown 工单。

## 路由

读取并执行：

- `skills/tool-jira/SKILL.md`

父 Skill 不直接写 issue，只负责识别这是工具治理问题并路由给子 Skill。

## 边界

- 不提前创建空子 Skill。
- 不把所有工程治理规则都塞进父 Skill。
- 不替代 `workflow-tao` 的回归测试协议；需要回归测试纪律时，引用 `workflow-tao`。
