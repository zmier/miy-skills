# UAT

## 结论

```text
pass / case-calibration-green / v2-arrow-table-green / subworkflow-recommended
```

## 验收项

| 验收项 | 结果 | 证据 |
|---|---|---|
| 恢复 `Y: 论文值得发表 / 贡献成立` 顶层论证 | pass | `paper-argument-tree.md` |
| 区分 `X1: 问题有意义` 与 `X2: 作者证明了核心发现` | pass | `paper-argument-tree.md` |
| 将至少 5 条欣媛意见映射到断裂箭头 | pass | `review-issue-arrow-map.md` 映射 12 条 |
| 每条映射说明削弱 X1/X2/Y | pass | `review-issue-arrow-map.md` |
| 明确可迁移规则和个案边界 | pass | `workflow-feedback.md` |
| 给出是否创建子 workflow 的建议 | pass | 建议创建 `workflow-academic-review-argument` |
| 是否遵循论效式抽树：命题化节点 + 断裂箭头 | pass after v2 | `paper-argument-tree.md` V2；`review-issue-arrow-map.md` V2 |
| X2 是否还原作者核心发现句，而非只写“作者做出来了” | pass after v2.1 | `paper-argument-tree.md` 的 X2-core；`review-issue-arrow-map.md` 的 X/M/Y 表述 |
| 中层节点是否继续展开到底层论据和箭头 | partial pass after v3 | 已展开 G1、P5、P8；后续子 workflow 应要求所有关键 G/P 节点按需展开 |
| 作者论证树是否与审稿攻击分离 | pass after v3.1 | `paper-argument-tree.md` 只保留作者论证；攻击映射放在 `review-issue-arrow-map.md` |
| 是否完成作者论证树关键节点完整展开 | pass after v4 | 已展开 G1-G4、P1-P9 和 Y 汇合箭头，并提供 V4 Mermaid 骨架 |
| 是否追溯到底层证据台账 | pass after v5 | `evidence-ledger.md` 记录表格、系数、显著性、变量定义、模型设定、文献引用和原文段落 |
| 底层证据是否画回 Mermaid 论证树 | pass after v5.1 | `paper-argument-tree.md` 新增 `V5 Mermaid：证据叶子展开图` |

## 关键发现

本 TASK 验证了：

```text
论效题小树 / GRE 小树
-> 可以迁移为学术论文大树
```

学术论文大树的稳定顶层结构是：

```text
X1：问题有意义
+ X2：作者证明了核心发现
-> Y：论文值得发表 / 贡献成立
```

欣媛审稿意见的多数 major concerns 并非散点技术意见，而是集中削弱 `X2: 作者证明了核心发现`。这解释了为什么样本、变量、聚类、POST、机制和稳健性问题会共同影响最终贡献判断。

## V2 复核

用户指出 v1 论证树仍有模块化倾向。复核后确认：

```text
V1：X1/X2/Y + 模块节点
V2：X1/X2/Y + 命题节点 + arrow table
```

V2 将“变量问题”“方法问题”“机制问题”改写为具体箭头，例如：

```text
KV 变化 -> 信息披露质量改善
同行披露质量短期改善 -> 行业自律发展
公司层面聚类后的显著结果 -> DID 识别可信
处罚不显著 -> 信息传导机制不存在
```

因此，TASK01 的最终 UAT 以 V2 为准。

## V2.1 复核

用户继续指出：`X2: 作者做出来了` 仍然过于概括，应该看到作者具体声称“哪几个 X 影响哪几个 Y”。该意见成立。

因此，V2.1 将 X2 改写为：

```text
X2：作者证明了“主动披露违规 -> 同行披露质量提升”这一核心发现，
并给出声誉竞争和市场压力机制解释。
```

并补充：

```text
X：上市公司主动披露违规
M1：声誉竞争机制
M2：市场压力机制
M3：信息传导机制排除
Y1：同行业其他企业信息披露质量提升
Y2：行业自律发展
```

