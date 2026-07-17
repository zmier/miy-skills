# 图型 Workflow 的 Node / Task 分层约定

## 背景

在 `workflow-research` 的 forward-test 中，`CASE-260521-基金经理研究` 暴露出一个 workflow 设计问题：有些项目不能用稳定主流程表示。它们不是“先 A 再 B 再 C”的树形工序，而是多个候选节点同时生长、竞争、合并、降级的图状探索。

## 问题

如果只用 `tasks/` 管理这种项目，容易产生误导：

```text
task 顺序看起来像研究顺序；
task 输出看起来像最终主轴；
不同候选路线的关系被压扁在一个执行日志里；
后续复盘时很难知道某次工作分别改变了哪些研究节点。
```

## 抽象

workflow 可能有不同拓扑：

```text
tree-like workflow：主干与分支较清晰，适合工序型编排；
graph-like workflow：主干和节点关系需要探索，适合 route / claim / hypothesis portfolio；
hybrid graph-of-trees：顶层图状探索，节点内部调用树形子 workflow。
```

图型 workflow 应区分：

```text
nodes/ = 图层节点，管理长期存在的 route / claim / design / evidence state
tasks/ = 执行层任务，管理一段时间内线性推进的工作包
```

## 规则

```text
Task 可以线性推进；
Task 的影响可以非线性地贡献到多个 Node；
Node 可以被多个 Task 反复更新；
Workflow 父入口应说明 Task 如何回挂 Node。
```

## 迁移边界

该规则首先适用于学术研究、产品探索、策略研究、复杂诊断等主轴尚未固定的项目。对于逆向工程、数据采集工程、格式转换交付等主流程清晰的 tree-like workflow，仍应以稳定工序和红绿灯为主，不需要强制建立 `nodes/`。
