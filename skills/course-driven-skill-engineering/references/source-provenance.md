# Source Provenance

## 外部提示词样本：中英提示词.pdf

- 记录日期：2026-06-25
- 来源类型：小红书转存的 PDF 提示词样本
- 本地路径：`/Users/narra/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/wxid_ivssdy1liead12_3cf9/temp/drag/中英提示词.pdf`
- 材料形态：`CLAUDE.md` 风格的中英双语学习仓库提示词
- 原始领域：CFP 考试备考
- 迁移目标：课程/教材学习会话治理
- 新增文件：`references/guided-learning-session-governance.md`
- 迁移状态：`structural-green / forward-test-pending`

## 采纳内容

- 引导式学习：先问已有理解，再讲解，再做理解检测。
- 会话记录：保存用户问题、初始理解、讲解方式、理解检测、掌握点和盲区。
- 全局进度：维护一个 single source of truth，避免多个 tracker 互相竞争。
- 高风险事实核验：对时效性强或高风险内容先查证，再讲解。

## 未采纳内容

- CFP 考纲、分值、具体科目和备考优先级。
- Roth IRA 等个案示例。
- 强绑定 `/sessions/`、`/progress/cfp-study-tracker.md` 的固定路径。
- “每次都必须联网”的领域化规则；已泛化为高风险/易过期事实核验。

## 清洗方式

- 去除 CFP 个案固定值；
- 去除固定目录约束；
- 将考试备考语境上抽为长期学习项目；
- 将提示词表达改写为 Skill/reference 可执行规则；
- 标记为尚需 forward-test，不写成已验证能力。

## 本地学习项目：SMK 实证资产定价逐章学习

- 记录日期：2026-06-25
- 来源类型：本地学习项目中的对话洞见与 TASK 产物
- 项目路径：`/Users/narra/Documents/alib/Writer/02 Sources/SMK/0 学术体系/实证资产定价-横截面股票收益`
- 关键证据：
  - `tasks/TASK02-原书方法框架精读/outputs/逐章学习档案/章节知识点TODO-总表.md`
  - `tasks/TASK02-原书方法框架精读/outputs/逐章学习档案/Ch01-Preliminaries-学习档案.md`
- 迁移目标：长期教材学习中的章节主线控制
- 新增文件：`references/textbook-learning-project-workflow.md`
- 影响文件：`references/guided-learning-session-governance.md`
- 迁移状态：`structural-green / forward-test-pending`

### 采纳内容

- 每章正式学习前建立知识点 TODO。
- 用户问题归入 `主线内 / 主线旁路 / 停车场`。
- TODO 字段包含知识点、角色、状态和通过标准。
- 核心 TODO 未完成，不进入下一章。
- 每轮讲解要声明正在推进哪个 TODO，并及时更新状态。
- 长期教材学习需要项目承载层，而不是只停留在聊天窗口。
- 技术拆书适合作导航，不能替代原书精读。
- 学习档案应记录用户问题、讲解、复述、盲区和项目迁移判断。
- 教材方法可以迁移到真实项目，但原书结论、变量口径和数据边界要单独审查。

### 未采纳内容

- 实证资产定价的具体章节知识点。
- A 股复现主题、数据字段、因子口径等项目固定内容。
- Ch.1-Ch.6 的具体表格。
- 具体 book-to-skill 输出文件、A 股数据路径和实盘语境细节。

### 清洗方式

- 将“逐章 TODO”上抽为“学习单元 TODO 控制”；
- 将“章节完成”上抽为“学习单元 Green”；
- 保留状态机和停车场机制；
- 将“SMK 项目建档、拆书、精读、迁移、刷题、反哺”上抽为教材学习项目工作流；
- 不把金融教材内容写入元 Skill。

## 本地方法系统：刷题学习法与 quiz-bank-builder

- 记录日期：2026-06-25
- 来源类型：本地刷题系统方法论与题库构建 Skill
- 本地路径：`/Users/narra/Documents/alib/Writer/99 Assets/Apps/刷题系统`
- 关键证据：
  - `刷题学习法.md`
  - `quiz-bank-builder/SKILL.md`
  - `quiz-bank-builder/references/knowledge-management.md`
