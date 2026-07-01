---
name: academic-argument-arrow-audit
description: 学术论文专用验箭头复合 Skill。用于在 paper-argument-tree、evidence-ledger 和审稿项目中，沿作者论证树逐条检查 arrow_id 的 A 到 B 是否推得动；按接收作者树、改写箭头、判断箭头类型、第一轮内部验箭头并集中标记外部证据需求、消费集中学习产物回填 audit ledger、生成候选、移交修复映射或选点执行；外部文献与领域学习优先交给 academic-field-evidence-learning，不负责选择 major concern。
---

# Academic Argument Arrow Audit

## 执行模式

调用本 Skill 前必须先确定执行模式，并在当前 TASK 的 `TASK说明` 或 `log.md` 顶部写明。

```text
mode: internal-blind-audit
```

用于盲跑、回归测试、材料初审或用户明确要求“先不查外部资料”的场景。执行：

```text
步骤 0-4：接收作者树、显影、改写箭头、分类、第一轮内部验箭头；
步骤 5：只生成 external-evidence-request.md；
步骤 6：生成 external-evidence-ledger.md，但所有外部请求标 not-searched / pending；
步骤 7-8：生成 break summary 和 issue selection candidates，但需要外部证据的判断必须保留 needs-external-evidence。
```

该模式下不得联网、不得调用数据库检索、不得伪造外部证据，也不得把 `needs-external-evidence` 写成已确认的 weak/broken。

```text
mode: full-evidence-audit
```

用于正式审稿诊断、需要判断 gap/方法/指标有效性、或用户要求“完整验箭头”的场景。执行完整诊断并与集中学习层配合：

```text
步骤 0-4：先完成内部验箭头并集中标记外部证据需求；
步骤 5：把 external-evidence-request.md 交给 academic-field-evidence-learning；
步骤 6：消费 external-evidence-ledger.md / handoff-to-arrow-audit.md 回填 academic-arrow-audit-table.md；
步骤 7-8：输出经过外部证据增强后的 break summary 和 issue selection candidates。
```

该模式下不能跳过 `external-evidence-request.md`，也不能边验边零散检索。所有外部学习必须绑定 `request_id` 和 `target_arrow`。

如果调用者没有指定模式，默认使用：

```text
mode: internal-blind-audit
```

除非用户明确说“查文献 / 完整验箭头 / 回填外部证据 / 判断 gap 是否真实 / 判断方法标准”，才切换为 `full-evidence-audit`。

## 定位

这是 `argument-arrow-audit` 的学术论文子 Skill。它把通用问题：

```text
A 是否足以推出 B？
```

翻译为学术审稿问题：

```text
稿件中的文献、理论、变量、数据、模型、表格、机制和稳健性
是否足以支撑作者声称的发现、因果解释、贡献和政策启示？
```

## 第一原则

本 Skill 是论效题“验箭头”方法在学术论文中的迁移版，不是传统审稿 checklist。

必须坚持：

```text
先取作者论证树上的 arrow_id；
再判断 from_node A 是否足以推出 to_node B；
最后才把断点翻译成学术审稿语言。
```

不得把流程写成：

```text
先查 gap
再查变量
再查样本
再查识别
再查机制
再查稳健性
```

这些模块名只能作为 `arrow_type` 或证据材料标签，不能替代“作者用 A 推 B，A 是否足以推出 B”的主轴。

本 Skill 只做诊断。若要把 weak/broken/unclear 箭头选择成 major concern、minor concern 或 revision action，调用：

```text
../../../argument-issue-selection/skills/academic-argument-issue-selection/SKILL.md
```

若要把 weak/broken/unclear/needs-qc/needs-external-evidence 箭头转为“应该补什么证据、实验、分析，或如何降调”的修复路线，先调用：

```text
../../../argument-arrow-repair-mapping/skills/academic-arrow-repair-mapping/SKILL.md
```

再把 `arrow-repair-map.md` 交给 issue selection。不要在本 Skill 中展开完整补救方案；本 Skill 最多保留 `fix_or_downgrade` 的一句话提示。

