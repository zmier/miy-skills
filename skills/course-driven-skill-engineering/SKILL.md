---
name: course-driven-skill-engineering
description: 将课程、训练营、教程、探索性课程项目、真实案例研究或对话洞见转化为可执行、可验证、可迁移的 Skills 体系。用于先冻结教师解法并独立复现，再解冻课程路线做差异分析，或在没有标准答案的探索性项目、真实项目反馈、心流讨论和共同推理中，把红灯、环境限制、服务端反馈、研究发现和方法论洞见沉淀为领域总编排 Skill、子 Skills、TASK 模板、evaluation 与迁移测试。用户提到边学课程边制作 Skills、先自己做再对照老师、把课程方法工程化、用案例完善 workflow、元 Skill、探索性课程作业、真实项目反哺 Skills、对话洞见、心流讨论沉淀、dialogue insight 或课程驱动的 Skill 研发时使用。
---

# 课程驱动的 Skill 工程

把课程案例、探索性项目、外部技术情报或对话洞见视为能力研发实验，而不是待抄写的标准答案：

```text
定义终点
→ 选择模式：标准课程 / 探索性课程项目
→ 冻结教师解法或冻结初始假设
→ 独立复现或探索推进
→ 解冻课程路线或吸收真实反馈
→ 或执行技术雷达评估
→ 或捕捉对话洞见
→ 选择性平行实验或路线转向
→ 提炼或升级 Skills
→ 回归与迁移评测
```

## 启动

1. 确认课程、案例或探索性项目、现有领域 Skills、目标产物与授权边界。
2. 阅读 `references/collaboration-boundaries.md`，决定是否调用：
   - `simon-learning-card-builder` 处理首次学习和知识卡片；
   - `task-driven-project-manager` 创建 TASK、日志和测试工程；
   - `skill-creator` 创建或更新具体 Skill。
3. 判断项目模式：
   - `course-case`：有明确课程案例、教师路线和可对照答案；
   - `exploratory-course-project`：由课程触发，但目标、数据通道、服务端行为或完成边界需要通过实验逐步发现；
   - `hybrid`：先按课程案例复现，随后进入真实项目扩展。
   - `technology-radar`：由官方文档、论文、工具 release、GitHub issue、工程文章或安全社区资料触发，用来判断外部技术进展是否改变现有 workflow。
   - `dialogue-insight`：由用户与 Codex 的心流讨论、共同推理、困惑澄清或方法论顿悟触发，用来先保存原始问题形状，再回顾提炼可迁移规则。
4. 从 `assets/case-charter-template.md` 创建案例研发契约；探索性项目还要读取 `references/exploratory-course-projects.md`。
   技术雷达项目读取 `references/technology-radar-feedback.md`，不必伪装成课程案例。
   对话洞见读取 `references/dialogue-insight-feedback.md`，必要时从 `assets/dialogue-insight-template.md` 创建 dialogue 札记。
5. 先审计已读材料是否泄漏关键函数、算法、参数或操作路线，再声明独立性：`strict-blind / limited-blind / prior-exposed / assisted / exploratory`。
6. 声明当前阶段：`blind / comparison / parallel / exploratory / extraction / transfer`。
   技术雷达可声明为 `radar / impact-assessment / extraction / transfer`。
   对话洞见可声明为 `flow / capture / review / transfer`。
7. 对教师材料、初始假设或既有经验设置冻结范围，并按 `references/blind-first-protocol.md` 执行。
8. 如果用户要求“按 Roadmap 连续推进直到交付”，进入批量推进模式：先确认 Roadmap、剩余 TASK、共享规则和停止条件；随后每个 TASK 固定输出“workflow 位置、之前是什么样、加入之后是什么样”，并在不改变授权边界和任务目标的前提下自主推进。

## 主流程

### 1. 定义终点与基线

- 明确最终要复现的现象、算法、工具工作流或交付物。
- 预先定义 Smoke、Unit、阶段 Green、端到端验收和安全边界。
- 清点现有 Skills，记录本案例开始前已经具备的能力。
- 区分“课程目标信息”和“教师解法信息”；前者可用于定目标，后者在 blind 阶段冻结。
- 知识地图若直接写出算法、关键工具或数据形态，也属于解法信息，不能因文件名叫“知识地图”就视为无泄漏。
- 对探索性项目，先定义可变终点和停止条件：当前要证明什么、允许发现什么新红灯、哪些结果只算阶段 Green，哪些结论必须等待更多入口或样本确认。

