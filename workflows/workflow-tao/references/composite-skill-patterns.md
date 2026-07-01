---
date: 2026-06-20
type: reference
status: structural-green
scope:
  - workflow-tao
---

# Composite Skill Patterns

## 定位

本文件沉淀复合 Skill 的结构类型。它来自 `workflow-argument-validity` 中两类能力的对比：

```text
argument-tree-extraction：抽树
academic-argument-arrow-audit：验箭头
```

两者都是复合 Skill，但子 Skill 拆法不同。原因不是风格问题，而是复杂性来源不同。

## 类型一：工序型复合 Skill

工序型复合 Skill 的复杂性来自一串稳定工作步骤。每一步都有相对独立的输入、输出、完成标准和 QC。

适用信号：

- 任务天然有稳定顺序；
- 上一步产物是下一步输入；
- 每一步都有明确中间物；
- 失败通常发生在某个工序质量不达标；
- 回归测试可以逐步定位是哪一步退化。

典型结构：

```text
父 Skill：定义总目标、主轴、输入输出契约、QC 和路由
子 Skill A：步骤 1
子 Skill B：步骤 2
子 Skill C：步骤 3
...
```

示例：

```text
paper 抽树：
定边界 -> 抽 claim -> 下钻 evidence -> 建 edge -> 画 Mermaid -> QC
```

这类能力适合按主轴步骤拆子 Skill，因为每一步本身就是一个可复用动作。

## 类型二：诊断路由型复合 Skill

诊断路由型复合 Skill 的主轴动作相对稳定，但某一步需要根据对象类型、风险类型、知识域或工具需求分诊。

适用信号：

- 核心动作可以用一句话概括；
- 大多数步骤由父 Skill 就能承载；
- 真正复杂的是“这类对象该用哪套专门知识验”；
- 子 Skill 不是工作流步骤本身，而是被路由出来的专科诊断模块；
- 子 Skill 通常承接“路由 + 具体执行”两个相邻环节。

典型结构：

```text
父 Skill：
  1. 固定对象
  2. 改写 / 标准化对象
  3. 判断类型
  4. 路由到专门验法
  5. 汇总诊断

子 Skill：
  - 类型 A 的专门验法
  - 类型 B 的专门验法
  - 类型 C 的专门验法
```

示例：

```text
学术验箭头：
固定 A -> B
判断 A 能否推出 B
按 arrow_type 路由到：
  文献 gap 审计
  因果识别 / DAG 审计
  统计结果审计
```

这里子 Skill 看起来都挂在“路由审查方法”下面，但它们并不只是路由；它们会继续执行具体审计，并把结果回填父 Skill 的 ledger。

## 类型三：混合型 workflow / 复合 Skill

大型 workflow 往往不是纯工序型或纯诊断路由型，而是混合形态。

最常见结构是：

```text
顶层诊断路由
-> 进入某条路线
-> 路线内部按工序推进
```

适用信号：

- 顶层有多条路线或策略梯度；
- 不同路线依赖不同工具、环境、权限或外部状态；
- 一旦选定路线，内部又需要稳定 pipeline；
- 红灯经常要求从当前工序退回顶层重新选路线；
- 同一项目可能在多条路线之间切换，但每条路线内部仍有严格 Green 标准。

示例：

```text
Android 逆向请求复现：
顶层按 A0/A1/A2/A3/A4/A5 路线分诊；
每条路线内部再按抓包、定位、hook、trace、replay、oracle、证据台账等工序推进。
```

因此 `workflow-android-reverse` 更适合归类为：

```text
顶层诊断路由型 workflow
+ 子路线工序型 pipeline
```

这类 workflow 的父入口要特别写清：

- 顶层路线梯度；
- 每条路线的 Green；
- 何时不能把 A4 写成 A1 成功；
- 何时因账号态、设备态、签名态、服务端窗口或授权边界退回重路由；
- 个案证据留在 TASK，通用路线规则进入 workflow。

## 执行模式与完成深度

除了“按步骤拆”和“按类型路由”，复杂 workflow 还常出现第三个维度：同一主轴在不同场景下执行深度不同。

这不是新的 workflow 类型，而是父入口必须声明的 mode-aware completion standard。

典型结构：

```text
mode: diagnose-only
  跑诊断、列请求、产出 pending ledger；
  不执行外部工具、不做最终定性。

mode: full-execution
  跑完整主轴；
  调用外部工具；
  回填 ledger；
  输出可交付结论。
```

判断规则：

```text
同一主轴、同一对象、只是执行深度不同 -> 用 mode；
目标、输入、产物和 Green 标准根本不同 -> 考虑拆子 workflow / 子 Skill。
```

例如：

```text
学术验箭头：
  internal-blind-audit = 内部验箭头 + 外部证据请求 pending；
  full-evidence-audit = 内部验箭头 + 集中文献/方法检索 + 回填判断。

逆向工程：
  diagnose-only = 定位路线、列证据缺口；
  full-reproduction = 跑 hook / trace / replay / oracle 并形成复现证据。
```

mode 不应藏在正文深处。父入口 `SKILL.md` 头部应直接写明可用 mode、默认 mode、切换条件、允许调用的工具、每种 mode 的完成标准和禁止事项。

## 如何选择

先问第一个问题：

```text
复杂性主要来自流程步骤很多，还是来自对象类型很多？
```

若答案是“流程步骤很多”，优先使用工序型。

若答案是“主轴很短，但不同对象需要不同知识”，优先使用诊断路由型。

若两者都强，可以混合：

```text
workflow 或父 Skill 先按工序拆主轴；
某个工序内部再使用诊断路由型子 Skill。
```

或者反过来：

```text
workflow 顶层先按路线诊断路由；
每条路线内部再使用工序型 pipeline。
```

例如：

```text
学术论文 workflow：
抽树 -> 验箭头 -> 选点 -> 行文

其中：
抽树 = 工序型复合 Skill
验箭头 = 诊断路由型复合 Skill
```

```text
Android reverse workflow：
Android Route Ladder = 顶层诊断路由
具体路线内的抓包 / hook / trace / replay / oracle = 工序型 pipeline
```

## 设计纪律

- 不要机械地把所有子 Skill 都按步骤拆；
- 不要机械地把所有子 Skill 都按类型拆；
- 父 Skill 必须说明子 Skill 是“步骤承载”还是“专科诊断”；
- 混合型 workflow 必须说明哪一层是路线分诊，哪一层是工序推进；
- 如果同一主轴有多种执行深度，父入口必须声明 mode，不要让执行者猜完成标准；
- 混合型 workflow 必须定义路线切换和降级条件，避免把低路线 Green 误写成高路线 Green；
- 诊断路由型子 Skill 的输出必须回填统一 ledger，避免各写各的；
- 工序型子 Skill 的输出必须能被下一步直接消费；
- 子 Skill 边界应来自实际失败模式、复用需求或工具需求，而不是目录美观。

## 反哺来源

本规则来自一次对话洞见：

```text
抽树是工序型复合 Skill；
验箭头是诊断路由型复合 Skill。
Android reverse 是顶层诊断路由型 + 子路线工序型的混合 workflow。
```

该洞见来自学术论文论证树与验箭头 Skill 设计过程。它应继续通过新 workflow / Skill 的实践回归校准。
