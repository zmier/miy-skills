# Argument Validity Fixtures

状态：`placeholder / forward-test-pending`

## 用途

记录后续迁移测试案例。当前 workflow 由课程资料和一个审稿项目讨论抽象而来，尚未在未参与提炼的新案例上 forward-test。

## 待补测试

| Fixture | 领域 | 输入 | 预期输出 | 状态 |
|---|---|---|---|---|
| academic-review-new-paper | 学术审稿 | 新论文贡献链与变量/方法段落 | argument-validity-map + review concern paragraph | pending |
| workflow-academic-argument-validity-routing | 学术论文子 workflow / 路由 | 一篇实证论文 Markdown + 一个写作自审请求 + 一个审稿请求 | 能统一进入 academic 子 workflow，并按目标输出作者树、arrow audit 或审稿/自审素材 | pending |
| argument-tree-extraction-routing | 抽树编排 Skill / 路由 | 一篇学术论文 Markdown + 一道论效题 | 能分别路由到 academic 子 Skill 和 exam 子 Skill，不把两者混用 | pending |
| argument-arrow-audit-routing | 验箭头父 Skill / 路由 | 一棵学术论文论证树 + 一棵论效题小树 | 能分别路由到 `academic-argument-arrow-audit` 和 `exam-argument-arrow-audit`，并输出不同形态的 arrow audit | pending |
| argument-arrow-audit-taxonomy-coverage | 验箭头 / 断点库 | 旧 `fallacy-taxonomy.md` + `arrow-break-taxonomy.md` + 论效/GRE 案例反哺 | `arrow-audit-core.md` 覆盖谬误标签、概念关系、数字统计、外推、机制预测和 GRE instruction outputs；子 Skill 与模板能引用该库 | pending |
| academic-fallacy-adapter-routing | 学术验箭头 / 领域表达适配 | 同一组 `break_type / fallacy_label`，分别来自实证论文、理论模型论文和综述/概念论文 | 能把通用断点翻译成不同论文类型的审稿表达，并保留 `arrow_id -> break_type -> domain_expression` 链条 | pending |
| academic-argument-arrow-audit | 学术论文 / 验箭头 | `paper-argument-tree.md` + `evidence-ledger.md` | 能生成全量 `academic-arrow-audit-table.md` 和 `issue-selection-candidates.md`，不直接选 major concern | pending |
| academic-arrow-repair-mapping | 学术论文 / 断箭头修复映射 | `academic-arrow-audit-table.md` + `academic-arrow-break-summary.md` + `external-evidence-ledger.md` | 能先声明 mode 并审计 `knowledge_source`，再生成 `arrow-repair-map.md`；新领域能输出 `repair-knowledge-learning-plan.md` 和 `case-repair-menu.md` | pending |
| academic-repair-knowledge-learning | 学术论文 / 修复知识学习 | `repair-knowledge-gap.md` + target arrows + candidate literature | 能区分摘要扫描和原文/图表/补充材料深读，生成 `abstract-scan-ledger.md`、`fulltext-pattern-ledger.md` 和 `case-repair-menu.md` | pending |
| CASE-J-260110-piqiu-repair-mapping-uat | 工科材料/器件论文 / 修复映射 UAT | TASK03 箭头审计产物，不读取真实审稿意见 | 干净 subAgent 生成 `arrow-repair-map.md`，命中 zeta potential、EIS、EDS mapping、SOTA benchmark、长时稳定、弯折洗涤、人工汗液等修复路线；见项目 TASK04 | pass / useful-with-feedback |
| academic-argument-issue-selection | 学术论文 / 选问题 | `academic-arrow-audit-table.md` + `arrow-repair-map.md` | 能生成 `review-issue-arrow-map.md`、major concern candidates 和 revision action map | pending |
| exam-argument-arrow-audit | 论效题 / GRE 验箭头 | 论效题/GRE 小型论证树 | 能生成全量 `exam-arrow-audit-table.md`，不直接选 3-4 个问题 | pending |
| exam-argument-issue-selection | 论效题 / GRE 选问题 | `exam-arrow-audit-table.md` | 能选出最可写 3-4 个断点，并按中文论效或 GRE 指令生成段落路线 | pending |
| academic-paper-argument-tree-extraction | 学术论文 / 作者树 | 一篇未参与提炼的新实证论文 Markdown | 能生成 `paper-argument-tree.md`、`evidence-ledger.md`、`evidence-expanded-mermaid.md`、`obsidian-link-map.md`，并标出表格/图/文献链接缺口 | pending |
| exam-argument-tree-extraction | 论效题 / GRE 作者树 | 一道未参与提炼的论效题或 GRE Argument | 能生成总论点、分论点、箭头表、隐含假设和 3-4 个可写断点候选 | pending |
| academic-review-argument-tree | 学术审稿 / 论证树 | 一篇未参与提炼的新实证论文 | 能恢复 `X1: 问题有意义`、`X2: 作者证明了具体核心发现`、`Y: 值得发表/贡献成立` 的双层论证树；同时给出一句话核心发现、X/M/Y/Y2 表、Mermaid `flowchart BT` 和关键弱箭头 | pending |
| exam-argument-tree | 论效题 | 一道未参与提炼的新论证有效性分析题 | 能先画出小型论证树，再把 2-4 条断裂箭头写成考试式分析段 | pending |
| CASE-J-260110-xinyuan-review | 学术审稿 / 来源案例回归 | J-260110 稿件与欣媛审稿意见 | 能解释强审稿意见中的论证断点与段落结构 | partial-source-case |
| policy-argument | 政策论证 | 一段政策建议文本 | 论证链与断点表 | pending |
| business-report | 商业报告 | 一段商业结论 | 标准匹配与过度推理检查 | pending |
