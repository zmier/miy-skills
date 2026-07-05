# Log

## 2026-06-20

### 0. 读取 SKILL 与边界

- 使用新版 `academic-argument-arrow-audit` SKILL。
- 已读取其直接要求的主轴、箭头类型、子 skill 边界、方法知识反馈、三个模板，以及父层 `argument-arrow-audit` 与 `arrow-audit-core.md`。
- 约束确认：只写入 TASK09 目录；不读欣媛意见、TASK08、旧版审稿/验箭头产物；不做 major/minor 选择；不写最终审稿意见。

### 1. 接收作者论证树

- 接收 TASK07 author-only 树：`Y0 <- X1, X2, P9`。
- 接收 node / edge / evidence ledger，边状态均为 `not-yet-audited` 或 `needs-qc`。
- 输入完整，但存在 TASK07 已标明的 QC caveats：表格逐单元格未完全复核、图1/图2需精确裁剪、表11列(3)正文/表格冲突、citation-link 多处未核。

### 2. 逐条改写作者箭头

- 将 A001-A043 全量改写为“作者用 A 证明 B”。
- E001-E034 是 evidence-set 到节点的低层证据边，本轮作为 evidence 支撑材料使用，不作为主审计边逐条展开。

### 3. 判断学术箭头类型

- 给 A001-A043 标注 `gap-contribution`、`construct-measure`、`identification-causal`、`result-finding`、`mechanism-claim`、`robustness-threat`、`finding-contribution` 等类型。
- 路由原则：文献 gap、KV 指标有效性、方法标准和 citation verification 进入 external evidence request；DID/统计细节先内部审计并标 `needs-qc` 或 `needs-external-evidence`。

### 4. 第一轮内部验箭头并集中标记外部证据需求

- 未进行联网或数据库检索。
- 第一轮只用 TASK07 内部 evidence 和 extraction QC。
- 重点内部断点：
  - A010：KV 下降是否足以推出“信息披露质量提升”需要外部指标有效性证据；内部只能确认作者定义与方向。
  - A012/A025/A026/A027：DID 识别链有内部支持，但聚类层级、分期处理、前趋势检验与 Bacon/stacked DID 的充分性需要方法 QC。
  - A014/A030：表11列(3)与作者机制叙述冲突，内部已可标为 weak/needs-qc。
  - A032：用距离和处罚不显著来排除监管信息传导，内部可见替代解释未完全排除。
  - A035/A036：Oster、替代变量、POST_Month 和 placebo 支撑稳健性，但需要方法/图表 QC。
  - A040：高竞争组和低竞争组方向相反，更适合作为边界条件而非稳健支持总体结论。

### 5. 集中外部证据增强

- 本轮按用户要求未检索。
- 生成 `external-evidence-request.md`，集中列出 literature-gap-search、measure-validity-search、method-standard-search、citation-verification 等请求。
- 生成 `external-evidence-ledger.md`，所有请求均为 `not-searched / pending`，不把外部问题伪装为已确认。

### 6. 回填 academic arrow audit ledger

- 将内部审计结果与未检索状态回填到 `academic-arrow-audit-table.md`。
- 需要外部证据才能定性的箭头保留 `needs-external-evidence`；需要表格/图/方法复核的箭头保留 `needs-qc` 或 `strong-with-qc`。

### 7. 生成 break summary 和 issue selection candidates

- 生成 `academic-arrow-break-summary.md`。
- 生成 `issue-selection-candidates.md`，只列候选，不选择 major/minor，不写审稿正文。

### 8. 移交 issue selection

- 本轮移交材料是候选表和全量 audit ledger。
- 未调用 issue-selection SKILL；未做 major/minor 选择。