### 2. 独立复现

- 只使用目标、原始样本、合法环境、现有 Skills 和自己产生的证据。
- 按 ReAct 记录 Reason、Action、Observation、Decision。
- 每项结论标注证据来源；课程笔记不能作为独立复现的 Green。
- 遇到阻塞时先尝试替代工具、降级路径和最小实验，不为赶进度提前解冻答案。
- 达到终点、明确阻塞，或继续探索的成本明显超过收益时结束 blind 阶段。
- 对探索性项目，把真实反馈也当作课程材料：服务端限制、UI 入口变化、账号风控、接口分页窗口、工具不可见流量和数据覆盖不足，都要进入 TASK 日志，并判断是否升级领域 Skill。

### 3. 教师路线对照

- 解冻课程笔记、代码和视频路线。
- 使用 `assets/route-comparison-template.md` 比较：
  - 目标与前提；
  - 工具和步骤；
  - 中间证据；
  - 效率、稳定性和可解释性；
  - 适用条件、失败模式和迁移价值。
- 不以“步骤不同”直接判定谁错；先检查版本、环境、函数边界、地址语义和交付目标是否不同。
- 按 `references/parallel-path-decision.md` 判断是否补做教师平行路线。

### 4. 平行实验

只在能获得新增价值时补做：

- 新知识或新工具能力；
- 更短、更稳或更通用的路径；
- 对独立结论的高价值交叉验证；
- 能揭示工具边界、失败模式或路线选择条件；
- 教学目标本身要求掌握该操作。

把平行 TASK 标注为 `blocking`、`confirmatory` 或 `enhancement`，不得自动回滚已通过的主交付。

### 4.5 批量推进

当一组课程 TASK 已有稳定规则和 Roadmap 时，可以连续推进，不必每个 TASK 都等待人工确认。

批量推进前必须满足：

- 用户已明确授权连续推进；
- 已有 Roadmap 或待处理 TASK 列表；
- 资产纳入、provenance、Skill 主体去课程化、upstream/optimized、个案脚本隔离等共享规则已经明确；
- 每个 TASK 的授权边界、停止条件和不能触碰的环境清楚。

每完成一个 TASK，至少更新：

- TASK 说明、case charter、审计或 UAT；
- 被影响的 Skill、reference、asset 或 template；
- 能力注册表、来源追溯文件、Roadmap 和 log；
- 当前状态：`workflow-integrated / upstream-copied / template-green / new-skill-valid / not-forward-tested` 等。

如果发现某个 TASK 需要真实设备、账号、服务端、付费工具、生产环境或明显高风险操作，先把它降级为 `forward-test-pending` 或 `blocked-by-environment`，不要为了完成 Roadmap 伪造 Green。

### 4.6 对话洞见捕捉

当方法论是在用户与 Codex 的讨论中共同生成，而不是直接来自课程、案例文件或外部资料时，按 `dialogue-insight` 处理：

- 先保留心流讨论的原始问题形状，不急于压缩成 Skill 规则；
- 使用 `assets/dialogue-insight-template.md` 在目标 workflow 的 `references/dialogues/` 或 case 的 `dialogue-insights/` 下创建札记；
- 标明触发场域，例如某个 course case、field case、技术雷达或普通对话；
- 区分：
  - `raw dialogue`：原始问答和困惑，至少包括用户原话、Codex 当时回答的核心内容，以及共同推进出的关键表达；
  - `shared discovery`：共同发现；
  - `candidate principle`：候选方法论命题；
  - `skill implication`：可能反哺的 workflow、Skill、reference 或 template；
- 暂不把未经回顾的顿悟写入通用 Skill 主流程；
- 讨论告一段落后再回顾，判断它应保留为思想札记、进入 reference、升级 workflow 规则、进入 domain adapter，还是形成新 Skill；
- 若该洞见由真实案例触发，case README 应反向链接对应 dialogue；case 保存证据，dialogue 保存共同思考，Skill 保存已成熟规则。

