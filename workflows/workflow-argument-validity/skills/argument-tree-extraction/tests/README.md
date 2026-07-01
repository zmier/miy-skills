# Argument Tree Extraction Regression Tests

## Purpose

`argument-tree-extraction` 是复合型父 Skill。父入口、主轴、路由或输出契约发生变化时，必须检查子分支是否退化。

回归协议遵循：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-tao/references/regression-test-protocol.md
```

## Clean SubAgent Rule

Skill 修改触发的回归应优先由纯净 subAgent 执行：

- `fork_context=false`；
- 只读测试输入、被测 Skill、必要 references/assets 和测试目标；
- 禁读修改讨论、旧答案、人工期望、无关 TASK；
- 产物写入独立测试 TASK 或 `tests/runs/`；
- 与 baseline / target md 做质量对比。

## Branch Smoke Targets

| branch | target |
|---|---|
| academic | 能产出学术 full-tree；不丢 citation/table/figure evidence；2A/2B 分离 |
| exam | 不被学术 full-tree 污染；保持考试抽树的结论、论据、隐含假设、漏洞选点适配 |
| GRE | 不被中文论效或学术论文主轴污染；保持 GRE argument instruction 适配 |

## Suggested Layout

```text
tests/
├── README.md
├── fixtures/
│   ├── academic-smoke/
│   ├── exam-smoke/
│   └── gre-smoke/
├── runs/
└── regression-log.md
```

如果 fixture 尚未稳定，先在真实项目 TASK 中回归；通过多次复用后再迁移到 `tests/fixtures/`。

## Required Comparison Output

每次回归至少产出：

```text
regression-comparison.md
```

字段：

```text
test_id
changed_skill
branch
baseline_output
new_output
target_quality_doc
observed_improvement
observed_regression
pass_fail
next_action
```
