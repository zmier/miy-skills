# Evidence-Gated Route Adjudication Structural Evaluation

> 日期：2026-07-14  
> 评测类型：source-case structural regression  
> 迁移状态：`structural-green / forward-test-pending`

## Source Case Chain

```text
TASK06/TASK09 frozen anchors
-> TASK10 measurement support stop
-> TASK00-1 multi-role route seminar
-> S01 promote-now / M01 queue-data / M02 theory-boundary
-> TASK09-22 primary-sample protocol repair
-> TASK11 economic-level Gate
-> TASK11-1 independent implementation audit
-> TASK00 portfolio / roadmap / next-data-object sync
```

## Structural UAT

| UAT | Check | Result | Evidence |
|---|---|---|---|
| SG-01 | 共同 anchors、negative evidence 与禁止声称先冻结 | pass | TASK00-1 seminar brief / Chair protocol |
| SG-02 | 多角色不是各写各的，存在 shared blackboard、cross-critique 与 response | pass | TASK00-1 Round 1--3 artifacts |
| SG-03 | 每条 stable route 有明确最终处置 | pass | Chair final adjudication |
| SG-04 | 只有一条 `promote-now`，其 Gate 可改变竞争 DGP 排序 | pass | TASK00-1 next Gate / TASK11 protocol |
| SG-05 | Seminar 与 evidence-owning empirical TASK 分离 | pass | TASK00-1 delivered；TASK11 independent top-level TASK |
| SG-06 | Frozen protocol mismatch 被实现检查发现并 append-only 修复 | pass | TASK09-22 protocol repair note / decision correction |
| SG-07 | Primary 与 sensitivity panels 分开，unique-key / sample tests 通过 | pass | repaired TASK09-22 tests |
| SG-08 | 高风险 layer/covariance result 有另一计算路线独立复现 | pass | TASK11-1 sparse FE / NumPy audit |
| SG-09 | Roadmap 区分 pattern、location、mechanism compatibility 与 causality | pass | TASK11 final synthesis / project roadmap |
| SG-10 | Gate 结果改变下一数据对象，而非只更新显著性文字 | pass | HYP-002 canonical-fund object refinement / Data Gate draft |
| SG-11 | 跨 Skill 规则有中央语义所有者，消费 Skills 只薄接入 | pass | workflow-research central reference and five target updates |
| SG-12 | 来源案例固定值未写入中央通用 reference | pass | generalized reference audit |

## Validation Run

| Check | Result |
|---|---|
| `skill-creator/scripts/quick_validate.py` | `task-driven-project-manager`、`research-roadmap`、`research-brainstorm`、`workflow-research`、`workflow-tao`、`course-driven-skill-engineering` 全部 valid |
| Local Markdown / Mermaid click links | checked set `missing=0` |
| Generic reference de-case audit | no domain estimates, platform names, database names or case-specific hypotheses |
| Migration status audit | all new capability claims remain `structural-green / forward-test-pending` |

回归过程中修复两个既有可调用性问题：`research-roadmap` frontmatter description 的 ASCII angle-bracket arrow，以及 `workflow-research` 顶层自定义 frontmatter keys。另将通用 Roadmap 中一个来源案例邮件 click 改为明确的 task-local placeholder，避免失效路径伪装成通用示例。

## Regression Boundary

本轮不得改变：

- 早期 idea 阶段的开放式 Brainstorm；
- 小型线性项目的普通 TASK scaffold；
- 普通 subagent 的既有 parent acceptance；
- 不涉及路线竞争的简单 Research Roadmap；
- `course-driven-skill-engineering` 已有 dialogue-insight 主流程。

因此本轮没有创建新的 `research-route-governance` Skill，也没有修改 course-driven 主 `SKILL.md`。

## Transfer Test Required

在一个未参与提炼的新研究项目中验证：

1. 至少有一个稳定 empirical anchor 和三条竞争 routes；
2. seminar 后能否只升格一项 high-information Gate；
3. promotion contract 是否在新 outcome 前冻结；
4. protocol-conformance tests 是否发现至少一种注入偏差或证明防护有效；
5. independent audit 是否能在不泄漏父实现的情况下复现或指出差异；
6. portfolio/roadmap 是否正确区分 location 与 why；
7. 维护成本是否低于减少规格漂移和解释污染的收益。

通过后才能考虑把迁移状态升级为 `validated`，并重新评估是否值得创建独立子 Skill。
