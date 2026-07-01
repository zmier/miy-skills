# CASE-J-260110 Xinyuan Review

状态：`case-study / comparison / structural-green / forward-test-pending`

## 目标

使用 J-260110 真实审稿案例，检验并反哺：

- `workflow-argument-validity`;
- `skills/argument-validity-audit`;
- `skills/academic-review-argument-audit`;
- `workflow-paper-writing-review` 中的最终审稿写作与 issue 组装环节。

核心问题：

```text
欣媛审稿意见是否体现了论证有效性分析方法？
哪些写法可迁移为审稿 adapter 的规则、模板或测试？
哪些只是个案判断，不能进入通用 Skill？
```

## 输入来源

源项目：

```text
/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/
```

主要材料：

- 稿件 Markdown：`企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.md`
- 审稿意见：`欣媛-企业主动披露-审稿意见.docx`
- 审稿笔记：`J-260110-审稿.md`

本 case 已复制必要证据到 `inputs/`，作为 case-local evidence bundle，便于以后离开源项目也能读懂本案例。证据全文只服务于本 case 的追溯、复核和 forward-test 设计，不进入通用 workflow 或 Skill 主流程。

| case-local 文件 | 来源 | 作用 |
|---|---|---|
| `inputs/manuscript.md` | 稿件 Markdown | 复核欣媛审稿意见所批评的原文论证链 |
| `inputs/xinyuan-review.docx` | 欣媛审稿意见原始 Word | 保留原始审稿意见格式与来源 |
| `inputs/xinyuan-review.txt` | `xinyuan-review.docx` 转换 | 便于检索、diff 和后续自动分析 |
| `inputs/source-review-notes.md` | `J-260110-审稿.md` | 保留源项目中的审稿笔记上下文 |

## 输出

| 文件 | 作用 |
|---|---|
| `case-charter.md` | 课程驱动 Skill 工程契约 |
| `inputs/README.md` | case-local evidence bundle 说明 |
| `outputs/xinyuan-review-argument-map.md` | 欣媛审稿意见中的论证有效性结构图 |
| `outputs/course-method-alignment.md` | 与课程忠实提取稿的对应关系 |
| `outputs/skill-gap-analysis.md` | 当前 Skill 缺口 |
| `outputs/skill-change-proposal.md` | 可迁移变更提案 |
| `outputs/UAT.md` | structural-green 验收 |

## TASK 树

| TASK | 状态 | 目标 | 入口 |
|---|---|---|---|
| TASK01-学术论文论证树迁移校准 | done / case-calibration-green / subworkflow-recommended | 以 `workflow-argument-validity` 为主轴，把 J-260110 稿件抽成 `X1 + X2 -> Y` 学术论文论证树，并将欣媛审稿意见映射到断裂箭头 | `tasks/TASK01-学术论文论证树迁移校准/TASK01-说明.md` |

TASK01 与既有 case 输出的关系：

```text
既有 outputs/
-> 说明欣媛审稿意见如何体现论证有效性写法

TASK01
-> 进一步校准“学术论文如何被读成论证树”
-> 为是否创建 workflow-academic-review-argument 子 workflow 提供证据
```

## 触发的对话洞见

| 文件 | 关系 |
|---|---|
| `../../references/dialogues/001-学术论文的双层论证与汇合箭头.md` | 本 case 讨论过程中触发的 dialogue insight；用于保留“学术论文双层论证与汇合箭头”的原始问答和候选方法论命题 |
| `../../references/dialogues/002-论文的顶层发表正当性论证.md` | 本 case 讨论过程中继续触发的 dialogue insight；用于保留“X1 问题有意义 + X2 作者做出来 -> Y 值得发表”的原始问答和候选方法论命题 |
| `../../references/dialogues/003-论证作为判断决策与治理的母结构.md` | 本 case 讨论过程中继续触发的高阶 dialogue insight；用于保留“拆搭箭头”向判断、决策与治理泛化的原始问答，但暂不改变审稿主流程 |
| `../../references/dialogues/004-论效题审稿与自下而上的论证树.md` | 从高阶泛化收回审稿后形成的 dialogue insight；用于保留“论效题与审稿都先绘制论证树，再用 Mermaid 自下而上表达支撑方向”的方法论发现 |

## 迁移边界

- 可以迁移：审稿意见如何定位、分析、回扣、建议；如何组织 major concern；如何识别 evidence-claim mismatch。
- TASK01 进一步检验：学术论文 `X1: 问题有意义`、`X2: 作者证明了具体核心发现`、`Y: 贡献成立 / 值得发表` 的论证树是否能解释真实审稿意见；其中 `X2` 必须写清哪个 X 通过什么机制 M 影响哪个 Y。
- 不迁移：具体稿件判断、作者/期刊信息、最终推荐意见、保密内容。
- 当前只证明来源案例可解释，不证明新案例可迁移。
