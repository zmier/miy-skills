---
date: 2026-07-05
type: reference
status: draft
scope:
  - workflow-tao
source_log: ../logs/2026-07-05-workflow拓扑-树形与图型.md
source_log_update: ../logs/2026-07-08-graph-workflow-node-task-contract.md
source_case:
  - workflow-research
  - CASE-260521-基金经理研究
migration: raw-insight -> draft-rule
---

# Workflow Topologies

## 定位

本文件补充 `workflow-tao` 对 workflow 形态的判断。

`composite-skill-patterns.md` 主要回答：

```text
复杂性来自工序步骤、诊断路由，还是二者混合？
```

本文件回答另一个问题：

```text
这个 workflow 的顶层结构更像树，还是图？
```

两者不是替代关系：

```text
composite pattern = 编排方式；
topology = 顶层结构形态。
```

同一个 workflow 可能同时是：

```text
诊断路由型 + tree-like；
工序型 + tree-like；
graph-like + 节点内部工序型；
graph-like + 节点内部仍然 graph-like。
```

## 为什么需要拓扑判断

一些 workflow 有清楚主目标和主干，适合用阶段、工序、Red/Green、UAT 和交付标准管理。

另一些 workflow 只有大方向，主干会在多个候选路线、证据、数据、文献和外部偏好之间后验浮现。若用线性阶段或固定主干管理它们，会把探索性任务误工程化。

典型风险：

```text
把探索性学术研究误写成 R1 -> R2 -> R3 -> R4；
把多个候选 paper route 过早压成单一主线；
把尚未完成竞争的 route 当成失败路线删除；
把本应后验决定的主干提前固定。
```

## 类型一：Tree-like Workflow

tree-like workflow 的主干较早可见。

特征：

```text
总目标较清楚；
主干较早可见；
分支服务主干；
完成标准相对明确；
失败处理通常是回退、替代路线、红灯或兜底；
项目推进可以用阶段、工序、路线图描述。
```

典型例子：

```text
逆向工程数据采集：
抓接口
→ 分析参数
   → 静态分析
   → 动态分析
→ 写脚本
→ 工程交付
```

其他可能例子：

```text
格式转换 workflow；
论文返修 workflow；
代码修复 / CI 修复 workflow；
数据清洗和交付 workflow；
已确定目标的采集工程。
```

适合的管理方式：

```text
阶段 / 工序；
Red -> Green -> Refactor；
UAT / acceptance contract；
失败回退和路线降级；
稳定 TASK 树；
可复现命令和测试。
```

Green 标准通常是：

```text
某条主路线达到可交付状态；
关键工序全部通过；
失败分支已关闭或明确降级；
输出满足验收契约。
```

## 类型二：Graph-like Workflow

graph-like workflow 的主干不是一开始就知道，而是在探索中后验浮现。

特征：

```text
总方向大致存在，但主干不一定一开始就知道；
多个候选节点 / route / claim 并行生长；
节点之间会互相影响、合并、拆分、降级或重组；
完成标准是阶段性、竞争性、组合性的；
失败处理不只是回退，也可能是降级为机制、附录、弃用路线或另一项目；
最终主干往往是后验选择出来的。
```

典型例子：

```text
学术研究项目；
产品探索；
理论构建；
复杂战略规划；
多方向 paper 孵化项目。
```

以学术研究为例，图中节点可能包括：

```text
候选问题 A；
候选问题 B；
候选问题 C；
数据资产 D；
文献线索 E；
识别设计 F；
期刊偏好 G；
导师反馈 H；
初步结果 I。
```

节点之间互相改写：

```text
数据 D 改变问题 A；
文献 E 否定问题 B；
初步结果 I 让 C 变成主线；
期刊偏好 G 让 A 降级为机制；
导师反馈 H 把两个 route 合并；
识别设计 F 暴露新的数据需求。
```

适合的管理方式：

```text
route portfolio；
candidate claims；
route cards；
证据竞争；
阶段性复盘；
合并 / 拆分 / 降级 / 弃用 ledger；
后验 paperization。
```

Green 标准通常不是“单一路径完成”，而是：

```text
当前 route portfolio 已被审计；
每条 route 的证据、缺口、风险和状态清楚；
优先路线、降级路线、待证路线和弃用路线有理由；
下一轮探索入口明确。
```

## 类型三：Hybrid Graph-of-Trees

一些 workflow 顶层是图，但每个节点内部又有树形执行。

结构：

```text
顶层：图
  多个 candidate routes / hypotheses / projects / claims 互相影响。

节点内部：树
  某条 route 内部可能有较清晰任务链：
  找文献 -> 找数据 -> 设计实验 -> 跑结果 -> 写解释。

节点内部也可能仍是图
  某条 route 内部继续分裂出多个子问题、子实验和候选解释。
```

这说明：

```text
不是所有 workflow 都是树；
也不是所有图型 workflow 都没有可执行主线；
图型 workflow 的局部节点可以调用树形子 workflow。
```

