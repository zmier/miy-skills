---
name: workflow-tao-orchestrator
description: 编排复杂领域 workflow 的创建、抽父、迁移和回收。用于判断一个能力应做成 Skill 还是 workflow，设计总编排/子 Skills/TASK 模板/证据台账/provenance/迁移评测，并把课程案例、真实项目、技术 Radar、成熟 workflow 抽父和正向构造/逆向审计实践反哺到领域 workflow。
---

# Workflow Tao Orchestrator

当前状态：`seed / not-installed`

## 目标

帮助把复杂实践领域从零散经验或单个 Skill，推进为可执行、可验证、可迁移的 workflow 工程。

## 启动流程

1. 判断当前对象是：
   - 新领域 workflow；
   - 成熟 workflow 抽父；
   - 课程/案例反哺；
   - 真实项目反哺；
   - 技术 Radar 反哺；
   - 正向构造 / 逆向审计共享质量系统。
2. 判断单个 Skill 是否足够；若不够，建立 workflow 工程容器。
3. 读取 `../../references/workflow-conception-log-policy.md`，在目标 workflow 的 `logs/` 下记录构思过程、关键原文、方案分歧和迁移边界。
4. 区分个案证据与通用能力，个案留在 project / TASK。
5. 读取 `../../references/workflow-skill-shape.md`，设计总编排 Skill、子 Skills、subworkflows、references、templates/assets、logs、tests、provenance 和 migration status。
6. 读取 `../../references/regression-test-protocol.md`，至少用一个实践样本回归，避免空抽象；若是 Skill 修改触发回归，先写 run 级 README / `task-contract.md`，再优先开纯净 subAgent 执行，并将产物与 baseline / target md 做质量对比。父 Skill 改动时，至少选择能代表主要分歧的子分支 smoke cases，并显式检查跨分支污染。
7. 只有通过迁移或 forward-test 后，才把经验升级为稳定 workflow 规则。

## 决策纪律

- 不把单次成功直接写成通用规则。
- 不让父 workflow 吞掉子 workflow 的平台或领域细节。
- workflow 的可调用载体就是 Skill；根目录必须有 `SKILL.md`，但正文要写清它是复合 workflow 型 Skill，不是单一原子 Skill。
- 不把 project 证据搬进 workflow 能力层。
- 不把 workflow 构思过程藏在最终规则里；重大创建或升级先写入目标 workflow 的 `logs/YYYY-MM-DD-主题.md`，再提升稳定规则。
- 不急着重构旧 Skill；先建立 provenance 和迁移计划。
- 回归测试本身也可以反哺 workflow；但只能提升可迁移的测试规则，不把单次测试样本答案写进通用能力层。
