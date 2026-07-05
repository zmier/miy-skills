# 2026-06-22 分形 Task-Driven Workflow 讨论记录

## 元信息

- 日期时间：2026-06-22 23:41 CST
- 主题：将 `task-driven-project-manager` 升级为分形 `workflow-task-driven` 的能力工程讨论
- 来源案例：`/Users/narra/Documents/alib/Writer/03 Projects/冒险者工会/PROJECT-小红书云手机自动发布`
- 触发场景：飞源信息客户的小红书云手机自动发布外包需求评估
- 记录目的：保留本次 workflow 抽象的原文脉络、概念演化和迁移边界

## 背景

本次讨论从一个外包客户需求开始。客户最初提到“小红书同行笔记数据采集和话题分析”，随后明确当前最紧急需求是“小红书笔记发布”，并希望基于摩云藤 Zeus 云手机和飞书/腾讯云文档入口实现发布自动化。

在使用 `task-driven-project-manager` 创建项目骨架后，用户进一步提出：这种“拿到需求、评估需求、到实际做不做”的前置阶段，是否需要一个更专用的 Skill 或 workflow。

## 关键原文记录

### 1. 用户提出是否需要更专用的 Skill

> OK，原始材料请落进去哦！此外，我们这种，拿到需求、评估需求、到实际做不做的，是不是应该有个更专用的SKILL啊？目前的通用「项目驱动SKILL」够用吗？我不知道我表达的是否清晰，请帮我总结下我的困惑

当时形成的初步判断：

> 现在的 `task-driven-project-manager` 很适合“需求已经决定要做了，然后把它工程化拆 TASK、建项目、做交付结构”。但你现在面对的是更前置的一层：客户刚来咨询，需求还混乱、优先级会变、风险不清楚、能不能接单也没判断。

### 2. 用户提出要和 workflow-tao 结合

> 所以但「目标驱动」的思路和哲学，应该还是OK的吧？只不过需要有个更完善的项目管理链路？比如：针对外包项目的、针对其他项目的（以后再细分，比如：学术研究/论文研究项目等，应该各有模板？我不知道我表达的是否清晰，请帮我总结下我的困惑）。而且我觉得应该思考下怎么可以和 workflow-tao 这个结合起来...

当时形成的总结：

> 目标驱动这个底层哲学是对的，但它现在只覆盖了“项目怎么做”，还没有完整覆盖“需求从哪里来、怎么判断值不值得做、怎么进入项目、不同项目类型怎么套不同模板”这一整条链路。

并提出链路：

```text
原始材料进入
-> 需求提炼
-> 风险与可行性评估
-> 接不接 / 怎么接 / 先验证什么
-> 选择项目类型模板
-> 创建 task-driven 项目
-> 执行、验收、复盘
-> 反哺 skill / workflow
```

### 3. 用户纠正：不是前半段用另一套方法，而是分形结构

用户选中文本并指出：

> 不是这样的。我觉得应该是个「分形结构」：几个阶段都应该是「task-driven」的。不过之前是一个task-driven（如何完成项目），现在应该在前面再加个「task-driven」（目标变成了评估要不要做）。但「目标驱动 / task-driven 仍然是核心哲学。它的价值是：任何复杂事情都不要散着做，而是围绕目标拆任务、留证据、设验收、复盘沉淀。」仍然是第一阶段的核心吧，只不过目标从：「完成这个项目」，变成了「收集梳理信息判断要不要做这个项目」？我不知道我表达的是否清晰，请帮我总结下我的困惑。

这是本次 workflow 升级的核心转折点。

当时形成的总结：

> 你的意思不是：
>
> `task-driven-project-manager` 只管后半段，前半段用另一套非 task-driven 方法。
>
> 而是：
>
> **task-driven 是一种分形结构。每一层、每一阶段都应该是 task-driven，只是“目标”不同。**

并形成分形结构：

```text
阶段 0：项目机会评估，也是 task-driven
目标：判断要不要做这个项目
TASK01 原始材料归档
TASK02 真实需求识别
TASK03 风险与可行性评估
TASK04 追问清单与客户确认
TASK05 PoC / 最小验证设计
TASK06 接单决策：接 / 不接 / 先验证 / 改范围

阶段 1：项目执行，也是 task-driven
目标：完成已确认的项目
TASK01 范围确认
TASK02 数据或接口准备
TASK03 原型实现
TASK04 测试验收
TASK05 交付复盘

阶段 2：能力沉淀，也是 task-driven
目标：把个案经验反哺成 skill / workflow
TASK01 复盘有效规则
TASK02 区分个案证据与通用方法
TASK03 更新模板或 skill
TASK04 回归测试
```

关键句：

