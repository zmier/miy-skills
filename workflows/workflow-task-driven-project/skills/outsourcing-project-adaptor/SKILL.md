---
name: outsourcing-project-adaptor
description: workflow-task-driven-project 的外包/客户需求场景 adaptor。用于把客户原始沟通转化为“机会评估型 task-driven project”，先判断接不接、怎么接、是否先 PoC，再决定是否进入实际执行项目。
---

# Outsourcing Project Adaptor

## Purpose

外包项目不能从“客户说想做什么”直接跳到“创建执行项目”。应先创建机会评估型 task-driven project：

```text
客户原始材料
-> 真实需求识别
-> 风险与可行性评估
-> 客户追问
-> PoC / 报价边界
-> 接单决策
```

## When To Use

使用本 adaptor，当用户输入包含：

- 客户聊天记录；
- 外包、报价、接单、项目咨询；
- 需求频繁变化；
- 需要判断能不能做、要不要做；
- 平台、账号、合规、授权或交付风险；
- 需要先做 PoC 或客户确认清单。

## Default Output

默认先创建或更新：

```text
PROJECT-机会评估-客户名或项目名/
```

若用户已经要求把机会评估纳入某个现有项目，则在该项目下创建：

```text
PROJECT-机会评估-*/
```

## TASK Template

```text
TASK01 原始材料归档
TASK02 真实需求识别
TASK03 风险与可行性评估
TASK04 客户追问与确认
TASK05 PoC / 最小验证设计
TASK06 接单决策
```

## Green Standards

机会评估 Green 不是“项目做完”，而是出现明确决策：

- `accept`：可接，进入执行型 task-driven project；
- `reject`：不接，说明原因；
- `poc-first`：先做小验证；
- `rescope`：改范围后再判断；
- `pending-client`：缺客户材料，不能定价或承诺。

## Risk Taxonomy

- 需求风险：表层需求和真实需求不一致。
- 技术风险：关键 API、数据、账号、环境不可验证。
- 合规风险：要求绕过平台规则、未授权采集、骚扰或隐私风险。
- 交付风险：验收口径不清、客户期待不现实。
- 协作风险：客户材料、账号、权限、响应速度不可控。
- 报价风险：一期二期混报、PoC 和正式交付混报。

## Required Artifacts

- 原始材料归档。
- 需求澄清纪要。
- 风险与可行性评估。
- 客户追问清单。
- 报价范围边界。
- 接单决策建议。

## Handoff To Execution

只有当机会评估 Green 为 `accept` 或 `poc-first` 时，才创建执行型 task-driven project。

执行型 project 的目标必须重新声明，不能沿用机会评估目标。

