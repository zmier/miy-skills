---
name: academic-paper-argument-tree-extraction
description: 从学术论文手稿、审稿项目 Markdown、PDF 还原稿或论文笔记中抽取学术论文论证树。用于需要还原一句话核心发现、X/M/Y/Y2、X1 问题有意义、X2 作者证明了具体核心发现、Y 贡献成立，生成 paper-argument-tree、evidence-ledger、evidence-expanded Mermaid、Obsidian 双链证据索引，并按实证论文、理论论文、综述/概念论文选择适配器时。
---

# Academic Paper Argument Tree Extraction

## 目标

把一篇学术论文读成可追溯的论证树：

```text
底层证据
-> 子观点
-> 中层命题
-> X1 / X2
-> Y 论文贡献成立 / 值得发表
```

完整论证树的主产物不是 Mermaid，而是：

```text
canonical recursive evidence tree
```

也就是一棵全篇主树的节点台账、边台账和证据台账。Mermaid 只是从这棵主树派生出来的视图。不要用几张分块 Mermaid 代替 canonical tree。

此 Skill 只负责“抽作者自己的树”。审稿人的攻击、削弱和修改建议应放到 `review-issue-arrow-map.md` 或审稿 adapter 中，不要混进作者树。

本 Skill 的核心方法不限定于经济学实证论文。只要论文是在证明一组 claim，并用实验、模型、数据、证明、系统评测、案例或文献作为 evidence 支撑，就可以使用这套 claim/evidence 抽树方法。当前最成熟的 adapter 是经济学/管理实证论文；工科论文、计算机系统论文、算法论文、实验科学论文需要读取或新增相应 adapter，不能硬套经济学的 X/变量/回归表格式。

本 Skill 是一个复合型子 Skill：它不是单一步骤，而是学术论文抽树的内部 workflow。父层 `../argument-tree-extraction/SKILL.md` 负责通用路由；本 Skill 负责学术论文场景下的主轴编排、适配器路由、证据下钻、文献证据、表图证据、视图生成和 QC。

学术论文 full-tree 必须按本 Skill 自己的主轴执行：

```text
task contract
-> academic argument spine
-> academic node ledger
-> academic evidence drilling
-> citation / table / figure evidence completion
-> academic edge ledger
-> derived views
-> extraction QC
```

不要在一个步骤里混写所有产物。若前序产物缺失，应写入 `extraction-qc.md` 或请求回退，而不是用概括性 Mermaid 补位。

学术主轴细则见 [academic-paper-main-axis.md](references/academic-paper-main-axis.md)。

第一批内部子 Skill：

```text
skills/academic-argument-spine-extraction/
skills/academic-node-ledger-builder/
skills/academic-evidence-drilling/
```

暂不把 edge ledger、view generation、QC、citation/table/figure 单独抽成子 Skill；这些先由本 Skill 的 references、assets 和主编排承载。若后续反复出现独立失败模式，再升级为子 Skill。

## 输入优先级

优先读取：

1. 手稿 Markdown / PDF restored Markdown；
2. 已有段落编号、图表编号、表格抽取结果；
3. 前序 TASK 输出，如 quick reconstruction、literature genealogy、variable/data audit；
4. 文献笔记、Obsidian vault 中的文献卡片；
5. 审稿意见或批注，仅用于后续 attack map，不用于作者树本体。

如果表格值、图注或文献链接缺失，标记 `needs-table-qc`、`needs-figure-qc` 或 `needs-citation-link`，不要伪造。

如果用户要求 case 回测、正式审稿、自审或 full-tree，必须特别检查 `citation-evidence`：作者用来支撑 gap、理论机制、变量操作化、方法和异质性的单篇文献是否已进入 evidence ledger。若只写“现有文献支持”，标记 `missing-citation-evidence`。

## 模式选择

默认按任务场景选择：

| 模式 | 何时使用 | 必交付 |
|---|---|---|
| `quick-tree` | 临时讨论、快速定位论文主线、用户只要求粗略理解 | 一句话核心发现、X/M/Y/Y2、简版作者树、QC |
| `full-tree` | 外部审稿、投稿前自审、case 回测、与专家审稿意见对照、正式写作自审、用户要求 Mermaid / Obsidian / 证据链 | `paper-argument-tree.md`、`evidence-ledger.md`、`evidence-expanded-mermaid.md`、`extraction-qc.md`；能做链接时再产出 `obsidian-link-map.md` |

