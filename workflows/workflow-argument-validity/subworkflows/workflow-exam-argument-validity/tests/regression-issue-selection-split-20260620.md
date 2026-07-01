---
date: 2026-06-20
type: regression-test-report
status: pass
scope:
  - workflow-exam-argument-validity
  - argument-arrow-audit
  - argument-issue-selection
  - exam-argument-issue-selection
---

# Regression: Issue Selection Split 2026-06-20

## 测试目的

本次回归只验证一件事：

```text
把“验箭头”和“选问题”拆成两个 Skill 后，
是否破坏既有论效题 / GRE 案例的输出结构。
```

这不是新题 UAT，也不重新声明 forward-test。它只检查旧输出能否按新架构无损解释为：

```text
exam-argument-arrow-audit
-> 全量箭头审计表

exam-argument-issue-selection
-> 3-4 个可写问题 / assumptions / questions
```

## 被测变更

新增：

```text
../../../skills/argument-issue-selection/
../../../skills/argument-issue-selection/skills/exam-argument-issue-selection/
```

同步瘦身：

```text
../../../skills/argument-arrow-audit/
../../../skills/argument-arrow-audit/skills/exam-argument-arrow-audit/
```

新边界：

```text
验箭头是诊断层：A -> B 到底推不推得动。
选问题是决策层：这么多断点里，这次要写哪几个。
```

## 回测样本

| Case | 旧输出 | 回测重点 | 结果 |
|---|---|---|---|
| CASE-UAT-260619-论效新题 | `projects/CASE-UAT-260619-论效新题/outputs/arrow-audit.md` | 中文论效：箭头表和选点是否可拆 | pass |
| TASK01-2013-勤俭节约过时了 | `projects/PROJECT-260619-论效案例学习/tasks/TASK01-2013-勤俭节约过时了/outputs/arrow-audit.md` | forward-test 样本：4 个可写问题是否仍成立 | pass |
| TASK02-2009-民主集中制 | `projects/PROJECT-260619-论效案例学习/tasks/TASK02-2009-民主集中制/outputs/arrow-audit.md` | 选点是否仍覆盖概念关系主链 | pass |
| TASK10-GRE-Corpora健身 | `projects/PROJECT-260619-论效案例学习/tasks/TASK10-GRE-Corpora健身/outputs/arrow-audit.md` | GRE assumptions 分支是否可拆 | pass |
| TASK11-GRE-Kali雕塑 | `projects/PROJECT-260619-论效案例学习/tasks/TASK11-GRE-Kali雕塑/outputs/arrow-audit.md` | GRE questions 分支是否可拆 | pass |

## CASE-UAT-260619 拆分检查

旧 `arrow-audit.md` 包含两层：

```text
箭头断点表
-> A1-A10 全量审计

选点
-> A1, A2, A4, A7/A8
```

按新架构解释：

| 旧段落 | 新归属 | 判断 |
|---|---|---|
| `箭头断点表` | `exam-argument-arrow-audit` | pass |
| `选点` | `exam-argument-issue-selection` | pass |
| `不优先写的点` | `exam-argument-issue-selection` 的 `discarded but noted` | pass |
| `行文规划` | exam writing / `exam-writing-rules.md` | pass |

旧选点与参考解析仍一致：

```text
A1: 时代变化不能推出勤俭节约过时
A2: 勤俭节约不等于只节流
A4: 勤俭持家不等于削减必要教育投入
A7/A8: 刺激内需不必然要求否定勤俭节约
```

结论：拆分后没有破坏 forward-test 样本。

## TASK02 民主集中制拆分检查

旧输出包含：

```text
A1-A6 全量箭头审计
-> 建议作文写 4 个断点
```

按新架构解释：

| 旧段落 | 新归属 | 判断 |
|---|---|---|
| `箭头断点表` | `exam-argument-arrow-audit` | pass |
| `选点` | `exam-argument-issue-selection` | pass |
| `概念关系命中` | issue selection / writing 的解释支撑 | pass |
| `行文规划` | exam writing | pass |

选出的四组问题仍覆盖主链：

```text
民主不等于简单多数
真理原则与民主程序未必根本对立
集中正确意见不等于少数人说了算
实践检验不等于决策前无法判断
```

结论：概念关系类案例未被拆分破坏。

## GRE 分支拆分检查

### TASK10 Corpora 健身

旧输出：

```text
箭头审查表
GRE 式核心假设清单
```

新归属：

| 旧段落 | 新归属 | 判断 |
|---|---|---|
| `TASK10 箭头审查` | `exam-argument-arrow-audit` | pass |
| `GRE 式核心假设清单` | `exam-argument-issue-selection` | pass |

关键 assumptions 仍绑定 target arrow：

```text
H1 -> A1+A2-B1
H2/H3 -> A3-B2
H4 -> A4-B3
H5 -> B3-F
```

### TASK11 Kali 雕塑

旧输出：

```text
箭头审查表
GRE 式问题影响链
```

新归属：

| 旧段落 | 新归属 | 判断 |
|---|---|---|
| `TASK11 箭头审查` | `exam-argument-arrow-audit` | pass |
| `GRE 式问题影响链` | `exam-argument-issue-selection` | pass |

关键 questions 仍绑定 target arrow：

```text
Q1/Q2 -> A1-B1
Q3 -> B1-B3
Q4 -> B2-B4
Q5 -> C1-D; C2-E
```

结论：GRE assumptions 和 questions 两个分支都能按新架构解释。

## 回归结论

`argument-issue-selection` 的拆出没有破坏既有论效 workflow。

当前旧输出可稳定映射为：

```text
旧 arrow-audit.md 的箭头表
-> exam-argument-arrow-audit

旧 arrow-audit.md 的选点 / assumptions / questions
-> exam-argument-issue-selection

旧 essay-draft / gre-response-draft
-> writing layer
```

## 后续建议

1. 不需要重写旧 case 输出，避免污染历史记录。
2. 后续新跑论效题时，建议实际拆成两个文件：

   ```text
   exam-arrow-audit-table.md
   exam-selected-issues.md
   ```

3. `CASE-UAT-260619-论效新题` 仍保持 `forward-test-pass`。
4. `PROJECT-260619-论效案例学习` 仍保持 `9/9 done`，两个 GRE assisted UAT 仍保持 pass。
