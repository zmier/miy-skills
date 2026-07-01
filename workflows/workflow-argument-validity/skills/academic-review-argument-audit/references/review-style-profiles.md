---
date: 2026-06-21
type: reference
status: seed
scope:
  - academic-review-argument-audit
---

# Review Style Profiles

本文件只控制“怎么写”，不控制“写什么”。审稿意见的事实内容必须来自 `review-issue-arrow-map.md`、`major-concern-candidates.md`、`arrow-repair-map.md` 等前序产物。

## 通用字段

`drafting-brief.md` 应声明：

```text
style_profile:
audience:
decision_posture:
language_policy:
allowed_reference_material:
output_forms:
qc_guardrail:
tone:
length:
```

## xinyuan-argument

适合：管理学、经济学、社科论文，或需要解释“为什么这是核心论证问题”的审稿。

特点：

- 先还原作者论证链；
- 再说明证据与上升 claim 之间的断裂；
- 强调贡献边界、理论机制、构念-指标匹配和证据闭环；
- 语气克制，但逻辑压强强；
- 少堆实验名，多解释“为什么这会影响结论成立”。

段落骨架：

```text
作者试图用 A 支撑 B，并进一步推出 C。
然而，A 更直接说明的是 A1；若要推出 B/C，还需要证明 ...
因此，当前证据更适合支持一个较弱的结论 ...
建议作者补充 ...，或将贡献表述降调为 ...
```

## materials-reviewer

适合：材料、器件、能源收集、传感器、柔性电子、可穿戴等工程实验论文。

特点：

- 问题直接；
- 逐条点出缺少哪些实验、指标、图表或补充材料；
- 具体写出 zeta potential、EIS、EDS mapping、BET、contact angle、load resistance、bending/washing cycles 等；
- 更像真实工程审稿人：少讲抽象理论，多讲证据包是否够。

段落骨架：

```text
The authors attribute ... to ...
However, the current evidence is mostly qualitative / indirect.
To support this claim, the authors should provide ...
Without these data, the claim should be tempered to ...
```

## hybrid-argument-materials

适合：本 workflow 默认的材料/器件学术审稿草稿。

特点：

- 先用论证语言说明 A -> B -> C 的断裂；
- 再用材料审稿人风格给出具体实验包；
- 既能让审稿意见有“为什么重要”，也能让作者知道“补什么”。

段落骨架：

```text
The manuscript uses A as evidence for B and then extends this to C.
The difficulty is that A only establishes ...
For this claim to be convincing, the authors would need to provide ...
If such evidence is not available, the claim should be reframed as ...
```

## concise-journal

适合：期刊系统表单、篇幅很紧或只需要粘贴短评。

特点：

- 3-5 个 major comments；
- 每条只保留 concern、why it matters、action request；
- 不展开 workflow 术语；
- 不写内部 issue id。

## developmental

适合：希望鼓励作者修改、论文有潜力但证据链需要增强。

特点：

- 开头肯定问题意识和潜在贡献；
- 重大问题写成“如何使论文更有说服力”；
- 语气建设性，避免 reject-like wording；
- 保留清晰的行动项。

## strict-reject

适合：用户明确要求拒稿或论文核心结论不可修复。

特点：

- 聚焦不可修复或高成本修复的根问题；
- 少给大量可补实验清单；
- 给编辑的理由比给作者的修改路线更重要；
- 语气克制，不使用情绪化词语。

## Guardrail

无论使用哪种风格：

- 不新增没有 issue id / target arrow / evidence 的重大问题；
- 不把 `hold-for-qc` 写成 confirmed error；
- 不把内部 workflow 术语直接写进 author-facing comments；
- 中文版和英文版判断强度必须一致；
- 具体实验请求必须来自 repair map、field learning、真实审稿 case 或稳定 reference menu。