读取 `references/dialogue-insight-feedback.md` 获取完整边界、状态标记和反哺标准。

### 5. 提炼 Skills

1. 先判断发现属于：
   - 领域知识；
   - 可复用程序步骤；
   - 可执行资产或脚手架模板；
   - 路线选择规则；
   - 分支参考路由；
   - 工具适配器；
   - 失败降级策略；
   - 交付形态约定；
   - 对话洞见；
   - 个案固定值。
2. 个案固定值留在 TASK 或 fixture，不写入通用 Skill。
3. 通用 Skill 主体只写可迁移规则、路线选择、输入输出、完成标准和安全边界；课程名、老师脚本名、固定 App 名、固定 URL、固定输出值和案例过程不得写进普通领域 Skill 的主流程。
4. 课程相关引用信息不能因为去课程化而删除。每次课程反哺 workflow，都要写入单独的来源追溯文件，例如 workflow 级 `references/course-provenance.md`，或 Skill 级 `references/source-provenance.md`。追溯文件记录课程/案例、原始笔记或代码路径、对应 TASK、被影响的 Skill/assets/scripts/references、证据角色、清洗方式、迁移状态和 forward-test 状态。
5. TASK、fixture、evaluation 和能力注册表可以保留课程锚点，但职责不同：TASK 记录过程证据，fixture/evaluation 记录可复验样本，能力注册表只做能力摘要，来源追溯文件负责集中回答“这个能力最初来自哪里、参考了什么、清洗成了什么”。
6. 若课程提供了可复用代码，不只写文字总结；先判断它应进入：
   - `assets/`：可复制模板、脚手架、配置样例；
   - `scripts/`：可直接运行的通用工具；
   - `references/`：路线对比、失败模式、证据契约；
   - TASK：绑定具体 App、固定值或授权资料的代码。
7. 区分通用脚本与特定案例脚本：
   - 通用脚本可以进入 Skill 的 `assets/upstream-*`，保留原始脚本和 upstream README，便于换环境时直接使用；
   - 若你认为原脚本可读性、配置、脱敏、日志格式或安全边界需要改进，可以同时提供 `optimized-*` 或模板化版本，但不要删除 upstream 原件；
   - 特定案例脚本、绑定某 App/包名/host/token/固定字段/固定 so 偏移的脚本，不原样进入通用 Skill，只能放在对应 TASK、fixture、case evidence 或 provenance 中引用；
   - 一个脚本若既有通用框架又夹带个案值，先拆分：通用框架进入 assets，个案配置进入 TASK-local manifest。
8. 对课程代码做清洗时，去掉固定 PID、固定包名、固定类名、真实 header/token/device id、真实 host、绝对路径和个案输出；替换为占位符、输入 schema、脱敏策略和 TASK-local manifest。
9. 优先升级已有 Skill；只有职责独立且可复用时才创建新 Skill。
10. 从案例漏点提炼规则时，避免把个案样例写成碎片化 checklist：
   - 先列出样例背后的共同判断动作、关系类型、触发条件和停止条件；
   - 能上抽为稳定动作的，写成上位规则，例如“识别关键概念并判断概念关系”，而不是只列“速度/总量、手段/结果、局部/整体”；
   - 只能在该案例成立、无法上抽的，留在 TASK、fixture、revision notes 或 reference comparison；
   - 如果上抽后的规则过宽，补上适用边界和反例，不用一串例子假装完成泛化。
11. 当课程内容高级、低频、工具链重、暂时没有当前案例复现需求，但能显著帮助某类红灯定位和路线选择时，采用 `branch-reference routing`，即“分支参考路由型反哺”：
   - 不急于创建新 Skill，也不把课程内容写成默认主流程；
   - 在相关分支 Skill 或 reference 中补充触发条件、首差红灯、课程查字典入口、回到 workflow 的下一步和证据边界；
   - 课程材料只作为解释、补课、寻找样本和路线选择参考，不能作为当前样本 Green；
   - 适合 OLLVM、VMP、eBPF、定制 ART、内核断点、复杂反调试、特定工具链横评等“平时不必走，一旦遇到就很关键”的资料；
   - 不适合已有通用脚本、明确靶场案例、常用主流程知识、泛泛科普或强绑定个案固定值的资料。