## 复合 Skill 主轴

本 Skill 是复合型验箭头 Skill。主轴固定为八步；两种执行模式的差异只在第 5-6 步是否有集中学习产物可回填：

```text
1. 接收作者论证树
2. 逐条改写作者箭头
3. 判断学术箭头类型
4. 第一轮内部验箭头并集中标记外部证据需求
5. 移交或接收集中外部学习产物
6. 回填 academic arrow audit ledger
7. 生成 break summary 和 issue selection candidates
8. 移交 issue selection
```

八步输入输出详见 `references/academic-arrow-audit-main-axis.md`。

## 输入

- `paper-argument-tree.md`;
- `canonical-node-ledger.md`;
- `canonical-edge-ledger.md`;
- `evidence-ledger.md`;
- `evidence-expanded Mermaid`;
- `extraction-qc.md`;
- restored manuscript Markdown / PDF 表格抽取；
- 前序审稿 TASK 输出，如变量审查、识别审查、结果叙事审查。

如果输入来自 `academic-paper-argument-tree-extraction`，本 Skill 默认先消费作者树，不重新抽树。若缺少 node / edge / evidence ledger，应标记 `incomplete-tree-input`，不要在验箭头阶段补造作者树。

## 学术箭头类型

详见 `references/academic-arrow-types.md`。这些类型用于给箭头贴标签，不是审查顺序。优先审计影响 `X2` 或 `Y` 的箭头：

```text
gap -> contribution
construct -> measure
treatment definition -> X
sample rule -> mechanism-relevant sample
model/result -> causal claim
mechanism test -> mechanism claim
robustness test -> core threat addressed
short-run finding -> broad contribution / policy implication
```

通用断点类型与逻辑谬误标签使用父 Skill 的 `../../references/arrow-audit-core.md`。学术表达映射使用 `references/academic-fallacy-adapter.md`。操作顺序是：

```text
1. 先用 arrow-audit-core 判断 A -> B 的通用断点；
2. 再用 academic-arrow-types 给这条箭头贴学术类型标签；
3. 再按 empirical / theory-model / review-concept 等论文类型读取 academic-fallacy-adapter；
4. 最后把断点翻译成审稿语言。
```

若论文是材料、器件、能源收集、传感器、柔性电子、可穿戴或其他工科实验论文，还要读取：

```text
references/materials-device-arrow-adapter.md
```

它用于把通用 `A 是否足以推出 B` 翻译成工科实验论文中的高频箭头，例如：

```text
characterization -> mechanism
metric normalization -> performance
SOTA table -> contribution
prototype demo -> application claim
stability test -> durability claim
```

不要先发明一个学术模块问题，再倒推箭头。gap、变量、样本、识别、结果、机制、稳健性、贡献上升都必须回到具体 `arrow_id`。

若论文是经管、金融、会计、管理、公共政策或相邻社科实证论文，还要调用：

```text
skills/empirical-social-science-review-adapter/SKILL.md
```

它用于把作者树中的箭头显影为经管/社科实证审稿敏感类型，例如：

```text
construct-proxy fit
sample-scope fit
model-identification fit
control-variable role
inference-clustering fit
mechanism-evidence strength
robustness-threat fit
descriptive-validity of constructed variables
```

若同时处于中文经管或中文社科审稿语境，该 adaptor 应继续路由到：

```text
skills/empirical-social-science-review-adapter/skills/chinese-management-econ-review-adapter/SKILL.md
```

中文经管 adaptor 只处理本土审稿语境中的方向、文本口径、中文文献谱系、制度背景、政策化表达和报告规范敏感点。它不应把具体题材、企业类型或单篇案例对象硬编码成规则。

## 子 Skill 化边界

不是每个箭头类型都要立刻拆成子 Skill。父 Skill 默认承载轻量判断、表格填充、通用断点映射和审稿语言翻译；只有满足下列条件之一时才拆子 Skill：

