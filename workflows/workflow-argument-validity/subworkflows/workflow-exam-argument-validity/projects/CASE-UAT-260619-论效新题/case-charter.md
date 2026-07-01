# 课程案例 Skill 研发契约

## 基本信息

- 项目模式：`course-case / forward-test`
- 课程/单元：论证有效性分析课程；早年 MBA 联考论效题资料
- 案例：CASE-UAT-260619 论效新题
- 原始样本：`inputs/_ori/`
- case-local evidence：
  - `inputs/prompt.md`
  - `inputs/reference.md`
  - `inputs/student-draft.md`
  - `inputs/final/`
- 授权与安全边界：本地学习与 workflow 研发资料；题目、解析、范文和点评只作为 case-local evidence 与测试语料，不复制到通用 Skill 主流程。
- 现有领域总编排：
  - `workflow-argument-validity`
  - `workflow-exam-argument-validity`
- 当前 Skills 基线：
  - `argument-workflow-orchestrator`
  - `argument-validity-audit`
  - `exam-argument-validity-orchestrator`

## 终点

- 最终复现目标：使用一篇未参与父 workflow 抽象的新论效题，验证 `workflow-exam-argument-validity` 是否能从题干独立产出审题记录、论证树、断点表、行文规划和作文草稿。
- 探索问题：
  - 六步论效 workflow 是否足以指导新题处理？
  - Mermaid 自下而上论证树是否能清楚表达题干主轴？
  - 箭头断点选择是否能避免只贴谬误标签？
  - 本论段是否能按“定位 -> 分析 -> 收尾”落成可读文字？
  - 哪些失败应回填到 reading / writing / practice references？
- 阶段终点类型：`capability / deliverable`
- Smoke：仅使用 `inputs/prompt.md`，能还原材料总论点和至少 3 条主要论证链。
- Unit/阶段 Green：产出 `outputs/argument-tree.md`、`outputs/arrow-audit.md`、`outputs/essay-draft.md`、`outputs/revision-notes.md`。
- 端到端验收：最终作文草稿至少包含标题、开头、本论 3-4 段、结尾；每个本论段绑定一条断裂箭头。
- 覆盖率声明：`阶段性`
- 明确不做：
  - 不把 `inputs/reference.md` 当作 blind 阶段答案；
  - 不把课程题库个案写成通用规则；
  - 不声称已覆盖所有论效题型；
  - 不把 2011、2012 两个缺源文件作为完整 UAT 样本。
- 停止条件：UAT 四个输出文件完成，并形成课程驱动 Skill 工程评测；若新题失败，记录首个失败层而不是改预期答案。

## 阶段与冻结

- 当前阶段：`blind / forward-test`
- 独立性等级：`limited-blind`
- 已读材料：
  - `workflow-exam-argument-validity/SKILL.md`
  - 论效课程忠实提取稿与子 workflow references
  - 本 case 的 OCR 清洗与 final corpus 索引
- 已暴露的解法信息：
  - 已知 `inputs/reference.md` 中存在 2013 题的论证结构、解析和范文；
  - 因此真正 forward-test 运行时，`reference.md` 只能作为事后对照，不能作为 primary 生成依据。
- blind 可读材料：
  - `inputs/prompt.md`
  - `workflow-exam-argument-validity/SKILL.md`
  - 子 workflow 的通用 references 和 assets
- 冻结的教师材料：
  - `inputs/reference.md`
  - `inputs/final/2013-10-MBA-勤俭节约过时了.final.md` 中除题干以外的解析、范文、点评部分
  - `inputs/final/FULL-CORPUS.final.md`
- 冻结的初始假设：
  - 不预设“勤俭节约过时了”材料必然只能写某几类问题；
  - 不预设课程范文就是唯一最佳答案。
- 解冻条件：
  - 四个 UAT 输出完成后，用 `inputs/reference.md` 做 comparison；
  - 或者 blind 阶段出现不可推进阻塞，并记录最小解冻范围。
- 是否发生提前解冻：`no`

## 证据

| 结论 | 证据角色 | 来源 | 落盘位置 | 状态 |
|---|---|---|---|---|
| OCR 已转为可测试 final corpus | primary | `inputs/_ori/` -> `inputs/cleaned/` -> `inputs/final/` | `inputs/final/README.md` | done |
| 2013 题可作为 forward-test 输入 | primary | `inputs/prompt.md` | `README.md`; `case-charter.md` | ready |
| 参考解析只能作为事后对照 | boundary | `inputs/reference.md`; `inputs/final/2013-*` | `case-charter.md` | declared |
| 2011、2012 缺源不能作为完整 UAT | boundary | `inputs/final/*.incomplete.md` | `inputs/final/README.md` | declared |

## 探索性反馈

| 发现 | 类型 | 影响的路线 | 证据 | 是否反哺 Skill |
|---|---|---|---|---|
| OCR 语料需要质量等级，否则会把缺源误判为模型失败 | operational-safeguard | UAT 输入准备 | `inputs/final/README.md` | yes, case-level |
| 题干与参考答案必须分离，避免 forward-test 泄漏 | workflow-rule | blind-first / exam workflow | `case-charter.md` | yes, evaluation |
| 点评区混排材料适合做写法和失分点参考，不适合做题干真值 | data-boundary | corpus routing | `inputs/final/README.md` | yes, fixture |

## Skill 工程状态

- 候选 Skill 变更：
  - 更新 `tests/exam-fixtures.md`，纳入 CASE-UAT-260619；
  - 更新父 workflow `references/source-provenance.md`，记录本 case 的 final corpus 和 UAT 状态；
  - 产出 `outputs/course-skill-evaluation.md` 和 `outputs/UAT.md`。
- 回归范围：
  - 不修改通用父 workflow 主流程；
  - 不修改课程忠实提取稿；
  - 只补论效子 workflow 的 fixture / provenance / UAT 记录。
- 迁移案例：`inputs/prompt.md` 2013 “勤俭节约”题。
- 迁移状态：`forward-test-pass`
