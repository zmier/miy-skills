---
date: 2026-06-18
type: workflow
status: seed
---

# Workflow Tao

这是一个元 workflow，用于研究和指导复杂领域 workflow 如何从实践案例中生成、维护、上提和迁移。

它不是单个 Skill。根目录负责组织元 workflow 工程；可调用执行单元放在 `skills/`；具体实践样本和实验过程放在 `projects/` 或 Writer 项目区。

## 核心问题

```text
当我们从一个复杂实践领域中沉淀 workflow 时，
哪些东西属于领域本身，
哪些东西属于可跨领域复用的 workflow 工程方法？
```

## 适用对象

- 从成熟 workflow 中抽父 workflow，例如从 Android 逆向抽出 `workflow-reverse-engineering`；
- 从正向构造和逆向审计中抽共享质量系统，例如论文写作与审稿；
- 判断一个领域应沉淀为单个 Skill、多个 Skills，还是 workflow 工程；
- 设计 workflow 的总编排、子 Skills、TASK 模板、证据台账、provenance 和迁移评测；
- 判断课程、真实项目和技术情报如何反哺 workflow。

## 与现有 Skill 的关系

`course-driven-skill-engineering` 是本元 workflow 的重要来源场景之一，但不是全部。

```text
workflow-tao
├── course-driven-skill-engineering    # 课程/案例驱动
├── field-project-feedback             # 真实项目反哺
├── technology-radar-feedback          # 技术情报反哺
└── skill-creator / task-driven-project-manager
```

## 当前结构

```text
workflow-tao/
├── README.md
├── SKILL.md
├── ROADMAP.md
├── docs/
├── references/
├── templates/
├── skills/
│   └── workflow-tao-orchestrator/
└── projects/
```

## 当前实践样本

- `workflow-reverse-engineering` 抽父实践；
- 论文写作 / 审稿 workflow 设计实践。

详细研究项目见：

```text
Writer/00 信息/知识管理/PROJECT-260618-元Workflow工程/
```

