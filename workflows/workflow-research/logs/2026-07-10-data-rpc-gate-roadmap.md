---
date: 2026-07-10
type: dialogue-insight
status: structural-green / forward-test-pending
source_case: CASE-260521 基金经理研究
affected:
  - /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/roadmap/SKILL.md
  - /Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-roadmap/SKILL.md
---

# Data RPC Gate Roadmap 规则抽象

## 来源场景

CASE-260521 的 TASK07 已形成一个机制探索路线：

```text
matched diagnostic 后，回答与 q+1 buy / redeem 两端更活跃相关，net flow 弱；
但季度数据无法拆开 recency / carryover 与 persistent pressure / attention episode。
```

下一步需要 CSMAR/RESSET 数据同学确认是否存在更细事件时间数据、基金事件日期、文本披露、新闻/关注代理等。用户指出：这不像普通内部任务，而像一次 RPC 调用；研究侧有入参，数据同学返回出参；在 roadmap 上应画出数据同学，并通过 mail 表达请求和回复。

## 原始问题形状

关键问题不是“要不要把邮件放进路线图”，而是：

```text
当研究路线依赖外部协作者查询数据时，
这个外部 actor、mail thread、Data Gate 和后续研究分支之间应该如何在 roadmap 中表达？
```

用户进一步提出：

```text
数据同学应在 Data Gate 正上方，和 Data Gate 之间有双箭头；
箭头旁边写入参和出参；
最好体现 mail；
数据同学节点应有独特视觉信息。
```

## 共同发现

本次讨论形成以下区分：

```text
Data Gate = 研究侧 decision gate；
数据同学 / provider = 外部 actor，不属于内部 task tree；
mail = request / reply 的可追溯 artifact；
入参 = 字段需求、频率、合并键、优先级、用途；
出参 = 表名、字段字典、样例、覆盖范围、限制、整理成本。
```

因此 roadmap 不应只画：

```text
Matched diagnostic -> Data Gate
```

而应在 TASK / Route 层画成：

```text
research decision gate
  <-> external data provider
  <-> mail thread
  -> yes / partial / no research routes
```

## 结构决定

本轮升级分两层：

1. 通用 `$roadmap`：
   - 增加 `external` class；
   - 增加 `mail` class；
   - 增加 `External Actor / Mail RPC Pattern`；
   - 规定外部 actor、mail artifact、decision gate 的视觉和语义边界。

2. `$research-roadmap`：
   - 增加 `Data RPC Gate` 研究专用模式；
   - 将 CASE-260521 中 CSMAR/RESSET 数据同学的邮件确认抽象为可迁移画法；
   - 规定 Project 级可压缩，TASK / Route 级可展开 actor + mail + gate。

## 提升到 Skill 的规则

已提升：

- 外部 actor 使用 `external` class，常配方角节点；
- mail / issue / ticket 使用 `mail` class；
- 入参和出参优先写在双向箭头标签上；
- mail request / reply 可作为可点击 artifact，链接到 `$miy-mail` 生成的 `EMAIL-*.md` / `REPLY-*.md`；整组往来可链接到 `emails/README.md` 或稳定 thread index；
- 外部数据请求只有在会改变路线决策时才进入 roadmap；
- 发出邮件不是数据证据，不能误写成 data available。

## 保留在 case 的内容

以下内容只保留在 CASE-260521 的 TASK / email / data memo 中，不进入通用 Skill：

- 具体 CSMAR/RESSET 表名和字段名；
- 基金经理研究的样本数、回归结果和估计值；
- 具体邮件全文；
- 平台内部字段和合并键的个案口径。

## 迁移状态

当前状态为：

```text
structural-green / forward-test-pending
```

它已在 CASE-260521 中形成清晰需求并落入 Skill 结构，但尚未在另一个研究项目中验证。

后续 forward-test 观察点：

- 另一个研究项目是否也会出现外部数据 provider / reviewer / domain expert；
- `external + mail + gate` 是否能减少 roadmap 上“等待外部输入”和“内部研究决策”的混淆；
- click 到 correspondence thread 是否能让协作者快速恢复上下文。
