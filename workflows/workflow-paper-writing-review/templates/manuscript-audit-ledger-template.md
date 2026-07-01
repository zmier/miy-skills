---
type: template
name: manuscript-audit-ledger
status: draft
---

# Manuscript Audit Ledger

## 使用场景

用于论文审稿、投稿前自审或返修前问题盘点。该模板只保存问题台账结构，不保存保密稿件正文。

## 基本信息

| 字段 | 内容 |
|---|---|
| project_id |  |
| manuscript_id |  |
| journal_or_target |  |
| title |  |
| review_deadline |  |
| task_type | external-review / pre-submission-audit / revision-audit |
| source_project |  |

## 通读检查

| 步骤 | 状态 | 备注 |
|---|---|---|
| 核对利益冲突 | unexamined |  |
| 检查重复发表、数据造假或抄袭等高风险信号 | unexamined |  |
| 通读摘要与引言 | unexamined |  |
| 通读理论/机制部分 | unexamined |  |
| 通读数据、变量与方法部分 | unexamined |  |
| 通读主要结果与稳健性 | unexamined |  |
| 通读结论与贡献叙事 | unexamined |  |

## 贡献链还原

| 节点 | 作者声称 | 当前状态 | 备注 |
|---|---|---|---|
| 研究问题 |  | unexamined |  |
| 文献缺口 |  | unexamined |  |
| 理论机制 |  | unexamined |  |
| 识别策略 / 研究设计 |  | unexamined |  |
| 数据、变量和样本 |  | unexamined |  |
| 结果、稳健性和边界 |  | unexamined |  |
| 贡献叙事 |  | unexamined |  |
| 表达、引用和结构 |  | unexamined |  |

## 问题台账

| issue_id | section | quality_dimension | claim_or_component | concern | evidence_needed | severity | author_action | editor_visibility | author_visibility | status |
|---|---|---|---|---|---|---|---|---|---|---|
| I-001 |  |  |  |  |  | major / moderate / minor |  | yes / no | yes / no | unexamined |

## 推荐意见校准

| 项目 | 判断 |
|---|---|
| 主要问题数量 |  |
| 是否存在根本性识别或设计问题 |  |
| 是否存在伦理、重复发表或数据可信度风险 |  |
| 是否适合写给编辑 |  |
| 是否适合写给作者 |  |
| 候选推荐意见 | accept / minor / major / reject |

## 审稿表单映射

| 表单位置 | 台账对应材料 |
|---|---|
| Recommendation | 推荐意见校准 |
| Confidential Comments to the Editors | 只给编辑看的判断、风险、推荐理由 |
| Comments to the Author | 可执行、具体、不给出身份信息的作者意见 |
| Attach Files | 如需附件，另在项目 review 目录准备 |

## Workflow 回流

| 可迁移发现 | 是否进入 workflow | 目标位置 |
|---|---|---|
|  | yes / no |  |
