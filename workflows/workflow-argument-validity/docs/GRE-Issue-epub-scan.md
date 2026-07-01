---
date: 2026-06-19
type: material-scan
status: scanned
scope:
  - workflow-argument-validity
source:
  - GRE Analytical Writing Supreme Solutions to the Real Essay Topics, Vibrant Publishers, 2023, EPUB
---

# GRE Issue EPUB 扫描记录

## 结论

这份 EPUB 可以打开。当前 `Writer/.venv` 中没有 `ebooklib`，但 EPUB 本质是 zip 包，已用 Python 标准库 `zipfile` 加 `bs4/lxml/markdownify` 完成结构探查。

它的主体不是 GRE `Analyze an Argument`，而是 GRE `Analyze an Issue`。因此它与管综论效题不是一一对应的“拆别人论证”材料，而是更适合补强本 workflow 中的正向论证构造、反方压力测试、隐含假设识别和写作输出层。

## 文件结构

- EPUB 内部约 107 个文件。
- 其中约 95 个 HTML/XHTML 章节。
- 目录显示主体包含 72 个 Issue Task。
- 章节常见结构包括：
  - `Strategies`
  - `Restate the Issue`
  - `In other words`
  - `Assumptions`
  - `Pros / Cons`
  - `Opposing viewpoint`
  - `Alternative viewpoint`
  - `Sample Essay`

## 与本 workflow 的关系

本 workflow 当前主轴是：

```text
恢复论证树 -> 检查支撑箭头 -> 标注断点影响 -> 输出可读文本
```

GRE Issue 材料更偏向：

```text
给定命题 -> 解释概念 -> 找隐含假设 -> 组织正反观点 -> 搭建自己的论证树 -> 写成文章
```

两者的共同底层仍然是“论证树”和“箭头”：

- 论效题：主要是拆作者已经搭好的箭头。
- GRE Issue：主要是自己搭箭头，同时预先检查反方可能攻击的箭头。
- 学术论文写作自审：同时需要搭箭头和验箭头。
- 学术审稿：主要是拆作者的发表正当性论证和内层发现论证。

## 可迁移能力

### 1. 正向搭箭头

当前父 workflow 对“拆箭头”较强，对“搭箭头”的显式步骤还不够。GRE Issue 的结构可以补一个正向构造流程：

```text
命题重述 -> 概念解释 -> 立场选择 -> 支撑理由 -> 例证 -> 反方观点 -> 条件限制 -> 结论
```

这可以服务于：

- 论文写作自审；
- 政策/商业报告写作；
- 论说文；
- 审稿意见中“为什么这个问题重要”的说明。

### 2. 隐含假设显性化

GRE Issue 高频要求先找 claim 中的 assumptions。这可以补强父 workflow 中的 `hidden premise` 处理：

```text
作者明说了什么
-> 他必须默认什么才说得通
-> 这些默认前提是否合理、是否需要条件化
```

在学术论文里对应：

- 指标能代表构念；
- 样本能代表目标总体；
- 机制解释排除了关键替代解释；
- 结果能支持理论命题。

### 3. 反方压力测试

GRE Issue 每题常见 `opposing viewpoint`、`alternative viewpoint` 和 `pros/cons`。这可以迁移为：

```text
每个主张至少问一次：
反方最强反驳是什么？
是否有替代解释？
是否有成立边界？
```

这对审稿尤其有价值，因为审稿意见常常不是证明作者一定错，而是证明作者目前没有排除足够强的替代解释。

### 4. 概念解释先行

Issue 任务经常先把题干换句话说，再解释关键词。它能加强我们刚沉淀的“概念关系审查”：

```text
先解释概念
再判断概念之间是同一、包含、交叉、并列、无关、手段目的还是因果关系
最后再验箭头
```

### 5. 输出层分化

GRE Issue 的 sample essay 对父 workflow 的 `output-ladder` 有启发：同一棵论证树可以有不同输出形态。

- 论效题：断点分析文章。
- GRE Issue / 论说文：立场文章。
- 学术审稿：审稿问题和修改建议。
- 论文写作自审：结构改写建议。

## 建议接入方式

### 短期

不把 EPUB 正文导入 Skill 主流程，只保留本扫描记录，并在 `source-provenance.md` 标记为可迁移参考材料。

### 中期

在父 workflow 增加一个“正向论证构造 / claim-building”分支，用于：

- 写论文；
- 写论说文；
- 写政策或商业判断；
- 审稿意见的论证组织。

### 长期

可新建子 workflow：

```text
subworkflows/workflow-gre-issue-writing
```

或更通用地命名为：

```text
subworkflows/workflow-claim-construction
```

它与 `workflow-exam-argument-validity` 的关系是：

```text
workflow-exam-argument-validity：拆错题中的论证树
workflow-claim-construction：搭自己的论证树并预先验箭头
```

## 版权与使用边界

- 不在 Skill 主流程中复制 EPUB 正文或 sample essay。
- 只抽象可迁移方法、章节结构和训练用途。
- 若后续做案例训练，应只保留任务编号、题型结构、自己的分析输出和必要的短引用。

