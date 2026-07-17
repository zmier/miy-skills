# 2026-07-10：research-brainstorm 的三类外部参考借鉴记录

## 背景

`research-brainstorm` 抽自 CASE-260521 基金经理研究的 TASK07-1-0。

当时 TASK07 的核心研究谜题是：

```text
基金经理回答问题后，为什么申购和赎回同时显著放大，但净 flow 不显著？
```

用户提出：既然处在脑暴阶段，是否可以让几个 subagent 模拟不同学术专长，并且让它们之间真的相互交流，而不是各写各的平行报告。

因此我们先找了三类外部 multi-agent brainstorming / council / war-room 参考：

| Ref | 来源 | 本地参考 |
|---|---|---|
| War Room | `https://github.com/openclaw/skills/blob/main/skills/maxkle1nz/war-room/SKILL.md` | CASE-260521 `TASK07-1-0/references/github/war-room/SKILL.lobehub.md` |
| AgentCouncil | `https://github.com/Sentry01/AgentCouncil` | CASE-260521 `TASK07-1-0/references/github/agent-council/README.md` |
| Multi-Agent Brainstorming | `https://github.com/sickn33/antigravity-awesome-skills/blob/main/plugins/antigravity-awesome-skills-claude/skills/multi-agent-brainstorming/SKILL.md` | CASE-260521 `TASK07-1-0/references/github/multi-agent-brainstorming/SKILL.md` |

这些参考只作为方法学习材料，没有安装、执行或复制为本地规范。

## 总体抽象

三个参考各有优势：

```text
War Room = 强在共享文件系统、分轮推进、挑战与复盘。
AgentCouncil = 强在独立发散、互读改进、协作/对抗双模式、orchestrator synthesis。
Multi-Agent Brainstorming = 强在角色边界、review loop、decision log 和退出标准。
```

`research-brainstorm` 最终抽象为：

```text
学术 seminar-style 多视角脑暴
= 共同 brief
+ 独立发散
+ 共享黑板
+ 交叉批评
+ 回应修正
+ Chair 合成
+ route gate
```

它的目标不是让 agent 投票，也不是直接产出结论，而是把一个研究谜题背后的机制空间组织成可检验的 route menu。

## War Room：从工程攻坚改造成研究黑板

### 借鉴点

War Room 的核心价值是把多个 specialist agent 放进同一个协作空间，让它们分 wave 推进，并用共享文件、挑战记录和复盘来避免产物散乱。

迁移到 `research-brainstorm` 后，对应为：

| War Room 元素 | research-brainstorm 改造 |
|---|---|
| shared filesystem | `brainstorming-blackboard.md` + `agents/<role>/round*.md` |
| wave protocol | Round 0-5 |
| challenge log | Round 3 cross critique |
| post-mortem | Chair synthesis + next gate |
| specialist agents | 学术视角角色，而不是工程职能角色 |

### 没有照搬的部分

没有迁移：

- prove-it code spike；
- build / ship phase；
- INTERCEPTOR autonomy；
- 工程发布导向的 hard delivery rhythm。

原因是 `research-brainstorm` 面向学术机制探索，不是工程交付。研究脑暴需要保留不成熟但有解释力的 minority idea，不能过早用“能否立即实现”筛掉。

## AgentCouncil：从 council 互读改造成 seminar 互评

### 借鉴点

AgentCouncil 的价值在于：agent 不是只独立写答案，而是会读彼此产物，并进入 collaborative / adversarial 的二次加工，最后由 orchestrator synthesis。

迁移到 `research-brainstorm` 后，对应为：

| AgentCouncil 元素 | research-brainstorm 改造 |
|---|---|
| independent drafts | Round 1 independent divergence |
| agents read each other's work | Round 3 cross critique |
| collaborative mode | 回应修正、机制合并、route refinement |
| adversarial mode | identification skeptic / threat register |
| orchestrator synthesis | Chair / Synthesis Agent |
| complexity gate | next gate：决定是否进入文献、数据、回归或 coauthor 讨论 |

### 没有照搬的部分

没有迁移：

