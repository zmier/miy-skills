---
name: automatic-summary
description: paper-reading 的自动文献摘要和自动提取模式。用于用户明确要求 Agent 自动读完一篇或一组论文并生成结构化摘要、实验设计提取、变量/机制/识别梳理、route mapping、writing patterns 或批量文献整理的场景；以文件产物和可复盘记录为优先，但必须标明阅读底稿状态、范围、不可引用边界和剩余风险。
---

# Automatic Summary

状态：`seed / file-first`

## 定位

本 Skill 用于“自动文献摘要 / 自动提取”。用户希望 Agent 自主读取材料并产出结构化文件，而不是先进行对话式讲解。

## 输入检查

开始前确认：

- 本轮目标是 summary、design extraction、route mapping、writing patterns，还是批量整理；
- Markdown substrate 是否通过 `research-literature-reader` 的接收验收；
- 若是 empirical / table-heavy paper，是否存在 table-leak、pending visual QC 或 degraded 状态；
- 输出应写入哪个 paper folder / task folder。

## 输出类型

根据用户目标选择最小充分输出：

```text
orientation summary；
claim-warrant map；
TASKxx-design-extraction.md；
route-map.md；
writing-patterns.md；
literature matrix；
reading-log.md。
```

若用户没有指定，优先输出结构化摘要，不默认写满所有资产。

## Claim-Warrant Map

自动摘要不能只按文献综述、理论、变量、识别、结果、稳健性做模块摘要。至少应保留一版简短的 `claim-warrant map`：

```text
core claim:
logical form:
proposition branches:
for each branch:
  abstract object:
  observable proxy:
  warrant:
  evidence:
  competing explanations:
  remaining uncertainty:
```

若核心发现是复合命题，先拆命题支；若某个命题支是 `Bx -> By`，分别处理 `Bx` 和 `By` 的 proxy / warrant / evidence。不得把整篇论文偷换成单组 X/Y。

## 必填说明

每个自动产物必须写明：

```text
source PDF / Markdown；
reading status；
是否完整视觉核验；
本轮阅读范围；
不可引用边界；
剩余风险；
下一步建议。
```

## 完成标准

- 用户要求的摘要 / extraction 已生成。
- 文件路径和产物范围清楚。
- 不把 rough draft 伪装成 restored manuscript。
- 不在 table-leak high risk 状态下引用表格系数、样本量、R2 或显著性。
- 若自动处理过程中发现用户其实需要对话解释，应切换到 collaborative-reading。

## 禁止事项

- 不在用户要求协同阅读时使用本模式。
- 不把批量自动摘要写成不可追溯的总文件。
- 不省略底稿状态和剩余风险。
- 不把自动摘要结论直接提升为 project-level 稳定判断。
