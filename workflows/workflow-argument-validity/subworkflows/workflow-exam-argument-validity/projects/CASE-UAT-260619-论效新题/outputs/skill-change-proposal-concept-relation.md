# Skill 变更提案：概念关系审查

- 来源案例：CASE-UAT-260619 论效新题
- 触发证据：`outputs/reference-comparison.md` 中，blind-run 命中主干断点，但 reference comparison 暴露出“财富滚滚而来 / 财富积累”等概念颗粒度漏点。
- 当前 Skill：
  - `workflow-exam-argument-validity`
  - `workflow-argument-validity`
  - `course-driven-skill-engineering`
- 问题类型：`missing-rule / refinement-rule`
- 建议：`update-existing`

## 泛化判断

- 可复用问题：论效题或审稿材料中，作者常用一个概念推出另一个概念，但两个概念之间并非同一关系。
- 触发条件：
  - 同一段或同一条论证链中出现多个相近概念；
  - 作者把 A 当作 B 的理由；
  - A 与 B 看似相关，但未说明二者关系。
- 停止条件：
  - 已判断 A 与 B 的关系属于同一、包含、交叉、并列相容、无关、手段目的或因果；
  - 已说明该关系是否足以支撑箭头。
- 不适用范围：
  - 纯事实陈述，不承担推理功能的概念；
  - 只是修辞重复、未改变论证链的同义替换。
- 是否含个案固定值：`no`

## 实现

- 修改文件：
  - `references/exam-reading-rules.md`
  - `../../references/arrow-break-taxonomy.md`
  - `outputs/reference-comparison.md`
  - `outputs/revision-notes.md`
  - `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/course-driven-skill-engineering/SKILL.md`
- 新增 reference/script/asset：无
- 总编排路由变化：无
- 模板变化：无

## 验证

- 来源案例回归：CASE-UAT-260619 已通过 reference comparison。
- 既有案例回归：不影响既有四件套输出契约；只是增强读题和断点分类。
- 新案例 forward-test：待第二个论效题样本验证。
- 迁移状态：`partial / forward-test-pass-on-source-case`

## 反哺结论

正式反哺不是“速度/总量、手段/结果、局部/整体”这些碎片项，而是：

> 当材料用一个概念推出另一个概念时，先判断两个概念之间的关系：同一、包含、交叉、并列相容、无关、手段目的或因果。若作者把“部分”当“整体”、把“有交集”当“可替代”、把“可并存”当“对立”、把“一种手段”当“唯一必要手段”，则形成断裂箭头。