- 需要专门方法知识，例如 DID、IV、RDD、DAG、事件研究、NPLR、非线性检验；
- 需要调用外部能力，例如 `scholar-kit-literature-search`、CNKI、WoS、OpenAlex；
- 高频出现且判断路径稳定，例如文献 gap、因果识别、统计结果解释；
- 输出会被后续阶段复用，例如 causal audit ledger、literature gap search brief、statistical result audit table。

子 Skill 与暂由父 Skill 承载的边界详见 `references/subskill-boundary.md`。

当前子 Skill：

| 子 Skill | 何时调用 |
|---|---|
| `skills/academic-literature-gap-arrow-audit` | 验 `文献 / 研究空白 -> gap / contribution`，且需要检索或知识树定位 |
| `skills/academic-causal-arrow-audit` | 验 `设计 / 模型 / 识别 -> 因果声称`，需要 DAG、后门/前门、DID/IV/PSM/RDD 等方法审查 |
| `skills/academic-statistical-result-arrow-audit` | 验 `表格 / 系数 / 显著性 / 量纲 -> 结果或经济意义`，需要统计解释和报告透明度审查 |
| `skills/empirical-social-science-review-adapter` | 经管/社科实证论文的诊断路由：显影 construct-proxy、sample-scope、control-variable、clustering、mechanism、robustness 等敏感箭头 |
| `skills/empirical-social-science-review-adapter/skills/chinese-management-econ-review-adapter` | 中文经管/中文社科审稿语境适配：显影指标方向、文本口径、本土制度语境、中文文献谱系和本地报告规范 |

暂由父 Skill 承载：

```text
construct-measure
sample-mechanism-fit
mechanism-claim
robustness-threat
finding-contribution
```

若这些类型在案例中反复变重，再按 `references/subskill-boundary.md` 升级。

## 复杂方法与知识缺口

DAG 是验 `identification-causal` 箭头的方法之一，不是所有箭头的通用工具。专用统计或学科方法如 NPLR、非线性显著性、材料表征、工程实验设计等，属于本 Skill 的路由管辖范围，但不要求主 Skill 预装所有知识。

如果拿不准某种新方法、新统计检验、近期顶刊做法或跨学科实验技术，不能硬验。先标记 `status: unclear` 或 `status: needs-qc`，并在 `qc_flags` 写 `method-qc`，再按 `references/method-knowledge-feedback.md` 执行：

```text
标记 method_knowledge_gap
-> 检索 / 联网 / scholar-kit 学习
-> 优先读取方法原始论文、顶刊应用、官方 appendix/code/documentation
-> 提炼该方法的验收点
-> 回到 target_arrow 判断 A 是否足以推出 B
-> 把案例学习留在 TASK，把可迁移规则沉淀为 reference candidate
```

遇到缺口时，必须记录：

```text
method_knowledge_gap:
  method:
  target_arrow:
  why_current_reference_insufficient:
  needed_external_source_or_skill:
  search_route:
  learning_notes_path:
  proposed_feedback_target:
```

方法知识沉淀规则见 `references/method-knowledge-feedback.md`。

## 外部证据请求与回填纪律

验箭头第一轮先集中判断稿件内部证据。不要边验边零散检索。若某条箭头需要文献、方法、官方文档、顶刊应用或 citation verification 才能定性，先打标并写入：

```text
external-evidence-request.md
```

然后交给 workflow 第 4 步：

```text
academic-field-evidence-learning
```

集中学习层处理后，再消费：

```text
external-evidence-ledger.md
handoff-to-arrow-audit.md
```

然后回填 `academic-arrow-audit-table.md`。典型需要外部证据的箭头包括：

```text
literature gap 是否真实；
某个指标是否仍是合适的 construct measure；
某种方法/统计检验的审查标准；
某个经典构念是否能被本文操作化方式承接；
近期顶刊或官方文档才知道的做法。
```

### 外部证据路由纪律

`full-evidence-audit` 不能把所有外部资料都交给普通 web search。外部检索由第 4 步集中学习层编排，但本 Skill 生成 request 时必须写清 required route：

