# Skill 变更提案

- 来源案例：CASE-J-260110-xinyuan-review
- 触发证据：欣媛审稿意见对理论前提、样本筛选、变量指标、计量设定和机制排除的结构化批评
- 当前 Skill：`academic-review-argument-audit`
- 问题类型：`missing-rule / template-gap`
- 建议：`update-existing`

## 泛化判断

- 可复用问题：
  - 同一理论前提在不同模块中是否一致；
  - 样本筛选是否剔除机制最相关事件；
  - 溢出效应是否需要 direct effect baseline；
  - 机制排除是否存在反向解释；
  - 稳健性是否回应核心质疑。
- 触发条件：
  - 审稿对象为经验论文；
  - 作者有机制、异质性、溢出效应、同群效应或政策建议；
  - 用户问“贡献是否成立”“机制是否可靠”“审稿意见怎么写得有力”。
- 停止条件：
  - 已输出 argument-validity map；
  - 已区分可迁移规则和个案判断；
  - 已进入 review issue ledger 或 review material。
- 不适用范围：
  - 纯理论论文；
  - 没有经验识别和机制链的短评；
  - 仅做语言润色的任务。
- 是否含个案固定值：`no`

## 实现

- 修改文件：
  - `skills/academic-review-argument-audit/SKILL.md`
  - `references/source-provenance.md`
  - `tests/argument-validity-fixtures.md`
- 新增 reference/script/asset：
  - `skills/academic-review-argument-audit/references/case-derived-review-patterns.md`
- 总编排路由变化：
  - 无需修改 paper workflow 主路线；
  - adapter 内部新增 case-derived trigger。
- 模板变化：
  - 暂不改通用模板；
  - 后续可把 strong-review concern 模板加入 assets。

## 验证

- 来源案例回归：J-260110 能解释欣媛审稿意见结构。
- 既有案例回归：不影响 EMFT 审稿 workflow。
- 新案例 forward-test：pending。
- 迁移状态：`partial / forward-test-pending`
