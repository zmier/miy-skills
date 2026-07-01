---
date: 2026-06-20
type: reference
status: structural-green
scope:
  - academic-argument-arrow-audit
---

# Subskill Boundary

## 原则

学术验箭头是复合 Skill，但不能把每个检查点都拆成子 Skill。拆分标准是：

```text
复杂度高
复用频率高
需要外部知识或工具
输出会被后续步骤复用
```

反之，轻量、稳定、只需填表和解释的判断，暂由父 Skill 承载。

## 适合子 Skill 化

| 箭头类型 | 是否子 Skill | 原因 |
|---|---|---|
| literature gap -> contribution | 是 | 经常需要检索、期刊门槛、知识树/文献谱系判断 |
| identification / design -> causal claim | 是 | 需要 DAG、后门/前门、识别假设、方法知识 |
| result table -> empirical finding | 是 | 需要显著性、量纲、经济意义、报告透明度和统计解释 |
| method-specific result -> method claim | 视情况 | DID/IV/RDD/NPLR/SEM 等高频后可拆 |

## 暂由父 Skill 承载

| 箭头类型 | 暂不拆原因 |
|---|---|
| construct -> measure | 高重要但路径相对稳定，可先用父层概念关系和 measurement mismatch 审 |
| sample rule -> mechanism-relevant sample | 先由父层检查样本与机制适配，反复复杂后再拆 |
| mechanism test -> mechanism claim | 先由父层处理；若需要大量中介/调节/实验机制方法，再拆 |
| robustness -> threat addressed | 先由父层按“稳健性是否回应目标威胁”审；若形成稳定方法库，再拆 |
| finding -> contribution / policy implication | 与选点和行文相邻，但验箭头阶段只诊断 overclaim，暂由父层承载 |
| materials/device experimental arrows | 先由 `materials-device-arrow-adapter.md` 承载；目前只 forward-tested once，不急于拆子 Skill |

## 升级流程

当父 Skill 遇到新的复杂方法或高频失败模式：

1. 在当前 TASK 的 `log.md` 记录；
2. 在 `method-knowledge-gap.md` 或 `workflow-feedback.md` 写明缺口；
3. 先沉淀为 reference 或 discipline adapter；
4. 至少一个新案例复用后，再升级成子 Skill；
5. 新子 Skill 必须声明输入、输出、完成标准和与父 Skill 的边界。

## 禁止事项

- 不因“名字像模块”就拆子 Skill；
- 不让子 Skill 重新抽作者树；
- 不让子 Skill 直接选择 major concern；
- 不把个案审稿判断硬编码为通用规则；
- 不让外部检索结果覆盖子 Skill 的原始产物状态。
