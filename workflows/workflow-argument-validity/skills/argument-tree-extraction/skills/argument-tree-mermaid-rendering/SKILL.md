---
name: argument-tree-mermaid-rendering
description: 将论证树 canonical node/edge/evidence ledger 渲染为可读、可复核、可发布的 Mermaid 视图和高清图片。用于 evidence-expanded Mermaid、中文版论证树、claim/evidence 视觉区分、Ant Design / Tailwind 风格配色、折线布局、分图、高清 PNG/SVG 渲染、Obsidian 可视化和 Mermaid 重叠/空框/文字缺失问题处理。
---

# Argument Tree Mermaid Rendering

## 定位

本 Skill 只负责论证树的视觉视图生成和渲染，不负责抽 claim、不负责抽 evidence、不负责验箭头。

输入必须来自前序产物：

```text
canonical-node-ledger.md
evidence-ledger.md
canonical-edge-ledger.md
recursive-tree-master.md
extraction-qc.md
```

输出是派生视图：

```text
evidence-expanded-mermaid.md
evidence-expanded-mermaid.zh.md
evidence-expanded-mermaid.zh.mmd
evidence-expanded-mermaid.zh.svg
evidence-expanded-mermaid.zh.full-chrome-scale2.png
mermaid-views/
mermaid-zh-views/
render-log.md
```

Mermaid 永远不是完整论证树本体；完整本体仍是 node / edge / evidence ledger。

## 触发条件

当用户提出以下需求时使用：

- Mermaid 图看不清、太乱、重叠、曲线缠绕；
- 要中文版 Mermaid；
- 要高清 PNG / SVG；
- 要区分 claim 和 evidence；
- 要 Ant Design / Tailwind CSS 风格；
- 要把完整 full-tree 拆成可读分图；
- Mermaid 图只有框没有字；
- Obsidian 中 Mermaid / 图片阅读体验需要优化；
- 需要把论证树图作为审稿、自审、教学或汇报材料。

## 核心原则

- **ledger first**：Mermaid 只能从 ledger 派生，不能在画图阶段新增 claim 或 evidence。
- **完整图和阅读图分离**：完整图保留所有关键 evidence leaf；阅读图按 X1 / X2 / 机制 / 性能 / 稳定性 / 贡献等分支拆分。
- **claim 与 evidence 视觉区分**：读者必须一眼看出哪个是作者论点，哪个是底层证据。
- **人类可读优先**：Mermaid 主要是给人读的视图，不是 Agent 的主数据结构；节点第一行必须是自然语言，编号只做回查锚点。
- **箭头方向稳定**：默认 `flowchart BT`，下层 evidence 支撑上层 claim。
- **折线优先**：优先用 Mermaid `curve: "linear"` 或 `"stepAfter"`，避免大树曲线缠绕。
- **节点短标签**：图中 label 用短句；完整内容放 ledger / summary。
- **渲染要验收**：不能只生成文件名；必须检查 PNG 尺寸、是否有文字、是否误用空框图。
- **SVG 优先保存**：SVG 适合放大检索；PNG 用于预览、汇报或图片查看器。

## 视觉语义

推荐节点类型：

| 类型 | Mermaid class | 形状 | 用途 |
|---|---|---|---|
| root claim | `rootClaim` | 圆角矩形 / stadium | 顶层结论、论文贡献、总论点 |
| major claim | `majorClaim` | 圆角矩形 | X1 / X2 / Y 或主要分支 |
| middle claim | `middleClaim` | 矩形 | 中层论点 |
| subclaim | `subClaim` | 矩形 | 子论点 / 孙论点 |
| evidence | `evidenceLeaf` | 直角矩形 | 最小证据叶子 |
| needs QC evidence | `needsQc` | 虚线边框或浅红/浅黄 | 未核验图表、文献、补充材料 |
| implicit premise | `implicitPremise` | 六边形或浅紫 | 隐含前提 |

Mermaid 形状语法有限时，用 class 样式代替形状差异。

## Human-Readable View

Mermaid 论证树默认是给人类阅读、讨论、汇报和质检的，不是给 Agent 保存逻辑的主结构。

Agent 读取论证树时，应优先消费：

