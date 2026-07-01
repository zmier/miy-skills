---
task: TASK11-GRE-Kali雕塑
stage: assisted-calibration-run
status: complete
route: workflow-exam-argument-validity / GRE Analyze an Argument
---

# TASK11 论证树

## 文本类型路由

| 字段 | 判断 |
|---|---|
| text_type | GRE Analyze an Argument |
| route | 论效 workflow 的 GRE Argument 分支 |
| output_target | questions-to-evaluate + impact analysis |
| independence | `prior-exposed / assisted` |
| reason | 题目要求讨论需要回答哪些问题，并说明答案如何帮助评估预测 |

## 作者想证明的根结论

关于 Kali Island 古代雕塑的发现会导致收藏价值变化：真人大小雕塑会贬值，微型雕塑会升值。

## Mermaid 论证树

```mermaid
flowchart BT
  A1["在 Kali 发现人头和手部模具"] --> B1["真人大小陶土人像由真实身体模具制成"]
  B1 --> B2["真人大小雕塑并非主要依靠雕刻工具和技巧"]
  B1 --> B3["微型雕塑风格不同，因为模具只能用于真人大小雕塑"]
  B2 --> B4["很少发现雕刻工具得到解释"]
  B1 --> C1["真人大小雕塑艺术/收藏价值下降"]
  B3 --> C2["微型雕塑相对更有艺术价值或稀缺价值"]
  C1 --> D["真人大小雕塑将贬值"]
  C2 --> E["微型雕塑将升值"]

  Q1["Q1: 头和手模具是否代表整件雕塑的生产方式？"] -.evaluates.-> A1
  Q2["Q2: 模具是生产工具、辅助工具还是练习工具？"] -.evaluates.-> B1
  Q3["Q3: 微型雕塑和真人大小雕塑是否可比？"] -.evaluates.-> B3
  Q4["Q4: 工具少是否等于未使用工具？"] -.evaluates.-> B4
  Q5["Q5: 收藏价值是否主要由制作方式决定？"] -.evaluates.-> D
  Q5 -.evaluates.-> E
```

## 节点台账

| node_id | type | content | 备注 |
|---|---|---|---|
| A1 | evidence | 发现头部和手部模具 | 局部证据 |
| B1 | subclaim | 真人大小雕塑由真实身体模具制成 | 需要证明模具覆盖整件雕塑和主要生产方式 |
| B2 | subclaim | 雕刻工具和技巧不是主要原因 | 需要排除工具/技巧与模具并用 |
| B3 | subclaim | 微型雕塑风格不同因不能用模具 | 需要排除材料、时期、用途、审美传统等替代解释 |
| B4 | subclaim | 工具少说明不靠雕刻工具 | 需要考虑工具腐坏、未发现、被转移、材料不同 |
| D/E | root prediction | 真人大小贬值，微型升值 | 需要市场机制与收藏者价值标准支撑 |
