# 自动抽与共同读：从并列模式到前后依赖

## 背景

在 `research-literature-reader` 当前结构中，`paper-reading` 将阅读模式分为：

```text
collaborative-reading：对话优先，先给用户 Paper Orientation Card，再等待追问或确认。
automatic-summary：文件优先，Agent 自动整理摘要 / extraction / route mapping。
```

这容易让 Agent 误解为：

```text
automatic-summary 和 collaborative-reading 是两个并列选项；
用户要共同读，就不需要先自动抽。
```

但在本次阅读 `Does Media Coverage of Stocks Affect Mutual Funds' Trading and Performance` 的过程中，实际经验显示：高质量的共同读并不是从零开始聊天，而是依赖 Agent 已经完成一轮结构化自动抽。

## 新认知

更合理的关系不是：

```text
automatic-summary vs collaborative-reading
```

而是：

```text
automatic extraction
  -> 产出结构化阅读文档
  -> collaborative reading 使用该文档作为输入
  -> 生成 / 修订 discussion agenda
  -> 与用户共同推进、纠偏、深化
```

换句话说：

```text
自动抽 = 完整能力 / 完整产物；
共同读 = 基于自动抽产物继续进行的交互式处理。
```

## 为什么共同读需要自动抽

共同读要生成一个好的 Agenda，前提是 Agent 已经知道论文的大致论证结构。

至少需要先抽出：

```text
作者核心断言；
形式逻辑结构；
命题支 P1/P2/P3；
A02 概念 / 构念 / 理论关系 / 文献基础；
A03 操作化 / proxy bridge；
A04 测量与数据构造；
A05 研究设计 / 识别策略；
A06 资料分析 / 结果；
A07 替代解释 / 稳健性 / 有效性威胁；
A08 项目迁移初判；
source anchors / unresolved questions。
```

如果没有这层自动抽，所谓共同读很容易退化为：

```text
泛泛摘要；
主 X / 主 Y 填空；
机制 / 文献 / gap / 识别 的八股栏目；
没有命题支回挂的表格罗列；
无法支撑用户持续追问的薄 Agenda。
```

## 自动抽不是共同读的临时内部步骤

需要特别区分：

```text
自动抽不是共同读内部的一次临时思考；
自动抽应是一个完整、可复用、可追溯的文献资产。
```

它应该有自己的稳定产物，例如：

```text
automatic-extraction.md
task-specific-extraction.md
或某种 structured-reading-extraction.md
```

这个产物可以独立服务：

```text
自动摘要；
批量文献整理；
route mapping；
实验设计提取；
后续共同读；
UAT / 复盘 / 审计。
```

## 共同读的定位

共同读不是“少抽”或“跳过自动抽”，而是：

```text
读取自动抽产物；
判断哪些地方适合先讨论；
生成 Discussion Agenda；
用低假设方式向用户呈现；
根据用户问题不断校正、深化、重排；
必要时反向修订自动抽产物或升级项目资产。
```

因此，共同读的高级之处不是不做结构化，而是：

```text
抽完以后不武断落锤；
而是把结构化理解转化成可讨论、可追问、可纠偏的 Agenda。
```

## 新架构草案

建议将 `research-literature-reader` 的阅读管线重构为：

```text
PDF / Markdown substrate
  -> automatic extraction document
  -> collaborative-reading discussion-outline
  -> task-specific extraction / route map / writing patterns
```

对应关系：

```text
automatic extraction:
  完整能力；
  产出结构化阅读文档；
  可以独立完成，也可以作为共同读输入。

collaborative reading:
  交互式处理能力；
  读取 automatic extraction 产物；
  生成 Orientation Card、Discussion Agenda、Discussion Ledger；
  与用户共同推进。

automatic summary:
  可能不应再作为与 collaborative reading 并列的“阅读模式”；
  更像 automatic extraction 的一种输出形态或下游资产化方式。
```

## 对现有 Skill 的潜在修改方向

后续可考虑修改：

```text
research-literature-reader/SKILL.md
skills/paper-reading/SKILL.md
skills/paper-reading/skills/automatic-summary/SKILL.md
skills/paper-reading/skills/collaborative-reading/SKILL.md
```

可能调整：

1. 将 `automatic-summary` 重命名或重定位为 `automatic-extraction`。
2. 将 `collaborative-reading` 声明为依赖 `automatic-extraction` 产物。
3. 明确共同读第一轮 Orientation Card / Agenda 的输入包括：
   - Markdown substrate；
   - automatic extraction document；
   - 当前 task / route；
   - 用户问题。
4. 如果没有 automatic extraction document，collaborative-reading 应先生成最小自动抽产物，再进入对话。
5. 将 discussion-outline 与 automatic extraction 分离：
   - automatic extraction = 结构化阅读底稿；
   - discussion-outline = 协同阅读工作台。

## 当前不立即修改的原因

这是一个架构层调整，影响父 Skill、paper-reading 路由、automatic-summary 命名、collaborative-reading 输入协议和文献资产结构。

因此本日志先记录认知，不直接改稳定规则。后续应单独开一次 Skill 重构任务，并用 `miy-uat` 验证：

```text
无 automatic extraction 时，协同阅读是否会先生成自动抽底稿；
有 automatic extraction 时，协同阅读是否能读取它生成更好的 Agenda；
automatic-summary 是否被正确重定位为 extraction/document-output，而不是和 collaborative-reading 平行竞争。
```

