# miy-skills / skills 目录说明

这个目录用于存放本地可复用的研究、写作、数据、展示和自动化 Skills。不同子目录的形态并不完全一致：有些是可直接被 Codex/Claude 识别的单一 Skill，有些是 Claude Code 项目脚手架，有些是工具包或领域工作流模板。

本文档先记录当前重点比较的两个经济学写作相关 Skill：

- [`econ-writing-skill`](./econ-writing-skill)：经济学论文写作规则 Skill。
- [`clo-author`](./clo-author)：经验经济学研究项目脚手架/多 agent 工作流系统。

## 快速判断

一句话区分：

- **`econ-writing-skill` 像一位“经济学论文写作教练”。**
  它关注一句话、一个段落、一节论文应该怎么写，尤其擅长把经济学论文写得具体、清楚、有识别、有结果。

- **`clo-author` 像一个“经验研究项目操作系统”。**
  它不只是写论文，而是把研究项目拆成 discovery、strategy、analysis、writing、review、submission，并用 worker-critic 成对机制和质量门槛治理整个流程。

如果目标是**打磨中文/英文论文文本**，优先使用 `econ-writing-skill`。  
如果目标是**从零组织一个经验经济学项目，包含文献、数据、代码、论文、审稿、投稿和复制包**，优先考虑 `clo-author`。

## 两者对比

| 维度 | `clo-author` | `econ-writing-skill` |
|---|---|---|
| 定位 | 经验经济学研究项目脚手架/生产线 | 经济学论文写作规则 Skill |
| 核心对象 | 整个研究项目：文献、数据、策略、分析、写作、审稿、投稿 | 论文文本：摘要、引言、结果、结论、识别策略、审稿回复 |
| 架构 | 多 agents + rules + hooks + project folders + slash commands | 单一主 Skill + 识别策略/LaTeX/审稿清单 |
| 平台 | 明确面向 Claude Code，主要在 `.claude/` 下 | 同时有 `.agents/` 和 `.claude/`，更容易适配 Codex |
| 工作方式 | `/discover → /strategize → /analyze → /write → /review → /submit` 流水线 | `/econ-write` 针对具体写作、改写、审稿任务 |
| 强项 | 项目治理、质量门槛、多 agent 审查、投稿流程、复制包 | 经济学写作规范、引言公式、结果表达、识别策略写法 |
| 粒度 | 工程化、流程化、项目级 | 文本级、章节级、写作规则级 |
| 风险 | 系统重，迁移到 Codex 需要改造；依赖 Claude Code 约定 | 功能窄一些，但可直接作为写作增强 Skill 使用 |

## `econ-writing-skill`

路径：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/econ-writing-skill
```

### 主要用途

用于经济学论文写作、改写和审稿，包括：

- 摘要、引言、结果、结论写作；
- 文献综述组织；
- 识别策略表述；
- 结果经济含义解释；
- 论文全文审计；
- 审稿回复；
- 政策简报与非学术写作；
- LaTeX、复制包、投稿前检查。

### 结构特点

关键文件：

```text
econ-writing-skill/
├── README.md
├── README.zh.md
├── .agents/skills/econ-write/
│   ├── SKILL.md
│   ├── identification-strategies.md
│   ├── latex-tips.md
│   └── review-checklist.md
├── .claude/skills/econ-write/
│   ├── SKILL.md
│   ├── identification-strategies.md
│   ├── latex-tips.md
│   └── review-checklist.md
├── examples/before-after.md
├── evals/test-cases.md
└── sources/SOURCES_RANKED.md
```

其中 `.agents/skills/econ-write/` 是适配 Codex/Agent Skills 的版本，`.claude/skills/econ-write/` 是适配 Claude Code 的版本。

### 当前 Codex 安装状态

已将 Codex 适配版软链到：

```text
/Users/narra/.codex/skills/econ-write
```

指向：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/econ-writing-skill/.agents/skills/econ-write
```

新开 Codex 会话后，理论上可被识别为 `econ-write` Skill。

