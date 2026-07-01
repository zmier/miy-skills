# Manual Review Protocol

## Step 1. 固定论文顶层论证

用以下结构读稿件：

```text
X1：问题有意义
+ X2：作者证明了具体核心发现
-> Y：论文值得发表 / 贡献成立
```

`X2` 不能只写抽象标签；必须先写一句话核心发现：

```text
哪个 X
通过什么机制 M
影响哪个 Y
是否上升到 Y2 / 政策启示 / 贡献声称
```

输出到 `outputs/paper-argument-tree.md`。

## Step 2. 抽取证据节点

将稿件内容放入对应节点：

| 节点 | 证据类型 |
|---|---|
| X1 | gap、importance、novelty、unresolved puzzle |
| X2 | theory、construct-measure fit、data/sample fit、identification、results、robustness/mechanism |
| Y | contribution claim、publication-worthiness、responds-to-gap |

同时建立底层证据台账：

```text
evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度
```

若表格具体值无法从当前底稿核实，标记 `needs-table-qc`。

## Step 3. 映射欣媛审稿意见

每条 major concern 必须映射到：

```text
review issue -> target arrow -> weakened node -> impact on Y
```

输出到 `outputs/review-issue-arrow-map.md`。

## Step 4. 判断 adapter 缺口

比较当前 `academic-review-argument-audit` 是否已经覆盖这些箭头类型：

```text
covered / partially-covered / missing
```

输出到 `outputs/adapter-gap-analysis.md`。

## Step 5. 反哺建议

只把可迁移规则写入 `outputs/workflow-feedback.md`：

- 规则从哪里来；
- 证据是什么；
- 应进入父 workflow、adapter reference、模板还是 test；
- 哪些内容留在 case。

## Step 6. UAT

按照 `acceptance-contract.md` 判断本 TASK 是否通过。
