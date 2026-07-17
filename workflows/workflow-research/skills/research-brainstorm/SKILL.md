---
name: research-brainstorm
description: 学术研究项目的 seminar-style 多视角脑暴 Skill。用于当一个研究项目已经有初始经验事实、核心谜题、候选机制、替代解释或 route 选择困境，需要组织多个学术视角/subagent 进行独立发散、共享黑板、交叉批评、回应修正和主席合成；适用于机制探索、假说生成、异质性/稳健性路线筛选、coauthor 讨论前准备、以及将脑暴结果沉淀为可检验 research route menu。
---

# Research Brainstorm

状态：`seed / source-case structural-green / forward-test-pending`

## 定位

`research-brainstorm` 把“随口脑暴”改造成可审计、可复用的研究 seminar。

它回答：

```text
当一个研究发现引出很多可能解释时，如何让多个学术视角真正相互交流，而不是各写各的报告？
```

核心原则：

```text
先发散，再互评；
先形成 possibility pool，再排序；
先明确可检验路线，再进入数据或因果表述。
```

本 Skill 适合 `workflow-research` 中的 R1/R4/R5 面板：研究问题、机制/实验设计、论证链和 paper route 选择。

`research-brainstorm` 负责生成、批评和仲裁路线；`research-zhihu-post` 负责把当前研究状态解释给陌生同行并暴露叙事断点。若已有最新知乎同行稿，可把它作为 Round 0 的可读背景，但仍须回查 evidence owner；若知乎稿暴露出新的具体困惑，可将其列入 seminar brief。Brainstorm 完成后，只把开放问题、路线处置和下一 Gate 回流给知乎稿，不把 Brainstorm 目录改造成持续更新的对外文章。

## 输入条件

启动前尽量准备：

- 一个待解释的经验事实、研究谜题或候选 claim；
- 当前已知数据、样本、变量和识别边界；
- 相关文献线索或至少一份文献扫描计划；
- 当前项目的 task / node / route 入口；
- 最新 `research-zhihu-post` outside-view audit 或同行稿（若有）；
- 明确说明本轮是脑暴，不是最终结论。

若输入不足，先写 `seminar brief`，把“已知 / 未知 / 不可声称”列清楚，再启动多视角讨论。

## 角色配置

默认角色：

| Role | 作用 |
|---|---|
| Chair / Synthesis Agent | 维护 brief、黑板、回合节奏、合成和下一步 gate |
| Domain Scholar | 从核心研究领域提出机制和文献锚点 |
| Adjacent Literature Scholar | 从相邻文献迁移理论和设计 |
| Data Generating Process Scholar | 质疑样本、平台、数据生成和 measurement |
| Identification Skeptic | 识别威胁、替代解释、反事实和 falsification |
| Practitioner / Institutional Expert | 补充真实制度、业务流程和操作约束 |

按项目替换角色。不要为“好听”增加角色；每个角色必须有不同的信息优势或批评函数。

## Round Protocol

### Round 0：共同 brief

Chair 写一份共同 brief：

```text
研究谜题
已知事实
数据与样本边界
禁止过度声称
本轮产出格式
```

必要时读取 `references/templates.md` 中的 `seminar-brief-template`。若本轮目标是从竞争路线中升格下一项实证任务，还要读取父 workflow 的 [`evidence-gated-route-adjudication`](../../references/evidence-gated-route-adjudication.md)。

### Round 1：独立发散

每个角色独立提出 3-7 个候选机制或解释，必须包含：

- 机制直觉；
- 与经验事实的连接；
- 文献锚点或可搜索关键词；
- 可观察 proxy；
- 关键反事实预测；
- 主要威胁；
- 下一步检验建议。

### Round 2：共享黑板

Chair 合并所有候选到 blackboard。每条候选至少有稳定 ID：

```text
M01, M02, ...
```

不要在这一轮删掉“看起来怪”的机制；只标记低可信、重复或数据缺口。

### Round 3：交叉批评

每个角色至少批评 2-3 条非自己提出的机制：

- 是否能解释目标现象；
- 是否和已有事实矛盾；
- 是否只是选择偏误、测量误差或样本口径；
- 需要什么数据才能区分；
- 哪个结果会推翻它。

### Round 4：回应修正

原提案者必须回应批评：

```text
保留 / 合并 / 降级 / 放弃 / 转为识别威胁 / 转为异质性路线
```

禁止把所有批评都写成“未来研究”。如果不能形成可检验预测，应降级。

### Round 5：Chair 合成与 route gate

Chair 产出：