典型管理方式：

```text
顶层用 route portfolio；
route 内部用 task-driven / tree-like execution；
阶段复盘时重新评估 route 之间的关系；
不要把 route 内部 green 误判为整个项目 green。
```

## Graph-like Workflow 的 Node / Task 分层

graph-like / hybrid graph-of-trees 的关键风险，是把线性执行记录误读成研究图本身。推荐区分：

```text
nodes/ = 图层节点，管理长期存在的 route / claim / design / evidence state
tasks/ = 执行层任务，管理一段时间内线性推进的工作包
```

关系不是一对一，而是多对多：

```text
一个 Task 可以更新多个 Node；
一个 Node 可以被多个 Task 更新；
Task 的顺序不等于 Node 的重要性；
Node 的合并、拆分、降级或弃用应保留 provenance。
```

Task 应记录：

```text
目标与输入；
实际动作；
直接产物；
影响了哪些 nodes；
分别更新了每个 node 的哪类信息；
哪些观察只留在 task 内，哪些需要回挂到 node。
```

Node 应记录：

```text
当前状态；
当前 claim / route 直觉；
已明确的信息；
候选但未确认的信息；
未明确信息；
关联 tasks；
关联文献或证据；
数据需求；
候选设计；
识别威胁；
下一步问题。
```

这一分层不要求所有项目都建立 `nodes/`。只有当项目主干尚未固定、多个候选路线并行竞争，或一个执行任务会同时改变多个研究/产品/策略节点时，才需要显式引入 Node / Task 双层结构。

## 判定 Checklist

创建或重构 workflow 型 Skill 时，除判断它是工序型、诊断路由型还是混合型，还应问：

```text
1. 主目标是否前置清晰？
2. 主干是否一开始可见？
3. 分支是服务主干，还是候选主线？
4. 失败处理主要是回退，还是合并 / 拆分 / 降级 / 转化？
5. Green 是单一路径完成，还是 route portfolio 阶段性收敛？
6. 节点内部是否能用稳定工序推进？
7. 是否存在后验 paperization / productization / route selection？
8. 是否需要保留被放弃路线的证据，以免后来无法复盘？
```

判断建议：

```text
如果 1-3 多数为“是”，更接近 tree-like。
如果 3-5 多数指向“候选主线 / 合并拆分 / 阶段性收敛”，更接近 graph-like。
如果顶层 graph-like，但 route 内部有稳定任务链，归为 hybrid graph-of-trees。
```

## 对父入口 SKILL.md 的影响

workflow 父入口可以考虑声明：

```yaml
topology: tree-like
```

或：

```yaml
topology: graph-like
```

或：

```yaml
topology: hybrid graph-of-trees
```

若暂不写 YAML，也应在正文说明：

```text
主干是否前置清晰；
是否允许多个候选 route 并行；
完成标准是单路线交付，还是 route portfolio 收敛；
哪些规则不能过早稳定化。
```

## 与 Composite Skill Patterns 的关系

`composite-skill-patterns.md` 的三类：

```text
工序型复合 Skill；
诊断路由型复合 Skill；
混合型 workflow。
```

描述的是子能力如何拆分和编排。

本文件的三类：

```text
tree-like；
graph-like；
hybrid graph-of-trees。
```

描述的是 workflow 顶层路线如何生长。

两者组合示例：

| Topology | Composite Pattern | 例子 |
|---|---|---|
| tree-like | 工序型 | PDF 转 Markdown、格式交付、数据清洗 |
| tree-like | 诊断路由型 + 子路线工序型 | Android reverse route ladder |
| graph-like | 诊断 / portfolio 管理 | 学术选题孵化、多路线 paper 设计 |
| hybrid graph-of-trees | 顶层 route portfolio + route 内部 task-driven | 基金经理研究项目 |

## 当前样本

### Graph-like 样本

```text
workflow-research
CASE-260521-基金经理研究
```

相关日志：

```text
../logs/2026-07-05-workflow拓扑-树形与图型.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/logs/2026-07-05-从线性阶段到探索性论证树.md
```

### Tree-like 候选样本

待 forward-test：

```text
workflow-android-reverse 或其他逆向工程 workflow；
workflow-paper 的返修 / 格式交付支线；
workflow-md-to-word-formatting；
数据清洗和交付型项目。
```

## 提升条件

当前状态：`draft`。

提升到 `structural-green` 前，至少需要：

```text
1. 一个 graph-like case 完成 forward-test；
2. 一个 tree-like case 完成对照验证；
3. 至少一个 hybrid graph-of-trees case 证明“顶层图 + 节点内部树”的管理方式有效；
4. 父入口是否需要 topology 字段得到一次真实 workflow 重构验证；
5. Green 标准、logs、templates 与 regression test 如何随 topology 改变得到明确样本。
```

在达到这些条件前，不应把本文件当作稳定规则，只作为 workflow 创建 / 重构时的 draft 诊断层。
