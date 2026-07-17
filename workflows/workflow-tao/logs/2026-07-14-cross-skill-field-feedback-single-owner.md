# 跨 Skill 真实项目反哺与 Single Semantic Owner

> 日期：2026-07-14  
> 状态：`structural-green / forward-test-pending`

## 来源问题

CASE-260521 完整跑过 research seminar、route promotion、协议修复、独立审计和 roadmap/portfolio 回写后，用户提出：这次实践似乎可以同时反哺 task-driven、research-roadmap、research-brainstorm、workflow-research 和 workflow-tao，应该怎样处理？

## 分歧

```text
A. 每个 Skill 分别复制完整经验
B. 立即抽一个新的 research-route-governance Skill
C. 选中央语义所有者，其他 Skill 薄接入；保留 provenance，等待新案例
```

采用 C。

## 抽象

跨 Skill 的案例反馈本质上有两层：

```text
domain workflow rule：证据门控的研究路线仲裁
meta workflow rule：多个 Skill 共享一个新规则时，谁拥有语义、谁只消费
```

本次由 `workflow-research/references/evidence-gated-route-adjudication.md` 持有完整协议。Brainstorm、Task Manager、Roadmap 各自只接入职责内动作；workflow-tao 只吸收 `single semantic owner` 元规则。

## 迁移边界

- 来源案例证明结构可运行，不证明跨领域稳定；
- 不把基金研究的估计值、数据对象或邮件流程写入元 Skill；
- 不因一次跨 Skill 更新就创建新 Skill；
- 新案例应验证语义所有者是否真的减少重复和规则漂移。

## 影响文件

- `workflow-tao/SKILL.md`
- `workflow-tao/references/reference-workflow-cases.md`
- `workflow-research/references/evidence-gated-route-adjudication.md`
- 相关消费 Skills 的薄路由

