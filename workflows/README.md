---
date: 2026-06-18
type: workflows-index
status: active
---

# Workflows

`workflows/` 用于沉淀跨项目、跨案例、可持续生长的能力工程系统。

它和 `skills/` 的分工如下：

```text
workflow = 工程系统、能力生态、总编排、子 workflow、模板、证据契约、迁移评测
skill    = 可被 Codex / agent 调用的单一执行单元
project  = 具体任务、案例、证据、日志和阶段产物
```

因此，当一个能力已经超过单个 Skill，开始需要总编排、多个子 Skills、TASK 模板、references、assets、tests、provenance 和迁移规则时，应进入 `workflows/`。

## 当前 Workflows

- `workflow-tao/`：元 workflow，用于研究复杂领域 workflow 如何被创建、维护、上提和迁移。
- `workflow-paper-writing-review/`：论文写作 / 审稿 workflow，用于验证正向构造与逆向验收共享质量系统。
- `workflow-reverse-engineering/`：逆向工程父 workflow，承载 Android、JS 等平台子 workflow。

## 放置规则

- 新 workflow 默认放在 `00 信息/miy-skills/workflows/<workflow-name>/`。
- workflow 根目录不放单一 `SKILL.md` 伪装成 Skill；可调用执行单元放在 `skills/<orchestrator-name>/SKILL.md`。
- 具体案例、课程 TASK、真实稿件、APK、日志和敏感证据不进入 workflow 根能力层，应保留在对应 project / TASK。
- 成熟 workflow 可以包含 `subworkflows/`，但父 workflow 不吞掉平台或领域专属细节。
- 元 workflow 的放置规则本身属于 `workflow-tao` 的治理内容。
