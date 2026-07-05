---
name: workflow-research-orchestrator
description: workflow-research 的总编排子 Skill。用于判断学术项目当前阶段，路由到文献、论证、数据可得性、研究设计、paper 写作或任务工程能力，并记录可反哺 workflow 的洞见。
status: seed
---

# Workflow Research Orchestrator

## 最小执行协议

1. 识别当前对象是“学术项目”还是“单篇 paper / 单个 TASK / 单份数据 / 单篇文献”。
2. 若是学术项目，先建立阶段判断：
   - R0 项目界定；
   - R1 研究问题；
   - R2 文献定位；
   - R3 数据可得性；
   - R4 研究设计；
   - R5 论证链；
   - R6 paper 化；
   - R7 交付与反哺。
3. 判断应调用的底层能力：
   - `workflow-paper`；
   - `workflow-argument-validity`；
   - `scholar-kit-*`；
   - `workflow-task-driven-project` / `task-driven-project-manager`；
   - 数据、实验、写作或格式类专用 skill。
4. 输出本次任务的产物边界：
   - 项目内产物；
   - paper 产物；
   - TASK 证据；
   - workflow 反哺候选。
5. 若出现可迁移洞见，先写入 `logs/` 或项目 case，不直接提升为稳定 reference。

## 当前 Green 标准

seed 阶段只要求：

```text
能说清当前项目阶段；
能避免把 task-driven 架构误当顶层研究逻辑；
能把个案证据和 workflow 规则分开。
```