```text
canonical-node-ledger.md
evidence-ledger.md
canonical-edge-ledger.md
recursive-tree-master.md
```

Mermaid 的作用是：

```text
让人一眼读懂主逻辑
让人看到 evidence 是否真的长到叶子上
让人发现图表、文献、机制、贡献上升在哪里需要继续追问
用于 Obsidian、汇报、讨论和回归质检
```

因此 Mermaid 节点不能只写机器代号。每个节点 label 必须遵守：

```text
第一行：自然语言判断 / 事实
第二行：编号或锚点
第三行：必要的 QC 标记或来源
```

合格：

```mermaid
E033["实测水传输速率提升<br/>NB 0.18 -> DB 0.32 mm/s<br/>E033 · needs-figure-qc"]:::needsQc
CMECH["脱木质素增强水传输，碳黑负责集电<br/>C-MECH"]:::middleClaim
```

不合格：

```mermaid
E033["E033 NB/DB水传输0.18/0.32mm/s"]
CMECH["C-MECH 水伏机制"]
CSOTA["SOTA/既有材料比较"]
```

原因：这些节点需要读者先知道内部代号体系，无法只看 Mermaid 读懂逻辑。

## View Types

同一棵 canonical tree 可以派生三类 Mermaid 视图：

| 视图 | 读者 | 特点 | 文件建议 |
|---|---|---|---|
| audit view | Agent / 研究助理 / 回归测试 | 保留完整编号、所有 evidence、便于回查；可读性可以较弱 | `evidence-expanded-mermaid.audit.md` |
| full-reading view | 人类审稿人 / 作者 / 讨论者 | 保留 full-tree 证据颗粒度，同时把节点 label 改成人话 | `evidence-expanded-mermaid.full-reading.zh.md` |
| summary-reading view | 人类快速浏览 | 合并部分 evidence，让主逻辑更顺；必须明确标注为摘要视图 | `argument-tree.summary-reading.zh.md` |
| presentation view | 汇报 / 教学 / 快速沟通 | 只保留主逻辑和关键证据，明确标为摘要视图 | `argument-tree.presentation.zh.md` |

默认交付中至少应有 `full-reading view` 或明确说明本轮只做了 `summary-reading view`。

`reading view` 不是“减少节点”的同义词。它首先意味着节点文案对人友好；证据是否合并，必须单独声明。

注意：

- `full-reading view` 不得合并或删除 full-tree 中的关键 evidence leaf；
- `summary-reading view` 和 `presentation view` 可以删减 / 合并 evidence，但必须明确标注它们不是 full-tree；
- 若把 E006-E007、E040/E044、E055-E056 等多个 evidence 合并成一个节点，必须在 README 或图注中写明 `merged-evidence-summary`；
- summary view 不能冒充 full-tree，也不能作为正式验箭头的唯一输入。

## Full-Reading vs Summary-Reading

两者的区别：

| 问题 | full-reading view | summary-reading view |
|---|---|---|
| 是否保留所有关键 evidence leaf | 是 | 不一定 |
| 节点是否写人话 | 是 | 是 |
| 是否适合正式审稿 / 验箭头前复核 | 是 | 只适合预览 |
| 是否能合并多个 evidence | 原则上不合并；若合并必须保留子证据或派生分图 | 可以合并，但要标注 |
| 是否可替代 evidence ledger | 否 | 否 |

如果用户说“之前更细”“节点少了很多”“是不是丢证据了”，优先判断当前图是否只是 `summary-reading view`。若是，应补做：

```text
full-reading view
= full-tree evidence 粒度
+ human-readable labels
+ claim / evidence / needs-qc style
+ readable subviews
```

不要把“可读性”作为删除 evidence 的理由。正确做法是：

1. 保留 full-reading view 的全部关键证据；
2. 通过分图、短 label、图例和高清渲染提升可读性；
3. 另行提供 summary-reading view 给快速浏览。

## Label Writing Rules

节点文案按以下规则写：

