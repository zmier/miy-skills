# Stage Gates

## 阶段路由

| 阶段 | 目标 | Green | 下一步 |
|---|---|---|---|
| opportunity-evaluation | 判断要不要做 | 接 / 不接 / 先 PoC / 改范围 | 进入执行、PoC 或终止 |
| execution-delivery | 完成已确认项目 | 交付物通过验收 | 进入复盘 |
| phase-review | 复盘阶段结果 | 证据地图、边界、经验候选明确 | 进入能力沉淀或收尾 |
| capability-generalization | 沉淀 workflow/skill/template | 规则有 provenance 和 forward test | 更新能力工程 |

## 机会评估 Green

机会评估不是以“项目做完”为 Green，而是以“决策可被证据支持”为 Green：

```text
接：范围清楚、风险可控、验收明确、资源可得。
不接：风险不可接受、授权不足、目标不合规或收益不匹配。
先 PoC：关键能力未知，但可通过小验证降低不确定性。
改范围：客户目标可做，但原范围混乱、过大或边界错误。
```

## 执行 Green

执行阶段 Green 必须对应已确认的验收合同：

- 交付物存在；
- 测试或 UAT 通过；
- 人工 gate 已记录；
- 已知边界写入 final_outputs；
- 原始材料和过程证据可追溯。

## 复盘 Green

复盘阶段 Green：

- 原始目标如何变化已记录；
- Red -> Green 路径已说明；
- 关键证据有 Obsidian 双链；
- 可迁移规则和不可迁移个案证据已区分；
- 明确是否反哺 workflow/skill。

