---
date: 2026-06-19
type: course-driven-learning-project
status: completed
workflow: workflow-exam-argument-validity
---

# PROJECT-260619 论效案例学习

## 目标

把现有可用论效题语料逐题做成 TASK：每题经历 `prompt blind-run -> reference comparison -> skill feedback decision`，用案例持续检验和反哺 `workflow-exam-argument-validity`。

2026-06-19 扩展纳入 GRE Analyze an Argument 官方样本，作为英文官方校准案例。由于题目和 reader commentary 已被读取，新增 GRE TASK 只标记为 `prior-exposed / assisted`，不作为 strict blind 证据。

## 来源语料

- 主语料目录：`../CASE-UAT-260619-论效新题/inputs/final/`
- 可标准学习：`final-complete`
- 可容错学习：`final-with-ocr-caveats`
- 不做标准学习：`incomplete-source`
- GRE 官方扩展语料：`../../../../docs/GRE-Argument-original-chapters.extract.md`

## 学习纪律

1. 每个 TASK 先拆出 `inputs/prompt.md` 和 `inputs/reference.md`。
2. blind 阶段只读 `prompt.md` 与通用 workflow 规则。
3. 生成 `argument-tree.md`、`arrow-audit.md`、`essay-draft.md` 后，才解冻 `reference.md`。
4. 反哺必须先判断是否能上抽为稳定动作，避免碎片 checklist。
5. 已被读过答案的题只能标为 `prior-exposed` 或 `assisted`，不能伪装 strict blind。

## 案例池

| TASK | 年份 | 题目 | 质量 | 模式 | 状态 | 说明 |
|---|---:|---|---|---|---|---|
| `TASK01` | 2013 | 勤俭节约过时了 | `final-complete` | `completed-uat` | `done / forward-test-pass` | 已完成 CASE-UAT-260619；可作为 forward-test-green 证据。 |
| `TASK02` | 2009 | 民主集中制 | `final-complete` | `completed-feedback` | `done / feedback-applied` | 已完成 CASE-FEEDBACK-260619；反哺定义回代与二分关系检查。 |
| `TASK03` | 2004 | 企业竞争 | `final-complete` | `blind` | `done / no-change` | 既有类比、二分、概念关系规则覆盖。 |
| `TASK04` | 2005 | 洋快餐 | `final-complete` | `blind` | `done / feedback-applied` | 反哺外推维度审查。 |
| `TASK05` | 2008 | 孝不是选拔官员的标准 | `final-complete` | `blind` | `done / feedback-applied` | 反哺条件关系审查。 |
| `TASK06` | 2010 | 权威的影响 | `final-complete` | `prior-exposed` | `done / assisted-feedback-applied` | 反哺对比实验控制变量审查；不作为 strict blind 证据。 |
| `TASK07` | 2006 | 企业丑闻 | `final-with-ocr-caveats` | `limited-blind / ocr-caveat` | `done / reinforce` | 强化可见记录与真实发生率，归入外推维度。 |
| `TASK08` | 2007 | 终身制和铁饭碗 | `final-with-ocr-caveats` | `prior-exposed / ocr-caveat` | `done / reinforce` | 强化概念簇边界审查。 |
| `TASK09` | 2003 | 蜜蜂实验 | `final-with-ocr-caveats` | `prior-exposed / ocr-caveat` | `done / reinforce` | 强化偶然成功不能推出策略有效。 |
| `TASK10` | GRE | Corpora 健身、电脑使用与经济衰退 | `official-gre-argument` | `prior-exposed / assisted` | `done / assisted-uat-pass / feedback-applied` | 官方 Task 1；已完成 GRE Argument 分支 UAT，反哺假设影响链与问题型输出。 |
| `TASK11` | GRE | Kali 雕塑、模具发现与收藏价值预测 | `official-gre-argument` | `prior-exposed / assisted` | `done / assisted-uat-pass / feedback-applied` | 官方 Task 2；完成 GRE 问题型输出 UAT，反哺 question-impact chain、工具机制审查和预测机制审查。 |

## 数量判断

- 中文/MBA 可学习案例：9 篇，已完成 9 篇。
- GRE 官方扩展校准案例：2 篇，TASK10/TASK11 均已完成 assisted UAT。
- 项目内 TASK 合计：11 个。
- 待做：0 篇；后续可另找未参与提炼的新 GRE Argument 做 strict / limited blind forward-test。
- 标准 blind-run 已完成：2004、2005、2008。
- assisted / caveat 学习已完成：2010、2006、2007、2003。
- GRE assisted calibration：TASK10/TASK11 已完成 assisted-run / UAT；TASK11 补强 question-impact chain。
- 暂不纳入标准学习：2011、2012，因 OCR 源缺主体。

## 输出汇总

每个 TASK 的最终判断会回收到：

- `final_outputs/学习进度总览.md`
- `final_outputs/反哺规则候选池.md`
- `../tests/exam-fixtures.md`
- `../../references/source-provenance.md`
