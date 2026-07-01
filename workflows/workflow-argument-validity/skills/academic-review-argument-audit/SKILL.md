---
name: academic-review-argument-audit
description: 学术论文审稿中的论证有效性写作适配 Skill。用于在 academic-paper-argument-tree-extraction、academic-argument-arrow-audit、academic-arrow-repair-mapping 和 academic-argument-issue-selection 已经产出作者树、箭头审计表、修复映射和已选审稿问题之后，把 selected issues 写成 construct-measure fit、evidence-claim match、causal claim validity 和 reviewer concern paragraph。
---

# Academic Review Argument Audit

## 目标

把已选论证断点写成学术论文审稿语言：

```text
作者实际观察到什么
-> 作者如何解释
-> 作者上升成什么理论 / 贡献 / 因果结论
-> 当前稿件是否足以支持这条上升链
```

本 Skill 必须区分两层：

```text
issue content = 写什么，由 issue-selection 决定
review style = 怎么写，由 drafting brief / style profile 决定
```

风格不能改变事实边界。`style_profile` 只能改变组织方式、语气、详略和实验请求粒度，不能新增没有 issue id、target arrow 或证据来源的重大问题。

## 与父 Workflow 的关系

本 Skill 是 `workflow-argument-validity` 的学术审稿写作 adapter。它位于抽树、验箭头和选问题之后：

```text
academic-paper-argument-tree-extraction
-> academic-argument-arrow-audit
-> academic-arrow-repair-mapping
-> academic-argument-issue-selection
-> academic-review-argument-audit
```

本 Skill 可以读取前序产物并补做局部核查，但不应重新承担全量抽树、全量验箭头或 major concern 选择。

课程忠实提取稿保存在父 workflow 的 `references/course-notes/extractions/`；本 Skill 下的 `references/course-adapted-extractions/` 只保存“课程方法如何迁移到学术审稿”的适配笔记，不代表课程原意本身。

## 输入

- `drafting-brief.md`（推荐，每次成文前先声明风格、读者、推荐姿态和 guardrail）；
- restored manuscript Markdown；
- `paper-argument-tree.md`；
- `academic-arrow-audit-table.md`；
- `arrow-repair-map.md`；
- `review-issue-arrow-map.md` 或 `major-concern-candidates.md`；
- `quick-read-contribution-chain.md`；
- literature genealogy / gap matrix；
- causal identification audit；
- variable-data-measurement audit；
- results narrative audit；
- review issue ledger；
- final review draft。

`drafting-brief.md` 推荐字段：

```text
style_profile:
audience:
decision_posture:
language_policy:
allowed_reference_material:
output_forms:
qc_guardrail:
tone:
length:
```

若没有 `drafting-brief.md`，必须先创建一个最小 brief，再开始写审稿段落。

可用风格 profile 见：

```text
references/review-style-profiles.md
```

## 审稿映射表

| 通用论证元素 | 学术审稿对应物 |
|---|---|
| 论点 | 作者核心贡献、理论结论、因果声称、政策启示 |
| 论据 | 文献、变量、数据、模型、结果表、稳健性、机制检验 |
| 箭头 | gap -> contribution；construct -> measure；identification -> causal claim；result -> theory |
| 概念不一致 | construct-measure mismatch |
| 过度推理 | evidence-claim mismatch |
| 因果跳跃 | identification 不足、后门路径未关闭、工具变量假设不足 |
| 以偏概全 | 样本、行业、国家、时期、企业类型外推 |
| 更换衡量标准 | 用不适配指标评价理论概念 |

## 写作流程

1. 读取 drafting brief 与风格 profile：
   - 明确读者是 author-facing、editor-facing 还是内部素材；
   - 明确 `decision_posture` 是 major revision、minor revision、reject、revise-and-resubmit，还是 draft/provisional；
   - 明确语言策略，如 `zh-first-en-parallel`；
   - 明确是否允许读取真实审稿意见作为 style calibration；
   - 明确 `hold-for-qc` 只能写成澄清/补充请求，不能写成作者已错。

2. 读取已选问题：

   ```text
   selected issue
   -> target arrow
   -> weakened node
   -> impact on X1/X2/Y
   -> repair route / downgrade route
   ```

   若没有 `review-issue-arrow-map.md` 或 `major-concern-candidates.md`，先返回上一环节调用 `academic-argument-issue-selection`。
   若没有 `arrow-repair-map.md`，只能写诊断型问题；涉及“建议作者补充实验/分析/文献”时，应先返回上一环节调用 `academic-arrow-repair-mapping`。

