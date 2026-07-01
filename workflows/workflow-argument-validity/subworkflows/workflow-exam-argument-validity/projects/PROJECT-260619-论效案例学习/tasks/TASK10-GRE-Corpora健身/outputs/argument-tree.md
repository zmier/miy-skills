---
task: TASK10-GRE-Corpora健身
stage: assisted-calibration-run
status: complete
route: workflow-argument-validity / GRE Analyze an Argument
---

# TASK10 论证树

## 文本类型路由

| 字段 | 判断 |
|---|---|
| text_type | GRE Analyze an Argument |
| route | 父层 `workflow-argument-validity` + 论效题子 workflow 的抽树/验箭头动作 |
| output_target | hidden assumptions + implication analysis |
| independence | `prior-exposed / assisted` |
| reason | 题目要求分析明示或暗含假设，不是表达自己对健康、电脑或经济的观点 |

## 作者想证明的根结论

Corpora 公民健康水平下降的主要原因不是电脑使用，而是经济衰退；经济好转后，健康水平会改善。

## Mermaid 论证树

```mermaid
flowchart BT
  A1["当前约 1/4 公民达到现行体能标准"] --> B1["当前健康水平低于过去"]
  A2["20 年前约 1/2 公民达到当时标准"] --> B1
  A3["电脑拥有率最高地区整体健康水平也最高"] --> B2["电脑使用并未导致健康水平下降"]
  A4["今年健身产品和服务支出异常低"] --> B3["经济衰退是健康下降主要原因"]
  B1 --> C["Corpora 公民健康水平下降"]
  B2 --> D["专家关于电脑使用的解释不成立"]
  B3 --> E["经济衰退才是主要原因"]
  D --> F["经济好转后健康水平会改善"]
  E --> F

  H1["H1: 20 年前标准与当前标准可比"] -.hidden support.-> B1
  H2["H2: 电脑拥有率能代表电脑使用时间"] -.hidden support.-> B2
  H3["H3: 高电脑拥有率地区与其他地区除电脑外可比"] -.hidden support.-> B2
  H4["H4: 健身支出能代表健康行为/锻炼水平"] -.hidden support.-> B3
  H5["H5: 经济好转会恢复健身支出并改善健康"] -.hidden support.-> F
```

## 节点台账

| node_id | type | content | 备注 |
|---|---|---|---|
| A1/A2 | evidence | 当前与 20 年前达标比例对比 | 依赖标准可比性 |
| A3 | evidence | 高电脑拥有率地区健康水平也高 | 依赖拥有率代表使用时间，且排除第三因素 |
| A4 | evidence | 健身支出异常低 | 依赖支出代表实际锻炼和健康投入 |
| B1 | subclaim | 健康水平下降 | 若标准不可比，基础现象不稳 |
| B2 | subclaim | 电脑不是健康下降原因 | 若拥有率不等于使用时间或有第三因素，箭头断裂 |
| B3 | subclaim | 经济衰退是主要原因 | 若存在免费锻炼或其他原因，箭头过强 |
| F | root claim | 经济好转后健康水平会改善 | 需要经济、支出、健康行为、健康结果之间连续成立 |