1. 第一行说人话，不写纯代号；
2. claim 节点写成“作者要读者相信的判断”；
3. evidence 节点写成“哪个事实 / 数值 / 图表 / 文献说明什么”；
4. 编号如 `E033`、`C-MECH` 放在第二行或末尾；
5. 术语如 `SOTA`、`EDL`、`CDB` 应展开或在图例解释；
6. `needs-qc`、`needs-figure-qc`、`needs-citation-link` 必须出现在节点或图例中；
7. 每张阅读图顶部或 README 中用一句话说明“本图在证明什么”；
8. 图例必须解释颜色和线型。

推荐格式：

```text
自然语言主句
编号 · 来源 / QC
```

例子：

```text
纤维形态让电流密度提高
C-SHAPE-PERF
```

```text
电流密度从 4 提高到 285 uA/cm2，约 71 倍
E024 · Fig.2d · needs-figure-qc
```

## Code / Label Boundary

Mermaid 内部节点 id 可以继续使用短代号：

```mermaid
E024 --> CSHAPEP
```

但显示 label 必须人类可读：

```mermaid
E024["电流密度从 4 提高到 285 uA/cm2，约 71 倍<br/>E024 · Fig.2d · needs-figure-qc"]:::needsQc
CSHAPEP["纤维形态提高单位面积输出<br/>C-SHAPE-PERF"]:::subClaim
```

这样 Agent 仍可通过 id 回查 ledger，人类也能直接读懂图。

## 推荐配色

采用接近 Ant Design / Tailwind 的克制风格：

```text
rootClaim:   bg #E6F4FF, border #1677FF, text #0F172A
majorClaim:  bg #F0FDF4, border #22C55E, text #0F172A
middleClaim: bg #F8FAFC, border #64748B, text #0F172A
subClaim:    bg #FFFFFF, border #94A3B8, text #334155
evidence:    bg #FFF7ED, border #F97316, text #431407
needsQc:     bg #FEF2F2, border #EF4444, text #7F1D1D
implicit:    bg #F5F3FF, border #8B5CF6, text #2E1065
```

不要使用大面积渐变、紫蓝渐变、装饰性背景或多余视觉特效。论证树是工作图，不是海报。

## Mermaid 初始化模板

使用以下 init 块作为默认起点：

```mermaid
%%{init: {
  "flowchart": {
    "nodeSpacing": 70,
    "rankSpacing": 90,
    "curve": "linear",
    "htmlLabels": true
  },
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif",
    "fontSize": "18px",
    "primaryColor": "#F8FAFC",
    "primaryBorderColor": "#334155",
    "lineColor": "#64748B"
  }
}}%%
```

若曲线仍缠绕，可改：

```text
"curve": "stepAfter"
```

或把完整图拆成分图。

## classDef 模板

```mermaid
classDef rootClaim fill:#E6F4FF,stroke:#1677FF,stroke-width:2px,color:#0F172A;
classDef majorClaim fill:#F0FDF4,stroke:#22C55E,stroke-width:2px,color:#0F172A;
classDef middleClaim fill:#F8FAFC,stroke:#64748B,stroke-width:1.5px,color:#0F172A;
classDef subClaim fill:#FFFFFF,stroke:#94A3B8,stroke-width:1px,color:#334155;
classDef evidenceLeaf fill:#FFF7ED,stroke:#F97316,stroke-width:1px,color:#431407;
classDef needsQc fill:#FEF2F2,stroke:#EF4444,stroke-width:1.5px,stroke-dasharray: 5 5,color:#7F1D1D;
classDef implicitPremise fill:#F5F3FF,stroke:#8B5CF6,stroke-width:1.5px,color:#2E1065;
```

节点创建后必须显式赋 class：

```mermaid
R0["R0 论文贡献"]:::rootClaim
X2["X2 具体核心发现"]:::majorClaim
P1["P1 机制 claim"]:::middleClaim
E001["E001 表4列(1): 系数=..."]:::evidenceLeaf
E034["E034 Fig S6: 缺补充材料"]:::needsQc
```

## 分图策略

完整 full-tree 通常不适合直接阅读。必须同时考虑：

1. 完整图：
   - 文件名：`evidence-expanded-mermaid.*`
   - 目标：保留全量 evidence leaf；
   - 缺点：可能很宽、很高、难读；
   - 用途：总索引、回归测试、证据覆盖检查。