3. 核对作者声称链：

   ```text
   实际观测发现 -> 作者解释 -> 作者上升贡献
   ```

4. 将已选问题翻译成学术审稿语言：

   | 已选问题类型 | 审稿表达 |
   |---|---|
   | gap -> contribution weak | contribution overclaim |
   | construct -> measure weak | construct-measure mismatch |
   | identification -> causal claim weak | causal claim validity concern |
   | result -> theory weak | evidence-claim mismatch |

5. 必要时补做局部证据核查：

   - 缺表格值时标记 `needs-table-qc`；
   - 缺段落锚点时标记 `needs-anchor`；
   - 缺文献链接时标记 `needs-citation-link`；
   - 不伪造未核实的系数、显著性或样本量。

6. 生成审稿段落：

   ```text
   定位：作者将 A 作为 B 的证据，并据此推出 C。
   分析：A 更直接反映的是 A1；若要推出 B，还需证明 ...。
   收尾：因此，当前证据尚不足以支持 C 的强表述。
   建议：作者应补充 ...，或将结论降调为 ...。
   ```

7. 风格化但不改事实：
   - 欣媛风格：突出论证链、贡献边界和为什么这是核心问题；
   - 材料/器件审稿人风格：逐点列出具体实验、指标、图表和补充材料请求；
   - hybrid 风格：先用论证语言说明问题，再用具体实验包说明作者可怎么修；
   - concise-journal 风格：压缩成系统表单可粘贴的短条目。

8. 做 drafting QC：
   - 每条意见能回到 issue id / target arrow / repair route；
   - `needs-qc`、`needs-source-figure-qc`、`needs-fulltext-pattern-check` 没有被写成 confirmed error；
   - 中文版能读懂，不假设读者知道前序讨论；
   - 英文版不是中文直译，而是正式审稿语气。

## 必须特别捕捉的问题

- 实际观测发现与上升发现是否 match；
- X 的操作化是否真的代表 X；
- Y 的操作化是否真的代表 Y；
- 宏观概念或国贸指标是否能直接适配企业层面；
- 识别策略是否足以支撑 causal language；
- 变量量纲、share / rate / index / log / level 是否解释清楚；
- 旧分类、基准年清单或历史指标是否忽略样本期新变化；
- 稳健性指标是否真是替代测量，还是换了层级或口径。

## 真实审稿案例触发规则

当稿件或审稿草稿出现以下情况时，读取 `references/case-derived-review-patterns.md`：

- 作者在主效应、机制、异质性或排除机制时切换核心理论前提；
- 样本筛选可能剔除了最能检验作者机制的事件；
- 论文主张溢出效应、同群效应或模仿效应，但缺少事件主体自身效应基准；
- 作者用某个结果不显著来排除机制，但存在反向解释；
- 常规稳健性没有回应样本、定义、识别或机制前提等核心质疑；
- 审稿段落结构有力但语气压强过高，需要保留结构并降低情绪性措辞。

## 输出

1. `argument-validity-review-notes.md`：
   - 已选问题；
   - target arrow；
   - weakened node；
   - impact on X1/X2/Y；
   - 审稿表达路线。
2. `review-issue-ledger` 更新项：
   - issue type: `argument-validity`;
   - severity；
   - evidence location；
   - route；
   - next action。
3. 审稿段落草稿：
   - 中文主体；
   - 必要术语括英文；
   - 英文版保留专业表达；
   - 每条意见有可执行建议。
4. `drafting-qc.md`：
   - 使用的 `style_profile`；
   - 每条段落对应的 issue id；
   - hold-for-qc / evidence guardrail 是否被正确保留；
   - 哪些句子需要人工确认。

## 中文可读性规则

- 中文不是英文硬翻译，必须让审稿人自己读得懂。
- 关键术语第一次出现时补括号英文，例如“构念-指标错配（construct-measure mismatch）”。
- 对“2001 年之后的新产品”“IFR 指标”“HS6 码”等背景桥，不假设读者已知道前序讨论。
- 每条技术意见都写清：
  - 作者说的是什么；
  - 实际证据是什么；
  - 两者为什么不完全一样；
  - 这对结论有什么影响；
  - 作者可以怎么改。

## 完成标准

- 至少覆盖贡献链中的一个关键箭头；
- 每个问题都能追溯到稿件证据或前序 TASK 输出；
- 没有把通用考试作文术语直接贴进审稿意见；
- 问题写法克制、专业、可执行；
- 若用于最终审稿文本，应交给 final drafting / QA / post-flight verifier 做二次检查。
