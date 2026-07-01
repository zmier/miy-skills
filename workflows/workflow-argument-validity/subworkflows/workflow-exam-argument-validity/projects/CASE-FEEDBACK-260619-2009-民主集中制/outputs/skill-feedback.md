# Skill Feedback

状态：`feedback-applied`

## 来源

- Case：CASE-FEEDBACK-260619 2009 民主集中制
- Blind-run：`outputs/argument-tree.md`、`outputs/arrow-audit.md`、`outputs/essay-draft.md`
- Reference comparison：`outputs/reference-comparison.md`

## 反哺判断

本 case 证明上一轮“概念关系审查”规则有效，但还需要补两个子动作：

1. 定义回代检查；
2. 二分关系检查。

## 修改目标

| 文件 | 变更 |
|---|---|
| `references/exam-reading-rules.md` | 在概念关系审查中加入定义回代与二分关系检查 |
| `../../references/arrow-break-taxonomy.md` | 新增 `false dichotomy` 断点 |
| `references/source-provenance.md` | 记录本 case 的反哺 |

## 泛化边界

适用：

- 题干明确给出概念定义；
- 题干提出 A/B 两种解释、方案、原则或路径；
- 作者通过否定 A 推出 B；
- 作者把两个概念说成缺一不可，但随后又给出相同定义。

不适用：

- 题干没有定义或二分结构；
- 两个选项确实互斥且穷尽；
- 定义只是背景说明，不承担推理功能。

## 反哺结论

本次反哺属于 `update-existing / source-case-green / forward-test-pending-on-next-case`。