### 推荐使用方式

适合直接用于已有论文材料：

```text
请使用 econ-writing-skill 检查这篇论文的标题、摘要、引言和结论是否形成闭环。
```

```text
请基于 econ-writing-skill 的 review-checklist，对全文做 deep review：
Methodologist、Field Expert、Writing Critic 三个视角分别给意见。
```

```text
请使用 econ-writing-skill 改写这段结果部分：
主结果前置，给出经济意义，不要只说显著。
```

## `clo-author`

路径：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/clo-author
```

### 主要用途

用于搭建和管理经验经济学研究项目，从研究想法到投稿流程。它提供：

- 项目目录结构；
- Claude Code 配置；
- 多 agent 工作流；
- discovery / strategy / analysis / writing / review / submission 流水线；
- worker-critic 成对审查机制；
- 质量门槛；
- 期刊画像；
- 复制包和投稿准备；
- Beamer / Quarto 展示支持。

### 结构特点

关键目录：

```text
clo-author/
├── README.md
├── README.zh.md
├── CLAUDE.md
├── .claude/
│   ├── agents/
│   ├── skills/
│   ├── rules/
│   ├── references/
│   └── hooks/
├── paper/
├── data/
├── scripts/
├── quality_reports/
├── explorations/
├── templates/
└── master_supporting_docs/
```

其中 `.claude/skills/` 下包含多个命令型 Skill：

- `/new-project`
- `/discover`
- `/strategize`
- `/analyze`
- `/write`
- `/review`
- `/revise`
- `/talk`
- `/submit`
- `/tools`
- `/checkpoint`

这些命令构成一套完整研究生产线。

### 与 Codex 的适配判断

`clo-author` 当前主要是 Claude Code 架构，只有 `.claude/skills/...`，没有像 `econ-writing-skill` 那样现成的 `.agents/skills/...` 目录。

因此，不能简单认为“软链到 `~/.codex/skills` 就能完整安装”。它依赖：

- Claude Code 的 slash command 习惯；
- `.claude/agents/` 的 agent 编排；
- `.claude/rules/` 的路径规则；
- `.claude/hooks/` 的钩子；
- 项目级 `CLAUDE.md`；
- `paper/`、`quality_reports/` 等固定项目结构。

如果要让 Codex 使用它，建议不是直接照搬，而是做一层适配：

1. 抽取其中最有价值的单项能力，例如 `review`、`write`、`strategize`；
2. 为 Codex 创建 `.agents/skills/clo-author-*` 或若干独立 Skill；
3. 将 Claude 专属的 agent 编排改写成 Codex 可执行的本地规则和工作流；
4. 保留项目目录模板，但不要依赖 Claude Code hooks；
5. 先适配一个最小可用版本，例如 `clo-review` 或 `clo-project-scaffold`。

## 两者如何配合使用

一个实用搭配方式：

1. 用 `clo-author` 管项目生命周期：
   - 新建项目；
   - 做文献综述；
   - 设计识别策略；
   - 组织分析代码；
   - 生成论文结构；
   - 做投稿与复制包检查。

2. 用 `econ-writing-skill` 精修论文表达：
   - 标题；
   - 摘要；
   - 引言；
   - 理论机制；
   - 结果段落；
   - 结论；
   - 全文写作审计。

如果把论文研究比作生产系统：

- `clo-author` 负责“工厂和流水线”；
- `econ-writing-skill` 负责“论文文本的工艺标准”。

## 当前维护建议

- 若只是日常中文论文返修、引言打磨、全文审查，优先使用 `econ-writing-skill`。
- 若要新建一个完整英文经验经济学项目，可以研究 `clo-author` 的项目模板。
- 若要把 `clo-author` 纳入 Codex，建议先做小范围适配，不要整套搬运。
- 每个新引入的 Skill，建议都补充：
  - `README.zh.md`
  - 目录结构说明
  - 与现有 Skills 的关系
  - Codex/Claude 适配状态
  - 推荐使用场景

