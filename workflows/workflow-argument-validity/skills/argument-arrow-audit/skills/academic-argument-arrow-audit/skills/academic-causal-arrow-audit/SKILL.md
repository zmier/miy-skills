---
name: academic-causal-arrow-audit
description: 学术论文因果识别箭头审计子 Skill。用于审查作者是否能用识别设计、模型、工具变量、DID/PSM/RDD/事件研究或 DAG 论证推出因果声称；输出 causal-arrow-audit ledger，不负责选择审稿重点。
---

# Academic Causal Arrow Audit

## 定位

本子 Skill 审查：

```text
design / model / identification evidence -> causal claim
```

核心问题：

```text
作者的设计是否足以支持“X 导致 Y”？
```

## 输入

- 目标 `arrow_id`；
- X、Y、M、样本、时间结构；
- 识别策略：DID、IV、PSM、RDD、事件研究、自然实验、实验设计等；
- 模型公式、固定效应、控制变量、聚类层级；
- 表格、系数、显著性、稳健性和机制检验 evidence_ids；
- 作者声称排除的替代解释。

## 审查主轴

1. 固定因果声称：

   ```text
   作者声称 X caused / affected / improved / reduced Y。
   ```

2. 还原设计逻辑：

   ```text
   哪个外生变化或比较结构识别 X？
   处理组和对照组是谁？
   反事实是什么？
   ```

3. DAG / 路径检查：

   ```text
   共同原因是否仍打开？
   反向因果是否可能？
   是否控制了中介或 collider？
   是否有前门路径声称？
   ```

4. 方法假设检查：

   ```text
   DID: parallel trends / anticipation / treatment timing / spillover
   IV: relevance / exclusion / monotonicity / first-stage strength
   PSM: observables only / balance / overlap
   RDD: cutoff manipulation / continuity / bandwidth
   event study: pre-trend / window / confounding events
   ```

5. 输出因果箭头状态：

   ```text
   strong / strong-with-qc / weak / broken / unclear / needs-qc / needs-external-evidence
   ```

   若是方法知识或人工复核缺口，一级 `status` 用 `needs-qc` 或 `unclear`，并在父表 `qc_flags` 写 `method-qc`、`cluster-level-qc`、`pretrend-qc` 等；不要把 `needs-method-qc` 当作一级 status。

## 输出

```text
causal_arrow_audit:
  arrow_id:
  causal_claim:
  design_logic_plain_language:
  dag_notes:
  open_backdoor_paths:
  reverse_causality_risk:
  method_assumption_status:
  evidence_ids:
  status:
  why_it_breaks_or_holds:
  impact_on_X2_or_Y:
  fix_or_downgrade:
```

## 完成标准

- 不把“显著相关”当成因果成立；
- 不只写方法名，必须写方法如何识别 X；
- 不要求所有设计完美，但必须说明剩余威胁影响哪条箭头；
- 若方法知识不足，写入 `method_knowledge_gap`，交回父 Skill。
