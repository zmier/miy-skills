---
name: workflow-paper
description: 论文研究总父 workflow 型 Skill。用于把学论文、写论文、审稿/自审、返修和格式交付放在同一论文工作系统中路由；组合 workflow-argument-validity、scholar-kit、workflow-md-to-word-formatting、workflow-task-driven-project 等底层引擎，但不复制它们。当前为最小路由版。
---

# Paper Workflow

状态：`seed / minimal-router`

## 目标

把论文相关工作放在同一个父 workflow 下路由：

```text
学论文 = 拆别人怎么搭论文
写论文 = 自己搭一篇论文
审稿 / 自审 = 检查论文搭得稳不稳
返修 = 根据反馈重搭或补强论文
格式交付 = 把论文整理成目标期刊/学校/项目要求的形态
```

本 workflow 当前只做最小父层路由，不提前展开复杂主轴。

## 设计原则

`workflow-paper` 组合通用引擎，而不继承或收编通用引擎。

```text
PaperWorkflow has an ArgumentEngine
而不是
PaperWorkflow extends ArgumentEngine
```

因此：

- `workflow-argument-validity` 是底层论证引擎，负责抽树、验箭头、修复映射和选问题；
- `scholar-kit-*` 是检索与文献工具能力；
- `workflow-md-to-word-formatting` 是格式交付能力；
- `workflow-task-driven-project` / `task-driven-project-manager` 是项目与 TASK 管理能力；
- 本 workflow 只负责论文领域的上层路由和边界。

## 最小路由

当用户提出论文相关请求时，先判断属于哪一路：

| 用户意图 | 路由 | 当前动作 |
|---|---|---|
| 学某篇论文、学一批基础文献、拆模板文献 | `subworkflows/workflow-paper-learning` | 进入学论文子 workflow |
| 写论文、搭选题、写引言、理论机制、方法或结果叙事 | `workflow-paper-writing` | 暂未创建；先记录需求并可组合 `workflow-argument-validity` 与已有写作 Skill |
| 审稿、投稿前自审、检查贡献链是否成立 | `workflow-paper-review` | 暂未创建；现阶段可组合 `workflow-argument-validity` 与既有 `workflow-paper-writing-review` |
| 返修、回复审稿人、整合导师批注 | `workflow-paper-revision` | 暂未创建；先组合现有修订类 Skill |
| Word / 期刊 / 学位论文格式 | `workflow-md-to-word-formatting` | 直接路由到格式 workflow |

## 与既有 workflow 的关系

本父 workflow 不替代既有能力：

- 旧 `workflow-paper-writing-review` 保留为论文审稿/写作审查相关能力库；
- 新 `workflow-paper` 先作为更高层父入口，后续再决定是否迁移、挂接或重命名旧能力；
- `workflow-argument-validity` 保持跨领域通用，不移动到本目录下。

## 子 Workflows

| Subworkflow | 职责 | 状态 |
|---|---|---|
| `subworkflows/workflow-paper-learning` | 学论文：从单篇或一组文献中提取研究问题、gap、机制、方法、证据、写法和可迁移模板 | `seed` |

## 输出契约

最小输出只需说明：

```text
本次属于哪一路；
需要组合哪些底层引擎；
预期产物是什么；
哪些内容暂时只记录为待设计，不展开。
```

## 构思日志

- `logs/2026-06-25-minimal-paper-workflow.md`

