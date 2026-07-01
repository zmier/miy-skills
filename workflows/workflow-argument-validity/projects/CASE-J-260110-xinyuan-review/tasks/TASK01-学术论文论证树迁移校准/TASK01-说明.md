# TASK01 学术论文论证树迁移校准

## 定位

本 TASK 是 `CASE-J-260110-xinyuan-review` 的子任务，用于把 `workflow-argument-validity` 从论效题 / GRE Argument 迁移到学术论文审稿场景。

本 TASK 暂不以 `workflow-paper-writing-review` 为主轴，而是以 `workflow-argument-validity` 的论证树主轴为核心：

```text
恢复论文论证树
-> 检查支撑箭头
-> 标注断点影响
-> 映射到审稿意见
-> 判断哪些规则可反哺 academic-review adapter
```

## 核心问题

用欣媛审稿案例校准：

```text
学术论文能否被读成一棵 X1 + X2 -> Y 的论证树？
欣媛审稿意见中的 major concerns 能否映射到这棵树上的断裂箭头？
哪些映射规则应进入 workflow-argument-validity / academic-review-argument-audit？
```

## 理论主轴

来自 `references/dialogues/001-004` 的对话洞见：

```text
X1：问题有意义
+ X2：作者证明了具体核心发现
-> Y：论文值得发表 / 贡献成立
```

其中：

```text
gap + importance + novelty + unresolved puzzle -> X1
theory + measurement + data + identification + results + robustness/mechanism -> X2
X1 + X2 + actually answers gap -> Y
```

## 输入

| 输入 | 位置 | 用途 |
|---|---|---|
| 稿件全文 Markdown | `../../inputs/manuscript.md` | 抽取作者自己的贡献链和证据节点 |
| 欣媛审稿意见 txt | `../../inputs/xinyuan-review.txt` | 将 major concerns 映射到断裂箭头 |
| 源项目审稿笔记 | `../../inputs/source-review-notes.md` | 补充当时审稿上下文 |
| 既有 argument map | `../../outputs/xinyuan-review-argument-map.md` | 复用上一轮 case 输出，避免重复分析 |
| 对话洞见 001-004 | `../../../../references/dialogues/` | 提供 X1/X2/Y 论证树主轴 |

## 预期输出

| 输出 | 内容 | 状态 |
|---|---|---|
| `outputs/paper-argument-tree.md` | 学术论文 X1/X2/Y 论证树与 Mermaid | done |
| `outputs/review-issue-arrow-map.md` | 欣媛审稿意见 major concerns -> 断裂箭头映射表 | done |
| `outputs/adapter-gap-analysis.md` | 当前 academic-review adapter 缺口 | done |
| `outputs/workflow-feedback.md` | 应反哺到父 workflow / adapter / reference 的规则 | done |
| `outputs/UAT.md` | 本 TASK 是否通过迁移校准验收 | done |
| `outputs/evidence-ledger.md` | 表格、系数、显著性、变量定义、文献引用等底层证据台账 | done |
| `logs/log.md` | ReAct 风格过程记录 | updated |

## Done 标准

- 产出一棵可读的学术论文论证树，根节点为 `Y: 论文值得发表 / 贡献成立`；
- 至少标出 `X1: 问题有意义` 与 `X2: 作者证明了具体核心发现` 两条一级支撑；
- `X2` 必须还原为一句话核心发现，写清哪个 X 通过什么机制 M 影响哪个 Y；
- 建立 `evidence-ledger.md`，把表格、系数、显著性、变量定义、模型设定、文献引用和原文段落追溯到对应节点/箭头；
- 若底稿缺少表格具体数值，标记 `needs-table-qc`，不得臆造；
- 至少将 5 条欣媛审稿意见映射到具体断裂箭头；
- 每条映射说明它削弱的是 `X1`、`X2` 还是 `Y`；
- 明确哪些规则可迁移，哪些只留在 J-260110 个案；
- 不把具体稿件内容、作者身份、期刊敏感信息写入通用 workflow / Skill 主流程；
- 给出是否创建 `workflow-academic-review-argument` 子 workflow 的建议。

## 边界

- 本 TASK 不重新审稿；
- 不判断 J-260110 最终录用建议；
- 不要求跑完整论文审稿业务流程；
- 不以 `workflow-paper-writing-review` 为主轴，只把它视作未来可调用的业务补充；
- 本 TASK 是 `prior-exposed / case-calibration`，不能作为 strict blind forward-test。
