# Exam Argument Validity Fixtures

状态：`forward-test-green`

## 待测样本

| Fixture | 输入 | 预期输出 | 状态 |
|---|---|---|---|
| CASE-UAT-260619-论效新题 | `projects/CASE-UAT-260619-论效新题/inputs/prompt.md` | 审题记录 + Mermaid 小树 + 箭头断点表 + 3-4 个本论段 + 修改清单 | pass；见 `projects/CASE-UAT-260619-论效新题/outputs/reference-comparison.md` |
| CASE-UAT-260619-writing-quality-v2 | `projects/CASE-UAT-260619-论效新题/outputs/arrow-audit.md` + `reference-comparison.md` | 拆出 `argument-issue-selection` 后重新生成 `exam-arrow-audit-table.v2.md`、`exam-selected-issues.v2.md`、`essay-draft.v2.md` 并检查行文质量 | pass / non-blind-regression；见 `projects/CASE-UAT-260619-论效新题/outputs/writing-quality-regression-v2.md` |
| PROJECT-260619-论效案例学习 | `projects/PROJECT-260619-论效案例学习/tasks/TASK01-*` 至 `TASK09-*` | 每题 `prompt/reference` 拆分、论证树、箭头审查、作文草稿、对照、skill feedback、log | pass；9/9 done；其中 2004/2005/2008 为 strict blind，2010/2007/2003 为 assisted，2006 为 limited blind |
| TASK10-GRE-Corpora健身 | `projects/PROJECT-260619-论效案例学习/tasks/TASK10-GRE-Corpora健身/` | GRE 路由、论证树、hidden assumption impact table、GRE response draft、官方答案对照、UAT | pass / assisted-uat；prior-exposed，不计入 strict blind |
| TASK11-GRE-Kali雕塑 | `projects/PROJECT-260619-论效案例学习/tasks/TASK11-GRE-Kali雕塑/` | GRE 问题型路由、论证树、question -> target arrow -> yes/no impact table、GRE response draft、官方答案对照、UAT | pass / assisted-uat；prior-exposed，不计入 strict blind |
| recent-real-exam | 一道未参与提炼的近年真题 | 审题记录 + Mermaid 小树 + 3-4 个本论段 | pending |
| course-example-regression | 课程讲过的代表例题 | 能复现课程中的结构识别、论证树、断点分类和段落规划 | pass；见 `unit-course-regression-20260619.md` |
| issue-selection-split-regression | 既有中文论效、GRE assumptions、GRE questions 输出 | 拆出 `argument-issue-selection` 后，旧 arrow-audit 输出可无损拆成全量验箭头与选问题 | pass；见 `regression-issue-selection-split-20260620.md` |
| simulated-material | 一道模拟论效材料 | 能发现主要断裂箭头，避免被故事带跑 | pending |
