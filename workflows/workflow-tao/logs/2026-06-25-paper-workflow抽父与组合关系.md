# 2026-06-25 paper workflow 抽父与组合关系

## 触发问题

在准备启动一个新的科研项目时，用户提出：学文献、审稿、写论文三件事高度相关，很多 Skill 是相通的。是否应在三者上方再抽一个父 workflow，例如 `workflow-paper`，下面承载：

- 文献学习 workflow；
- 论文写作 workflow；
- 论文审稿 / 自审 workflow；
- 并复用 `workflow-argument-validity`。

同时用户指出：`workflow-paper-learning` 不应只针对 strong paper；strong paper learning 应只是其下的一个子 Skill 或子路线。

## 核心判断

这个判断成立：论文相关工作已经具备抽父信号。

原因是：

```text
学文献、审稿、写论文看似是三个任务，
但底层都在处理同一个东西：论文作为一套论证工程。
```

三者关系可以概括为：

```text
学文献 = 拆别人怎么搭论文
审稿 = 检查别人搭得稳不稳
写论文 = 自己搭一篇出来
```

因此，上层可以有一个 `workflow-paper` 作为论文研究总父 workflow，统一组织论文学习、写作、审稿、自审、返修、格式和项目管理等能力。

## 组合优于继承

关键设计点是：`workflow-paper` 不应“继承”或“收编” `workflow-argument-validity`，而应“组合”它。

用面向对象类比：

```text
workflow-argument-validity = ArgumentEngine
workflow-paper = PaperWorkflow

PaperWorkflow has an ArgumentEngine
而不是
PaperWorkflow extends ArgumentEngine
```

中文表述：

```text
论文工作流不是论证工作流的子类；
论文工作流把论证工作流作为底层引擎组合进来。
```

原因是 `workflow-argument-validity` 的边界更通用，它不仅服务论文，还服务：

- 论效题；
- GRE Analyze an Argument；
- 学术审稿；
- 论文写作自审；
- 政策论证；
- 商业报告；
- 普通论证分析。

如果把它物理放进 `workflow-paper`，会污染它的通用性，也会让其他领域调用时背上论文场景的规则。

## 推荐结构

更稳的结构是：

```text
workflow-paper/
├── SKILL.md
├── references/
│   ├── paper-workflow-map.md
│   ├── paper-quality-ladder.md
│   └── shared-engine-links.md
├── subworkflows/
│   ├── workflow-paper-learning/
│   ├── workflow-paper-writing/
│   ├── workflow-paper-review/
│   └── workflow-paper-revision/
└── logs/
```

其中：

```text
workflow-paper
├── 组合 workflow-argument-validity
├── 组合 scholar-kit / literature-search
├── 组合 workflow-md-to-word-formatting
├── 组合 workflow-task-driven-project
├── 组合 course-driven-skill-engineering
└── 内部子 workflow:
    ├── workflow-paper-learning
    ├── workflow-paper-writing
    ├── workflow-paper-review
    └── workflow-paper-revision
```

## paper-learning 的边界

`workflow-paper-learning` 不应等同于 strong paper learning。

它应是“学文献”的父 workflow，下面再分多种学习路线：

```text
workflow-paper-learning/
├── SKILL.md
├── skills/
│   ├── strong-paper-template-learning
│   ├── field-foundation-literature-learning
│   ├── method-paper-learning
│   ├── theory-paper-learning
│   ├── data-and-measurement-paper-learning
│   └── target-journal-style-learning
```

其中 strong paper learning 的目标是：

```text
拆一篇强参考文献如何提出问题、构造 gap、搭机制、设计方法、组织结果和写贡献，
并把这些拆解结果转成可迁移写作模板。
```

但普通 field foundation literature learning 的目标可能是：

```text
建立领域地图、概念谱系、方法谱系、关键争议和经典问题。
```

二者不应混同。

## 可提升规则

本次讨论可先沉淀为构思日志，后续若创建 `workflow-paper`，可提升为稳定规则：

```text
领域 workflow 应组合跨领域底层引擎，而不是把底层引擎收编为子 workflow。
```

以及：

```text
正向构造、逆向审计与模板学习共享质量标准时，应考虑抽父；
但共享引擎应保持通用边界，通过组合方式被多个领域 workflow 调用。
```

## 迁移边界

这条规则不只适用于论文工作流，也适用于其他复杂实践领域。例如：

- Android 逆向 workflow 可以组合通用项目管理、日志、测试和证据台账能力；
- 学术审稿 workflow 可以组合论证有效性、文献检索、PDF 还原和 Word 输出能力；
- 写作 workflow 可以组合论证引擎、文献学习、期刊样式和修订整合能力。

判断标准是：

```text
如果某能力跨多个领域复用，就保持为 shared engine；
如果某能力只服务某一领域的具体路线，就放入该领域 workflow 的 subworkflow 或 skills/。
```