- 迁移目标：课程/教材材料的原子知识点覆盖表与题库化流程
- 新增文件：`references/atomized-reading-to-quiz-workflow.md`
- 影响文件：`references/guided-learning-session-governance.md`
- 迁移状态：`structural-green / forward-test-pending`

### 采纳内容

- 题目是原子知识点的检测器。
- 先用低摩擦单选题建立识别能力，再逐步升级题型。
- 题库结果要回流课程层知识修复、Zettelkasten 和 MOC，而不是孤立停留在题库里。
- 每道题应能映射回章节、知识点和修复位置。

### 未采纳内容

- 刷题系统的具体 JSON schema 字段细节。
- 某个题库文件名、HTML 构建路径和本地 App 实现细节。
- 考试真题优先的具体备考语境；在教材学习项目中泛化为“可靠来源优先，模型题需标注来源”。

### 清洗方式

- 将“刷题学习法”上抽为学习项目中的诊断分支；
- 将刷题系统的课程层/Zettelkasten/MOC 三层回流，转写为通用学习项目回流协议；
- 保留题库来源标注和错题修复原则；
- 不把具体 App 工程路径写进 Skill 主流程。

## 本地学习项目：SMK 实证资产定价 Ch1-Ch6 题库化

- 记录日期：2026-06-25
- 来源类型：本地学习项目中的 TASK 设计与对话洞见
- 项目路径：`/Users/narra/Documents/alib/Writer/02 Sources/SMK/0 学术体系/实证资产定价-横截面股票收益`
- 关键证据：
  - `tasks/TASK02-原书方法框架精读/subtasks/SUBTASK02A-刷题学习法题库化/SUBTASK02A-说明.md`
  - `tasks/TASK02-原书方法框架精读/subtasks/SUBTASK02A-刷题学习法题库化/outputs/Ch1-Ch6-原子知识点覆盖表模板.md`
  - `references/dialogues/2026-06-25-逐段读与刷题学习法题库化.md`
- 迁移目标：长篇教材逐段读取、段落功能分类、atom 覆盖表和题库化的通用协议
- 新增文件：`references/atomized-reading-to-quiz-workflow.md`
- 迁移状态：`structural-green / forward-test-pending`

### 采纳内容

- 覆盖表应逐章建立，并回到原文逐段判断。
- 逐段读不等于每段都抽题，应先做段落功能分类。
- atom 必须能被一道题检测，且有明确正确/错误边界。
- 正式题库生成前必须先完成覆盖表。
- 题量不机械平均到章节，而按知识密度、易混点和迁移价值决定。

### 未采纳内容

- Ch1-Ch6 的具体资产定价知识点。
- A 股热榜因子、非平衡 panel 等项目讲解样例。
- 具体正式题库和 smoke 题库路径。

### 清洗方式

- 将“前 6 章刷题化”上抽为“长篇学习材料 atom-to-quiz 工作流”；
- 将资产定价例子去领域化，只保留抽取与题库化动作；
- 将具体题库产物留在 SMK 项目和刷题系统中。

## 对话修正：不只沉淀逐段读

- 记录日期：2026-06-25
- 来源类型：用户对 Skill 反哺范围的即时修正
- 触发原话：`不仅仅是逐段读哦！前面讨论的那些相关的，都应该沉淀进来吧？`
- 迁移目标：避免把教材学习项目误缩窄为 atom 抽取流程
- 新增文件：`references/textbook-learning-project-workflow.md`
- 影响文件：
  - `references/atomized-reading-to-quiz-workflow.md`
  - `references/guided-learning-session-governance.md`
  - `references/dialogues/2026-06-25-逐段读与刷题学习法题库化.md`
- 迁移状态：`structural-green / forward-test-pending`

### 采纳内容

- 整本教材学习需要总工作流承接，而不是只沉淀逐段读取。
- 前序讨论中的项目建档、book-to-skill 调研、原书精读、逐章档案、TODO 主线控制、A 股迁移、刷题诊断、知识修复和 Skill 反哺，属于同一条教材学习工程链。
- atom-to-quiz 应作为总工作流的刷题分支，而不是替代总工作流。

### 清洗方式

- 将用户提醒上抽为 reference 层级设计规则；
- 把总链路写入 `textbook-learning-project-workflow.md`；
- 保留 `atomized-reading-to-quiz-workflow.md` 作为更细的执行协议。
