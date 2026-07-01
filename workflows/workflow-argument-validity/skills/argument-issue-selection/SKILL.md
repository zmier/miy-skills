---
name: argument-issue-selection
description: 通用论证问题选择复合 Skill。用于在 argument-arrow-audit 已经全量验箭头之后，从 weak、broken、unclear、needs-qc 或 needs-external-evidence 箭头中选择最值得写、最影响根结论、最符合任务目标的问题，并路由到论效题/GRE 选点或学术论文审稿 issue selection 子 Skill；对 needs-external-evidence 只能标为待外部证据增强或暂缓定性，不能写成已确认问题。
---

# Argument Issue Selection

## 定位

这是“选问题”的父复合 Skill。它位于验箭头之后、成文之前：

```text
argument-tree-extraction
-> argument-arrow-audit
-> argument-arrow-repair-mapping
-> argument-issue-selection
-> writing / review drafting
```

核心分层原则：

```text
验箭头是诊断层：A -> B 到底推不推得动。
修复映射是治疗方案层：断了以后补什么证据、实验、分析，或如何降调。
问题候选池是铺陈层：把所有可写断点摊开，不替用户过早删除。
选问题是决策层：这么多断点和修复方案里，这次要写哪几个。
```

不要把选题、选点、major concern 排序塞回验箭头 Skill。验箭头应尽量全量、忠实、低偏好；选问题才引入任务目标、篇幅、读者、可写性、审稿优先级和输出策略。

重要纪律：选问题 Skill 不能只输出最终 selected issues。必须先输出全量候选池，再输出建议选点方案。最终取舍由用户 / 主 Agent / 审稿人决定，subAgent 不得因为篇幅或自认为重复而删除候选池中的重要断点。

## 输入

- `arrow-audit-table.md` 或同等内容；
- `arrow-repair-map.md` 或同等修复映射；若没有，则只能基于诊断选择，并在输出中标记 `missing-repair-map`；
- `node-ledger.md` / `paper-argument-tree.md` / exam argument tree；
- 根结论或 `X1/X2/Y`；
- 任务目标：论效题、GRE prompt instruction、学术审稿、投稿前自审、局部论证改写；
- 可用篇幅、输出格式和用户偏好。

## 路由

| 场景 | 调用 |
|---|---|
| 中文论效题、GRE Analyze an Argument | `skills/exam-argument-issue-selection/SKILL.md` |
| 学术论文审稿、论文写作自审、投稿前自查 | `skills/academic-argument-issue-selection/SKILL.md` |
| 普通政策、商业、局部论证 | 使用父层协议直接选择问题，必要时沉淀新子 Skill |

## 通用选问题协议

1. 读取全量箭头审计表：

   ```text
   arrow_id | from_node | to_node | status | break_type | why_it_breaks | impact_on_root
   ```

2. 只从以下候选中选择：

   ```text
   weak
   broken
   unclear
   needs-qc
   needs-external-evidence
   ```

   `strong` 箭头一般不进入问题选择，除非任务是说明“哪些论证较稳”。

   `needs-external-evidence` 可以进入候选池，但在外部证据增强完成前，只能作为：

   ```text
   evidence-needed issue
   search-before-major
   hold-for-external-evidence
   ```

   不得直接写成 confirmed major concern。

3. 计算选择优先级：

   ```text
   影响根结论或 X1/X2/Y
   + 能清楚说明 A 为什么推不出 B
   + 有可定位证据或可明确说明需要补证据
   + 有可执行修复路径，或明确只能降调
   + 不与其他问题重复
   + 符合当前输出任务
   -> selected issue
   ```

4. 先生成全量候选池：
   - 所有 `weak / broken / unclear / needs-qc / needs-external-evidence` 箭头都必须进入候选池，除非明确标为 irrelevant；
   - 每个候选 issue 同时保留机器字段和人类可读字段；
   - 不得只输出 `A6 / E-X1 / qc_flags` 这类机器代号；
   - 必须写成接近 review draft / essay issue paragraph 的自然语言，使用户不用回查代码表也能读懂。

   每个候选至少包含：

   ```text
   issue_id
   target_arrow_id
   surface_issue: 表层问题
   deep_arrow_break: 深层箭头断点
   human_readable_summary: 2-4 句自然语言说明
   evidence_basis: 证据位置或 QC 缺口
   why_it_matters: 为什么影响上层结论
   possible_revision: 作者/写作者可如何修
   suggested_bucket: major-candidate / minor-candidate / revision-action / hold
   merge_split_advice: 可合并但不得丢失的点
   ```

5. 再生成建议选点方案：
   - 多个断点削弱同一上层节点时，可合并成一个问题；
   - 一个断点同时影响多个上层节点时，优先按最接近根结论的影响写；
   - 不把 minor reporting issue 升成核心问题，除非它影响主要箭头可信度。
   - 合并时必须保留每个子问题的人类可读解释，不得把深层断点压成“变量不透明”“方法不清楚”等泛泛标签。

6. 输出选择结果：

   ```text
   selected_issue_id
   target_arrow_id
   issue_claim
   weakened_node
   impact_on_root
   why_selected
   writing_route
   repair_route
   ```

## 输出

最小输出：

```text
full issue candidate pool:
  issue_id | target_arrow | surface_issue | deep_arrow_break | human_readable_summary | why_it_matters | possible_revision | suggested_bucket
selected issues:
  issue_id | target_arrow | why_selected | impact | repair_route | writing_route
discarded but noted:
  arrow_id | reason_not_selected
```

完整输出可按场景转为：

```text
exam-selected-issues.md
full-issue-candidate-pool.md
human-readable-issue-candidates.md
review-issue-arrow-map.md
major-concern-candidates.md
revision-action-map.md
```

## 子 Skill 分工

- `exam-argument-issue-selection`：从断点中选 3-4 个最可写问题，响应中文论效或 GRE prompt instruction。
- `academic-argument-issue-selection`：从学术箭头审计表中选 major concern、minor concern 或 revision action，生成 review issue arrow map。

## 边界

- 不重新抽树；
- 不重新全量验箭头；
- 不把未审计箭头直接选为问题；
- 不直接写最终作文或最终审稿意见；
- 不把“选中的问题”误认为“唯一存在的问题”。
- 不把全量候选池写成只有机器代号的 ledger；必须同时提供人能读懂、接近成文语气的候选说明。
