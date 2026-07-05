---
name: research-literature-reader
description: workflow-research 的研究项目文献阅读编排子 Skill。用于在学术研究项目中，围绕当前 task、candidate research route、实验设计、变量构造、识别策略、数据需求、机制、稳健性、写作范式或期刊定位读取一篇或一组文献；把 PDF、Markdown、coauthor 备注和项目数据约束转化为可复用研究资产。需要按论文建立 raw PDF、restored Markdown、task-specific extraction、route mapping、writing patterns 和 reading logs，并可编排 scholar-pdf-markdown-restoration、workflow-paper-learning、workflow-argument-validity、scholar-kit 与 task-driven-project-manager。
---

# Research Literature Reader

状态：`seed / forward-test-with-CASE-260521`

## 定位

本 Skill 是 `workflow-research` 的文献阅读编排层，不是 PDF 转 Markdown 工具，也不是通用 literature review 生成器。

它回答：

```text
在一个探索性研究项目中，如何带着当前 task / candidate route 去读文献，并把文献转化为后续可复用的研究资产？
```

核心原则：

```text
当前 task / route 决定读什么；
文献资产沉淀决定以后能否复用；
PDF 还原、论文学习、论证审计和 task 管理由相邻 Skill 承接。
```

## 输入

优先定位：

- project README、docs、logs 和 tasks；
- 当前 task 说明、task log、coauthor 备注、候选 routes；
- 原始 PDF 或 PDF 目录；
- 已有 Markdown / restored Markdown / extraction logs；
- 主数据链接、字段说明、数据缺口和合规边界。

若用户只给出 PDF 目录，先列出论文清单，并判断哪些文献和当前 task / route 关系最直接。

## 文献资产结构

一篇文献建议对应一个文件夹。若项目已有目录结构，优先兼容现状；若需要新建，使用下列形状：

```text
<paper-slug>/
├── 0-raw/
│   └── <title>.pdf
├── 1-md/
│   ├── manuscript_raw.md
│   ├── manuscript_restored.md
│   └── sections/
├── 2-task-readings/
│   └── TASK01-design-extraction.md
├── 3-route-mapping/
│   └── route-map.md
├── 4-writing-patterns/
│   └── writing-patterns.md
└── logs/
    ├── restoration-qc.md
    └── reading-log.md
```

最小可接受结构：

```text
raw source；
restored reading substrate；
task-specific extraction；
route / claim mapping；
writing-pattern extraction；
logs / provenance。
```

不要把所有阅读笔记塞进一个总文件。要能回答：

```text
这篇文献的原文在哪里；
可信 Markdown 底稿在哪里；
本 task 当时从中提取了什么；
它支持或威胁哪条 candidate route；
后续写作时可复用哪些范式；
哪些判断仍未核验。
```

## 执行协议

1. 明确本轮阅读目的：
   - 设计实验；
   - 找变量 / 数据；
   - 学识别策略；
   - 学机制和异质性；
   - 找 robustness；
   - 学写作范式；
   - 判断 candidate route 是否值得推进。
2. 读取当前 project / task / route 材料，写出本轮文献阅读问题清单。
3. 定位 PDF 与已有 Markdown。若没有可信 Markdown，转入 `scholar-pdf-markdown-restoration`；执行前读取该 Skill，并按其 QC 规则产出 restored Markdown 或明确降级状态。
4. 建立或补全文献文件夹。不要移动用户已有文件，除非用户明确要求；可用索引或相对链接先把原始 PDF 纳入资产图。
5. 做 task-specific extraction。面向实验设计时，至少提取：
   - research question；
   - empirical setting / data；
   - treatment / exposure / event；
   - outcome variables；
   - key explanatory variables；
   - identification strategy；
   - controls / fixed effects；
   - mechanism and heterogeneity；
   - robustness / placebo；
   - contribution claim；
   - what maps to current project；
   - what does not transfer；
   - data needed beyond current project data；
   - threats and unresolved questions。
6. 做 route mapping：
   - 这篇文献支持哪条 candidate route；
   - 它提供的是主干设计、机制、变量、robustness、写作范式还是反例；
   - 它要求补充哪些数据；
   - 它暴露哪些识别威胁。
7. 若本轮目标包含写作，单独写 `4-writing-patterns/writing-patterns.md`。不要把写作范式混进实验设计提取里。
8. 更新 task log，记录本轮读文献的目的、输入、产物、未解决风险和下一步。
9. 将可能可迁移的流程洞见先写入 `workflow-research/logs` 或项目 log，不直接提升为稳定 reference。

## TASK01 设计提取模板

用于 `TASK01-coauthor-literature-to-design` 这类“从 coauthor 文献到第一版实验设计”的阅读：

```markdown
# <Paper Title> - TASK01 Design Extraction

## Source

- PDF:
- Markdown substrate:
- Restoration / reading status:
- Read date:
- Current task:
- Candidate route:

## Why This Paper Matters For This Task

## Core Design

- Research question:
- Setting and sample:
- Data:
- Treatment / exposure / event:
- Outcomes:
- Key variables:
- Identification:
- Controls / fixed effects:
- Mechanism:
- Heterogeneity:
- Robustness:

## Transfer To 基金经理请回答

- Directly reusable:
- Requires adaptation:
- Not transferable:
- Data we already have:
- Data we need:
- Measurement idea:
- Identification threat:

## Route Mapping

- Main route supported:
- Possible branch route:
- Could become:
- Current confidence:

## Open Questions
```

## 输出

一次完成的文献阅读应至少更新：

- 单篇文献文件夹中的 task-specific extraction；
- route mapping 或 task 输出文件；
- task log；
- 若有 PDF 转 Markdown，更新 restoration QC；
- 若有可迁移 workflow 洞见，更新 project log 或 `workflow-research/logs`。

## 完成标准

- 本轮阅读问题来自当前 task / route，而不是无目标摘抄。
- 原始文献、Markdown 底稿、阅读产物和日志可追溯。
- 明确说明哪些设计可迁移到当前项目，哪些不可迁移。
- 明确列出当前主数据已经满足什么、还缺什么数据。
- 明确记录识别威胁和下一步实验设计问题。
- 如果 Markdown 底稿未完成可靠还原，最终产物必须标为 reading draft / degraded，不得声称已完成精读。

## 禁止事项

- 不把 PDF 转 Markdown 当成文献阅读完成。
- 不把单篇文献读成泛泛摘要，而忽略当前 task / route。
- 不把 task-specific 阅读笔记当成永久稳定的 project-level 结论。
- 不在没有数据和识别检查时宣称某条 route 已经成立。
- 不把写作范式、实验设计、变量构造和引用信息混在同一个不可复盘文件里。
