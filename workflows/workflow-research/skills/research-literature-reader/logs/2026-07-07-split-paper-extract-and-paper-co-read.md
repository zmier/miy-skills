# 拆分 paper-extract 与 paper-co-read

## 背景

此前 `paper-reading` 将阅读模式写成：

```text
collaborative-reading vs automatic-summary
```

这容易导致误解：共同读似乎可以绕过自动抽，直接从零开始聊天；自动摘要似乎只是另一个平行模式。

本次基于 `Does Media Coverage of Stocks Affect Mutual Funds' Trading and Performance` 的协同阅读经验，确认更合理的结构是：

```text
paper-extract
  -> paper-co-read / automatic file output
```

## 新增 Skill

### paper-extract

路径：

```text
skills/paper-reading/skills/paper-extract/SKILL.md
```

职责：

```text
结构化自动抽取；
生成 automatic-extraction.md；
覆盖 A01-A08；
保留 proposition IDs、source anchors、reading status、不可引用边界和剩余风险；
作为共同读、自动文件输出、task-specific extraction、route map 的上游输入。
```

模板：

```text
skills/paper-reading/skills/paper-extract/templates/automatic-extraction-template.md
```

### paper-co-read

路径：

```text
skills/paper-reading/skills/paper-co-read/SKILL.md
```

职责：

```text
读取 automatic-extraction.md；
生成低假设 Paper Orientation Card；
创建 / 更新 discussion-outline.md；
维护 Discussion Agenda、Ledger、用户问题、当前共识、pending 项和提纲外问题；
必要时标记 automatic extraction revision needed。
```

模板：

```text
skills/paper-reading/skills/paper-co-read/templates/discussion-outline-template.md
```

## 父级编排调整

`paper-reading/SKILL.md` 已从 mode-router 调整为 pipeline-router：

```text
PDF / Markdown substrate
  -> paper-extract
     automatic-extraction.md
  -> paper-co-read 或 automatic file output
     discussion-outline.md / task-specific extraction / route map / writing patterns
```

`research-literature-reader/SKILL.md` 同步更新：

```text
用户共同读：
  paper-extract -> paper-co-read

用户自动文件输出：
  paper-extract -> automatic file output

用户要服务 task / route：
  先 paper-extract，再按用户意图进入 co-read 或资产沉淀。
```

## Legacy 保留

旧入口暂不删除：

```text
skills/paper-reading/skills/collaborative-reading/SKILL.md
skills/paper-reading/skills/automatic-summary/SKILL.md
```

原因：

```text
collaborative-reading 内含大量 A01-A08 规则，是本次拆分来源和回归参照；
automatic-summary 是早期文件优先自动提取入口，后续可验证是否并入 paper-extract；
直接删除会影响既有调用和 UAT 对比。
```

后续验证通过后，再决定：

```text
collaborative-reading -> 退役 / alias 到 paper-co-read；
automatic-summary -> 退役 / alias 到 paper-extract / 保留为 automatic file output 薄封装。
```

## 关键认知

```text
paper-extract 是认知引擎；
paper-co-read 是交互推进层。
```

共同读不是不抽，而是基于抽取产物进行可追问、可纠偏、可深化的协同阅读。