2. 阅读分图：
   - `00-overview`
   - `01-x1-problem`
   - `02-x2-data-method-or-fabrication`
   - `03-mechanism-performance`
   - `04-stability-robustness-scale`
   - `05-contribution`
   - 场景子 Skill 可以调整命名。

分图必须从同一 ledger 派生；不能为了美观删除关键证据而不记录。

## 重叠与缠绕处理

Mermaid 大图重叠常见原因是节点过长、分支过多、曲线过多、rank 距离不足。

处理顺序：

1. 缩短节点 label，把长文本移入 ledger / summary；
2. 设置 `curve: "linear"` 或 `curve: "stepAfter"`；
3. 增大 `nodeSpacing` 和 `rankSpacing`；
4. 把 evidence 分支拆成阅读分图；
5. 使用 `subgraph` 分组，但不要让 subgraph 代替 ledger 层级；
6. 若仍重叠，保留完整 SVG，并在 README 说明使用分图阅读。

不要通过删除 evidence leaf 来“解决重叠”。

## 高清渲染

优先使用 Mermaid CLI / Chromium 渲染 PNG，因为它能正确处理 Mermaid 的 HTML labels 和中文文本：

```bash
npx --yes @mermaid-js/mermaid-cli \
  -i evidence-expanded-mermaid.zh.mmd \
  -o evidence-expanded-mermaid.zh.full-chrome-scale2.png \
  -b white \
  -w 24000 \
  -H 1800 \
  --scale 2
```

同时输出 SVG：

```bash
npx --yes @mermaid-js/mermaid-cli \
  -i evidence-expanded-mermaid.zh.mmd \
  -o evidence-expanded-mermaid.zh.svg \
  -b white
```

不要用 `rsvg-convert` 直接把 Mermaid SVG 转 PNG，除非已经确认文字正常。`rsvg-convert` 可能因为 Mermaid `foreignObject` / HTML label 支持问题，只渲染边框、不渲染文字。

如果必须从 SVG 转 PNG：

1. 先用 `view_image` 或图片查看器做人工确认；
2. 若只剩框没有字，立即废弃该 PNG；
3. 用 Mermaid CLI / Chromium 重新渲染。

## 验收清单

生成 Mermaid 和图片后，必须检查：

- 是否从 ledger 派生；
- 是否存在只靠代号无法理解的节点；
- 节点第一行是否是自然语言；
- 只读 Mermaid 是否能读出“证据 -> 子 claim -> 上层 claim -> 根结论”的逻辑；
- 是否区分 claim / evidence / needs-qc；
- 是否有中文版版本；
- 是否有完整图和分图；
- 是否有 reading view；若只有 audit view，必须说明不适合直接阅读；
- reading view 是否保留了 full-tree 证据颗粒度；若合并证据，是否明确标为 `summary-reading view`；
- 是否存在多个 evidence 被合并但没有 `merged-evidence-summary` 标记；
- 是否有图例解释颜色、虚线和 QC 标记；
- PNG 是否有文字，不是空框；
- PNG 尺寸是否足够大；
- README 是否告诉用户优先打开哪个文件；
- 旧的错误渲染图是否删除或明确标 `broken-no-text`；
- 日志是否记录渲染命令和 QC。

## 输出命名

推荐：

```text
evidence-expanded-mermaid.md
evidence-expanded-mermaid.zh.md
evidence-expanded-mermaid.zh.mmd
evidence-expanded-mermaid.zh.svg
evidence-expanded-mermaid.zh.full-chrome-scale2.png
evidence-expanded-mermaid.full-reading.zh.md
evidence-expanded-mermaid.full-reading.zh.mmd
evidence-expanded-mermaid.full-reading.zh.chrome-scale2.png
mermaid-zh-views/README.md
mermaid-zh-views/00-overview.zh.md
mermaid-zh-views/00-overview.zh.mmd
mermaid-zh-views/00-overview.zh.svg
mermaid-zh-views/00-overview.zh.chrome-scale2.png
```

若有英文版，同步生成 `mermaid-en-views/`。

## 边界

- 不在本 Skill 中重新抽树；
- 不新增 evidence；
- 不判断箭头强弱；
- 不用漂亮图替代 canonical ledger；
- 不把渲染成功等同于抽树质量成功。
