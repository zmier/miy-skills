---
date: 2026-06-19
type: reference
status: structural-green
scope:
  - workflow-argument-validity
---

# 论证树核心模型

## 目的

把任意文本的“作者想让读者相信什么”恢复为一棵可检查的论证树。

```text
evidence / premise
-> subclaim
-> root claim
```

论证树不是文章目录，而是支撑关系图。

## 节点类型

关键 claim 节点必须先写成可判真假的命题。尤其是 `root claim`、`major support`、`subclaim` 和学术论文中的 `X2`，不得只写成“问题有意义”“核心发现成立”“机制检验”“贡献成立”这类标签。

命题化规则见 `proposition-form-core.md`。形式逻辑是主骨架；论文写作或研究设计标签只是辅助说明。

| 节点 | 含义 | 示例 |
|---|---|---|
| root claim | 最终要证明的结论 | 论文值得发表；政策应推行；材料结论可信 |
| major support | 一级支撑 | 问题有意义；作者证明了具体核心发现；方案有效 |
| subclaim | 二级/三级分论点 | gap 存在；识别可信；结果支持 |
| evidence | 事实、数据、文献、结果、案例 | 回归表；调查数据；报道事实 |
| hidden premise | 隐含前提 | 该指标能代表构念；样本可外推 |

## 箭头类型

| 箭头 | 含义 |
|---|---|
| direct support | A 直接支持 B |
| joint support | A + B + C 合推 D |
| serial support | A -> B -> C |
| split support | A 被用来支持 B / C / D |
| hidden support | A 需要隐含前提 H 才能支持 B |

## 通用流程

1. 找根结论；
2. 找一级支撑；
3. 找二级 / 三级支撑；
4. 找证据节点；
5. 补隐含前提；
6. 为每条箭头标注支撑关系；
7. 回原文校正是否误读。

## 学术论文默认根结构

学术论文通常不是只证明 `X -> Y`，而是在证明：

```text
X1：问题有意义
+ X2：作者证明了具体核心发现
-> Y：论文值得发表 / 贡献成立
```

其中：

```text
gap + importance + novelty + unresolved puzzle -> X1
theory + measurement + data + identification + results + robustness/mechanism -> X2
```

`X2` 不能只写成“作者做出来了”或“核心发现成立”。必须先还原作者的一句话发现：

```text
哪几个 X
通过什么机制 M
影响哪几个 Y
是否进一步上升到 Y2 / 政策启示 / 贡献声称
```

更严格地说，`X2` 必须能还原成形式逻辑视角下的简单命题或复合命题，例如直言、假言、联言或选言命题。`X/M/Y/Y2` 只帮助定位命题成分，不能替代命题本身。

建议同时保留：

```text
logical_form
full_logical_restoration
readable_compressed_version
component_propositions
research_function_label
```

其中 `full_logical_restoration` 用于保证命题结构完整，`readable_compressed_version` 用于保留锋利的一句话表达。

学术论文论证树还应继续展开到底层 evidence nodes：

```text
表格 / 系数 / 显著性 / 变量定义 / 模型设定 / 文献引用 / 原文段落
-> evidence node
-> subclaim
-> X1 / X2 / Y
```

如果表格、系数、t 值、标准误或显著性没有在当前底稿中保留，必须标注 `needs-table-qc`，不能伪造具体数值。

建立 evidence ledger 后，还应至少生成一版 evidence-expanded Mermaid view，把关键证据节点画回树上：

```text
E-* 具体证据
-> e 子观点
-> G/P 中层命题
-> X1 / X2 / Y
```

否则只能说明“证据被记录了”，不能说明“树真的变茂盛了”。

## 完成标准

- 根结论明确；
- 至少一层支撑节点明确；
- 每个关键节点有原文或证据来源；
- 关键 claim 节点能表述为形式逻辑视角下的简单命题或复合命题；
- 学术论文场景下，X2 必须写成具体核心发现句，而不是抽象标签；
- 学术论文场景下，关键支撑应有 evidence ledger，追溯到表格、系数、显著性、变量定义、模型设定、文献引用或原文段落；
- 学术论文场景下，关键 evidence node 应画回 Mermaid，形成可见的证据叶子；
- 隐含前提没有被当成已证明事实；
- 论证树能转成 Mermaid `flowchart BT`。