| evidence need | required route | fallback / notes |
|---|---|---|
| `literature-gap-search` | 优先调用 `scholar-kit-literature-search`，并按其路由使用 OpenAlex / WoS / CNKI | 普通 web 只能做补充定位，不能替代数据库级检索；若未调用 scholar-kit，必须说明原因 |
| `citation-verification` | 优先走 scholar-kit / DOI / journal page / publisher metadata / cited paper source | 找不到全文不等于引用不存在；要区分 metadata verified、fulltext verified、manual verification needed |
| 中文文献、中文期刊谱系、中文核心/川大B以上 | 必须考虑 CNKI 路线或说明 CNKI 未跑原因 | 不能用英文 web 结果替代中文深库 |
| `method-standard-search` | 方法原始论文、顶刊应用、官方 package/docs、权威 handbook | web/blog 只作理解辅助，不能单独作为强判断依据 |
| `policy-document-check` / `regulatory-filing-check` | 官方监管机构、法律法规、交易所、政府部门原文 | 二手解读不能替代官方文件；法律解释需保守 |
| `official-data-check` | 官方统计、监管数据库、交易所/政府/机构数据说明 | 普通网页摘要不能替代数据源定义 |
| 表格、图、公式、原文数字冲突 | 回到底稿阶段的 PDF/DOCX source QC；需要大模型视觉能力或人工表图核验 | 外部检索不能解决作者原稿表格是否抽错、图是否看错 |

若因为登录、验证码、数据库不可用、权限或技术失败而未能完成指定路线，第 4 步必须在 `external-evidence-ledger.md` 写：

```text
search_status: technical-failure / manual-verification-needed / insufficient-result
missing_required_route:
why_route_not_completed:
what_can_be_concluded:
what_cannot_be_concluded:
```

不得把“没跑 WoS/CNKI/官方源”包装成“没有文献/没有证据”。

如果用户明确要求快速内部审计，可以先不检索，但必须保留 `needs-external-evidence` 或 `needs-qc`，并在 `qc_flags` 写明 `literature-search-needed`、`method-source-needed`、`citation-qc` 等需求，不得把它们写成已定论。

## 流程

0. 从作者树和 evidence ledger 建立 `review-sensitivity-map.md`，显影哪些证据组合最值得验箭头。该步骤是学术验箭头的默认准备物；若输入材料过少无法生成，也必须在 `audit-input-status.md` 说明为什么跳过。该步骤不写最终审稿意见，也不把攻击节点回写作者树。

   ```text
   sensitivity_id | 类型 | 需并读的 evidence_ids | 需回看的原文链接 | 为什么值得后续验箭头 | 影响 X1/X2/Y
   ```

   重点显影：

   - 同一概念在不同章节的用法是否一致；
   - 同一机制在理论、主结果、机制检验、异质性和结论中是否一致；
   - 同一变量在定义、描述统计、回归解释和稳健性中是否一致；
   - 同一样本在主回归、图示、机制检验和异质性中是否一致；
   - 同一时间结构在理论反应过程、事件窗口、POST 编码和动态效应中是否一致；
   - 同一文献指标在原始定义层级和本文操作化层级中是否一致；
   - 不显著结果是否被作者用于排除机制，以及是否存在反向解释；
   - 常规稳健性是否真的回应核心威胁，而不是在同一偏误框架内重复验证。

   具体显影规则见 `references/review-sensitivity-mapping.md`。不要只显影“表文冲突”这种显性问题，还要显影 TASK08 中容易被干净审计漏掉的高敏感前提，例如：

   - `treatment-definition`：所谓“主动”是否只是操作性排除规则，而非真实动机；
   - `sample-mechanism-fit`：样本筛选是否剔除了最能检验机制的事件、对象或对照基准；
   - `construct-level-fit`：作者借用的经典构念是否从宏观/行业层级滑到公司/事件层级；
   - `timing-fit`：处理发生、信息可见、行为反应和结果测量是否在同一时间逻辑中；
   - `baseline-fit`：剔除某类对象后，是否失去判断溢出、学习或竞争机制所需的基准。

