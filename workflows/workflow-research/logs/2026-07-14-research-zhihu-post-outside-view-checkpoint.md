# 2026-07-14 Research Zhihu Post：将知乎稿提升为 Outside-View Checkpoint

## 触发

CASE-260521 的知乎同行稿随着 TASK07--TASK11 持续追加，逐渐同时出现两个问题：对外读者需要理解任务编号和私有术语；对内研究者也难以看出哪些机制仍成立、哪些已被后续证据降级。

用户提出：知乎稿既要真的面向知乎读者，也要作为“站在外部人的角度重新审视研究进展”的方法。

## 架构判断

采用 `workflow-tao` 的 single semantic owner 与 mode-aware completion：

```text
workflow-research
└── skills/research-zhihu-post
```

不把完整规则复制进 `task-driven-project-manager`、`research-brainstorm` 或 `research-roadmap`。这些能力只保留触发、输入、链接和回流职责。

暂不创建通用 `project-explainback` 父 Skill。当前只有一个完整研究案例，过早抽父会把研究特有的 claim ladder、识别边界和负证据治理错误泛化到所有项目。

## 模式

```text
outside-view-audit：内部使用，默认；
peer-discussion-draft：供同行审阅，不自动公开；
publish-ready：用户明确要求发布或同步后启用。
```

“知乎”同时保留平台用途和写作姿态，但不等于默认发布授权。

## 核心规则

1. 先冻结 evidence cutoff，再写稿；
2. 更新旧稿必须对账 current anchor、negative evidence 与 superseded claim；
3. 后续证据改变旧解释时，重写旧段，不只在末尾追加；
4. 正文按认识演进组织，不按 TASK 流水账组织；
5. 分开统计事实、经济含义、机制相容和因果；
6. 运行 zero-private-context 与 confidentiality audit；
7. 把暴露出的困惑回写 route portfolio、brainstorm 和 roadmap；
8. 平台同步后回读标题、公式、表格、降级结论与下一步。

## 边界

来源案例的具体估计、样本、基金机制和平台 token 不提升为通用规则。完整来源与迁移状态见：

```text
skills/research-zhihu-post/logs/2026-07-14-source-case-and-skill-design.md
references/source-provenance.md
```

## 迁移状态

```text
structural-green / source-case-tested / independent-forward-test-pending
```