- 多模型 CLI 依赖；
- Copilot CLI 安装方式；
- 固定模型家族分配；
- 只用少数泛化角色。

原因是本项目的关键不是模型编排，而是研究视角编排。角色必须由研究问题决定，例如 fund flow、behavioral finance、communication/disclosure、platform/data generating process、identification skeptic、product/operations expert。

## Multi-Agent Brainstorming：从设计评审改造成机制空间发散

### 借鉴点

Multi-Agent Brainstorming 的价值在于把角色边界、review loop、decision log 和 exit criteria 写清楚。它提醒我们：多 agent 脑暴不能无限扩散，也不能让 objection 悬空。

迁移到 `research-brainstorm` 后，对应为：

| Multi-Agent Brainstorming 元素 | research-brainstorm 改造 |
|---|---|
| role boundary | 每个学术角色有明确视角和批评函数 |
| reviewer objections | 每个角色至少批评 2-3 条非自己提出的机制 |
| objections must be resolved | Round 4 response and revision |
| decision log | blackboard 中记录 merge / downgrade / archive |
| hard stop / exit criteria | Round 5 route gate |

### 没有照搬的部分

没有迁移：

- one designer + multiple reviewers 的结构；
- 过早围绕单一方案做评审；
- 把创造力集中到一个 designer 身上。

原因是 TASK07-1 当时处于机制空间探索早期。我们还不知道最有价值的机制路线是什么，因此需要先让多个学术视角独立发散，再进入 seminar-style 互评。

## 最终 Skill 设计映射

`research-brainstorm` 的 Round Protocol 来源如下：

| research-brainstorm round | 主要来源 | 设计意图 |
|---|---|---|
| Round 0 Common Brief | War Room + Multi-Agent Brainstorming | 先锁定问题、边界、禁止声称和输出格式 |
| Round 1 Independent Divergence | AgentCouncil + 研究 seminar 需要 | 避免被第一个方案锚定，先生成机制空间 |
| Round 2 Shared Blackboard | War Room | 把所有候选放进同一事实层，避免散乱报告 |
| Round 3 Cross Critique | AgentCouncil + Multi-Agent Brainstorming | 让 agent 互读、攻击、补强，而不是平行输出 |
| Round 4 Response and Revision | Multi-Agent Brainstorming | objection 必须被回应，机制必须修正、合并或降级 |
| Round 5 Chair Synthesis and Route Gate | AgentCouncil + War Room | 由 Chair 合成 possibility pool、route menu、threat register 和 next gate |

## 研究场景下的核心改写

外部参考大多偏工程或通用协作。`research-brainstorm` 做了四个研究化改写：

1. 角色按学术解释视角划分，而不是按工程职能或模型能力划分。
2. 输出目标是 `mechanism route menu`，不是产品方案、代码实现或多数票结论。
3. 批评必须落到文献、proxy、反事实预测、识别威胁和数据可检验性。
4. Chair 不投票、不宣布最终真相，只负责把机制、替代解释、样本诊断和异质性路线分开，并给出下一步 gate。

## 当前边界

`research-brainstorm` 当前状态仍是：

```text
seed / extracted-from-CASE-260521
```

它已经适合在 TASK07-1-1 中 forward-test，但还不应视为完全稳定的通用流程。后续需要观察：

- 多个学术角色是否真的给出不同机制；
- 交叉批评是否改变 route menu；
- Chair synthesis 是否能收敛出 1-3 条可执行路线；
- 输出是否能自然回写到 Research Roadmap、task-driven 项目结构和 coauthor 沟通中。

## 相关文件

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-brainstorm/SKILL.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-brainstorm/references/templates.md
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK07-gross-trading-mechanism-exploration/subtasks/TASK07-1-mechanism-route-scoping/subtasks/TASK07-1-0-research-seminar-brainstorming-protocol/outputs/reference-review-and-adaptation.md
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK07-gross-trading-mechanism-exploration/subtasks/TASK07-1-mechanism-route-scoping/subtasks/TASK07-1-0-research-seminar-brainstorming-protocol/references/source-provenance.md
```
