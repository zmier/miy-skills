---
name: workflow-research-orchestrator
description: workflow-research 的总编排子 Skill。用于诊断学术项目的 route portfolio 与 R0-R7 工作面，路由到文献、论证、数据、研究设计、route adjudication、paper 写作或任务工程能力，并记录可反哺 workflow 的洞见。
status: seed
---

# Workflow Research Orchestrator

## 最小执行协议

1. 识别当前对象是“学术项目”还是“单篇 paper / 单个 TASK / 单份数据 / 单篇文献”。
2. 若是学术项目，先识别 route portfolio，而不是给项目强行分配线性阶段：
   - 当前 active / queued / diagnostic / archived routes；
   - 每条 route 的 question / literature / data / design / evidence / threat / contribution；
   - R0--R7 中本轮需要诊断的工作面。
3. 判断应调用的底层能力：
   - `workflow-paper`；
   - `workflow-argument-validity`；
   - `scholar-kit-*`；
   - `workflow-task-driven-project` / `task-driven-project-manager`；
   - 数据、实验、写作或格式类专用 skill。
4. 若已有 anchors、negative evidence 和多条竞争解释，路由到 `research-brainstorm` 与 `references/evidence-gated-route-adjudication.md`；先做 Chair Gate，再由 `task-driven-project-manager` 承接 promoted TASK。
5. 输出本次任务的产物边界：
   - 项目内产物；
   - paper 产物；
   - TASK 证据；
   - workflow 反哺候选。
6. 若出现可迁移洞见，先写入 `logs/` 或项目 case，不直接提升为稳定 reference。

## 当前 Green 标准

seed 阶段只要求：

```text
能说清当前 route portfolio 与本轮诊断面板；
能避免把 task-driven 架构误当顶层研究逻辑；
能在多路线竞争时选择 high-information Gate，而不是顺序追加规格；
能把个案证据和 workflow 规则分开。
```
