# 2026-07-09：research-brainstorm 子 Skill

## 来源

CASE-260521 基金经理研究进入 TASK07 后，核心问题从“回答是否影响净 flow”转为：

```text
为什么基金经理回答后，申购和赎回同时放大，而净 flow 不显著？
```

用户提出希望让多个 subagent 模拟不同学术专长，并且不是各写各的，而是真的相互交流。由此开立 TASK07-1-0，下载并研究 War Room、AgentCouncil、Multi-Agent Brainstorming 等外部参考，形成 project-local seminar protocol。

## 抽象规则

可迁移的研究方法不是“多叫几个 agent”，而是：

```text
共同 brief -> 独立发散 -> 共享黑板 -> 交叉批评 -> 回应修正 -> 主席合成 -> route gate
```

它适合用于：

- 初始事实引出多个机制解释；
- 候选 research routes 太多，需要排序；
- coauthor 讨论前需要整理 possibility pool；
- 需要把机制、替代解释、识别威胁和异质性路线分开；
- 后续要把脑暴结果转成可检验路线菜单。

## 新增 Skill

```text
skills/research-brainstorm/
```

核心文件：

```text
SKILL.md
references/templates.md
agents/openai.yaml
```

当前状态：

```text
seed / extracted-from-CASE-260521
```

## 边界

`research-brainstorm` 不直接生成因果结论，不替代文献检索、数据分析或识别设计。它只负责把研究侧的发散、批评和路线收束组织成可追踪过程。

后续需要在 TASK07-1-1 中 forward-test，观察：

- 角色是否过多或过少；
- 交叉批评是否真正改变候选机制；
- Chair synthesis 是否能给出可执行的 1-3 条 next route；
- 输出是否能回写到 Research Roadmap 和 task-driven 项目结构中。
