---
date: 2026-06-22
type: reference
status: structural-green
scope:
  - workflow-tao
---

# Workflow Conception Log Policy

## 一句话

创建或重大升级 workflow 时，必须把“workflow 是如何被构思出来的”保留在目标 workflow 的 `logs/` 下。

```text
logs/YYYY-MM-DD-主题.md
```

这类日志是 workflow 能力工程的 provenance 层。它保存讨论、分歧、原文、抽象路径和迁移边界；稳定规则再提升到 `references/`、`templates/` 或 `SKILL.md`。

## 为什么需要

很多 workflow 不是一次写出来的，而是从真实项目、对话洞见、失败复盘或旧 workflow 抽父中逐步形成。若只保留最终 `SKILL.md`，会丢失：

- 为什么这个 workflow 需要存在；
- 为什么不是单个 Skill；
- 为什么选择父 workflow + adaptor / subworkflow；
- 哪些规则来自个案，哪些已被抽象；
- 哪些想法尚未稳定，不能提升为 reference；
- 后续回归测试应该回看哪个原始判断。

## 触发条件

满足任一条件时，应写 conception log：

- 创建新的 workflow 型 Skill；
- 将单一 Skill 升级为 workflow；
- 给 workflow 增加新 adaptor、subworkflow 或 mode；
- 一次对话产生了新的 workflow 架构判断；
- 项目复盘产生了可迁移的 workflow 规则；
- 修改父入口 `SKILL.md` 的核心哲学、路由或 Green 标准。

## 推荐位置

日志应写在目标 workflow 自己的 `logs/` 目录：

```text
workflow-xxxx/
├── SKILL.md
├── references/
├── templates/
├── skills/
└── logs/
    └── 2026-06-22-主题.md
```

不要只写在来源 project 中。来源 project 可以保留个案证据；目标 workflow 的 `logs/` 保留能力抽象过程。

## 推荐内容

每个 conception log 至少包含：

- 日期时间；
- 主题；
- 来源案例或来源对话；
- 原始问题；
- 关键原文或摘要；
- 方案分歧；
- 最终结构决定；
- 新增/更新的文件；
- 哪些规则提升到 reference/template/SKILL；
- 哪些内容必须留在 project/TASK；
- 后续 forward-test 或迁移观察点。

## 与 references 的边界

```text
logs/
  保存构思过程、原始讨论、未稳定判断、设计分歧、临时假设。

references/
  保存已经抽象、可复用、可被其他任务直接调用的稳定规则。

templates/
  保存可复制的文档、台账、TASK 骨架。

SKILL.md
  保存入口协议、路由、完成标准和禁止事项。
```

不要把整段对话原文直接提升进 `references/`。先在 `logs/` 保真保存，再提炼稳定规则。

## 文件命名

```text
logs/YYYY-MM-DD-短主题.md
```

示例：

```text
logs/2026-06-22-分形task-driven-workflow讨论记录.md
logs/2026-06-22-android-route-ladder抽父记录.md
logs/2026-06-22-论文审稿workflow-mode分歧记录.md
```

## Provenance 状态

日志中的规则建议标注迁移状态：

```text
raw-insight       # 原始洞见，尚未抽象
draft-rule        # 已形成草案规则
structural-green  # 已落入结构，可被调用
forward-test      # 已在新样本中验证
stable            # 多样本稳定
```

