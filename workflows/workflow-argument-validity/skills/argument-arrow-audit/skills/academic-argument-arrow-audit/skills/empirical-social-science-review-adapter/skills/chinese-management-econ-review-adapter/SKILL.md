---
name: chinese-management-econ-review-adapter
description: 经管/社科实证审稿适配器下的中文经管子适配器。用于中文经管、中文社科和本土期刊审稿语境中，显影指标方向、文本口径、本土制度语境、中文文献谱系、政策化表达、表格变量说明和本地审稿敏感澄清点；输出 chinese-reviewer-sensitive-candidates、chinese-literature-gap-request、local-expression-and-format-qc，并移交验箭头、领域学习和选点。
---

# Chinese Management / Econ Review Adapter

## 定位

这是 `empirical-social-science-review-adapter` 的子 Skill。

它处理的不是“中文写作润色”，而是中文经管审稿语境中会影响论证有效性的本地化敏感点。

主轴仍然是：

```text
target_arrow_id: A -> B
这个中文经管敏感点是否会削弱 A -> B？
如果会，它卡住哪个 parent claim？
```

## 触发条件

满足任一条件时调用：

- 手稿为中文经管、中文社科、中文管理、中文金融、中文会计、中文公共政策类论文；
- 目标期刊或审稿语境是中文期刊；
- 核心概念、政策语境、制度背景或文献谱系主要来自中文研究；
- `empirical-social-science-review-adapter` 发现变量方向、文本口径、中文制度外推、中文文献或本土表达可能影响论证。

## 输入

```text
empirical-review-sensitivity-map.md
empirical-arrow-candidate-ledger.md
canonical-node-ledger.md
canonical-edge-ledger.md
evidence-ledger.md
restored manuscript Markdown
references / bibliography
external-evidence-request.md
```

## 输出

```text
chinese-reviewer-sensitive-candidates.md
chinese-literature-gap-request.md
local-expression-and-format-qc.md
handoff-to-field-learning.md
handoff-to-issue-selection.md
```

## 主流程

1. 读取经管实证敏感箭头，只处理已绑定 `target_arrow_id` 的候选。
2. 检查中文经管敏感类型，见：

   ```text
   references/chinese-management-econ-reviewer-sensitive-points.md
   ```

3. 对每个触发点写入 `chinese-reviewer-sensitive-candidates.md`：

   ```text
   candidate_id
   target_arrow_id
   local_sensitivity_type
   evidence_ids
   manuscript_location
   why_sensitive_in_chinese_review_context
   parent_claim_id
   bottleneck_status_candidate
   external_cn_literature_need
   suggested_issue_level
   ```

4. 对需要中文文献谱系、本土制度或中文期刊规范支撑的点，写入 `chinese-literature-gap-request.md`，移交 `academic-field-evidence-learning`。
5. 对只影响表达、格式或透明度的点，写入 `local-expression-and-format-qc.md`，并标注是否只是 `minor / revision-action / cosmetic`。
6. 移交选点层，不直接决定 major。

`chinese-literature-gap-request.md` 必须能被第 4 步直接转入 `cnki-request-ledger.md`，至少包含：

```text
source_request_id
target_arrow_id
local_sensitivity_type
query_intent
suggested_exact_terms
suggested_expanded_terms
suggested_adjacent_construct_terms
required_scope
required_quality_floor
why_cnki_needed
what_can_be_concluded_without_cnki
what_cannot_be_concluded_without_cnki
```

不要只写“需查 CNKI”。必须说明查 CNKI 是为了判断哪条箭头，以及如果不查，哪些审稿判断只能保留为 `evidence-needed` 或 `search-before-major`。

## 禁止事项

- 不把具体题材、企业类型、数据库或政策名写成永久规则；
- 不把所有中文期刊表达问题都升级为 major；
- 不把“中文文献少”直接当成问题，必须说明它削弱哪条 gap / construct / mechanism / contribution 箭头；
- 不把格式规范当成审稿攻击，除非它导致核心证据不可复核；
- 不用内部 Skill 术语替代作者可读的中文说明。

## 完成标准

- 每个候选项绑定 `target_arrow_id`；
- 每个候选项说明其 parent claim 和可能瓶颈状态；
- 中文文献或制度语境需求进入 `chinese-literature-gap-request.md`；
- `chinese-literature-gap-request.md` 已具备转入 `cnki-request-ledger.md` 的字段，不只是自然语言提醒；
- 只影响表达或格式的点与核心论证断点分离；
- 输出可以被 `academic-field-evidence-learning` 和 `academic-argument-issue-selection` 消费。
