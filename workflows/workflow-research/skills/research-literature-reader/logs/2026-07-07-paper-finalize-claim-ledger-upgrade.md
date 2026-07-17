# paper-finalize claim ledger upgrade

## Background

`extract -> finalize` 黑箱 UAT 显示路由可用，但 finalize 产物仍有三个问题：

```text
1. 正文草案默认写成英文，不适合中文项目工作流；
2. verified-citable 状态太粗，无法区分正文总结、方向性结果、方法描述和已核表格数值；
3. final note 有状态标注，但 source-check log 还不够像逐条 claim 的核验账本。
```

## Changes

本次只更新 `paper-finalize`：

```text
skills/paper-finalize/SKILL.md；
skills/paper-finalize/templates/final-literature-note-template.md。
```

## Claim Status Expansion

新增更细的 claim status：

```text
verified-citable-text-summary:
  作者正文明确总结，可引用为作者文本总结；
  若含精确数值，表格值仍需核验。

verified-citable-method-description:
  方法、数据、变量、模型设定已核验，可引用。

verified-citable-directional-result:
  方向性结果已核验，可引用；
  精确数值仍需表格 / PDF 核验。

verified-citable-table-value:
  精确数值已由 PDF / restored table / source table 核验，可引用。
```

保留原有：

```text
verified-citable；
verified-understanding；
inferred-not-citable；
needs-source-check；
contradicted-or-revise。
```

## Exact Number Rule

强化规则：

```text
凡是精确百分比、年化差距、系数、t-stat、p-value、R2、样本量、公式符号细节，
即使出现在摘要、引言、正文或结论的文字叙述中，
也不得直接标普通 verified-citable。

若只核验到正文文字：
  标 verified-citable-text-summary + table-value-needs-check。

若已核验 PDF / restored table / source table：
  才可标 verified-citable-table-value。
```

## Language Rule

新增输出语言规则：

```text
默认输出语言跟随用户语言；
中文项目中 final-literature-note / verified-claims / source-check-log 默认中文；
关键英文术语首次出现时括注英文。
```

示例：

```text
有限注意力（limited attention）；
买入媒体报道股票倾向（PROPENSITY_BUY_MEDIA）；
预测关系（predictive relation）；
机制一致性证据（mechanism-consistent evidence）。
```

## Three-Artifact Requirement

明确 `paper-finalize` 默认输出三件套：

```text
final-literature-note.md；
verified-claims.md；
source-check-log.md。
```

如果由于篇幅限制不能完整展示，必须说明：

```text
本轮已展示；
本轮未展示但应生成；
未展示原因。
```

## Source-Check Log as Ledger

`source-check-log.md` 被明确为逐条 claim 的核验账本，而不是 final note 的摘要附录。

每条核心 claim 至少记录：

```text
claim ID；
claim type；
first-pass statement；
verified statement；
source checked；
check action；
claim status；
remaining risk；
next check。
```

## Expected Effect

下一轮 UAT 应重点检查：

```text
1. 中文输出是否稳定；
2. 精确数值是否不再直接标普通 verified-citable；
3. 是否出现 verified-citable-text-summary + table-value-needs-check；
4. 是否输出或明确规划三件套；
5. source-check-log 是否像核验账本。
```
