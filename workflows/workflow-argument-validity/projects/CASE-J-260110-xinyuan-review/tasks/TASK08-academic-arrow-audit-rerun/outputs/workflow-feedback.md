# Workflow Feedback

## What Worked

1. 八步主轴可执行。

   TASK07 的 canonical edge ledger 能直接进入“改写箭头 -> 判断类型 -> 路由方法 -> 逐条审计”。

2. 诊断路由型设计是合适的。

   本轮确实不是按 gap/变量/识别/机制 checklist 巡检，而是先从 `arrow_id` 出发，再给箭头贴类型。

3. `needs-method-qc` 纪律有效。

   对 Oster、Bacon、聚类层级等方法点，没有硬判；而是区分初步审计和后续强论证前的 method QC。

4. `review-sensitivity-map` 应该属于验箭头阶段。

   本轮显影图使用 TASK07 的 evidence ledger，不把审稿攻击回写作者树。

## Skill Improvement Candidates

| candidate | target | reason | status |
|---|---|---|---|
| 增加 `strong-with-qc` 状态 | `academic-arrow-audit-table` template | A028 这类结果方向/显著性支持作者，但表格还没 cell-level 复核；`strong` 和 `needs-qc` 二选一不够精细。 | candidate |
| 增加 `needs-method-qc-if-used-as-major` | `method-knowledge-feedback.md` | 有些方法点不阻塞初审，但若进入 major concern 需要补方法来源。 | candidate |
| 明确 `review-sensitivity-map` 是步骤 0 准备物 | `academic-arrow-audit-main-axis.md` | 当前已修正为验箭头阶段准备物，不属于抽树必交付。 | applied |
| 给 `academic-causal-arrow-audit` 增加聚类层级检查字段 | causal 子 Skill | 本轮 A025 显示处理层级与聚类层级是高频计量审查点。 | candidate |
| 给 `academic-statistical-result-arrow-audit` 增加“proxy result vs substantive claim”字段 | statistical 子 Skill | A013/A029 显示显著结果常常支持代理指标，但不自动支持实体概念。 | candidate |
| 增加 `reporting-qc` 字段 | statistical 子 Skill / template | 欣媛意见指出括号值疑似 t 值但表注写标准误；这种表注-统计量错配需要独立显影。 | candidate |
| 增加机制概念滑动检查 | academic arrow types / main axis | 欣媛意见的“行为信号 vs 内容信息”说明，机制箭头不仅看显著性，还要看理论解释跨章节是否一致。 | candidate |
| 增加机制样本一致性检查 | mechanism-claim route | 图/事件研究样本和机制回归样本可能不同，若不显影会漏掉推断跳跃。 | candidate |

## No Immediate Skill Split

本轮暂不建议新开子 Skill。

原因：

```text
construct-measure、sample-mechanism、mechanism-claim、robustness-threat
都能由父 Skill 承载并输出有效诊断。
```

若后续多篇论文反复出现“稳健性是否回应目标威胁”的复杂路线，可考虑拆 `academic-robustness-threat-arrow-audit`。
