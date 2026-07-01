# Tests

## 目的

本目录保存 `workflow-exam-argument-validity` 的回归测试、UAT 计划和迁移验证记录。

## 测试分层

| 层级 | 材料 | 作用 | 状态 |
|---|---|---|---|
| unit / regression | 老王课堂已讲过的范例 | 验证规则是否能复现课程动作，防止后续修改破坏既有能力 | 已有 |
| integration | 已知完整题干 + 解析/范文 | 验证六步 workflow 能否串起来 | 待补 |
| UAT / forward-test | 未参与提炼的新论效题 | 验证 workflow 是否具有迁移能力 | 待补 |

## 当前测试入口

| 文件 | 类型 | 用途 |
|---|---|---|
| `exam-fixtures.md` | fixture registry | 记录待测样本、预期输出和状态 |
| `unit-course-regression-20260619.md` | unit / regression report | 用老王课堂范例回归审题、画树、验箭头、选点和行文规划 |
| `regression-issue-selection-split-20260620.md` | regression report | 验证拆出 `argument-issue-selection` 后，既有论效/GRE 案例未被破坏 |

## 回归纪律

每次修改以下内容后，应至少回看或回跑 `unit-course-regression-20260619.md`：

- `../SKILL.md`
- `../skills/exam-argument-validity-orchestrator/SKILL.md`
- `../references/exam-reading-rules.md`
- `../references/exam-writing-rules.md`
- `../references/exam-practice-loop.md`
- `../assets/exam-argument-tree-template.md`
- `../assets/exam-paragraph-template.md`
- 父层 `../../../skills/argument-arrow-audit/references/arrow-audit-core.md`
- 父层 `../../../skills/argument-issue-selection/SKILL.md`
- 父层历史断点参考 `../../../references/arrow-break-taxonomy.md`

## 状态边界

`course-regression-pass` 只表示能复现课堂范例，不等于 `forward-test-green`。

只有使用未参与提炼的新题完整跑出：

```text
审题记录 -> Mermaid 论证树 -> 箭头断点表 -> 行文规划 -> 文章草稿 -> 修改清单
```

并通过预设验收标准，才可以标记为 `forward-test-green`。
