# Source Provenance

## 来源

本 workflow 的初始抽象来自一组论证有效性分析课程文字稿与对应提取稿。原始资料用于能力研发，不进入普通 Skill 主流程。

## 资料位置

```text
references/course-notes/
├── 01-论证有效性分析-总论.md
├── 02-论证有效性分析-审题.md
├── 03-论证有效性分析-行文1.md
├── 04-论证有效性分析-行文2.md
├── 05-论证有效性分析-行文3.md
├── 06-论证有效性分析-谬误识别1.md
├── 07-论证有效性分析-谬误识别2.md
├── 08-论证有效性分析-谬误识别3.md
├── 09-论证有效性分析-谬误识别4.md
├── 10-论证有效性分析-练习方法.md
└── extractions/                         # 忠于课程的逐讲提取稿
```

审稿迁移版提取稿已单独移到：

```text
skills/academic-review-argument-audit/references/course-adapted-extractions/
```

## 清洗方式

| 原始内容 | 迁移后形态 |
|---|---|
| 课程讲解中的审题动作 | `references/course-notes/extractions/02-论证有效性分析-审题.extract.md`；抽象后进入 `references/argument-structure.md` |
| 课程讲解中的谬误类型 | `references/course-notes/extractions/06-09-*`；抽象后进入 `references/fallacy-taxonomy.md` |
| 课程讲解中的行文方法 | `references/course-notes/extractions/03-05-*`；抽象后进入 `references/writing-patterns.md` |
| 课程训练方法 | `references/course-notes/extractions/10-论证有效性分析-练习方法.extract.md`；抽象后进入 workflow 的 structural-green / forward-test-pending 纪律 |
| 应试作文场景 | 去课程化为通用论证有效性审查 |
| 学术审稿迁移讨论 | `skills/academic-review-argument-audit` 与其 `references/course-adapted-extractions/` |

## 迁移状态

| 项目 | 状态 |
|---|---|
| 原始文字稿保存 | done |
| 忠于课程的逐讲提取稿 | done |
| 学术审稿迁移版提取稿 | moved to adapter reference |
| J-260110 真实审稿案例 | structural-green case-study |
| 通用 workflow 结构 | structural-green |
| 通用 Skill | structural-green |
| 学术审稿 adapter | structural-green |
| 论效题子 workflow | structural-green / forward-test-green |
| 新案例 forward-test | pending |

## 边界

- 原始课程材料只作为来源追溯和进一步学习资料。
- 普通 Skill 主流程不依赖课程名、讲师名、考试题号或应试语境。
- 后续若用新审稿项目验证，应在 tests 或项目 TASK 中标记为 forward-test。

## 真实案例反哺记录

| Case | 类型 | 位置 | 反哺内容 | 状态 |
|---|---|---|---|---|
| CASE-J-260110-xinyuan-review | real-review case-study / field-discovery | `projects/CASE-J-260110-xinyuan-review/` | 新增审稿 adapter 的 case-derived review patterns：故事线前提一致性、机制相关样本剔除、溢出效应直接效应基准、机制排除反向解释、核心质疑导向稳健性、强结构低压措辞 | partial / forward-test-pending |

## 对话洞见反哺记录

