---
task: TASK07-2006-企业丑闻
stage: limited-blind-run
status: complete
---

# TASK07 箭头审查

| arrow_id | from_node | to_node | status | break_type | why_it_breaks | impact_on_root |
|---|---|---|---|---|---|---|
| A1-B1 | 美国曝光丑闻多 | 经济发展不带来道德进步 | weak | measurement mismatch | 曝光多可能因监管、媒体、透明度更高，不等于真实丑闻更多或道德更差 | 中 |
| A2-B2 | 企业丑闻可能败坏道德风气 | 怀疑企业组织存在意义 | broken | overclaim | 丑闻不能抵消企业创造财富、就业、创新等社会功能 | 中高 |
| A3-B3 | 股东难知高管是否滥权 | 怀疑高报酬合理性 | weak | hidden premise missing | 需要证明监督不足导致高薪无效或滥用普遍存在 | 中 |
| A4-B4 | 高薪但亏损无罚金 | 激励机制无效 | weak | condition relation | 罚金只是约束机制之一，亏损也未必完全由高管过错造成 | 高 |
| B4-D | 激励机制无效导致丑闻 | 只有有效激励机制才能杜绝丑闻 | broken | necessary/sufficient confusion / overclaim | 企业丑闻还受法律、监管、治理、文化、审计等影响；“杜绝”强度过高 | 高 |

## 最可写的 4 个断点

1. 曝光数量不等于真实发生数量，更不等于道德水平。
2. 企业丑闻不能推出企业组织存在意义可疑。
3. 高管亏损不罚不必然说明激励机制完全无效。
4. 有效激励机制不是杜绝丑闻的唯一条件，也未必能杜绝。
