# Writing Quality Regression V2

状态：`pass / non-blind-regression`

## 回归问题

本次回归检查：

```text
拆出 argument-issue-selection 后，
重新按“全量验箭头 -> 选问题 -> 写作”生成作文，
最终行文质量是否比旧稿变差。
```

## 输入边界

本次不是 blind-run。读取了：

- `outputs/arrow-audit.md`
- `outputs/essay-draft.md`
- `outputs/revision-notes.md`
- `outputs/reference-comparison.md`
- `exam-writing-rules.md`
- `exam-issue-selection.md`

因此，本次只验证写作质量回归，不重复声明 forward-test。

## 新链条产物

| 环节 | 文件 | 判断 |
|---|---|---|
| 全量验箭头 | `exam-arrow-audit-table.v2.md` | pass |
| 选问题 | `exam-selected-issues.v2.md` | pass |
| 行文成稿 | `essay-draft.v2.md` | pass |

## 与旧稿对比

| 维度 | 旧稿 | V2 | 判断 |
|---|---|---|---|
| 标题 | 勤俭节约真的过时了吗？ | 同旧稿 | 持平 |
| 开头 | 稳，但略长 | 略压缩，仍交代论点和问题 | 小幅改善 |
| 本论段数量 | 4 段 | 4 段 | 持平 |
| 每段是否有定位 | 有 | 有 | 持平 |
| 每段是否有分析 | 有 | 有，并补充参考对照中的细颗粒概念关系 | 小幅改善 |
| 每段是否有收尾 | 有 | 有 | 持平 |
| 是否堆术语 | 否 | 否 | 持平 |
| 是否写成价值评论 | 否 | 否 | 持平 |
| 是否覆盖主要断点 | A1、A2、A4、A7/A8 | A1、A2/A3、A4/A5、A7/A8/A10 | 小幅改善 |
| 是否变薄 | 否 | 否 | pass |

## 质量观察

V2 相比旧稿主要变化：

1. 第二段补入“财富收入增长速度”和“财富总量积累”的概念关系判断；
2. 第四段补入“未来保障”和“产品升级、转产或结构调整”的替代条件；
3. 每段仍维持“定位 -> 分析 -> 收尾”的论效结构；
4. 没有因为拆出 `exam-selected-issues.v2.md` 而把作文写成选点清单。

## 风险

V2 因读取了 reference comparison，内容比 blind-run 旧稿更细。这说明它适合作为行文质量回归，不适合作为新的 blind-run 成绩。

## 结论

没有证据显示最终行文质量变差。

更准确地说：

```text
新拆分链条没有降低作文质量；
在本题上，V2 因吸收旧 reference comparison 的二稿建议，质量略有改善；
但这不是新的 blind forward-test。
```