| Dialogue | 类型 | 位置 | 反哺内容 | 状态 |
|---|---|---|---|---|
| 001-004 | dialogue-derived workflow discovery | `references/dialogues/` | 将论效题与学术审稿统一为“恢复论证树 -> 检查支撑箭头 -> 标注断点影响 -> 输出可读文本”；明确学术论文的双层论证结构，以及 Mermaid `flowchart BT` 在 Obsidian 中表达自下而上支撑关系的默认规则 | structural-green / forward-test-pending |
| workflow-tao comparison | meta-workflow pattern | `../workflow-tao/references/workflow-skill-shape.md` | 将本 workflow 固定为“父层通用论证树 + 子层领域适配”的 workflow 型 Skill：父层负责抽树、验箭头和输出阶梯，子层负责论效题、审稿、写作自审等差异 | structural-green / forward-test-pending |
| TASK07-论效Workflow子实现 | course-driven subworkflow | `subworkflows/workflow-exam-argument-validity/`；`/Users/narra/Documents/alib/Writer/00 信息/知识管理/PROJECT-260618-元Workflow工程/tasks/TASK07-论效Workflow子实现/` | 以课程忠实提取稿为来源，建立论效题子 workflow：审题抓论证、行文规划、练习回归和考试式本论段输出；已由 CASE-UAT-260619 完成新题 forward-test | structural-green / forward-test-green |
| CASE-UAT-260619-论效新题 | course-driven forward-test case | `subworkflows/workflow-exam-argument-validity/projects/CASE-UAT-260619-论效新题/` | 将早年 MBA 联考 OCR 资料整理为 final corpus，并以 2013 “勤俭节约”题完成论效子 workflow 新题 blind-run 与 reference comparison；由“财富滚滚而来/财富积累”等漏点上抽出“概念关系审查”规则，避免碎片 checklist | forward-test-pass / concept-relation-rule-added |
| CASE-FEEDBACK-260619-2009-民主集中制 | course-driven feedback case | `subworkflows/workflow-exam-argument-validity/projects/CASE-FEEDBACK-260619-2009-民主集中制/` | 使用 2009 “民主集中制”题检验概念关系审查；新增“定义回代检查”和“二分关系检查”，并在父层断点分类加入 `false dichotomy` | source-case-green / feedback-applied |
| PROJECT-260619-论效案例学习 | course-driven learning project | `subworkflows/workflow-exam-argument-validity/projects/PROJECT-260619-论效案例学习/` | 将现有 9 篇可学习论效题整理为逐题 TASK 池并全部完成：2013/2009 先行完成，2004/2005/2008 strict blind，2010/2007/2003 assisted，2006 limited blind；新增或强化外推维度、条件关系、对比实验控制变量、概念簇边界、偶然成功与策略有效等规则。2026-06-19 追加 GRE 官方 Analyze an Argument 两题为 TASK10/TASK11，并均完成 assisted UAT：TASK10 反哺 GRE Argument 分支、假设影响链和问题型输出展开；TASK11 反哺 question-impact chain、工具存在与主因机制区分、预测类结论的市场/行为机制审查 | completed / 9 Chinese cases done / TASK10-TASK11 GRE assisted-uat-pass |
| SMK 实证资产定价逐章学习 | local-learning project / candidate-domain-adapter | `skills/argument-arrow-audit/skills/academic-argument-arrow-audit/skills/empirical-social-science-review-adapter/references/candidate-asset-pricing-review-adapter.md` | 将 Ch.1 中样本口径、非平衡 panel、缺失值、控制变量吸收等学习洞见，暂存为资产定价论文拆箭头候选 adapter；待 Ch.1-Ch.6 完成后再判断是否升级为子 Skill | draft / forward-test-pending |

## 外部类比材料扫描

| Source | 类型 | 位置 | 可迁移内容 | 状态 |
|---|---|---|---|---|
| GRE Analytical Writing Supreme, Issue Tasks | GRE Issue / 正向立论材料 | `docs/GRE-Issue-epub-scan.md`；原 EPUB 位于 `docs/` | 该书主体为 GRE Analyze an Issue，不是 Analyze an Argument；适合补强正向搭箭头、隐含假设显性化、反方压力测试、概念解释先行和输出层分化 | scanned / candidate-for-claim-construction |
| Official GRE Verbal Reasoning Practice Questions, Analytical Writing chapter | GRE Argument / 官方论证分析材料 | `docs/GRE-Argument-useful-extraction.md`；原 PDF 位于 `docs/` | 含 Analyze an Argument 方法说明、任务边界、假设/替代解释/反例/统计材料审查、评分标准、练习题与 reader commentary；适合补强父 workflow 的任务指令识别、假设影响链、问题型输出、数字统计审查和质量阶梯 | extracted / candidate-for-workflow-upgrade |

## GRE 方法论反哺记录

| Source | 触发 TASK | 被影响位置 | 反哺内容 | 状态 |
|---|---|---|---|---|
| Official GRE Argument methodology | `PROJECT-260619-论效案例学习` TASK10/TASK11 | `skills/argument-workflow-orchestrator/SKILL.md`; `skills/argument-validity-audit/SKILL.md`; `subworkflows/workflow-exam-argument-validity/skills/exam-argument-validity-orchestrator/SKILL.md`; `references/output-ladder.md` | 将 GRE 官方方法论从父 workflow 概念层下沉到执行层：任务指令识别、assumption-impact chain、question-impact chain、evidence strengthen/weaken、alternative explanation、数字统计审查和输出质量阶梯 | structural-green / gre-assisted-source |
