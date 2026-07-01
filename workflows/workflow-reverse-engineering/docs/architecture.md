# Architecture

## Workflow 与 Skill 的边界

```text
workflow = 工程系统
Skill = 可调用执行单元
subworkflow = 平台专属实现
TASK = 个案证据与迁移过程
reference = 稳定方法、边界、路线选择
template = 可复用文档/台账形态
```

顶层 workflow 不用根目录 `SKILL.md` 伪装自己。总编排 Skill 应放在：

```text
skills/reverse-workflow-orchestrator/SKILL.md
```

## 父 Workflow 和子 Workflow

父 workflow 负责“跨平台逆向工程”的共同骨架。

子 workflow 负责具体平台：

- Android；
- JS；
- Windows；
- Unity。

父 workflow 不直接搬走子 workflow 的平台细节，只在足够稳定并经多个平台验证后上提共性。

