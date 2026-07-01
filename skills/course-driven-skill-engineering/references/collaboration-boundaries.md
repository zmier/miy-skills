# 协作边界

| Skill | 核心问题 | 主要产物 |
|---|---|---|
| `simon-learning-card-builder` | 如何让课程可首次学习、可复习 | 学习指南、知识地图、永久卡片 |
| `task-driven-project-manager` | 如何让案例执行过程可复现 | TASK、Makefile、日志、测试、交付物 |
| `course-driven-skill-engineering` | 如何从课程实践中研发可迁移 Skills | 冻结契约、路线对照、Skill 变更、迁移评测 |
| `skill-creator` | 一个具体 Skill 应如何创建和验证 | `SKILL.md`、references、scripts、agents metadata |

## 推荐协作顺序

```text
Simon：建立学习地图和知识基线
→ Course-driven：定义盲做与对照实验
→ Task-driven：承载实际案例复现
→ Skill Creator：实现具体 Skill 变更
→ Course-driven：组织回归与迁移评测
```

这些步骤按需求调用，不要求每个课程都完整走一遍。

## 探索性课程项目

当课程触发了一个没有标准答案的真实探索项目时，协作顺序变为：

```text
Course-driven：定义探索问题、阶段终点、冻结假设和停止条件
→ Task-driven：承载实验、日志、输出、限速、断点和 UAT
→ 领域总编排 Skill：执行当前最小红灯并选择子 Skill
→ Course-driven：判断真实反馈是否是 field-discovery、workflow-gap、tool-gap 或 boundary
→ Skill Creator：把稳定发现升级为具体 Skill/reference/template
→ Course-driven：组织回归、迁移评测和覆盖率声明
```

探索性项目里，`task-driven-project-manager` 负责“这次项目怎么可复现”，`course-driven-skill-engineering` 负责“这次项目暴露的能力缺口是否值得泛化”。不要把真实项目的临时数据、账号状态或固定接口结果写进元 Skill。

## 不越界

- 本 Skill 不代替领域总编排，不决定 Android、经济学或写作领域的具体技术路线。
- 不把知识卡片当作运行证据。
- 不把 TASK 日志直接复制成 Skill。
- 不在元 Skill 中保存课程个案的地址、密钥、固定字段或业务结论。
