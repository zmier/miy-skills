---
type: reference
status: draft
source_case: CASE-260521-基金经理研究
---

# Research Project Structure

## 一句话

学术研究项目的顶层目录应表达研究主轴，不应被执行层目录接管。

```text
Top level tells the research story.
Workspace level holds execution details.
```

## 当前草案规则

对于处在孵化、数据可得性探索、文献定位和 paper 化之间的学术项目，顶层优先保留：

```text
README.md
docs/
literature/ 或 99-文献与项目管理/
manuscripts/ 或 papers/
final_outputs/
archive/
workspace/
```

`workspace/` 或 `research-workspace/` 承载执行层材料：

```text
workspace/
├── data/
├── code/ 或 common/
├── tasks/
├── experiments/
├── logs/
└── outputs/
```

## 为什么

`data/`、`common/`、`tasks/`、`experiments/`、`logs/`、`outputs/` 是研究项目的执行层。它们很重要，但它们不应该在顶层替代研究问题、文献定位、数据可得性、识别设计和论文路线。

顶层过早暴露执行层目录，会让项目看起来像一个数据工程或自动化工程，而不是一个学术研究项目。

## 适用边界

适用：

- 学术项目；
- 选题孵化项目；
- 数据可得性尚未完全确定的研究项目；
- 同时包含文献、数据、实验、论文和技术支线的项目。

不强制适用：

- 纯数据工程；
- 纯软件项目；
- 单一脚本仓库；
- 已经拆成独立代码库的项目。

## 迁移原则

不要为了清爽顶层立刻移动目录。先检查：

- README、Makefile、Notebook 是否引用旧路径；
- TASK 文档和脚本是否依赖旧路径；
- 数据下载或实验是否仍在进行；
- 是否需要先保留失败路线证据；
- 是否已建立新的项目地图和轻量索引。

推荐顺序：

```text
先写清理审计
→ 再建 workspace/ 或 research-workspace/
→ 再迁移执行层目录
→ 再更新 README / Makefile / docs 引用
→ 最后清理旧入口
```

## 数据采集工程与研究项目分离

来自 `CASE-260521-基金经理研究` 的补充规则：

```text
研究项目不应长期承载完整数据采集工程。
```

当一个学术项目为了数据可得性临时吸收了爬虫、逆向、Appium、RPC、抓包、调度队列、raw 响应和运行日志时，这些材料在探索期可以留在项目内。但一旦数据入口已经形成稳定 SQLite、CSV、Parquet 或其他可读研究库，就应考虑分层：

```text
研究项目
  保留：研究问题、文献定位、变量设计、只读数据入口、清洗后分析表、论文输出

数据采集工程
  保留：采集脚本、接口地图、请求池、raw 响应、设备/运行态日志、质量审计、调度与测试

Sources / 技能资料
  保留：课程资料、技术学习材料、可跨项目复用的工具知识
```

推荐原则：

- 研究项目内可放主库软链、只读副本或导出表；
- 全量 raw 和采集运行日志应留在独立数据工程；
- 技术课程资料应归入 Sources，而不是长期留在具体学术项目；
- 论文项目只引用数据说明、质量边界和可复现实证入口。

迁移状态：`draft-rule / first-forward-evidence / first-docs-cleanup-evidence`。

2026-07-05，`CASE-260521-基金经理研究` 已完成第一轮真实迁移：

```text
common/
data/
tasks/
experiments/
logs/
outputs/
```

已收束为：

```text
workspace/
├── common/
├── data/
├── tasks/
├── experiments/
├── logs/
└── outputs/
```

2026-07-05 后续迁移中，该 case 又完成了：

```text
主 SQLite 稳定软链入口
数据采集工程迁入「冒险者工会」
逆向课程资料迁入 Sources
docs/ 中外部技术剪藏迁入 Sources
旧 mPaaS/Reqable 长文迁入 archive
docs/ 中保留 DATA-AVAILABILITY.md 与 TECHNICAL-LEARNING-SOURCES.md 两个结论型入口
```

## docs/ 的结论型入口原则

来自 `CASE-260521-基金经理研究` 的补充规则：

```text
学术项目的 docs/ 不应长期承载原始技术资料剪藏。
```

在数据可得性探索期，`docs/` 可以临时承载技术路线长文、外部文章摘录和工具链判断。但当研究数据入口已经固化后，`docs/` 应收束为结论型、可引用、可服务论文和研究设计的文档：

```text
docs/
  保留：研究地图、数据入口、数据质量、文献地图、研究问题、路线结论、项目审计

archive/
  保留：旧路线长文、失败路线、旧项目管理尝试、过程复盘

Sources/
  保留：课程资料、外部技术文章剪藏、跨项目可复用技能资料
```

推荐原则：

- 外部文章剪藏不应长期留在研究项目 `docs/`；
- 技术路线长文应在完成路线取舍后归档；
- 研究项目 `docs/` 保留精简后的结论文档和索引；
- 若旧技术材料解释了数据可得性或合规边界，应保留 archive 路径并在结论文档中引用；
- 这个过程本身应写入迁移看板，作为项目结构演化证据。
