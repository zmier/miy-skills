# 课程案例 Skill 研发契约

## 基本信息

- 项目模式：`hybrid`
- 课程/单元：论证有效性分析课程；真实审稿意见案例
- 案例：J-260110《企业主动披露违规何以引导行业自律发展》及欣媛审稿意见
- 原始样本：`/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/`
- case-local evidence：`inputs/`
- 授权与安全边界：本地私有审稿项目；稿件全文与审稿意见可复制到本 case 的 `inputs/` 作为证据包，但不得复制到通用 workflow / Skill 主流程；不写入作者身份或期刊系统敏感信息
- 现有领域总编排：
  - `workflow-argument-validity`
  - `workflow-paper-writing-review`
- 当前 Skills 基线：
  - `argument-validity-audit`
  - `academic-review-argument-audit`
  - `manuscript-final-review-drafting`
  - `multi-agent-academic-review-qa`
  - `post-flight-review-verifier`

## 终点

- 最终复现目标：解释欣媛审稿意见中哪些段落符合“论据是否支持结论”的论证有效性写法，并提炼可迁移规则。
- 探索问题：
  - 欣媛审稿意见是否体现“少评论、多分析”？
  - 她如何定位作者论证链中的断点？
  - 当前 academic-review adapter 是否覆盖这些写法？
  - 哪些增量应进入 Skill/reference/template/test？
- 阶段终点类型：`explanation / coverage / deliverable`
- Smoke：能列出至少 5 类欣媛审稿意见中的论证断点，并映射到课程方法。
- Unit/阶段 Green：产出 argument map、alignment、skill gap、change proposal 和 UAT。
- 端到端验收：有明确变更建议进入 adapter reference，且不污染通用 Skill 主流程。
- 覆盖率声明：`阶段性`
- 明确不做：
  - 不重新审稿；
  - 不判断最终录用建议；
  - 不把全文证据复制到通用 workflow / Skill 主流程；
  - 不把欣媛个案判断写成通用规则。
- 停止条件：case 输出文件齐全，并完成 structural-green UAT。

## 阶段与冻结

- 当前阶段：`comparison / extraction / transfer`
- 独立性等级：`prior-exposed`
- 已读材料：
  - J-260110 稿件 Markdown 首部、方法与结果片段；
  - 欣媛审稿意见 docx 纯文本；
  - 论证有效性课程忠实提取稿。
- 已暴露的解法信息：
  - 欣媛审稿意见全文结构和主要问题；
  - 前序对该审稿意见的初步判断。
- blind 可读材料：不适用，本案例不声明 blind。
- 冻结的教师材料：无；课程材料已作为方法来源。
- 冻结的初始假设：不把“欣媛意见好”预设为结论；只检查其结构与方法。
- 解冻条件：不适用。
- 是否发生提前解冻：`no`

## 证据

| 结论 | 证据角色 | 来源 | 落盘位置 | 状态 |
|---|---|---|---|---|
| 欣媛意见大量采用定位-分析-建议结构 | primary | `inputs/xinyuan-review.docx`; `inputs/xinyuan-review.txt` | `outputs/course-method-alignment.md` | done |
| 欣媛意见覆盖多类论证断点 | primary | `inputs/xinyuan-review.txt` + `inputs/manuscript.md` | `outputs/xinyuan-review-argument-map.md` | done |
| 当前 adapter 需要补“强审稿段落模式” | exploratory | case 对照分析 | `outputs/skill-gap-analysis.md` | done |

## 探索性反馈

| 发现 | 类型 | 影响的路线 | 证据 | 是否反哺 Skill |
|---|---|---|---|---|
| 强审稿意见常先攻击核心故事线一致性 | field-discovery | `academic-review-argument-audit` | 概念界定与理论逻辑段 | yes |
| 样本筛选偏差可作为外部有效性 major concern 的主轴 | field-discovery | `academic-review-argument-audit` | 样本选择与外部有效性段 | yes |
| 机制排除也要审查反向解释 | field-discovery | `academic-review-argument-audit` | 信息传导机制排除段 | yes |
| 审稿意见中的语气可能需要 post-flight 调整 | field-boundary | final drafting / verifier | “基本常识”“低级错误”等措辞 | yes |

## Skill 工程状态

- 候选 Skill 变更：
  - 新增 `case-derived-review-patterns.md`;
  - 更新 `academic-review-argument-audit/SKILL.md`;
  - 更新 `tests/argument-validity-fixtures.md`;
  - 更新 `source-provenance.md`。
- 回归范围：
  - 不修改通用父 Skill 主流程；
  - 只补审稿 adapter 的 reference 和触发规则。
- 迁移案例：pending。
- 迁移状态：`partial / forward-test-pending`
