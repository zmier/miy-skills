# Workflow Placement Policy

## 核心规则

以后可持续生长的 workflows 默认沉淀到：

```text
Writer/00 信息/miy-skills/workflows/
```

这条规则属于 `workflow-tao` 的元治理内容。

## 为什么不是 `skills/`

Skill 是可调用执行单元，适合回答“做某类任务时怎么执行”。

Workflow 是能力工程系统，适合承载：

- 总编排；
- 子 Skills；
- 子 workflows；
- TASK 模板；
- references；
- templates / assets；
- tests / evaluation；
- provenance；
- migration / forward-test 状态。

如果一个能力只有一个入口和一套稳定步骤，放在 `skills/`。

如果一个能力需要工程化生长、多个子能力、多个实践样本和迁移验证，放在 `workflows/`。

## 为什么不是 `03 Projects/`

Project 保存具体任务和证据。它可以孵化 workflow，但不应该长期承载通用能力本体。

当一个 project 中的经验被证明可复用，应迁移或抽象到 `workflows/`，并在 project 中保留 provenance 链接。

## 为什么元 workflow 也放在 workflows

`workflow-tao` 本身研究的是 workflow 如何生成 workflow。

它不是普通知识笔记，也不是单个 Skill，而是一个会通过实践样本持续更新的元 workflow。因此它应与 `workflow-reverse-engineering` 等领域 workflow 并列放在 `workflows/` 下。

