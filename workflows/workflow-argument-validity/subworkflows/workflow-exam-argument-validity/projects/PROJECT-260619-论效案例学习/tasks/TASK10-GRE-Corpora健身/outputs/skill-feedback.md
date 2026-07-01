---
task: TASK10-GRE-Corpora健身
stage: skill-feedback
status: candidate-applied
---

# TASK10 Skill Feedback

## 候选反哺 1：假设影响链

### 规则

当题目要求分析 assumptions / hidden premises 时，每个问题都必须写成：

```text
假设是什么 -> 它支撑哪条箭头 -> 如果它不成立，上层结论如何降级或断裂
```

### 泛化价值

这不仅适用于 GRE，也适用于：

- 学术审稿中 `identification -> causal claim`；
- 论文写作自审中 `measure -> construct`；
- 政策报告中 `pilot result -> national rollout`；
- 论效题中“只问问题但没有说明影响”的失分段。

## 候选反哺 2：问题型输出展开

### 规则

只提出“是否可能存在其他原因？”还不够。必须补充：

```text
如果答案是 yes/no，作者结论会怎样改变？
```

### 目标文件

- `references/output-ladder.md`
- `references/text-type-routing.md`
- 父层 `SKILL.md` 的输出契约

## 候选反哺 3：GRE Argument 路由

GRE Analyze an Argument 与中文论效题同属“逆向验收论证”，但输出格式不同：

| 项目 | 中文论效题 | GRE Analyze an Argument |
|---|---|---|
| 核心动作 | 找断点并写本论段 | 找 assumptions 并解释 implications |
| 典型段落 | 定位 -> 分析 -> 收尾 | assumption -> why needed -> if false |
| 评分重点 | 逻辑问题是否抓准，行文是否清楚 | 是否回应 instruction，是否展开假设影响 |

当前不必新建 `workflow-gre-argument`，先作为父 workflow 的路由分支；若 TASK11 再次证明差异稳定，再考虑抽子 workflow。