如果任务是 `full-tree` 场景，但只生成简版树，必须在输出和日志中标记：

```text
incomplete-full-tree
```

并说明缺少哪些必交付文件。`incomplete-full-tree` 不能直接作为后续 `academic-argument-arrow-audit` 和 `academic-argument-issue-selection` 的正式输入，只能作为临时草图。

## 路由

先判断论文类型：

| 类型 | 读取 |
|---|---|
| 实证论文 | `references/empirical-paper-adapter.md` |
| 含实验 / 准实验 / 因果识别设计 | `references/identification-design-adapter.md` |
| 理论 / 模型论文 | `references/theory-paper-adapter.md` |
| 综述 / 概念 / 框架论文 | `references/conceptual-review-adapter.md` |
| 材料 / 器件 / 水伏发电论文 | `references/materials-hydrovoltaic-adapter.md` |
| 其他工科 / 系统 / 算法 / 实验科学论文 | 暂用共同 claim/evidence 协议；必要时新增 engineering / system / algorithm / experiment adapter |
| 需要 Obsidian 双链 | `references/obsidian-evidence-linking.md` |
| 需要 full-tree / case 回测 / 专家对照 | `references/canonical-recursive-tree.md` |
| 需要学术论文复合主轴 / 多环节协同 | `references/academic-paper-main-axis.md` |
| 需要区分 claim 节点和 evidence 叶子 | `references/claim-vs-evidence-boundary.md` |

无法判断类型时，先抽共同骨架，再把无法归类的证据标为 `unclear-paper-type`。

## 主流程

学术论文抽树按“作者树主轴”执行。主轴负责把作者自己的论证还原为可追溯树；审稿显影和验箭头属于后续 `academic-argument-arrow-audit`，不要把多个环节混成一张含糊的树：

```text
0 定边界 task contract
1 抽学术主干 academic argument spine
2 建 academic canonical node ledger
3 证据下钻 evidence ledger
4 补齐 citation / table / figure evidence
5 建 canonical edge ledger
6 生成 recursive tree / Mermaid / Obsidian link map
7 extraction QC
```

抽树阶段不攻击作者，只允许把箭头标为 `not-yet-audited`、`needs-qc` 或在 QC 中记录输入缺口。需要把“可疑箭头/可疑证据组合”显影时，交给后续 `academic-argument-arrow-audit` 的 sensitivity mapping。

`full-tree`、case 回测、正式审稿、专家意见对照必须读取 `references/canonical-recursive-tree.md`，并以其中的 canonical ledger 协议为主产物。

### 2A 作者证据树

1. 固定一句话核心发现：

   ```text
   哪个 X
   通过什么机制 M
   影响哪个 Y
   是否上升到 Y2 / 政策启示 / 贡献声称
   ```

2. 建立顶层树：

   ```text
   X1：问题有意义
   + X2：作者证明了具体核心发现
   -> Y：论文贡献成立 / 值得发表
   ```

3. 展开 X1：

   ```text
   gap
   importance
   novelty
   unresolved puzzle
   relevance to target field / journal
   ```

4. 展开 X2：

   - 理论机制或模型逻辑；
   - 概念和变量 / 定义；
   - 数据、样本或材料；
   - 方法、识别或证明；
   - 主结果；
   - 机制、异质性、边界条件、稳健性；
   - 贡献上升是否回应 X1。

5. 建立 canonical tree ledgers。先建 ledger，再生成任何 Mermaid：

   ```text
   canonical-node-ledger.md
   canonical-edge-ledger.md
   evidence-ledger.md
   ```

   节点台账：

   ```text
   node_id | label | type | depth | parent_id | child_ids | evidence_ids | source_links | status
   ```

   边台账：

   ```text
   edge_id | from_node | to_node | relation | support_type | status | notes
   ```

   建边阶段只还原作者声称的支撑关系：

   ```text
   作者用 A 支撑 B。
   ```

   不判断：

   ```text
   A 是否真的足以推出 B。
   ```

   因此抽树阶段的 edge status 只能使用 `not-yet-audited` 或 `needs-qc`。`strong / weak / broken / unclear` 属于后续 `academic-argument-arrow-audit`。

   证据台账：

   ```text
   evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度 | Obsidian 链接
   ```

   `full-tree` 模式下，关键 X1/X2/Y 节点必须至少各有底层证据；实证论文还必须覆盖变量定义、样本规则、模型设定、主结果、机制 / 异质性、稳健性和贡献上升。缺失项写入 `extraction-qc.md`，不得用中层摘要替代证据节点。

