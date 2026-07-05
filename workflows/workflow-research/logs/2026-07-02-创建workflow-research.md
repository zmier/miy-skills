---
date: 2026-07-02
status: raw-insight / structural-draft
source_project: /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究
---

# 创建 workflow-research

## 来源

本日志来自“基金经理请回答”学术项目整理对话。

用户指出：此前尝试用 `task-driven-project-manager` 管理该项目，但学术项目不能在顶层硬套 task-driven workflow。`workflow-paper` 又主要面向 paper 的学习、写作、审稿、返修和格式交付，不完全覆盖一个学术项目从模糊 idea 到数据、实验、文献、论证和多篇 paper 路线的完整过程。

## 原始困惑摘要

学术项目包含写 paper，也包含论证、实验、文献、数据可得性和项目路线取舍。`workflow-paper` 包含其中一些动作，但作用对象更接近“论文”；`task-driven-project-manager` 可以组织任务和证据，但它是执行层，不应成为研究项目顶层逻辑。

## 当前结构决定

建立 `workflow-research` 作为学术研究项目总父 workflow：

```text
workflow-research
  -> workflow-paper
  -> workflow-argument-validity
  -> scholar-kit
  -> workflow-task-driven-project / task-driven-project-manager
```

## 当前提升到结构层的规则

- 研究问题和证据链坐在驾驶座；TASK 和目录结构坐在副驾驶。
- 学术项目 workflow 管 paper 之前和 paper 之间的路线治理。
- 单篇 paper workflow 是 research workflow 的子能力，不是替代品。
- task-driven project manager 是执行层脚手架，不是学术项目 ontology。
- 学术项目顶层应表达研究主轴；`data/`、`common/`、`tasks/`、`experiments/`、`logs/`、`outputs/` 等执行层目录可收束到 `workspace/` 或 `research-workspace/`。

## 2026-07-05 补充：顶层清爽原则

来自 `CASE-260521-基金经理研究` 的目录整理讨论。用户指出 `common/`、`data/` 等目录不应长期位于学术项目顶层，顶层应该清爽。

该判断已先写入项目个案：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/docs/PROJECT-CLEANUP-AUDIT.md
```

并提升为 draft reference：

```text
references/project-structure.md
```

迁移状态：`draft-rule`。后续需要在至少一个真实学术项目中完成路径迁移与 README 改写后，再提升到 `structural-green`。

## 必须留在项目个案中的内容

- 支付宝基金经理问答数据可得性；
- 模拟器/Appium 失败路线；
- mPaaS/Reqable 观察；
- 当前文献和课程材料混杂造成的目录治理问题；
- 未来数据下载后的真实字段、样本、匹配与研究设计。

## 后续 forward-test 观察点

- `260521-基金经理研究` 是否能用 R0-R7 主轴重建项目地图；
- 是否能把技术支线降级为数据可得性证据，而不是顶层主线；
- 是否能从该项目沉淀出学术项目目录模板；
- 是否需要独立 `subworkflows/workflow-research-data-availability`。