12. 分支参考路由型反哺至少落盘：
   - 触发它的红灯或判断条件；
   - 对应现有分支 Skill；
   - 课程目录、课时、笔记或转写位置；
   - 使用边界：查资料不等于完成证据；
   - 回到当前 workflow 的动作，例如静态确认函数窗口、动态 trace、补环境、路线横评或另开 TASK；
   - 来源追溯与迁移状态，通常标记为 `structural-green / forward-test-pending`。
13. 执行分支参考路由型反哺时，按“课时簇审计”推进：
   - 先把课程目录按能力簇分组，例如 Java Hook 基础、Native Hook 基础、OLLVM 动态辅助、Trace/Stalker；
   - 对每个能力簇列出候选承接 Skill、红灯触发条件和回到 workflow 的动作；
   - 逐个检查现有 Skill 是否已经覆盖：已覆盖则只在来源追溯或课程索引记录，不重复污染 Skill；覆盖不足才补 reference 入口；
   - 低频高级内容优先补到分支 reference，不写进总编排默认步骤；
   - 常用基础内容若只是补课入口，写成“反复卡住时查看”的弱触发，不升级为必经路线；
   - 明确记录“不补”的理由，例如已有资产覆盖、过于基础、太像泛泛科普、当前没有可迁移动作或会让主流程变重。
14. 对每个候选分支参考路由，使用“双价值四象限”判断是否值得写入分支 Skill：
   - 高 Codex 执行价值 / 高用户学习价值：最优先补到分支 Skill 或 reference。它既能降低自动执行时的路线判断成本，又能帮助用户把真实红灯和课程知识接起来。
   - 高 Codex 执行价值 / 低用户学习价值：补到 Skill，但写成简短执行规则、路线选择或失败降级，不必保留显眼课程入口。
   - 低 Codex 执行价值 / 高用户学习价值：优先放到课程索引、知识卡片、README 或 provenance；若写入 Skill，只能作为弱触发的补课入口，不得阻塞任务推进。
   - 低 Codex 执行价值 / 低用户学习价值：不补到 Skill，只在盘点表中记录“不补”理由。
15. 判断 Codex 执行价值时，看它是否能减少路线误判、补齐失败分层、提供可迁移动作、暴露工具边界或提高证据质量。判断用户学习价值时，看它是否能解释关键概念、连接课程进度、帮助复习、降低认知负担或支持后续自主判断。
16. 分支参考路由不得把“课程入口”变成“人工补课阻塞”。默认由 Codex 读取现有索引、笔记、转写和 reference 后继续推进；只有用户明确进入学习模式，或资料缺失导致无法解释某个知识点时，才建议用户观看原课。
17. 使用 `assets/skill-change-proposal-template.md` 记录触发证据、变更位置、泛化边界和回归范围。
18. 创建新 Skill 或大幅修改时调用 `skill-creator`；工程结构交给 `task-driven-project-manager`。
19. 同步更新总编排的能力注册表、路由、模板、evaluation 和来源追溯文件。
20. 完成后执行一次“Skill 主体去课程化”审计：普通领域 Skill 的 `SKILL.md` 不应出现具体课程来源、老师脚本名或 App 名；这些信息应只出现在课程迁移 Skill、TASK、能力注册表、评测记录或专门的来源追溯文件中。分支参考路由可以在 reference 或课程索引中保留课程入口，但主流程必须写成通用触发条件。
21. 对审计结果分层：本轮新增或修改内容必须立即修正；历史遗留措辞或既有技术债可以进入 `cleanup-debt`，不得阻塞本轮结构交付，但必须在 UAT 中声明。

课程中的交付形态也要作为可迁移能力评估。例如 Java wrapper、Python subprocess caller、HTTP wrapper、CLI/Jar、Makefile target、Notebook dashboard 等，可能不改变逆向路线，但会改变能力是否可复跑、可迁移、可验收。

探索性项目提炼时额外区分：

