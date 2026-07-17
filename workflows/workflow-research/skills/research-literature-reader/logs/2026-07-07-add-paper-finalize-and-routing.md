# Add paper-finalize and routing

## Context

在测试 `paper-extract -> paper-co-read` 后，当前 Skill 已能稳定生成 first-pass automatic extraction 和 co-reading orientation。但用户进一步追问：

```text
这些结论是否能作为最终文献笔记或可引用结论？
```

由此确认：first-pass 抽取和共同读并不等于可引用最终笔记。还需要一个下游核验定稿层。

## Decision

新增 `paper-finalize`：

```text
paper-reading/skills/paper-finalize/SKILL.md
paper-reading/skills/paper-finalize/templates/final-literature-note-template.md
```

它的职责是：

```text
接收 automatic-extraction.md；
可选接收 discussion-outline.md；
回到 PDF / restored manuscript / tables / figures / source anchors；
核验 A01-A08 核心论证链；
输出 final-literature-note.md / verified-claims.md / source-check-log.md；
区分可引用结论、理解性结论、推断性结论和待核验结论。
```

## Routing

正式流程定义为三条：

```text
默认推荐：
  paper-extract -> paper-co-read -> paper-finalize

用户明确要求先核验：
  paper-extract -> paper-finalize -> paper-co-read

批量 / 正式文献库：
  paper-extract -> paper-finalize
```

## Rationale

`paper-extract` 的目标是快速形成结构化地图，允许 `needs-source-check`。

`paper-co-read` 的目标是共同解释、纠偏和确定阅读议程。

`paper-finalize` 的目标是 source-verified finalization：

```text
不是重新摘要；
不是共同读聊天；
而是逐项核验哪些判断能引用。
```

如果把 finalize 塞进 `paper-extract`，会让每次 first-pass 阅读成本过高，也会让用户只是想先理解论文时被迫进入表格核验。

如果只写在 `paper-finalize` 自己的 Skill 中，父级编排不会知道何时路由。因此本次同时更新：

```text
research-literature-reader/SKILL.md；
paper-reading/SKILL.md。
```

## Cold-Start Finalization

用户可以明确要求：

```text
paper-extract -> paper-finalize -> paper-co-read
```

此时必须标记：

```text
finalization mode: cold-start finalization
co-read status: not performed
scope warning: 未经过共同读筛选，核验范围以 A01-A08 核心论证链为主。
```

这允许先拿稳定底稿，再共同读；但成本高于默认流程。

## Claim Status

`paper-finalize` 引入 claim status：

```text
verified-citable；
verified-understanding；
inferred-not-citable；
needs-source-check；
contradicted-or-revise。
```

这将防止 first-pass 结论被误当成最终可引用结论。

## Asset Implication

文献目录建议新增：

```text
2-task-readings/<TASKxx>-final-literature-note.md
2-task-readings/<TASKxx>-verified-claims.md
logs/<TASKxx>-source-check-log.md
```

项目级资产结构已同步更新。

## Next Validation

后续可用 `$miy-uat` 做三类验证：

```text
black-box:
  用户要求最终可引用文献笔记时，是否自然路由到 paper-finalize。

gray-box:
  paper-finalize 是否保留 final-literature-note 模板。

source-check:
  表格数值未核验时是否保持 needs-source-check，避免伪可引用。
```
