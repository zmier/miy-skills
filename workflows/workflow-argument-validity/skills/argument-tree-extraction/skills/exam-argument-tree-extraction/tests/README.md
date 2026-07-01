# Exam Argument Tree Regression Tests

## Purpose

`exam-argument-tree-extraction` 是考试型抽树子 Skill。父层抽树协议、exam 主流程、管理类论效适配、GRE 适配或输出字段变化后，应做 exam 分支回归。

## Clean SubAgent Rule

按 `workflow-tao/references/regression-test-protocol.md`：

- 使用纯净 subAgent；
- 禁读修改讨论和无关旧答案；
- 只读测试输入、被测 Skill、必要 references/assets 和 target；
- 产物与 baseline / target md 做质量对比。

## Smoke Target

- [ ] 快速抓到总论点 / 分论点；
- [ ] 恢复题干事实 / 数据 / 例子 -> 分论点 -> 总论点的小型树；
- [ ] 生成 arrow table；
- [ ] 定位 hidden assumptions；
- [ ] 生成 candidate flaws；
- [ ] 筛出 best 3-4 writable points；
- [ ] 中文论效题输出可服务成文；
- [ ] GRE 输出按 prompt instruction 适配；
- [ ] 没有被学术论文 X1/X2/Y、citation evidence、table/figure evidence 污染。

## Suggested Regression Cases

- management-exam smoke：从已完成论效案例中选一题；
- GRE smoke：从 TASK10/TASK11 这类 GRE Argument 案例中选一题。
