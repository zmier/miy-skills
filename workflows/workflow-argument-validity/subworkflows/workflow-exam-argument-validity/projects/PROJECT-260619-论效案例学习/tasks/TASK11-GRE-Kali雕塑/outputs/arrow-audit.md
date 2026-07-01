---
task: TASK11-GRE-Kali雕塑
stage: assisted-calibration-run
status: complete
---

# TASK11 箭头审查

| arrow_id | from_node | to_node | status | break_type | question_needed | why_it_matters | impact_on_root |
|---|---|---|---|---|---|---|---|
| A1-B1 | 发现头部和手部模具 | 真人大小雕塑由真实身体模具制成 | weak | scope expansion / extrapolation mismatch | 这些模具是否用于整件真人大小雕塑，还是只用于头和手？ | 如果模具只覆盖局部，就不能推出整件雕塑的生产机制 | 高 |
| A1-B1 | 发现模具 | 模具是主要生产方式 | weak | hidden premise missing / condition confusion | 模具是否为生产工具，而非练习、研究或辅助工具？ | 如果模具只是辅助工具，雕刻技巧仍可能是主要价值来源 | 高 |
| B1-B3 | 真人大小可用模具 | 微型雕塑因不能用模具而风格不同 | weak | alternative explanation / comparison mismatch | 微型与真人大小雕塑是否同一时期、同一材料、同一艺术传统和用途？ | 若二者本就属于不同传统，风格差异不能归因于模具限制 | 高 |
| B2-B4 | 不靠雕刻工具 | 很少发现工具得到解释 | weak | measurement mismatch / alternative explanation | 工具少是否因为没有使用，还是因腐坏、未发现或被转移？ | 如果工具保存率低，工具少不能支持“不靠工具” | 中高 |
| B1-C1-D | 模具制成 | 真人大小雕塑贬值 | weak | value prediction / overclaim | 收藏者是否真的按制作方式而非稀缺性、历史意义、审美价值定价？ | 若市场重视历史或稀缺性，模具发现未必导致贬值 | 高 |
| B3-C2-E | 微型雕塑风格不同 | 微型雕塑升值 | weak | value prediction / hidden premise missing | 微型雕塑的市场需求是否会因该发现上升？ | 若买家不改变偏好，微型雕塑不必然升值 | 高 |

## GRE 式问题影响链

| question_id | 需要回答的问题 | 对应箭头 | 若答案为 yes | 若答案为 no |
|---|---|---|---|---|
| Q1 | 模具是否足以代表真人大小雕塑整体制作方式？ | A1 -> B1 | 支持作者的模具机制 | 只能说明局部或个别部位，整件机制不成立 |
| Q2 | 模具是否为主要生产工具？ | A1 -> B1/B2 | 削弱雕刻技巧的重要性 | 模具可能只是辅助，价值判断不稳 |
| Q3 | 微型与真人大小雕塑是否可比？ | B1 -> B3 | 风格差异可能与制作方式有关 | 风格差异可能来自时代、用途、材料或传统 |
| Q4 | 工具少是否说明未使用工具？ | B2 -> B4 | 支持作者对工具少的解释 | 工具保存/发现偏差会削弱解释 |
| Q5 | 收藏价值是否主要由制作方式决定？ | C1 -> D; C2 -> E | 预测更可信 | 价格预测缺少市场机制 |