- `workflow-rule`：流程规则，如先判断目标流量是否走系统代理；
- `research-strategy`：研究策略，如多入口扩展问题 ID 再去重；
- `operational-safeguard`：操作约束，如限速、断点续跑、脱敏保存；
- `data-boundary`：数据边界，如服务端只暴露约 1000 条访问窗口；
- `tooling-gap`：工具缺口，如 GUI 抓包不够可重复，需要 mitmproxy/Frida RPC。

这些发现不一定来自教师路线，但只要可复用、可验证、边界清晰，就可以反哺 Skills。

技术雷达提炼时额外区分：

- `platform-change`：平台变化，如 Android 新版本、ART、权限、内存安全或安装验证变化；
- `toolchain-change`：工具变化，如 Frida、Unidbg、IDA、JADX、Magisk、LSPosed、KernelSU、mitmproxy 等版本和兼容性变化；
- `research-signal`：论文、会议或研究项目暴露的新路线；
- `ecosystem-signal`：开源项目、issue、PR 或社区文章体现的工程趋势；
- `watchlist`：暂不修改 workflow，但值得定期观察的主题。

技术雷达反哺的关键不是“追最新”，而是判断新资料是否改变某个 `X -> ✅` 路线、失败分层、工具边界或证据标准。没有明确 workflow 影响的资料，优先放到技术雷达目录或知识索引，不进入普通领域 Skill。

对话洞见提炼时额外区分：

- `dialogue-trigger`：触发洞见的用户问题、困惑或真实案例场域；
- `raw-formulation`：保留原始提问方式、用户关键原话、Codex 当时回答和当时的回答脉络；
- `shared-discovery`：对话中共同生成的新判断；
- `candidate-principle`：可迁移但尚未验证的方法论命题；
- `workflow-implication`：它改变了哪条 workflow 主轴、分支路由、输出契约或验收标准；
- `case-link`：若由某个真实案例触发，记录 case-local evidence 与 dialogue 的双向链接。

对话洞见的关键不是把聊天记录原封不动变成规则，而是保护“问题如何被问出来”。原始 dialogue 可以有温度、有问答、有临时表达；正式 Skill 只能接收已经回顾、去个案化、可执行、可验证的部分。

### 6. 评测与迁移

- 使用 `references/evaluation-and-transfer.md`。
- 至少区分：
  - `primary`：独立可重复、直接满足 Green；
  - `confirmatory`：教师路线或独立工具复核；
  - `exploratory`：发现线索；
  - `superseded`：已被更完整证据替代。
- 区分 `structural-green` 与 `forward-test-green`：
  - `structural-green`：TASK、Skill、assets、provenance、registry、Roadmap 和 UAT 都已落盘且自洽；
  - `forward-test-green`：至少在未参与提炼的新案例上运行并通过预设 Green。
- 当前案例回归通过，只证明 Skill 能解释已知案例。
- 至少在一个未参与提炼的新案例上 forward-test，才能声称具备迁移性。
- 迁移失败时先收窄适用条件，不用追加个案补丁掩盖问题。

## 决策纪律

- 课程不是唯一真相；当前环境的可重复证据优先。
- 独立路线更快，不代表教师路线无价值；教师路线更完整，也不代表必须成为主路线。
- 探索性项目没有标准答案时，不能把“当前能跑通”误报成“全量已解决”；必须保留覆盖率、时效、风控和服务端窗口等边界。
- 不为追求“覆盖所有知识点”把所有工具设为必经步骤。
- 区分交付路线、分析路线和 TASK 角色。
- Skill 中记录判断规则和程序知识，TASK 中记录个案过程和证据。
- 不因一次成功就创建新 Skill；先检查是否已有职责相同的能力。
- 不因一次失败就宣称通用能力不存在；先记录环境、版本和首个差异层。
- 当真实项目反过来暴露课程未覆盖的问题，把它标成 `field-discovery`，先进入 TASK 证据，再决定是否升级 Skill。
- 当外部技术情报看似很新，先把它标成 `technology-radar`，再判断是否只是观察项、分支参考，还是确实需要修改默认 workflow。
- 当对话中出现“这是不是一类问题”“我们是不是应该重构 workflow 主轴”“这个发现值得沉淀”之类信号，先标成 `dialogue-insight`，保存原始问答和触发场域，再做 Skill 化判断。
- 当课程材料进入刷题学习法或题库化阶段，读取 `references/atomized-reading-to-quiz-workflow.md`。覆盖表、校验和构建可以脚本化，但正式题目的题干、选项、干扰项和解析必须逐题人工编写与审阅，禁止用模板脚本批量生成题目内容。

