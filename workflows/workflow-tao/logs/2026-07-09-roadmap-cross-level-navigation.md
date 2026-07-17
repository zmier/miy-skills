# 2026-07-09 roadmap cross-level navigation

## 来源

CASE-260521 基金经理研究在 TASK06 阶段暴露出一个可迁移问题：

```text
任务谱系图能说明文件结构，却不能说明研究或项目为什么这样推进。
```

在该案例中，TASK01-TASK06 的真实演进是：

```text
文献与候选路线 -> 支付宝分析数据层 -> research design v0 -> 外部数据 inventory -> 外部 panel -> 第一轮经验发现 -> 新 puzzle / 机制探索。
```

单纯的 task tree 无法清楚表达：

- 初始发现如何引出新的问题；
- 哪些任务是主线、诊断、机制、稳健性或归档；
- 哪些节点已验收、正在推进、规划中、阻塞或 superseded；
- 上层图如何跳转到下层 README / memo / results。

## 抽象决策

将 `workflow-research/skills/research-roadmap` 中的通用图谱能力抽出为：

```text
skills/roadmap/SKILL.md
```

通用 `$roadmap` 负责：

- Mermaid 折线、节点形状、状态 class、emoji 第二信号；
- `click` 链接和 fallback link table；
- Project Roadmap、Task Lineage Map、Project Change Map、Technical Route 的分工；
- workflow / project / route / task / subtask / communication 跨层级导航。

`research-roadmap` 改为研究语境子 Skill：

```text
先读取 `$roadmap`；
再补充 research question、initial fact、puzzle、mechanism、identification diagnosis、evidence convergence、paperization 等研究专属规则。
```

## 迁移边界

当前规则来自真实研究项目 forward-test，但仍是 seed：

```text
green = 能让项目入口图比目录树更清楚地表达主线和状态；
not green yet = 尚未在非研究项目、软件工程项目或课程项目中充分回归。
```

因此，`workflow-tao` 只提升元原则：

```text
graph-like / hybrid graph-of-trees workflow 应提供跨层级 roadmap / navigation map。
```

具体视觉语法交给 `$roadmap` 维护，不在每个 workflow 中复制。