6. 递归下钻每个非叶子 claim。对每个 claim，必须继续问：

   ```text
   作者用哪些更小命题或证据支撑它？
   ```

   如果答案仍是“样本设计、主结果、稳健性、机制检验、文献支持、变量定义”这类概括性短语，它不是叶子，必须继续拆。

7. 停在最小证据单位。只有以下对象可以作为 evidence leaf：

   - 一句可定位的原文；
   - 一个脚注筛选规则；
   - 一个表格中的一个系数、t 值 / 标准误、显著性星号或样本量；
   - 一个变量定义、量纲、方向或转换；
   - 一个模型设定、固定效应、控制变量或聚类层级；
   - 一个图表结果；
   - 一篇文献被作者用于支持某个命题；
   - 一个政策文件或制度事实。

   不合格叶子示例：

   ```text
   E-R1 表4主结果
   E-D2 样本剔除规则
   E-M1 CAR为正
   E-H5 行业竞争异质性
   ```

   合格叶子示例：

   ```text
   E-R1a 表4列(1)：Peerdumy×POST = -0.0157***
   E-R1b 表4列(2)：Peerdumy×POST = -0.0111***
   E-R1c 表4表注：括号内为公司层面聚类调整标准误
   E-D2a 脚注：t 至 t+2 不应存在第二次冲击
   E-D2b 脚注：t-5 至 t 不应存在主动披露违规
   E-M1a 表10：CAR[-5,5] = 0.0182***
   ```

8. 生成 master tree 和 view trees：

   ```text
   recursive-tree-master.md
   view-x1-tree.md
   view-x2-identification-tree.md
   view-mechanism-tree.md
   view-contribution-tree.md
   ```

   `recursive-tree-master.md` 是全篇一棵树的主视图；`view-*` 只是从 master tree 派生的阅读视图，不是新的树本体。

9. 生成 evidence-expanded Mermaid：

   ```text
   E-* 具体证据
   -> e 子观点
   -> G/P/T/C 中层命题
   -> X1 / X2 / Y
   ```

   默认使用 `flowchart BT`，箭头表示下层 supports 上层。

   Mermaid 必须从 canonical-node-ledger / canonical-edge-ledger / evidence-ledger 派生。不得直接手写几张概括图后宣称完成 full-tree。

   `evidence-expanded-mermaid.md` 优先追求完整，而不是好读。full-tree 场景下，应尽量从顶层 claim 画到最底层 evidence。不要因为图太大而删除 evidence leaf；若 Mermaid 渲染限制导致无法全量展示，必须在 `extraction-qc.md` 标记 `incomplete-mermaid-evidence-view` 或 `mermaid-render-limit`，并用 `recursive-tree-master.md` 保留全量结构。

   如果用户要求中文版、高清图片、可读分图、配色优化、claim/evidence 视觉区分，或 Mermaid 出现重叠、曲线缠绕、文字太小、只有框没有字等问题，调用父级子 Skill：

   ```text
   ../argument-tree-mermaid-rendering/SKILL.md
   ```

   学术论文 full-tree 的 Mermaid 推荐同时输出：

   ```text
   evidence-expanded-mermaid.md
   evidence-expanded-mermaid.zh.md
   evidence-expanded-mermaid.zh.mmd
   evidence-expanded-mermaid.zh.svg
   evidence-expanded-mermaid.zh.full-chrome-scale2.png
   mermaid-zh-views/README.md
   mermaid-zh-views/00-overview.zh.chrome-scale2.png
   mermaid-zh-views/01-x1-problem.zh.chrome-scale2.png
   mermaid-zh-views/02-*.zh.chrome-scale2.png
   ```

   图形规范：

   - claim 和 evidence 必须用颜色 / class 区分；
   - reading view 中节点第一行必须是自然语言，不能只有 `E033` / `C-MECH` / `CSOTA` 等代号；
   - 代号只作为第二行或末尾的回查锚点；
   - 只读 Mermaid 应能看懂作者的“证据 -> claim -> 贡献”逻辑；
   - 区分 `full-reading view` 和 `summary-reading view`：正式审稿和验箭头前应保留 full-tree 证据颗粒度；
   - 若为可读性合并多个 evidence，必须明确标为 `summary-reading view` 或 `merged-evidence-summary`，不能冒充 full-tree；
   - `needs-qc` / `needs-figure-qc` / `needs-citation-link` evidence 不能画成普通已核验证据；
   - 使用 Ant Design / Tailwind 风格的克制配色；
   - 优先折线，使用 `curve: "linear"` 或 `curve: "stepAfter"`；
   - 完整图负责覆盖，分图负责阅读；
   - 不能为了可读性删除 evidence leaf。

