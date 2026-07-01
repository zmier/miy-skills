# Arrow Audit Table Template

| arrow_id | from_node | to_node | 作者如何推出 | evidence_ids | task_instruction | status | break_type | fallacy_label | hidden_premise | why_it_breaks | impact_on_parent | impact_on_root | fix_or_downgrade | selection_hint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 |  |  |  |  | assumption/question/evidence/alternative/paragraph/review concern | strong/strong-with-qc/weak/broken/unclear/needs-qc/needs-external-evidence |  |  |  |  |  |  |  | candidate-major/candidate-useful/minor/no-issue |

## Paragraph Draft

```text
定位：作者将 [A] 作为 [B] 的依据，并进一步用于支持 [C/root]。
分析：但 [A] 更直接说明的是 [...]；若要推出 [B]，还需要证明 [...]。当前稿件/材料尚未充分说明这一前提。
标签：如果需要，可将该断点概括为 [break_type / fallacy_label]，但术语不替代上述分析。
影响：因此，[B] 以及其上层结论 [C/root] 的支撑力度下降。
建议：作者应补充 [...]，或将结论降调为 [...]。
```
