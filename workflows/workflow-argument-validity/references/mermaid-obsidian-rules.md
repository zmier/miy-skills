---
date: 2026-06-19
type: reference
status: structural-green
scope:
  - workflow-argument-validity
---

# Mermaid / Obsidian 论证树规则

## 分工

```text
Mermaid = 让论证树可见
Obsidian = 让论证树可追溯、可积累、可复用
```

## 默认方向

默认使用 `flowchart BT` 表达支撑方向：

```text
底部：证据 / 论据 / 子支撑
中部：分论点 / 一级支撑
顶部：根结论
箭头：supports，下层支撑上层
```

不要默认使用 top-down 表达支撑方向。若临时使用 top-down，必须注明箭头表示 `requires / 展开`，不是 supports。

## 节点命名

- 节点 ID 使用稳定短 ID：`Y`, `X1`, `X2`, `G1`, `F1`。
- 节点 label 写人能读懂的判断句。
- Obsidian 场景可使用双链：

```mermaid
flowchart BT
    G1["[[gap 存在]]"] --> X1["[[X1-问题有意义]]"]
    F5["[[识别策略可信]]"] --> X2["[[X2-具体核心发现已被证明]]"]
    X1 --> Y["[[Y-贡献成立]]"]
    X2 --> Y
```

## 箭头标签

可用标签表达状态：

```mermaid
flowchart BT
    F5["识别策略"] -- "broken: 后门路径未关闭" --> X2["X2: 作者证明了具体核心发现"]
    G1["gap"] -- "weak: 与既有研究差异不足" --> X1["X1: 问题有意义"]
    X1 -- "partial" --> Y["Y: 贡献成立"]
    X2 -- "broken" --> Y
```

## 最小输出

每个 `argument-tree.md` 至少包含：

1. Mermaid 图；
2. 节点表；
3. 箭头审计表；
4. 断点摘要；
5. 对根结论影响。

## 可读性规则

- 不把所有细节塞进节点 label；
- 复杂证据放到节点表，不放图里；
- 同一层节点数量过多时拆成多个子图；
- 图用于看结构，表用于承载证据。
