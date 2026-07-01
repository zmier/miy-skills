# Conceptual / Review Paper Adapter

用于综述、概念文章、框架文章、分类法文章和理论整合型文章。

## 节点命名

建议使用：

```text
G* = X1 支撑节点
C* = X2 概念/框架支撑节点
E-* = 文献、概念定义、分类依据、整合步骤或例证
```

## X2 最小展开

| 节点 | 问题 |
|---|---|
| C1 概念边界清楚 | 核心概念与相邻概念如何区分 |
| C2 文献谱系完整 | 关键文献流派是否覆盖 |
| C3 分类维度有效 | 分类依据是否互斥、穷尽、有解释力 |
| C4 整合逻辑成立 | 作者如何从文献推出框架 |
| C5 框架能解释现象 | 框架是否比既有框架更能解释问题 |
| C6 研究议程合理 | future research 是否来自前文缺口 |
| C7 贡献上升成立 | 概念贡献是否不同于重新命名或普通综述 |

## Evidence Ledger 要求

底层证据可包括：

```text
seminal citation
stream summary
definition quote
taxonomy dimension
comparison table
case example
research agenda item
```

文献链接要说明该文献支撑：

```text
gap
definition
mechanism
taxonomy
boundary
future research
```

## QC 标记

- `needs-literature-qc`：文献覆盖可能不足；
- `concept-boundary-unclear`：概念边界不清；
- `taxonomy-overlap`：分类维度交叉；
- `old-wine-new-bottle-risk`：可能只是改名或包装。