- `raw possibility pool`：保留所有合理候选；
- `mechanism route menu`：按解释力、文献支撑、数据可检验性、贡献潜力排序；
- `threat register`：把机制、替代解释和识别威胁分开；
- `next gate`：建议进入 1-3 条路线，说明先做文献、数据、回归、文本标注还是 coauthor 讨论。

Chair 还必须给每条 stable ID 一个最终处置：

```text
promote-now / queue-data / theory-boundary /
diagnostic-only / merge / archive
```

默认只保留一条 `promote-now`。它应是能用一个正/负/混合结果重排至少两个竞争 DGP 的 high-information Gate，而不是“最容易显著”的规格。升格前必须写 `promotion contract`：经济对象、主样本、唯一 Gate、falsifier、pass/mixed/fail 后果、禁止追加规格、claim ceiling 和独立审计触发条件。

Seminar 到此结束。升格后的新数据构造、模型和结果由新的 evidence-owning TASK / subtask 负责；Brainstorm 目录不吸收下游实证结果。

## 推荐文件结构

在 task-driven 项目中，建议把一次脑暴作为 subtask 管理：

```text
TASKxx-parent/
└── subtasks/
    └── TASKxx-y-research-seminar-brainstorming/
        ├── README.md
        ├── TASKxx-y-说明.md
        ├── outputs/
        │   ├── seminar-brief.md
        │   ├── brainstorming-blackboard.md
        │   ├── raw-possibility-pool.md
        │   ├── mechanism-route-menu-after-seminar.md
        │   ├── chair-final-adjudication.md
        │   ├── promotion-contract.md
        │   └── seminar-next-gate.md
        ├── agents/
        │   └── <role>/
        │       ├── round1.md
        │       ├── round2-critique.md
        │       └── round3-response.md
        └── logs/
            └── log.md
```

若只是准备协议而不运行讨论，可使用 `TASKxx-y-0-*protocol`；真正运行讨论使用 `TASKxx-y-1-*brainstorming`。

## 输出契约

每次使用本 Skill，至少交付：

| Artifact | 内容 |
|---|---|
| `seminar-brief.md` | 共同输入、边界、禁止声称 |
| `brainstorming-blackboard.md` | 所有候选机制、提出者、状态 |
| `cross-critique` | 每个角色对其他机制的批评 |
| `raw-possibility-pool.md` | 未过早筛掉的可能性池 |
| `route-menu-after-seminar.md` | 排序后的路线菜单 |
| `chair-final-adjudication.md` | 每条 stable ID 的 promote/queue/boundary/merge/archive 决定 |
| `promotion-contract.md` | 唯一 high-information Gate、冻结边界与停止规则 |
| `next-gate.md` | 下一步 1-3 条优先路线和所需证据 |

需要具体模板时，读取：

```text
references/templates.md
```

## 管理规则

- 把“机制候选”“识别威胁”“样本诊断”“异质性路线”分开。
- 不把脑暴结果写成因果结论。
- 不让 subagent 修改父任务 README、log、email 或共享数据，除非明确授权。
- subagent 只写自己的 `agents/<role>/` 和本轮指定输出。
- Chair 负责合成，不负责压制少数但可检验的观点。
- 保留被降级路线，标注原因；不要静默删除。
- 若本轮发现需要新数据，写成 data request 或 next gate，不直接改数据口径。
- 不因某条路线拥有更多显著候选规格而优先升格；优先比较 falsifiability 和 information gain。
- `queue-data` 与 `theory-boundary` 必须分开：前者等待可命名输入，后者当前缺少必要行为角色或路径，不能靠制造 proxy 解决。

## 质量检查

交付前检查：

- 是否能一眼看出“初始事实 -> 核心谜题 -> 候选机制 -> 批评 -> 修正 -> 下一步”；
- 每个机制是否至少有一个可观察 proxy 或明确数据缺口；
- 是否存在反事实预测，而不是只有故事；
- 识别威胁是否单独列出；
- 是否避免过度因果语言；
- 是否给出下一步优先级，而不是无限扩散；
- 是否每条 stable ID 都有最终处置，且只有少量路线取得 `promote-now`；
- 是否已为 `promote-now` 写明唯一 Gate、停止规则和禁止事后扩张的规格；
- 文件是否能被父 TASK / Research Roadmap 点击进入。

## 来源模式

本 Skill 抽自 CASE-260521 基金经理研究的 TASK07-1-0：

```text
tasks/TASK07-gross-trading-mechanism-exploration/
subtasks/TASK07-1-mechanism-route-scoping/
subtasks/TASK07-1-0-research-seminar-brainstorming-protocol/
```

方法借鉴了 War Room、AgentCouncil 和 Multi-Agent Brainstorming 的 shared filesystem、council、review loop 和 synthesis 思路，但本 Skill 已改写为学术研究场景，不安装或依赖第三方 skill。
