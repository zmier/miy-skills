---
name: timeline-ex
description: Build and maintain a data-driven External Timeline for projects whose route depends on outside notices, authorities, submission obligations, eligibility gates, reviews, approvals, decisions, or deadline windows. Use when a project needs a clickable HTML lifecycle timeline, EVT/OBL/GATE/OUT node records, dependency arrows, certainty-aware date windows, Gate registers, calendar projections, or traceable updates from new external notices without confusing external state transitions with internal TASK work.
---

# Timeline-Ex

状态：`structural-green / forward-tested-on-MPA`

## 定位

把项目的外部接口层表达成可追溯生命周期，而不是一张静态日程图。

```text
Roadmap    = 内部为什么这样推进、哪些 TASK 串成路线。
Timeline-Ex = 外部何时、由谁、依据什么条件允许项目进入下一状态。
TASK       = 为路线或外部 Gate 生产材料、证据和交付物的内部工作单元。
```

默认模型：

```text
结构化节点数据
→ HTML 时间主视图
→ 箭线式状态关系
→ 节点 Markdown 证据
→ Roadmap / TASK 交叉链接
```

不要把 Timeline-Ex 降级为 README 中的一串日期，也不要把每封普通通知都升级成顶层节点。

## 启用条件

当项目出现以下任一情况时启用：

- 外部机构、导师、客户、评审方或平台决定项目能否继续；
- 通知会新增、修改、确认或取消未来时间窗口；
- 申请、提交、查重、盲审、答辩、验收、审批、招标、上线等环节存在资格门槛；
- 某一 Gate 通过后才解锁下一 Gate，失败会进入延期、返工或终止分支；
- Roadmap 已能解释内部工作，却无法清楚表达外部生命周期；
- 用户需要时间缩放、今天标记、节点筛选、状态详情和来源追溯。

以下情况不启用：

- 只有一个普通截止日期，写在 TASK 说明中已足够；
- 通知、寒暄或会议不改变资格、时间、路线或责任；
- 项目只是内部执行流水线，没有外部状态转换；
- 用户只需要一个一次性汇报图，不需要维护节点和来源。

## 节点与箭线语法

只使用四类顶层节点：

| 类型 | 含义 | 例子 |
|---|---|---|
| `EVT` | 已发生的外部事件或权威通知 | 发布新规、老师发通知、客户变更要求 |
| `OBL` | 项目必须向外履行的义务 | 提交申请、递交材料、缴费、回复整改 |
| `GATE` | 外部资格、评审、批准或决策门槛 | 预答辩、盲审、验收、审批、上线许可 |
| `OUT` | 外部结果或条件后果 | 通过、驳回、延期、授位、终止 |

常用箭线：

```text
creates              = 新事件创建未来节点；
updates              = 新事件修改节点属性但不否认历史；
supersedes           = 新节点或新通知替代旧口径；
requires             = 进入本节点前必须满足；
participation-unlocks = 参加后获得下一步申请资格；
pass-unlocks         = 通过后解锁；
fail-leads-to        = 失败后进入某结果或返工分支；
produces-evidence-for = 内部 TASK 为外部 Gate 生产证据；
confirms             = 外部结果确认某状态。
```

这里吸收箭线图和项目进度网络图的依赖思想，但不要冒充严格的双代号箭线图：Timeline-Ex 的节点是外部状态对象，箭线表达语义关系，不一定代表耗时活动。

定义或扩展字段、状态和箭线前，完整阅读 [`references/node-contract.md`](references/node-contract.md)。

## 事实源与视图分工

使用以下层次，避免把内容、样式和证据混在一个 HTML 文件中：

```text
timeline-data.js = 当前节点状态与关系的结构化事实源；
nodes/*.md        = 通知原文、规则解释、影响和待确认项的证据源；
index.html        = 人首先打开的交互式主视图；
register.md       = 可选的纯文本表格投影；
calendar/reminder = 可选的提醒投影；
logs/log.md       = 追加式变更历史。
```

HTML 可以是主文档和主入口，但不能是唯一事实源。不要把节点数据写死在 DOM 卡片里。

## 推荐落点

默认放到项目级跨切面目录：

```text
docs/external-timeline/
├── index.html
├── timeline-data.js
├── assets/
│   ├── timeline.css
│   └── timeline.js
├── nodes/
│   ├── EVT-*.md
│   ├── OBL-*.md
│   ├── GATE-*.md
│   └── OUT-*.md
└── register.md              # 可选
```

只有当外部生命周期完全属于一个 TASK、不会影响其他任务或项目级路线时，才放到 `tasks/TASKxx/docs/external-timeline/`。

## 构建流程

### 1. 审计权威来源

- 保存通知原文、文件、邮件或稳定来源链接；
- 区分权威原文、用户转述、Agent 推断；
- 记录收到日期与发布方；
- 不为缺失字段补写虚构规则。

### 2. 先登记 EVT

