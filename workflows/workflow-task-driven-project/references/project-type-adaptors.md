# Project Type Adaptors

## 定位

通用 workflow 负责分形 task-driven 骨架；adaptor 负责不同项目类型的入口材料、风险分类、验收标准和模板。

## 当前 adaptor

| Adaptor | 场景 | 状态 |
|---|---|---|
| outsourcing-project-adaptor | 客户需求、外包接单、报价前评估 | structural-green |

## 预留 adaptor

| Adaptor | 场景 | 关键差异 |
|---|---|---|
| academic-research-adaptor | 学术研究项目 | 研究问题、文献、数据、识别策略、论文贡献 |
| manuscript-project-adaptor | 论文写作/修改 | 论证树、审稿意见、期刊规范、版本控制 |
| software-tool-adaptor | 软件/工具开发 | 用户故事、架构、测试、部署、维护 |
| data-analysis-adaptor | 数据分析项目 | 数据源、清洗、指标、可复现 notebook、结果解释 |

## Adaptor 契约

每个 adaptor 至少说明：

- 适用场景；
- 输入材料；
- TASK 拆解模板；
- 风险 taxonomy；
- Green 标准；
- 人工 gate；
- 输出物；
- 何时进入执行型 project。

