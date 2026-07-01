---
task: TASK04-2005-洋快餐
stage: blind-run
status: complete
---

# TASK04 箭头审查

| arrow_id | from_node | to_node | status | break_type | why_it_breaks | impact_on_root |
|---|---|---|---|---|---|---|
| A1-B1 | 大城市过去五年网点增长 40% | 未来 10 年全国市场份额超过 20% | weak | scope expansion / overclaim | 过去不等于未来，大城市不等于全国，网点数不等于市场占有率 | 高 |
| A3-B2 | 消费者尤其少年儿童喜爱 | 健康质疑站不住脚 | broken | concept mismatch / causal leap | 喜爱不能推出健康，儿童偏好也不能代表营养事实 | 高 |
| A4-B2 | 店内问卷 90% 认为有助营养均衡 | 洋快餐确有营养帮助 | weak | sample weakness / measurement mismatch | 店内样本可能偏向洋快餐消费者；主观认为不等于客观营养均衡 | 高 |
| A5-B3 | 未成年人未来更有消费能力 | 市场需求大幅跃升 | weak | hidden premise missing | 需要证明偏好成年后稳定，且消费能力会转化为洋快餐消费 | 中高 |
| A6-B4 | 标准化迎合无差异需要 | 快速发展优势 | weak | scope expansion | 只说明部分消费者部分场景偏好，不能覆盖所有饮食需求 | 中 |
| C-D | 洋快餐成为重要选择，中国式快餐无大发展 | 洋快餐一定成为饮食行业霸主 | broken | false dichotomy / overclaim | 饮食行业不只有洋快餐和中国式快餐；正餐、其他餐饮、替代业态仍可能占主导 | 高 |

## 最可写的 4 个断点

1. 从大城市过去增长外推到全国未来份额，时间和范围都扩大。
2. 消费者喜爱不能反驳健康风险。
3. 店内问卷有样本偏差，主观营养感受不能替代客观健康结论。
4. 中国式快餐不发展也不能推出洋快餐成为饮食行业霸主。