10. 生成 Obsidian 链接索引：

   - 链到稿件 Markdown 中的段落、图、表；
   - 链到文献笔记或 DOI / URL；
   - 链到 evidence ledger；
   - 链到后续 review issue map。

### 验收 QC

11. 做完整性检查：

   - X2 是否是具体核心发现，不是“作者做出来了”“核心发现成立”等空泛占位；
   - 每个关键 G/P/T/C 节点是否有底层证据；
   - Mermaid 图是否看得见最小证据叶子；
  - `evidence-expanded-mermaid.md` 是否尽量覆盖从 root claim 到 minimal evidence 的完整链条；
   - Mermaid 是否区分 claim / evidence / needs-qc；
   - Mermaid reading view 是否只看图也能读懂逻辑，而不是必须先读 ledger 才懂；
   - Mermaid reading view 是否保留 full-tree 关键 evidence；若减少节点，是否标为 summary view；
   - 若生成 PNG，是否确认不是“只有框没有字”的坏图；
   - 若 full-tree 图过大，是否生成阅读分图和 README；
   - 是否先产出 canonical-node-ledger、canonical-edge-ledger、evidence-ledger，再生成 Mermaid；
   - 每个非叶子 claim 是否有 child_ids 或 evidence_ids；
   - 是否存在抽象证据叶子，如“主结果”“稳健性”“机制检验”“样本规则”；若存在，标记 `abstract-evidence-leaf`；
   - 无法核实的表格值是否标了 QC；
   - 作者树和审稿攻击是否分离；
   - `full-tree` 场景是否产出 `evidence-ledger.md` 和 `evidence-expanded-mermaid.md`；若否，标记 `incomplete-full-tree`。
   - 若没有 canonical ledgers，标记 `incomplete-canonical-tree`。
   - 若没有递归拆到最小证据单位，标记 `incomplete-recursive-tree`。
   - 若用户需要审稿显影或验箭头，标记 handoff：`ready-for-academic-arrow-audit` 或说明缺口。

## 输出文件

`quick-tree` 可输出：

```text
paper-argument-tree.quick.md
extraction-qc.quick.md
```

`full-tree` 必须输出：

```text
task-contract.md
academic-argument-spine.md
canonical-node-ledger.md
canonical-edge-ledger.md
paper-argument-tree.md
recursive-tree-master.md
evidence-ledger.md
evidence-expanded-mermaid.md
extraction-qc.md
```

能稳定定位段落、图表、文献或 Obsidian 双链时，再输出：

```text
obsidian-link-map.md
```

若用户要求中文可视化或高清图，推荐再输出：

```text
evidence-expanded-mermaid.zh.md
evidence-expanded-mermaid.zh.mmd
evidence-expanded-mermaid.zh.svg
evidence-expanded-mermaid.zh.full-chrome-scale2.png
mermaid-zh-views/README.md
mermaid-zh-views/*.chrome-scale2.png
argument-tree-summary.zh.md
```

若在项目 TASK 中工作，写入该 TASK 的 `outputs/`，并在 `logs/log.md` 记录：