学术论文论证树以后应避免把 `X2` 只写成“做出来了”。必须先还原“一句话发现”和 X/M/Y 关系。

## V3 复核

用户进一步指出：即使 X2 已经还原为核心发现，树上仍有很多中层命题没有充分展开，例如：

```text
G1 信息披露监管重要
P5 样本能代表机制相关事件
P8 稳健性回应核心威胁
```

这些节点也应继续拆出它们自己的论据和箭头。该意见成立。

V3 已先展开三类代表节点：

```text
G1: 制度变化 / 处罚提高 / 违规仍多 / 事前预防 -> 信息披露监管重要
P5: 样本筛选规则 -> 干净同行溢出样本 -> 机制相关代表性样本
P8: 常规稳健性检验 -> 结果稳健 -> 核心威胁已被回应
```

最终判断：

```text
学术论文大型论证树 = 顶层 X1/X2/Y + 核心发现 X/M/Y + 中层命题展开 + arrow table
```

TASK01 v3 仍是 calibration，不等于所有节点已完全穷尽展开；它证明了子 workflow 的模板必须支持这种递归展开。

## V3.1 图层分离

用户指出：欣媛如何攻击不应直接放在作者论证树上，否则树会乱。该意见成立。

V3.1 将输出分成两层：

```text
paper-argument-tree.md
-> 只画作者自己的论证树

review-issue-arrow-map.md
-> 记录审稿意见如何攻击具体箭头
```

后续如果需要可视化审稿攻击，可另建：

```text
critique-tree.md
```

## V4 完整展开

用户要求继续做“完整展开论证树”。V4 已将作者论证树展开为：

```text
X1:
  G1 信息披露监管重要
  G2 文献 gap
  G3 主动披露违规视角新
  G4 现实监管意义

X2:
  P1 X 被定义和操作化
  P2 市场正向反馈
  P3 同行因声誉竞争/市场压力改善披露
  P4 Y1 被 KV 捕捉
  P5 样本代表机制相关事件
  P6 DID 识别 X -> Y1
  P7 机制检验证明 M1/M2 并排除 M3
  P8 稳健性回应核心威胁

Y:
  X1 + X2 + P9 行业自律/政策启示 -> 贡献成立
```

V4 仍保持图层分离：作者树不放审稿攻击；审稿攻击继续由 `review-issue-arrow-map.md` 承接。

## V5 底层证据台账

用户继续指出：论证树不能只展开到“P4 Y 被 KV 捕捉”“P8 稳健性回应威胁”这类命题，还要能追到最底层证据，例如：

```text
表格编号
系数
显著性
变量定义
模型设定
文献引用
原文段落
```

该意见成立。V5 新增：

```text
outputs/evidence-ledger.md
```

其作用是把底层证据作为论证树叶子节点：

```text
evidence node -> subclaim -> X1 / X2 / Y
```

V5.1 进一步把 `evidence-ledger.md` 中的 `E-*` 证据节点画回 Mermaid，形成：

```text
E-* 具体证据
-> e 子观点
-> G/P 中层命题
-> X1 / X2 / Y
```

V5 同时固定一条重要边界：

```text
如果 restored Markdown 没有保存表格中的具体系数、t 值、标准误、显著性或样本量，
必须标记为 needs-table-qc，
不能为了让树完整而臆造数值。
```

因此，TASK01 的学术论文论证树现在包含三层输出：

```text
paper-argument-tree.md
-> 作者命题树

evidence-ledger.md
-> 作者底层证据台账

review-issue-arrow-map.md
-> 审稿攻击映射
```

## 边界声明

- 本 TASK 是 `prior-exposed / case-calibration`；
- 不作为 strict blind forward-test；
- 不重新审稿；
- 不判断 J-260110 最终录用建议；
- 不把个案判断直接写入通用 workflow。

## 下一步

建议进入结构建设：

```text
subworkflows/workflow-academic-review-argument/
```

并将本 TASK 作为该子 workflow 的 seed case，而不是作为普遍有效性的最终证据。后续需要用 EMFT 或新论文做 forward-test。