> **我不是想在 task-driven 前面加一个别的东西，而是想让 task-driven 自己向前延展：从“项目执行方法”扩展成“机会评估、项目执行、交付复盘、能力沉淀”每一层都可递归使用的目标驱动工作法。**

### 4. 用户确认架构问题：workflow 还是 adaptor

用户继续追问：

> 非常对！！就是这个意思！！所以你是建议，把task-driven这个SKILL升级成个workflow吗？升级成个专用的workflow还是个通用的workflow？还是「通用workflow」配上「专用场景的adaptor」？我不知道我表达的是否清晰，请帮我总结下我的困惑

当时形成的建议：

> 我倾向于方案 C。
>
> 也就是：
>
> `workflow-task-driven = 通用分形目标驱动 workflow`
>
> `adaptor-outsourcing-project = 外包/客户需求/接单评估场景`
>
> `adaptor-academic-research-project = 学术研究/论文研究场景`
>
> `adaptor-software-project = 工具/系统开发场景`

核心判断：

> 你真正发现的“道”是通用的，不属于外包项目本身。

通用部分：

```text
目标定义
-> TASK 拆解
-> 证据归档
-> 验收标准
-> 阶段 gate
-> 复盘
-> 反哺 skill / workflow
```

专用 adaptor 负责不同场景的差异：

```text
外包项目：客户原始材料、真实需求识别、预算和报价边界、风险/合规/平台限制、接不接单。
学术研究：研究问题、文献证据、理论框架、数据可得性、识别策略、论文结构。
软件项目：用户故事、技术栈、架构边界、测试策略、部署、维护成本。
```

### 5. 用户确认使用方式

用户进一步确认：

> 哎！就是这个意思！那我们也可以直接用升级后的workflow-task-driven嘛对吧？效果和之前用 task-driven-project-manager差不多或者更好更通用？然后如果特别指明是「外包项目」的话，会先开一个「评估要不要做的task-driven-project」如果要做，再开一个「实际开发的task-driven-project」。类似这种思路？我不知道我表达的是否清晰，请帮我总结下我的困惑

当时形成的总结：

> 以后是不是可以默认调用升级后的 `workflow-task-driven`，而不是直接调用 `task-driven-project-manager`？

回答：

> 可以，而且更合理。
>
> 因为升级后的 `workflow-task-driven` 不是替代“任务驱动”，而是把它提升成总入口。它会根据场景决定当前应该创建哪一种 task-driven project。

外包项目生命周期：

```text
外包项目生命周期
├── PROJECT-A 机会评估
│   ├── 目标：判断要不要做
│   ├── TASK01 原始材料归档
│   ├── TASK02 真实需求识别
│   ├── TASK03 风险和可行性
│   ├── TASK04 客户追问
│   └── TASK05 接单决策
│
└── PROJECT-B 实际执行
    ├── 目标：完成已确认项目
    ├── TASK01 范围确认
    ├── TASK02 原型
    ├── TASK03 开发
    ├── TASK04 测试
    └── TASK05 交付
```

关键句：

> **每一阶段都不是散着做，而是一个独立的目标驱动项目。**

## 本次落地的 workflow 更新

本次将既有目录：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-task-driven-project
```

升级为兼容旧名称的分形 task-driven workflow，并在入口说明中声明别名：

```text
workflow-task-driven
```

新增或更新文件：

```text
SKILL.md
references/fractal-task-driven.md
references/stage-gates.md
references/project-type-adaptors.md
references/routing.md
references/core-loop.md
references/source-provenance.md
templates/opportunity-evaluation-project-template.md
skills/task-driven-project-orchestrator/SKILL.md
skills/outsourcing-project-adaptor/SKILL.md
logs/2026-06-22-分形task-driven-workflow讨论记录.md
```

## 当前稳定结论

1. `task-driven` 是分形工作哲学，不是单一项目执行工具。
2. “评估要不要做”本身就是一个 task-driven project。
3. `workflow-task-driven` 应作为总入口，负责目标阶段判断、场景 adaptor 选择和 Gate。
4. `task-driven-project-manager` 应保留为 scaffold 子能力。
5. 外包项目默认先走机会评估 project，通过 gate 后再进入执行 project。
6. 学术研究、论文研究、软件工具等未来应各自拥有 adaptor，而不是复制一堆互不相干的项目模板。

## 迁移边界

进入 workflow 的通用规则：

- 分形 task-driven；
- 阶段 gate；
- 机会评估型 project；
- 外包项目 adaptor；
- scaffold 子能力关系；
- provenance 和 forward-test 要求。

留在个案项目的内容：

- 飞源信息客户原始沟通全文；
- 小红书、摩云藤、飞书/腾讯文档的具体业务细节；
- 截图路径和客户材料；
- 具体报价和执行判断。

