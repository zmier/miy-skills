# Exam Arrow Audit Table V2

状态：`non-blind-regression / split-from-issue-selection`

## 边界

本文件用于回测“验箭头”和“选问题”拆分后，论效题链条是否仍能保持原有行文质量。它不声明新的 blind-run；原 blind-run 仍见 `arrow-audit.md`。

本文件只负责全量诊断箭头，不负责最终选择 3-4 个可写问题。

## 箭头审计表

| arrow_id | from_node | to_node | status | break_type | why_it_breaks | impact_on_root | selection_hint |
|---|---|---|---|---|---|---|---|
| A1 | 形势、任务、观念都在变化 | 勤俭节约观念需要改变 | weak | overclaim / hidden premise missing | 观念需要与时俱进，不等于所有传统观念都应被改变；要推出勤俭节约过时，还需证明它已不适应当下或弊大于利。 | 高 | candidate-major |
| A2 | 过分强调勤俭节约会关注节流 | 不重视开源，财富难以积累 | weak | concept mismatch | 勤俭节约不等于只节流、不增收；“勤”本身也可能包含努力工作、增加收入。 | 高 | candidate-major |
| A3 | 比尔·盖茨财富不是靠省出来 | 个人财富不是省出来的 | weak | sample weakness | 单一个案不能推出普遍财富规律，也不能证明节流没有价值；更适合作为 A2 的辅助证据问题。 | 中 | candidate-useful |
| A4 | 勤俭持家会导致不上学、不买钢琴 | 青年人提倡勤俭持家有害无益 | broken | concept mismatch / alternative explanation | 勤俭持家可以是合理安排支出，并不等于削减必要教育投入或能力投资。 | 高 | candidate-major |
| A5 | 郎朗家长买钢琴 | 家庭不能一味节俭 | weak | sample weakness | 个案最多说明某些家庭投资可能重要，不能推出勤俭持家普遍有害。 | 中 | candidate-useful |
| A6 | 出口不行、投资过高 | 中国只能依靠内需 | weak | overclaim | 即使内需重要，也未必说明“只能”依靠内需；宏观政策工具不止消费观念一种。 | 中 | candidate-useful |
| A7 | 需要刺激内需 | 必须揭示勤俭节约弊端 | weak | hidden premise missing / means-end mismatch | 刺激内需需要证明勤俭节约是主要障碍；材料没有证明合理节约与合理消费不能并存。 | 高 | candidate-major |
| A8 | 提倡敢花会鼓励消费 | 会促进流通、消除积压、解决就业 | weak | causal leap / overclaim | 消费增长未必自动解决产品积压和就业问题，还取决于收入预期、未来保障、产品质量、需求结构和企业调整。 | 高 | candidate-major |
| A9 | 提倡能挣会带来奋斗、创新、活力 | 能挣敢花优于勤俭节约 | weak | comparison mismatch | “能挣”与“勤俭”不是对立项，可以同时成立。 | 中 | candidate-useful |
| A10 | 大家不舍得花会导致工人失业 | 勤俭节约祸害他人 | broken | causal leap / overclaim | 下岗失业可能有产业结构、企业管理、需求变化等多种原因，不能简单归因于勤俭节约。 | 高 | candidate-useful |

## 交给选问题环节的候选

高优先候选：

```text
A1, A2, A4, A7/A8
```

可作为辅助或合并候选：

```text
A3 -> 并入 A2
A5 -> 并入 A4
A6/A9/A10 -> 视篇幅并入 A7/A8
```
