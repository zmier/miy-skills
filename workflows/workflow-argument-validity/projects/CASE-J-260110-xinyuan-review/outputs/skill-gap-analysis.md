# Skill Gap Analysis

## 当前 Skill 已覆盖

`academic-review-argument-audit` 已覆盖：

- 实际观察发现与上升发现是否 match；
- X/Y 操作化是否代表构念；
- 宏观概念或领域指标是否适配论文层级；
- 识别策略是否支撑 causal language；
- 结果是否越过证据；
- 中文可读性和术语背景桥。

## 来源案例暴露的新缺口

### Gap 1：核心故事线一致性审查还不够显式

欣媛最强的一条意见不是单点变量问题，而是指出作者在不同地方切换“披露行为的信号效应”和“披露内容的信息效应”。

当前 Skill 有“关键词一致性”，但缺少一个更强的检查：

```text
同一理论机制在不同表格、异质性、机制排除和结论解释中是否保持同一前提。
```

建议：新增 `storyline-premise-consistency` 检查。

### Gap 2：样本筛选规则的机制相关偏差

当前 Skill 会查样本和外部有效性，但没有明确要求：

```text
样本筛选是否剔除了最能检验作者机制的事件。
```

J-260110 中，剔除同业集中违规可能剔除市场关注度最高、溢出效应最可能强的事件。

建议：新增 `mechanism-relevant-sample-exclusion` 检查。

### Gap 3：直接效应作为溢出效应前提

欣媛指出：如果要说同行模仿，需要先看事件公司自身是否改善或获益。

当前 Skill 有“作者声称链”，但缺少：

```text
溢出效应 / 同群效应论文需检查 direct effect baseline。
```

建议：在 adapter reference 中补充，不写入通用父 Skill。

### Gap 4：机制排除不能只看结果不显著

当前 Skill 会查机制和替代解释，但案例提示一种常见模式：

```text
作者用某结果不显著排除机制；
但该不显著结果也可能是机制生效后的结果。
```

建议：新增 `mechanism-exclusion-reversal` 检查。

### Gap 5：稳健性是否回应核心质疑

当前 Skill 有“稳健性是否解决核心威胁”，但可强化成：

```text
常规稳健性检验不能替代针对核心断点的稳健性检验。
```

建议：写入 case-derived patterns。

### Gap 6：审稿语气 post-flight

欣媛意见结构强，但少数措辞压强偏高。当前 post-flight verifier 有语气和可读性规则，但 adapter 中没有把“保留锋利结构、降低人格化/情绪性措辞”写清。

建议：在 adapter 中补一句：case-derived patterns 只迁移结构，不迁移高压措辞。

## 不建议进入通用 Skill 的内容

| 内容 | 原因 |
|---|---|
| KV 指数边缘化判断 | 需要领域证据，不能通用化 |
| 具体 6 个月剔除规则 | 个案建议，不宜固定 |
| 具体文献引用 | 放在 TASK 或领域 reference，不进通用 Skill |
| 对该稿最终推荐意见 | 保密且个案化 |

## 推荐落点

| 增量 | 落点 |
|---|---|
| story premise consistency | `academic-review-argument-audit/references/case-derived-review-patterns.md` |
| mechanism-relevant sample exclusion | 同上 |
| direct effect baseline for spillover | 同上 |
| mechanism-exclusion reversal | 同上 |
| robustness must answer core threats | 同上 |
| tone downgrade note | `academic-review-argument-audit/SKILL.md` |
