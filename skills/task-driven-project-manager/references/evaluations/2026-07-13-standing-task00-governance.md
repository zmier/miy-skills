# Standing TASK00 Governance Structural Evaluation

> 日期：2026-07-13
> 评测类型：source-case structural evaluation
> 迁移状态：`structural-green / forward-test-pending`

## Source Case

```text
Writer/03 Projects/260521-基金经理研究/tasks/TASK00-project-governance/
```

## Structural UAT

| UAT | Check | Result | Evidence |
|---|---|---|---|
| SG-01 | TASK00 明确为 standing governance，而非实质研究任务 | pass | `TASK00-说明.md`、`README.md` |
| SG-02 | Registry 覆盖全部顶层 TASK | pass | `task-registry.md` 覆盖 TASK00--TASK08 |
| SG-03 | Portfolio Roadmap 与 Task Lineage Map 分开 | pass | TASK00 `README.md` |
| SG-04 | 每条当前线头有证据、缺口、状态和下一动作 | pass | `research-thread-portfolio.md` |
| SG-05 | 项目级决策与普通执行日志分离 | pass | `decision-log.md`、`logs/log.md` |
| SG-06 | 评审以日期保存，不覆盖旧状态 | pass | `reviews/2026-07-13-research-portfolio-review.md` |
| SG-07 | root README 指向 TASK00，TASK01--TASK08 可返回 TASK00 | pass | 项目 README 与各顶层 TASK 入口 |
| SG-08 | click/fallback 相对链接可解析 | pass | 来源案例检查 200 个相对链接，missing=0 |
| SG-09 | 下级 TASK 的数据、模型和结果未被迁入或重写 | pass | 只新增治理入口与摘要文件 |
| SG-10 | 没有把局部显著性自动升级为项目主线 | pass | portfolio review 先设置压力审计 Gate |

## Regression Boundary

本次规则是条件触发，因此不应改变：

- 小型线性项目的普通 `TASK01/TASK02` 脚手架；
- 单一大型 TASK 的 parent/subtask 结构；
- 默认 Task Lineage Map；
- 发生结构变化时的 Project Change Map；
- Multi-Agent Subtask Governance 与 parent acceptance。

这些能力与 TASK00 是并列补充关系：

```text
Lineage Map = 任务如何组织
Change Map = 结构/解释如何改变
TASK00 Portfolio = 多条路线如何比较并决定下一步
```

## Transfer Gap

来源案例参与了规则提炼，只能证明 structural-green。尚缺：

1. 一个未参与提炼的新项目；
2. 至少三个已有顶层 TASK 和两个真实竞争 workstreams；
3. 在不移动既有证据的情况下建立 TASK00；
4. 由 portfolio gate 实际触发一次 `promote / hold / archive`；
5. 验证维护成本没有超过决策收益。

完成后方可将状态升级为 `validated`。

## Cleanup Debt

`task-driven-project-manager/SKILL.md` 当前约 605 行，历史上已同时承载 scaffold、roadmap、change map、multi-agent、peer brief、environment、TDD 和 review 规则，超过 `skill-creator` 建议的 500 行左右渐进披露目标。

本轮新增 TASK00 能力已将完整协议和模板下沉到 reference/asset，主 Skill 只保留条件路由；未对既有 multi-agent、peer brief 等大段内容做无关重构。后续可另开 cleanup：将既有详细协议继续下沉，并做回归验证。该技术债不影响本轮 structural-green，但在升级为 validated 前应重新评估主 Skill 的加载成本。