1. 从作者树读取关键 `arrow_id`，不重新抽树。优先审查 `review-sensitivity-map.md` 显影出的箭头；若 sensitivity map 不完整，则继续全量遍历影响 X1/X2/Y 的关键箭头。

   学术作者树里可能同时存在 claim-to-claim arrows 和 evidence-to-claim arrows。默认策略是：

   ```text
   claim-to-claim arrows: 全量审计；
   evidence-to-claim arrows: 作为 evidence_ids 绑定到对应 claim arrow；
   ```

   只有当底层 evidence 本身被用于推出关键结论、存在表格/图/引用冲突、或 evidence edge 直接影响 X1/X2/Y 时，才单独审计 evidence-to-claim arrow。不要因为 evidence edge 数量大而机械展开，也不要因为它们底层就完全忽略。
2. 对每条箭头写明：

   ```text
   from_node A
   to_node B
   作者如何用 A 推出 B
   对应 evidence_ids
   ```

3. 判断 A 与 B 的关系：

   - 同一、包含、交叉、并列相容、手段目的、因果、条件、二分；
   - A 是证据、指标、样本规则、模型结果、机制检验、稳健性检验，还是上升性表述；
   - B 是构念、发现、因果声称、机制声称、贡献声称，还是政策启示。

4. 追问隐含前提：

   ```text
   A -> B 需要 H 成立；
   稿件是否证明 H；
   如果 H 不成立，B/X2/Y 如何变弱。
   ```

5. 第一轮内部审计时标注：

   ```text
   strong / strong-with-qc / weak / broken / unclear / needs-qc / needs-external-evidence
   ```

   状态层级必须统一：

   ```text
   status: strong / strong-with-qc / weak / broken / unclear / needs-qc / needs-external-evidence
   qc_flags: table-cell-qc / figure-qc / citation-qc / sample-consistency-qc / method-qc / external-evidence-qc / ...
   ```

   不要把 `needs-table-qc`、`needs-method-qc`、`needs-citation-qc` 同时当作一级 status。它们应放在 `qc_flags`；若 QC 完全阻止定性，一级 status 用 `needs-qc`。

6. 对需要外部证据的箭头集中生成 `external-evidence-request.md`。不要在本步骤零散调用文献检索；把请求交给 workflow 第 4 步 `academic-field-evidence-learning`。如果第 4 步已经返回 `external-evidence-ledger.md` / `handoff-to-arrow-audit.md`，再回填对应 `arrow_id` 的判断。

   如果本轮不检索，仍然必须生成 `external-evidence-ledger.md`，但只能写 `not-searched / pending`，不能伪造外部来源，也不能把 `needs-external-evidence` 改写成已确认的 weak/broken。

7. 将断点翻译成审稿语言：

   | 通用断点 | 审稿表达 |
   |---|---|
   | concept-mismatch | construct mismatch |
   | measurement-mismatch | construct-measure mismatch |
   | causal-leap | identification does not support causal claim |
   | sample-weakness | sample selection / external validity concern |
   | overclaim | evidence-claim mismatch |
   | evidence-qc-gap | table/reporting transparency concern |

   更完整的论文类型映射见 `references/academic-fallacy-adapter.md`。可选附上 `fallacy_label`，但审稿正文应优先使用克制、可执行的学术表达，避免直接指责作者“犯了某某谬误”。

8. 输出 issue selection 候选：
   - 列出 `weak / broken / unclear / needs-qc / needs-external-evidence` 箭头；
   - 保留 `target arrow -> weakened node -> impact on X1/X2/Y`；
   - 不在本 Skill 中决定哪些进入 major concern。

## 步骤输入输出