## 完成标准

一个课程单元的 Skill 工程闭环至少满足：

1. 独立复现阶段及冻结边界有记录；
2. 已审计先验暴露，并准确声明独立性等级；
3. primary 证据不把教师答案伪装成独立发现；
4. 教师路线已对照，差异有解释；
5. 平行路线已执行或有明确不执行理由；
6. Skill 变更可追溯到真实证据；
7. 课程来源已进入单独的 provenance/source 文件，且不污染普通领域 Skill 主流程；
8. 相关回归测试和 evaluation 通过；
9. 已声明迁移状态：`not-tested / partial / validated`；
10. 原始笔记、TASK、知识卡片、来源追溯文件和 Skills 各自承担清晰职责。
11. 若只是结构集成，明确标记为 `structural-green / forward-test-pending`，不得写成 `validated`。
12. 若存在历史 Skill 清理债务，已列出范围、影响和后续处理方式。
13. 若采用分支参考路由型反哺，已写清触发红灯、承接分支 Skill、课程查字典入口、回到 workflow 的下一动作、证据边界和迁移状态；不得把“已建立课程入口”写成“当前技术已掌握或可自动解决”。
14. 若使用双价值四象限，已记录候选资料对 Codex 执行价值和用户学习价值的判断，以及补到 Skill、仅放索引/卡片/provenance 或不补的理由。

探索性课程项目还要满足：

15. 已声明当前终点是阶段性、覆盖性还是全量性；
16. 已记录真实环境反馈如何改变路线、限速、停止条件或数据边界；
17. 已把可复用的失败模式、研究策略和操作护栏沉淀到领域 workflow，而不是只留在对话里；
18. 已区分“可以作为工具使用”的阶段成果和“仍需研究验证”的假设。

技术雷达反哺还要满足：

19. 已记录检索日期、来源类型和关键链接；
20. 已说明资料影响的 workflow 红灯或不影响的理由；
21. 已区分 `radar-recorded / structural-green / forward-test-pending / validated`；
22. 已避免把单篇文章、单个 issue 或未复现工具写成通用能力；
23. 若只是观察项，已进入 watchlist，而不是污染 Skill 主流程。

对话洞见反哺还要满足：

24. 已保存原始问题、共同发现、候选命题和触发场域；
25. 已区分 dialogue 原文、case 证据、reference 解释和 Skill 规则；
26. 已记录反哺目标、状态和是否需要 forward-test；
27. 未把未经回顾的心流表达直接写入通用 Skill 主流程；
28. 若由真实案例触发，case 与 dialogue 已双向链接。

## 参考资料

- 与 Simon、Task-driven、Skill Creator 的职责划分见 `references/collaboration-boundaries.md`。
- 设置冻结边界、解冻门和防止答案泄漏见 `references/blind-first-protocol.md`。
- 处理无标准答案、边做边学的探索性课程项目见 `references/exploratory-course-projects.md`。
- 用户要求按 Roadmap 连续推进多个 TASK 时读取 `references/batch-roadmap-execution.md`。
- 用最新技术情报、官方文档、论文、release 或 issue 反哺 workflow 时读取 `references/technology-radar-feedback.md`。
- 将心流讨论、共同推理或方法论顿悟沉淀为 dialogue insight 时读取 `references/dialogue-insight-feedback.md`。
- 治理长期学习项目的单次学习会话、理解检测、进度入口和高风险事实核验时读取 `references/guided-learning-session-governance.md`。
- 把一本教材或长课程组织成可持续学习项目、拆书、精读、逐章档案、项目迁移、刷题诊断和 Skill 反哺闭环时读取 `references/textbook-learning-project-workflow.md`。
- 将教材、讲义或长篇学习材料逐段拆成原子知识点，并接入刷题学习法时读取 `references/atomized-reading-to-quiz-workflow.md`。
- 决定是否补做教师路线见 `references/parallel-path-decision.md`。
- 设计 evaluation 与迁移验证见 `references/evaluation-and-transfer.md`。