```text
输入文件
论文类型判断
读取的 adapter
关键缺口 / QC 标记
是否更新 workflow / Skill
抽树模式：quick-tree 或 full-tree
若 full-tree 不完整：incomplete-full-tree 原因
是否可移交 academic-argument-arrow-audit
```

## 资源

- `references/empirical-paper-adapter.md`：实证论文抽树适配。
- `references/identification-design-adapter.md`：实验、准实验和因果识别设计的 claim/evidence 抽取适配，服务后续 DAG / 验箭头。
- `references/theory-paper-adapter.md`：理论 / 模型论文抽树适配。
- `references/conceptual-review-adapter.md`：综述 / 概念 / 框架论文抽树适配。
- `references/materials-hydrovoltaic-adapter.md`：材料、器件和水伏发电论文抽树适配。
- `references/canonical-recursive-tree.md`：canonical recursive evidence tree 的节点、边、证据、递归和验收规则。
- `references/obsidian-evidence-linking.md`：Obsidian 双链与证据定位规则。
- `references/academic-paper-main-axis.md`：学术论文抽树复合主轴、内部环节分工、写权限和回退规则。
- `references/claim-vs-evidence-boundary.md`：claim 节点与 evidence 叶子的边界规则。
- `../argument-tree-mermaid-rendering/SKILL.md`：论证树 Mermaid 视图、中文版、高清 PNG/SVG、分图、claim/evidence 视觉规范和渲染 QC。
- `skills/academic-argument-spine-extraction/SKILL.md`：抽学术主干。
- `skills/academic-node-ledger-builder/SKILL.md`：建 claim 节点台账。
- `skills/academic-evidence-drilling/SKILL.md`：下钻最小证据叶子。
- `assets/canonical-node-ledger-template.md`：canonical 节点台账模板。
- `assets/canonical-edge-ledger-template.md`：canonical 边台账模板。
- `assets/paper-argument-tree-template.md`：论证树输出模板。
- `assets/evidence-ledger-template.md`：证据台账模板。
- `assets/obsidian-link-map-template.md`：Obsidian 链接索引模板。

## 边界

- 不把单篇论文的实体判断写成通用规则。
- 不把审稿人攻击节点画进作者论证树。
- 不把表格摘要当成已核实系数；没有具体值就标 QC。
- 不因 Mermaid 图过大而删除 evidence ledger；图大时拆成 X1 / X2 / Y 子图。
- 不因 Mermaid 图不好读而删除底层 evidence；full-tree 的 Mermaid 首要目标是完整显影。
- 不让简版树冒充完整树；case 回测、正式审稿和专家意见对照默认是 full-tree。
- 不在 paper 抽树阶段生成审稿显影树；该步骤属于 `academic-argument-arrow-audit`。
- 不把 Mermaid 当主产物；canonical-node-ledger、canonical-edge-ledger 和 evidence-ledger 才是完整树本体。
- 不把“高清但没有字”的 PNG 当作成功渲染；必须做视觉或尺寸/文本复核。
- 不用曲线缠绕、节点重叠的完整大图替代可读分图；完整图和阅读图要分离。
- 不把概括性 evidence node 当最小证据叶子；抽象叶子必须继续拆或标记 `abstract-evidence-leaf`。

## 回归测试

本 Skill 是学术论文抽树的复合型子 Skill。凡修改学术主轴、论文类型 adapter、claim/evidence 边界、evidence ledger 规则、citation evidence、table/figure evidence 或输出契约，必须按 `workflow-tao` 的回归测试协议处理：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-tao/references/regression-test-protocol.md
```

如果是 Skill 修改触发回归，优先开纯净 subAgent 执行，用新产物与 baseline / target md 做质量对比。不能由修改者只凭主观判断“质量变好了”。

学术分支回归至少检查：

- X/M/Y/Y2 是否更清楚；
- canonical node/edge/evidence ledger 是否齐；
- evidence 是否拆到最小可核单位；
- citation evidence 是否进入 evidence ledger，而不是只出现在 link map；
- table / figure evidence 是否有 QC 状态；
- 作者树是否与审稿显影 / 验箭头分离；
- Mermaid 是否从 ledger 派生；
- Mermaid 是否区分 claim / evidence / needs-qc，并在需要时生成中文版、高清图和阅读分图。
