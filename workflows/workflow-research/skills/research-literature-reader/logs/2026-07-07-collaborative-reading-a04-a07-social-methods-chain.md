# Collaborative Reading: A04-A07 社会研究方法链条升级

## 背景

在 A01-A03 已经稳定为：

```text
A01 = 命题 / 假设
A02 = 概念、构念、理论关系、文献基础
A03 = 概念操作化 / proxy bridge
```

之后，需要继续把 A04-A07 从旧的论文八股栏目升级为《社会研究方法》意义上的经验研究链条。

## 核心调整

旧结构：

```text
A04 = Main mechanism
A05 = Literature conversation
A06 = Research gap
A07 = Identification / empirical design
```

新结构：

```text
A04 = Measurement / Data Construction
A05 = Research Design / Identification Strategy
A06 = Data Analysis / Empirical Results
A07 = Alternative Explanations / Robustness / Validity Threats
```

## 认知依据

操作化还不是测量，测量也不是研究设计；研究设计也不等于结果或稳健性。

因此 A03 之后应继续追问：

```text
A04:
  这个 proxy / measure 在数据中到底如何被量出来？

A05:
  作者如何把变量组织成对 Pi-R 的检验？

A06:
  资料分析和结果是否支持 Pi-R？

A07:
  为什么不是别的原因，为什么结果不是口径、样本、模型或测量偶然造成的？
```

## 机制、文献和 gap 的新位置

机制、文献对话和 research gap 仍然重要，但不再默认占用 A04-A06 的主编号。

```text
机制 / warrant:
  挂回 A02 的 Pi-R、A05 的设计逻辑、A06 的机制性结果，或 A07 的 diagnostic pattern。

文献对话 / knowledge base:
  优先写入 A02 的 Pi-KB；必要时在 A08 项目迁移中总结。

research gap:
  优先写入 A02 的 Pi-KB 和 A08 的迁移判断；若服务整篇论文，可标 P-all。
```

这样做的目的不是削弱机制、文献和 gap，而是把它们放回“作者如何论证核心命题”的链条中。

## 文件变更

- `collaborative-reading/SKILL.md`
  - 更新 Proposition ID System 中 A04-A07 的回挂含义。
  - 新增 `A04-A07 Research Methods Chain`。
  - 明确 A04/A05/A06/A07 的边界和默认检查问题。

- `collaborative-reading/templates/discussion-outline-template.md`
  - Discussion Agenda 改为 A04-A07 方法链条。
  - 新增 Measurement Table、Design Table、Results Table、Validity Threat Table。
  - 更新 A02/A03 prompts 中的后续 Agenda 指向。

## 后续建议

下一步可用 `miy-uat` 做一次黑箱或灰箱验收，验证新模板是否会自然产出：

```text
A04 measurement/data construction
A05 research design/identification
A06 empirical results
A07 validity threats/robustness
```

而不是复发旧结构。