把会改变路线的通知登记为不可覆写的 `EVT` 节点。新通知到来时新增 EVT，再用 `updates` 或 `supersedes` 连接旧节点，不要直接改写历史通知。

### 3. 派生 OBL / GATE / OUT

逐条抽取：

- 谁必须做什么；
- 何时开始、截止或发生；
- 哪些条件决定可申请、可进入、通过或失败；
- 通过后解锁什么；
- 失败、错过或驳回会发生什么；
- 哪些内容仍待后续通知。

### 4. 映射内部 TASK

不要把 Gate 当成 TASK：

```text
TASK：准备预答辩材料
  -- produces-evidence-for -->
GATE：第 1 轮预答辩
```

在节点中记录 `affectedTasks`，并在 TASK Roadmap 或说明中回链所服务的 Gate。外部节点不进入 TASK 编号序列。

### 5. 处理时间确定性

保留原始语言：

```text
exact       = 官方精确日期；
confirmed-window = 官方确认的月份或区间；
tentative   = 暂定窗口；
window      = 只有月份/季度范围；
tbd         = 尚无时间；
conditional = 仅在条件触发后发生。
```

若可视化库需要精确起止日，可为“1 月初”“下旬”“某月”指定近似展示区间，但必须：

- 保留 `displayTime` 原文；
- 标明 `certainty`；
- 在页面和节点档案声明近似区间仅用于布局；
- 不把近似日写入日历或对外提交材料。

### 6. 生成 HTML 主视图

复制并定制 [`assets/static-template/`](assets/static-template/)；默认使用：

```text
原生 HTML/CSS
+ vis-timeline 时间视图
+ timeline-data.js 数据源
+ 生命周期链 / Gate 表格 / 详情抽屉
```

完整阅读 [`references/html-architecture.md`](references/html-architecture.md) 后再修改模板。

第一版不要引入 React、Ant Design 或 Tailwind。只有当项目需要在线编辑表单、多人协作、后端状态或大量 UI 组件时，才考虑 React + Ant Design。只有当依赖网络复杂到时间视图无法解释时，才增加 AntV G6 作为第二个“依赖网络”标签页。

### 7. 更新项目入口

- 从项目 `README.md` 链接 `index.html` 和节点档案入口；
- 在 Roadmap 中说明“内部路线”和“外部生命周期”的边界；
- 更新受影响 TASK 的下一步、风险或验收条件；
- 在项目日志中记录通知如何改变 Timeline。

### 8. 验收

至少检查：

- 节点 ID 唯一；
- 所有箭线端点存在；
- 每个节点的 Markdown 档案存在；
- EVT 原文与派生 Gate 没有越界推断；
- 暂定、窗口、条件和确定日期视觉上可区分；
- HTML 主视图可打开，时间缩放、筛选、详情抽屉可用；
- CDN 不可用时有可读降级视图；
- Roadmap 与 TASK 没把外部 Gate 伪装成内部可控工作；
- 新通知采用追加式更新，而非覆盖历史。

## HTML 视觉原则

- 使用真实时间比例，不把时间顺序伪装成等间距步骤；
- 同时提供生命周期链，解释 `creates / pass / fail` 关系；
- 用稳定颜色编码类型，用实线/虚线编码确定性；
- 显示“今天”竖线、当前批次、下一 Gate 和失败影响；
- 点击节点打开详情和来源档案；
- 提供表格降级视图，保证搜索、复制和无脚本阅读；
- 视觉美化服务状态识别，不用装饰动画掩盖不确定性。

## 更新协议

收到新外部信息时按顺序执行：

```text
新增 EVT
→ 与当前 Timeline 做差异比较
→ 新建 / 更新 / supersede 受影响节点
→ 更新 timeline-data.js 与节点档案
→ 更新受影响 TASK / Roadmap
→ 更新 register / calendar / reminder 投影
→ 追加日志和残余不确定性
```

如果新信息只确认精确日期，保留原 EVT，并新增确认 EVT 或在新来源清楚可追溯时更新 Gate 的 `certainty/sourceEvents`。不要删除最初通知。

## 反模式

不要：

- 用一个巨大 HTML 同时保存数据、原文、样式和历史；
- 为了“完整”把所有邮件、会议和聊天都画成节点；
- 把 `暂定 1 月初` 写成 `1 月 5 日正式截止`；
- 把外部 Gate 编成 `TASK03`，暗示它由内部执行即可完成；
- 只画时间点，不画资格依赖和失败分支；
- 只画漂亮箭线，不提供稳定 Markdown 证据；
- 新通知到来后静默覆盖旧口径；
- 第一版就引入重型前端工程、数据库或编辑器。

## 来源追溯

本 Skill 的对话洞见、教材映射、MPA 前向测试及泛化边界见 [`references/source-provenance.md`](references/source-provenance.md)。领域通知、姓名、学号和具体授位材料保留在 MPA 项目，不进入通用 Skill。
