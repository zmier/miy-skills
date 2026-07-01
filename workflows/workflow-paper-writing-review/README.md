---
date: 2026-06-18
type: workflow
status: seed
---

# Paper Writing Review Workflow

这是一个论文写作 / 审稿 workflow，用于承载学术论文从正向构造到逆向验收的共享质量系统。

它不是单个 Skill。根目录负责组织 workflow 工程；可被 Codex 调用的执行单元放在 `skills/`；具体论文、审稿、返修项目的证据留在各自 project / TASK 中。

## 核心判断

```text
论文写作 = 正向构造贡献链
论文审稿 = 逆向验收贡献链
```

二者共享同一套质量系统：

```text
研究问题 -> 文献缺口 -> 理论机制 -> 识别/数据 -> 结果 -> 贡献叙事 -> 表达与引用
```

## 当前结构

```text
workflow-paper-writing-review/
├── README.md
├── SKILL.md
├── ROADMAP.md
├── docs/
├── references/
│   ├── paper-quality-system.md
│   ├── external-peer-review-orchestration.md
│   └── skill-registry.md
├── templates/
├── skills/
│   ├── paper-workflow-orchestrator/
│   ├── manuscript-quick-reconstruction/
│   ├── manuscript-literature-genealogy/
│   ├── manuscript-causal-identification-audit/
│   ├── manuscript-variable-data-measurement-audit/
│   ├── manuscript-results-narrative-consistency/
│   ├── manuscript-review-material-assembly/
│   ├── manuscript-final-review-drafting/
│   ├── review-issue-priority-synthesizer/
│   ├── multi-agent-academic-review-qa/
│   ├── post-flight-review-verifier/
│   └── scholar-pdf-markdown-restoration/
├── subworkflows/
└── projects/
```

## 与现有 Skills 的关系

本 workflow 不替代既有领域 Skills，而是做上层编排：

- `econ-write` / `econ-write-modular`：经济学论文写作能力；
- `manuscript-review`：逐段审读与批注能力；
- `reference-audit`：参考文献质量核查；
- `publication-grade-citation-enrichment`：发表级引文增强；
- 其他文档、PDF、citation 相关 Skills。

## Workflow 内子 Skills

- `paper-workflow-orchestrator`：上层编排论文写作、投稿前自审、外部审稿和返修。
- `scholar-pdf-markdown-restoration`：将 PDF 抽取、分章节还原为 Markdown，并使用模型能力逐章修复正文、公式、图表和 `[para N]`；公式还原为 `$$...$$`，图片/图表用 Obsidian 语法嵌入，生成可直接审读的 restored Markdown。
- `manuscript-quick-reconstruction`：快速通读手稿并还原作者声称的贡献链，输出可供文献定位、方法审查、变量审查和审稿素材组装继续使用的 Markdown 笔记。
- `manuscript-literature-genealogy`：编排 scholar-kit 检索能力，基于 FT50、UTD24/领域顶刊、`Nature`、`Science`、`PNAS` 等综合顶刊和中文川大社科 B 以上文献，重建知识树/文献谱系，输出文献定位矩阵和 Mermaid 知识树。
- `manuscript-causal-identification-audit`：区分实际观测发现与作者上升发现，用 DAG、后门/前门、IV、PSM、DiD、固定效应和稳健性检查识别主张。
- `manuscript-variable-data-measurement-audit`：审查核心概念、变量操作化、数据来源、样本、编码匹配、时间结构、测量误差和外部有效性。
- `manuscript-results-narrative-consistency`：检查理论机制、模型公式、数据方法、结果、机制、异质性、稳健性、拓展分析和结论是否闭环。
- `manuscript-review-material-assembly`：组装 reviewer-owned 的贡献总结、重大问题、次要问题、可执行修改建议和推荐意见理由。
- `manuscript-final-review-drafting`：编排最终审稿文本撰写，把审稿素材包和人工 gate 转换为 author-facing / editor-facing 最终审稿文本草稿和 ScholarOne 字段映射。
- `review-issue-priority-synthesizer`：在最终撰写前综合 issue ledger、审稿素材、多 Agent / 外部 benchmark findings，把分散问题去重、合并、排序为少数可写入终稿的 CRITICAL / MAJOR / MINOR 问题簇。
- `multi-agent-academic-review-qa`：用冷读者、技术清晰度、证据边界和可执行性视角做多 Agent / 多角色终稿 QA，暴露读者背景桥、技术推理和语气问题。
- `post-flight-review-verifier`：在最终草稿进入 ScholarOne 或交给审稿人前，逐条验证重大评论、推荐理由和 confidential comments 的证据来源、边界、读者背景桥和 paste-ready 状态。

完整能力地图与候选 Skill 见 `references/skill-registry.md`。当前策略是先用真实项目沉淀 seed Skill，再按稳定输入、输出和失败模式逐步升级共享 audit Skills。

## 外部审稿路线

外部审稿固定为十个模块：

```text
项目归档
-> 文本底稿
-> 快速通读
-> 文献定位
-> 方法与识别审查
-> 变量、数据与测量审查
-> 结果叙事一致性
-> 审稿素材组装
-> 终稿前人工复核门
-> 最终审稿文本撰写
   -> 问题优先级综合
   -> 多 Agent / 冷读者终稿 QA（按需）
   -> post-flight 终稿验收
```

详见 `references/external-peer-review-orchestration.md`。该路线来自真实 EMFT 审稿项目回流，但不包含具体稿件正文、审稿意见或期刊系统敏感信息。

## 实践项目

本 workflow 的创建过程由以下项目管理：

```text
Writer/00 信息/知识管理/PROJECT-260618-元Workflow工程/tasks/TASK06-论文写作审稿Workflow实践/
```
