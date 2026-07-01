---
task: TASK10-GRE-Corpora健身
stage: assisted-calibration-run
status: complete
---

# TASK10 箭头审查

| arrow_id | from_node | to_node | status | break_type | hidden_assumption | why_it_breaks | impact_on_root |
|---|---|---|---|---|---|---|---|
| A1+A2-B1 | 当前 1/4 达标 + 20 年前 1/2 达标 | 当前健康水平低于过去 | weak | standard shift / extrapolation mismatch | 两个时期的体能标准可比 | 如果现行标准更严格，达标比例下降不必然说明真实健康下降 | 高 |
| A3-B2 | 电脑拥有率高地区健康水平高 | 电脑使用未导致健康下降 | broken | measurement mismatch / alternative explanation | 拥有率能代表使用时间，且地区之间除电脑外可比 | 拥有电脑不等于长时间使用；高拥有率地区可能更富裕、饮食更好、医疗和健身资源更多 | 高 |
| A4-B3 | 健身产品和服务支出低 | 经济衰退是健康下降主要原因 | weak | measurement mismatch / causal leap | 健身支出能代表锻炼量和健康投入 | 人们可能用免费方式锻炼；支出低也可能来自价格下降、偏好变化或替代活动 | 高 |
| B3-F | 经济衰退是主因 | 经济好转后健康会改善 | weak | hidden premise missing / overclaim | 经济改善会带来健身支出恢复，且支出会转化为健康改善 | 即使经济好转，人们也未必改变行为；健康改善还有饮食、时间、公共设施等条件 | 高 |

## GRE 式核心假设清单

| assumption_id | 假设 | 支撑箭头 | 若假设不成立，影响 |
|---|---|---|---|
| H1 | 当前体能标准与 20 年前标准可比 | A1+A2 -> B1 | 健康下降这个基础事实会被削弱 |
| H2 | 电脑拥有率可以代表电脑使用时间 | A3 -> B2 | 电脑解释不能被有效反驳 |
| H3 | 高电脑拥有率地区没有其他更强健康优势 | A3 -> B2 | 地区健康水平高可能来自收入、资源、饮食等第三因素 |
| H4 | 健身支出低代表健康行为下降 | A4 -> B3 | 支出低不能证明经济衰退导致健康下降 |
| H5 | 经济好转会改善健康行为并改善健康结果 | B3 -> F | 预测会变成缺乏支撑的乐观推测 |
