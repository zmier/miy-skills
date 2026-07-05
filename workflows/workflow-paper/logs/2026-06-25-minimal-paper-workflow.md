# 2026-06-25 minimal paper workflow 构思日志

## 触发问题

用户提出：学论文、审稿、写论文三件事有很多 Skill 相通，是否应在三者之上创建一个更高层父 workflow：`workflow-paper`。

用户要求：

- 先做最简单版父 workflow；
- 父 workflow 只做路由，不超前设计；
- 下面先有一个“学论文”子 workflow；
- 学论文子 workflow 也只先搭架子；
- 不急着拆“强参考文献”或“弱参考文献”，后面边学边做。

## 当前决定

创建：

```text
workflow-paper/
├── SKILL.md
├── subworkflows/
│   └── workflow-paper-learning/
│       └── SKILL.md
├── references/
└── logs/
```

父层状态为：

```text
seed / minimal-router
```

子层状态为：

```text
seed / scaffold-only
```

## 关键边界

`workflow-paper` 不收编 `workflow-argument-validity`，只组合调用它。

```text
论文工作流不是论证工作流的子类；
论文工作流把论证工作流作为底层引擎组合进来。
```

`workflow-paper-learning` 不等同于 strong paper learning。

```text
学论文是父路线；
强参考文献学习只是未来可能分化出的子路线之一。
```

## 暂不做的事

- 暂不迁移旧 `workflow-paper-writing-review`；
- 暂不创建 `workflow-paper-writing` / `workflow-paper-review` / `workflow-paper-revision`；
- 暂不创建 strong paper 子 Skill；
- 暂不定义复杂 TASK 模板和测试；
- 暂不把真实科研项目内容写入 workflow。

## 下一步

用真实科研项目中的第一批基础文献学习来 forward-test `workflow-paper-learning`，再决定：

- 是否需要文献类型路由；
- 是否需要 strong paper template learning 子 Skill；
- 学习卡模板是否稳定；
- 是否把部分规则提升到 references。

