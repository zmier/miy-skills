# Xinyuan Comparison

本文件在 `academic-arrow-audit-table.md` 冻结后生成。用途是评估本轮验箭头 Skill 的覆盖率，不把欣媛意见倒灌进审计表。

## Overall Verdict

TASK08 的验箭头覆盖了欣媛意见的大多数主轴问题，尤其是：

- 主动披露定义；
- KV 指标有效性；
- 样本筛选偏差；
- 事件公司自身效应缺失；
- 聚类层级；
- POST 时点；
- 声誉机制表11冲突；
- 信息传导排除逻辑；
- 稳健性避重就轻；
- EFD 层级错配；
- 政策建议上升过度。

主要不足：

1. 对“行为信号 vs 内容信息”这条理论概念滑动，TASK08 有分散覆盖，但没有单独形成一个显眼 candidate。
2. 对“表注写标准误但括号值像 t 值”覆盖不足，只在 `needs-table-qc` 中泛化提到，未形成独立 reporting issue。
3. 对“KV 在顶级财会研究中逐渐边缘化、应补文本指标/交易所评级”等外部文献建议，TASK08 标为 literature search，但没有实际调用检索。
4. 对“图3样本与表11样本是否一致”，TASK08 有 A030/table conflict，但未单列 sample-consistency issue。

## Issue Coverage

| Xinyuan issue | TASK08 coverage | TASK08 arrows | judgment |
|---|---|---|---|
| 低信息含量违规 vs 强正向 CAR / 行为信号与内容信息滑动 | partial | A030; A031; A040; S06 | 捕捉到声誉机制冲突和机制证据不稳定，但没有把“行为信号/内容信息”作为概念关系显式审计。 |
| 样本筛选标准导致偏差 | high | A011; C03 | 覆盖清楚。 |
| 事件公司自身效应基准缺失 | high | A018; C03 | 覆盖清楚。 |
| KV 指数代理局限 | high | A010; A013; A029; C01 | 覆盖清楚。 |
| 主动披露违规定义时序漏洞 | high | A008; A017; C02 | 覆盖清楚。 |
| EFD 公司层 vs RZ 行业层构念错配 | high | A039; C08 | 覆盖清楚。 |
| 标准误聚类层级 | high | A025; C04 | 覆盖清楚。 |
| POST 变量定义可能稀释处理效应 | high | A017; A026; C02/C04 | 覆盖清楚。 |
| 声誉竞争机制图3与表11样本一致性 | partial | A030; S06 | 捕捉表11冲突，但没显式要求图3/表11样本一致性核查。 |
| 信息传导排除反向因果 | high | A032; C06 | 覆盖清楚。 |
| 稳健性避重就轻 | high | A033-A036; C07 | 覆盖清楚。 |
| 替代行业分类稳健性 | partial | A012/A015 | 仅在共同冲击/行业边界中泛化覆盖，未单列 industry classification boundary。 |
| 表格括号值疑似 t 值但表注写标准误 | low | QC caveat only | 需要反哺 reporting-QC 字段和候选 issue。 |

## Skill Feedback From Comparison

| feedback | why transferable | target |
|---|---|---|
| 机制箭头要检查“同一机制在理论、机制表、异质性、排除解释中的概念是否滑动”。 | 欣媛 case 显示，机制不是单表显著性问题，而是行为信号、内容信息、市场奖励、违规严重度之间的一致性问题。 | `academic-arrow-audit-main-axis.md`; `academic-arrow-types.md` |
| 机制证据中加入 `sample-consistency-qc`。 | 图/事件研究样本与机制回归样本不一致会造成推断跳跃，是机制审查高频风险。 | `academic-arrow-types.md`; `academic-arrow-audit-template.md` |
| 统计结果箭头增加 `reporting-qc`：括号值、标准误/t值、聚类说明、星号含义。 | 表格规范错误会影响读者判断显著性，也常见于审稿。 | `academic-statistical-result-arrow-audit`; template |
| 文献/方法建议若依赖“顶刊近期做法”，必须进入 literature/method search，而非凭记忆。 | KV 替代指标和 Abadie et al. 聚类建议都属于外部知识增强。 | `method-knowledge-feedback.md`; `academic-literature-gap-arrow-audit` |

