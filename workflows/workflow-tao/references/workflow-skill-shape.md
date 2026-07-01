---
date: 2026-06-19
type: reference
status: structural-green
scope:
  - workflow-tao
---

# Workflow 型 Skill 应该长什么样

## 一句话

workflow 的载体其实是 Skill。它不是 Codex 之外的新文件格式，而是一类更复杂的复合 Skill：

```text
普通 Skill = 一个相对聚焦的可调用能力
复合 Skill = 一个父入口 + 内部子 Skills + routing/reference/template 的中型能力系统
workflow 型 Skill = 一个带总编排、子能力、证据边界、模板、回归和迁移状态的能力工程系统
```

因此工程上采用：

```text
目录名：workflow-xxxx
入口文件：SKILL.md
```

但这不是说所有父子结构都必须命名为 `workflow-xxxx`。如果一个能力仍是局部能力，只是内部需要多个子 Skill，也可以保留普通 Skill 名称，并采用相同的父子组织：

```text
skill-name/
├── SKILL.md
├── skills/
│   ├── child-skill-a/
│   │   └── SKILL.md
│   └── child-skill-b/
│       └── SKILL.md
├── references/
├── assets/ 或 templates/
└── tests/
```

判断重点不是名字，而是职责：

```text
父入口负责抽象协议、路由、完成标准和子 Skill 调度；
子 Skill 负责具体场景、文本类型、平台或交付形态；
reference/template/test 负责稳定知识、复用结构和回归验证。
```

复合 Skill 不只有一种拆法。设计内部 `skills/` 前，先判断复杂性主要来自“工序链条”还是“诊断分流”：

```text
工序型复合 Skill：按主轴步骤拆，例如定边界、抽 claim、下钻 evidence、建 edge、画 Mermaid、QC。
诊断路由型复合 Skill：主轴动作稳定，但第 N 步需要按对象类型、风险类型或知识域分诊，例如验箭头时按文献 gap、因果识别、统计结果等路由。
混合型 workflow：顶层按路线、红灯、环境状态或策略梯度分诊，子路线内部再按工序推进，例如 Android reverse 先选 A0-A5 路线，再在路线内抓包、hook、trace、replay、oracle。
```

详见 `composite-skill-patterns.md`。

## 什么时候需要 workflow 型 Skill

出现以下信号时，不宜只做单个 Skill：

- 任务需要总编排来路由多个子能力；
- 同一目标存在多条路线、分支、红灯和回退策略；
- 需要区分通用能力与个案证据；
- 需要证据台账、Mermaid 树、模板、状态机或测试；
- 正向构造和逆向验收共享同一质量标准；
- 需要父 workflow 抽象多个平台、文本类型或子领域。

如果只出现“一个父能力需要路由少数几个子能力”，但暂时不需要 project/TASK、provenance、复杂状态机或跨案例迁移评测，可以先做复合 Skill，而不是立即升级为 workflow 型 Skill。

## 推荐结构

大型 workflow 型 Skill 推荐：

```text
workflow-xxxx/
├── SKILL.md
├── skills/
│   └── xxxx-orchestrator/
│       └── SKILL.md
├── references/
│   ├── routing.md
│   ├── red-light-or-break-taxonomy.md
│   ├── core-loop.md
│   └── source-provenance.md
├── templates/ 或 assets/
│   ├── ledger-template.md
│   └── mermaid-tree-template.md
├── logs/
│   └── YYYY-MM-DD-主题.md
├── subworkflows/
│   ├── workflow-subdomain-a/
│   │   └── SKILL.md
│   └── workflow-subdomain-b/
│       └── SKILL.md
├── projects/
│   └── CASE-.../
└── tests/
```

`logs/` 用于保存 workflow 构思过程，包括来源讨论、关键原文、方案分歧、抽象决策和迁移边界。稳定规则不应只埋在 logs 中；经过复核后应提升到 `references/`、`templates/` 或 `SKILL.md`。详细规范见 `workflow-conception-log-policy.md`。

中型复合 Skill 推荐：

```text
skill-name/
├── SKILL.md
├── skills/
│   ├── skill-name-orchestrator/
│   │   └── SKILL.md
│   ├── child-skill-a/
│   │   └── SKILL.md
│   └── child-skill-b/
│       └── SKILL.md
├── references/
├── assets/ 或 templates/
└── tests/
```

## 父层应该放什么

父 workflow 只放跨场景稳定存在的能力：

- 目标定义与完成标准；
- 路由规则；
- 证据台账或节点台账；
- 红灯 / 断点分类；
- 核心循环；
- Mermaid 树或任务树；
- 输出阶梯；
- provenance；
- conception logs；
- structural-green / forward-test-green 状态。

父层不要写某个平台、某篇稿件、某个课程案例的固定细节。

同理，复合 Skill 的父入口也不应塞满各子场景细节；它应负责：

- 说明通用抽象；
- 判断输入类型；
- 路由到内部 `skills/` 下的子 Skill；
- 定义统一输出契约；
- 收敛子 Skill 结果。

## 子层应该放什么

子 workflow 负责具体领域实现：

- 平台专属工具链；
- 文本类型专属节点；
- 领域专属验收标准；
- 领域专属输出模板；
- 子领域的失败模式与回退路线。

原则：

```text
父 workflow 定义抽象协议；
子 workflow 实现领域协议。
```

对复合 Skill 也一样：

```text
父 Skill 定义抽象协议并路由；
子 Skill 实现具体协议。
```

## Orchestrator 应该写什么

`skills/*-orchestrator/SKILL.md` 负责真正执行编排：

1. 判断任务类型或目标形态；
2. 建立证据 / 节点台账；
3. 读取 routing reference；
4. 读取 red-light / break taxonomy；
5. 选择子 workflow 或父级模板；
6. 产出可复核中间物；
7. 回收发现到 TASK / reference / template / Skill；
8. 标注迁移状态。

## 从 Reverse Workflow 抽出的范式

成熟样本 `workflow-reverse-engineering` 暴露出一组通用形态：

| Reverse 范式 | 通用化后 | 论证树类比 |
|---|---|---|
| platform-routing | 场景 / 类型路由 | 论效题、审稿、写作自审路由 |
| red-light-taxonomy | 失败 / 断点分类 | 箭头断点分类 |
| evidence-ledger | 证据台账 | 论证节点证据台账 |
| mermaid-evidence-tree | 可视任务树 | Mermaid 论证树 |
| static-dynamic-loop | 交叉校正循环 | 抽树-验箭头-回原文校正 |
| reproduction-ladder | 交付阶梯 | 图、表、段落、完整报告 |
| subworkflows | 平台实现 | 文本类型 / 领域实现 |

更多可参考样本见 `reference-workflow-cases.md`。该索引只提供链接，不复制样本内容。

## 完成标准

一个 workflow 型 Skill 至少满足：

- 根目录有 `SKILL.md`；
- 名称为 `workflow-xxxx`；
- `SKILL.md` 说明它是复合 workflow 型 Skill；
- 有 orchestrator 或明确说明为什么暂不需要；
- 有 routing / taxonomy / ledger / template 中至少两类结构；
- 重大创建或升级有 `logs/YYYY-MM-DD-主题.md` 构思记录；
- 有 case / TASK / provenance 边界；
- 有 structural-green 与 forward-test 状态；
- 若软链到 `~/.codex/skills`，路径和名称一致。