| 步骤 | 父/子承载 | 输入 | 输出 |
|---|---|---|---|
| 1. 接收作者论证树 | 父 Skill | canonical node/edge ledger、evidence ledger、QC | `audit-input-status.md`，含缺口标记 |
| 2. 改写作者箭头 | 父 Skill | canonical-edge-ledger | `plain-language-arrow-list.md` |
| 3. 判断箭头类型 | 父 Skill + `academic-arrow-types.md` | arrow list、evidence type | `typed-arrow-ledger.md` |
| 4. 第一轮内部验箭头与外部证据打标 | 父 Skill + 子 Skill | typed-arrow-ledger、稿件内部 evidence | `internal-arrow-audit-table.md`、`external-evidence-request.md` |
| 5. 移交或接收集中外部学习产物 | 父 Skill + `academic-field-evidence-learning` | external requests / handoff-to-arrow-audit | `external-evidence-ledger.md`、方法/文献 notes 或 pending handoff |
| 6. 回填 audit ledger | 父 Skill | internal audit + external evidence ledger / handoff-to-arrow-audit | `academic-arrow-audit-table.md` |
| 7. 生成 break summary 和 candidates | 父 Skill | 全量审计表 | `academic-arrow-break-summary.md`、`issue-selection-candidates.md` |
| 8. 移交修复映射 / 选点 | 父 Skill | candidates | 优先交给 `argument-arrow-repair-mapping` 生成 `arrow-repair-map.md`，再交给 `argument-issue-selection`；不写最终审稿意见 |

## 输出

1. `academic-arrow-audit-table.md`
2. `academic-arrow-break-summary.md`
3. `issue-selection-candidates.md`
4. `review-sensitivity-map.md`
5. `sensitivity-expanded-mermaid.md`
6. `audit-route-plan.md`
7. `empirical-review-sensitivity-map.md`（经管/社科实证论文，如有）
8. `empirical-arrow-candidate-ledger.md`（经管/社科实证论文，如有）
9. `chinese-reviewer-sensitive-candidates.md`（中文经管/中文社科语境，如有）
10. `method-knowledge-gap.md`（如有）
11. `external-evidence-request.md`（如有）
12. `external-evidence-ledger.md`（如有）

模板见 `assets/academic-arrow-audit-template.md`。

## 案例反哺

遇到真实审稿意见、返修意见、优秀论文表达或本对话中形成的新映射时，按 `course-driven-skill-engineering` 的真实案例/对话洞见机制处理：

```text
case / TASK 保存具体证据和上下文；
references/academic-fallacy-adapter.md 保存去个案化后的表达映射；
references/materials-device-arrow-adapter.md 保存材料/器件/工科实验论文的去个案化箭头规则；
skills/empirical-social-science-review-adapter/references/ 保存经管/社科实证论文的去个案化敏感箭头规则；
skills/empirical-social-science-review-adapter/skills/chinese-management-econ-review-adapter/references/ 保存中文经管审稿语境的去个案化敏感点；
tests/argument-validity-fixtures.md 记录是否需要 forward-test。
```

新增映射必须绑定具体 `arrow_id` 和 `break_type`，不能只积累漂亮句子。

## 完成标准

- 每条审查都以 `arrow_id: A -> B` 为主轴，不以 gap/变量/识别/机制/稳健性 checklist 为主轴；
- `review-sensitivity-map.md` 只能消费作者树和 evidence ledger，不允许凭空增加没有原文锚点的问题；
- 每个 `break_type` 优先来自 `../../references/arrow-audit-core.md`，每个 `arrow_type` 来自 `references/academic-arrow-types.md`；
- 每个审稿表达应能追溯到 `references/academic-fallacy-adapter.md` 的通用映射、论文类型映射、`references/materials-device-arrow-adapter.md` 的工科实验映射，或明确标注为 case-derived candidate；
- 每个 weak/broken 箭头说明影响 `X1`、`X2` 还是 `Y`；
- 表格或系数无法核实时标 `status: needs-qc`，并在 `qc_flags` 写 `table-cell-qc` 或 `reporting-qc`；
- 审计说明用大白话说明“作者说的是什么、证据是什么、为什么推不出”；
- 不在本 Skill 中选择 major concern 或写最终审稿段落；
- 不把作者树和审稿攻击混在同一张图里。
