# Data-Side Request Email Template

> 用途：研究侧把文献启发的变量、机制、识别需求转成数据侧可执行请求。建议配合 `miy-mail` 使用，正文放在 `## Sendable Body` 下。

## Sendable Body

主题：<项目 / route> 外部数据 inventory 与取数需求确认

你好，

我这边基于当前文献阅读和核心数据盘点，整理了一版数据需求。目标不是一次性扩大所有数据，而是先确认哪些表/字段能够支撑当前研究设计。

## 1. 研究侧背景

```text
project:
candidate route / claim:
reference papers:
core data already available:
current design question:
```

## 2. 文献启发的数据需求

| 研究构念 | 文献启发 | 需要的数据字段/表 | 粒度 | 优先级 |
|---|---|---|---|---|
| <construct> | <paper / mechanism> | <field/table> | <unit> | required / optional / deferred |

## 3. P0 Required

请优先确认这些表/字段是否可得，并尽量交付 raw/source provenance、字段说明、样本覆盖和 QC：

```text
<table 1>
<table 2>
```

## 4. P1 Priority / Optional

这些表用于机制、异质性或 robustness。建议先做 inventory、字段字典或 bounded sample，不急着 full-download：

```text
<table 1>
<table 2>
```

## 5. Deferred

这一轮暂不需要：

```text
<large table / full text / low-priority data>
```

## 6. 希望交付

```text
outputs/<inventory_or_qc>.md
outputs/<field_dictionary>.md 或 .csv
outputs/<code_dictionary>.csv, if applicable
data/interim/<sample>.csv, if sample stage
docs/download-ledger.md 更新, if download occurs
```

## 7. 研究侧 review 标准

我这边会重点 review：

```text
1. 字段是否能支撑 required variables；
2. 代码口径是否清楚；
3. 粒度是否能与核心数据 merge；
4. 覆盖是否足够；
5. 是否需要 scope-lock 到 processed analytical table。
```

谢谢！

## Context Notes

- 本邮件由研究侧发起，用于把文献与研究设计需求转成数据侧可执行任务。
- 不要求数据侧替研究侧决定理论贡献或最终模型。
- 不要求本轮一次性下载所有 optional/deferred 数据。
