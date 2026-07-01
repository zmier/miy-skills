---
date: 2026-06-19
type: reference-index
status: structural-green
scope:
  - workflow-tao
---

# 参考 Workflow 样本索引

本文件只做链接索引，不复制案例内容。需要创建、重构或抽父 workflow 型 Skill 时，可按场景读取对应样本。

## 成熟样本

| 样本 | 路径 | 可借鉴点 |
|---|---|---|
| 逆向工程父 workflow | `../workflow-reverse-engineering/` | 父层抽象、平台路由、红灯分类、证据台账、Mermaid evidence tree、subworkflows、forward-test |
| Android 逆向子 workflow | `../workflow-reverse-engineering/subworkflows/workflow-android-reverse/` | 平台子 workflow 如何承载大量子 Skills、references、scripts、tests 和工具链 |
| JS 逆向子 workflow | `../workflow-reverse-engineering/subworkflows/workflow-js-reverse/` | 新平台子 workflow 如何从最小流程、request construction ledger 和待验证分支开始 |

## 发展中样本

| 样本 | 路径 | 可借鉴点 |
|---|---|---|
| 论文写作 / 审稿 workflow | `../workflow-paper-writing-review/` | 正向构造与逆向验收共享质量系统；审稿 TASK 如何反哺 workflow |
| 论证有效性 / 论证树 workflow | `../workflow-argument-validity/` | 对话洞见、课程方法、论证树、Mermaid/Obsidian、父子 workflow 设计 |
| 任务驱动项目 workflow | `../workflow-task-driven-project/` | 从项目脚手架升级到 TASK 树、证据台账、ReAct 日志、阶段复盘、Obsidian 双链和 workflow/skill 反哺 |

## 外部项目样本

| 样本 | 路径 | 可借鉴点 |
|---|---|---|
| 元 Workflow 工程项目 | `/Users/narra/Documents/alib/Writer/00 信息/知识管理/PROJECT-260618-元Workflow工程/` | workflow 抽象过程、TASK 分层、设计原则沉淀、实践样本回填 |

## 使用规则

- 只在需要样本结构时读取，不把样本内容复制进 `workflow-tao`。
- 先看 `workflow-skill-shape.md`，再按需读取具体样本。
- 参考样本只能提供结构启发，不能直接证明新 workflow 已通过迁移。
- 若从样本中抽出通用规则，必须记录来源和迁移状态。
