# Dialogue Insight Feedback

用于把用户与 Codex 在心流讨论、困惑澄清、案例复盘或方法论脑暴中共同生成的洞见，沉淀为可追溯、可回顾、可迁移的 workflow / Skill 改进。

## 适用信号

当出现以下信号时，按 `dialogue-insight` 处理：

- 用户说“这个发现很重要”“值得沉淀”“我们是不是应该重构 workflow”；
- 对话中出现新的分类、主轴、层级关系或判断框架；
- 发现不是直接来自课程原文、案例证据或外部资料，而是由共同推理生成；
- 某个真实 case 触发了超出该 case 的方法论发现；
- 当前不适合立刻改 Skill，但明显需要保留问题形状。

## 三层保存

| 层级 | 保存内容 | 推荐位置 |
|---|---|---|
| case evidence | 原始案例、输入材料、日志、证据 | `projects/CASE-*/inputs/` |
| dialogue insight | 用户原话、Codex 当时回答、原始困惑、共同发现、候选命题 | `references/dialogues/` 或 `projects/CASE-*/dialogue-insights/` |
| skill rule | 已回顾、去个案化、可执行、可验证的规则 | `SKILL.md`、`references/`、`assets/`、`tests/` |

原则：

- case 保存证据；
- dialogue 保存共同思考；
- Skill 保存成熟规则。

## 推荐流程

1. **捕捉**
   - 用 `assets/dialogue-insight-template.md` 创建札记；
   - 保留用户原始问题、Codex 当时回答的核心表达，以及双方共同推进出的关键表述；
   - 标注触发场域，例如 course、field case、technology radar 或 ordinary dialogue。
2. **命名**
   - 使用序号加短标题，例如 `001-review-as-expanded-argument-validity.md`；
   - 中文工作流可用中文标题，但文件名保持可检索。
3. **分层**
   - `raw dialogue`：原始困惑和问答，包括用户原话、Codex 当时回答和必要上下文；
   - `shared discovery`：对话中共同生成的发现；
   - `candidate principle`：可能迁移的方法论命题；
   - `skill implication`：可能修改的 workflow、Skill、reference、asset 或 test。
4. **回顾**
   - 讨论告一段落后再判断是否升级；
   - 不在心流讨论过程中强行工程化全部内容；
   - 若洞见仍含个案固定值，只留在 dialogue 或 case，不进入通用 Skill。
5. **反哺**
   - 进入 reference：适合解释型、判断型、低频但有价值的内容；
   - 进入 SKILL.md：适合高频、稳定、会改变默认行为的规则；
   - 进入 asset/template：适合可复制结构；
   - 进入 tests/fixture：适合迁移验证或回归样本。

## 状态标记

| 状态 | 含义 |
|---|---|
| `captured` | 已保存原始对话和洞见 |
| `review-pending` | 尚未判断是否反哺 |
| `reference-integrated` | 已进入 reference，但不改变默认主流程 |
| `workflow-integrated` | 已改变 workflow 主轴、路由或阶段 |
| `skill-integrated` | 已进入某个 Skill 的默认规则或触发规则 |
| `template-integrated` | 已进入 asset/template |
| `forward-test-pending` | 尚未在新案例验证 |
| `validated` | 已在未参与提炼的新案例上通过 |

## 反哺判断

对每个候选洞见回答：

1. 它是新的方法论判断，还是个案感受？
2. 它是否改变 Codex 下次执行任务时的路线选择？
3. 它是否能写成可操作的输入、动作、输出或验收标准？
4. 它是否需要专业证据或新案例验证？
5. 它应该保留为 dialogue、进入 reference，还是升级为 Skill 主流程？

## 边界

- 不把未经回顾的聊天表达直接写入通用 Skill 主流程。
- 不把单个 case 的结论伪装成普遍规则。
- 不为了“沉淀”打断心流讨论；可以先临时记录，讨论结束后整理。
- 若包含私有审稿、商业、账号或敏感材料，dialogue 中只保留必要摘要和本地路径。
- 若一个洞见由真实 case 触发，case README 应链接 dialogue；dialogue 应链接 case 证据。
