---
date: 2026-06-20
type: reference
status: seed
---

# Review Sensitivity Mapping

## 定位

`review-sensitivity-map.md` 是学术验箭头的前置显影产物，不属于 paper 抽树阶段。

它消费作者树：

```text
canonical-node-ledger.md
canonical-edge-ledger.md
evidence-ledger.md
extraction-qc.md
```

并产出“哪些证据组合值得验箭头”。它不重新抽作者树，不写最终审稿意见，不决定 major concern。

## 输出格式

```text
sensitivity_id | 类型 | 需并读的 evidence_ids | 需回看的原文链接 | 为什么值得后续验箭头 | 影响 X1/X2/Y | target_arrow_ids
```

可选视图：

```text
sensitivity-expanded-mermaid.md
```

## 重点类型

- 表文冲突；
- construct-measure mismatch；
- construct-level mismatch；
- macro-micro mismatch；
- treatment timing mismatch；
- treatment-definition mismatch；
- sample-mechanism mismatch；
- baseline missing；
- cluster-level mismatch；
- null-result reversal；
- robustness-threat mismatch；
- elevated claim over evidence；
- missing citation evidence。

## 高敏感显影规则

显影图的作用不是替代验箭头，而是防止第一轮内部审计变钝。生成时必须尽量把下列问题映射到具体 `target_arrow_ids`：

| sensitivity type | 触发信号 | 应追问 |
|---|---|---|
| treatment-definition mismatch | 作者用排除规则、编码规则或事件窗口定义 X | 这个操作性规则是否真的推出作者声称的 X？是否混入选择、预期、被动披露或监管滞后？ |
| sample-mechanism mismatch | 样本筛选、剔除事件、多事件处理、只保留首次事件 | 样本是否剔除了最能检验机制的对象？清洁样本是否削弱机制外推？ |
| baseline missing | 作者聚焦溢出、同行、学习、竞争、排除机制 | 是否缺少事件公司、自身变化、未受影响对象或其他必要基准？ |
| construct-level mismatch | 作者借用经典构念、宏观指标、行业指标后改成公司/事件指标 | 原构念层级和本文操作化层级是否一致？若不一致，作者是否解释适配？ |
| timing mismatch | 年度 POST、月度稳健性、事件日、结果变量窗口并存 | 信息何时可见？行为何时反应？结果何时测量？这些窗口是否能推出同一个因果链？ |
| mechanism over-exclusion | 作者用不显著结果排除某机制 | 不显著是否只表示“未发现证据”，而非“机制不存在”？ |
| heterogeneity reverse direction | 异质性某组方向相反或显著性与叙述不一致 | 这是边界条件、反向机制，还是正文选择性解释？ |
| robustness-threat mismatch | 稳健性数量多但没有 threat-to-test 对照 | 每个稳健性到底回应哪个核心威胁？是否遗漏主威胁？ |

每条 sensitivity 必须绑定 evidence_ids 和 target_arrow_ids。若只能凭直觉怀疑但没有 evidence_id，不写入 map，而是写入 `audit-input-status.md` 的待补材料。

## 边界

- 不把 sensitivity 节点写回作者树；
- 不凭空增加没有 evidence_id 的问题；
- 不把 sensitivity map 写成审稿意见；
- 不替代全量 arrow audit，只负责把高风险箭头显影出来。
