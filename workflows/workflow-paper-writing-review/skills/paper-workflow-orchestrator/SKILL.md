---
name: paper-workflow-orchestrator
description: 编排论文写作、投稿前自审、审稿和返修 workflow。用于先定义论文质量系统和贡献链，再根据任务方向路由到研究问题、文献缺口、理论机制、识别策略、数据变量、结果叙事、引用质量、表达结构和审稿意见组装等子能力。适合经济学和社会科学论文写作/审读场景；具体学科细节应交给 econ-write、manuscript-review、reference-audit 等领域 Skills。
---

# Paper Workflow Orchestrator

当前状态：`seed / not-installed`

## 目标

把论文写作、投稿前自审、审稿和返修放在同一套质量系统下编排。

## 启动流程

1. 判断任务方向：
   - 写作；
   - 投稿前自审；
   - 外部审稿；
   - 返修整合；
   - 引文/表达/结构专项审计。
2. 读取 `references/paper-quality-system.md`。
3. 如果任务方向是外部审稿，同时读取 `references/external-peer-review-orchestration.md`。
4. 如果审稿对象是实证论文，读取 `references/empirical-paper-component-coverage.md`，确认作者目录体系（理论机制、模型公式、数据方法、结果）已被审稿模块覆盖。
5. 当用户询问“贡献是否成立”“论证是否跳步”“实际发现与上升表述是否匹配”“审稿意见怎么讲清楚”等论证有效性问题时，调用 `../../../workflow-argument-validity/skills/academic-review-argument-audit/SKILL.md`；不要把通用论证有效性知识复制进本 workflow。
6. 建立或定位具体 project / TASK，个案证据不写入 workflow 本体。
7. 展开贡献链：
   - 研究问题；
   - 文献缺口；
   - 理论机制；
   - 识别策略 / 研究设计；
   - 数据、变量和样本；
   - 结果、稳健性和边界；
   - 贡献叙事；
   - 表达、引用和结构。
8. 按任务方向路由到已有 Skills 或待建子 Skill。
9. 每个质量项记录状态：`unexamined / questioned / supported / weak-supported / unsupported / overclaimed / revision-needed / acceptable`。
10. 对审稿和投稿前自审，建立或更新 `notes/review-issue-ledger.md`，滚动记录疑惑点、脆弱点、证据位置、状态和后续路由。
11. 输出写作台账、自审台账、审稿素材或返修整合计划。

## 外部审稿编排路线

当用户在审稿项目中询问“接下来做什么”“文献位置”“贡献是否成立”“方法是否可靠”“审稿意见怎么组织”等问题时，按以下模块组织工作：

1. 项目归档：确认邮件、系统页面、截止日期、稿件材料、表单位置和敏感边界。
2. 文本底稿：用 PDF/HTML 还原 Markdown、段落编号、抽取日志和人工 QC 清单建立可定位底稿。
3. 快速通读：调用 `manuscript-quick-reconstruction`，还原作者声称的研究问题、理论框架、核心变量、数据、识别策略、主要结论和贡献，并输出贡献链 Markdown。
4. 文献定位：调用 `manuscript-literature-genealogy`，编排 scholar-kit 检索能力，基于 FT50、UTD24/领域顶刊、`Nature`、`Science`、`PNAS` 等综合顶刊和中文川大社科 B 以上文献，重建知识树/文献谱系，输出文献定位矩阵和 Mermaid 知识树，判断 gap 是否真实、重要且不同于既有研究；必要时调用 `academic-review-argument-audit` 检查 `gap -> contribution` 箭头是否成立。
5. 方法识别审查：调用 `manuscript-causal-identification-audit`，先区分实际观测发现与作者上升发现，再用 DAG、后门路径、前门/机制路径、IV/PSM/DiD、固定效应、控制变量和稳健性检验判断识别假设是否支撑结论。
6. 变量数据审查：调用 `manuscript-variable-data-measurement-audit`，检查核心概念是否被合适变量操作化，样本、数据合并、编码匹配、时间结构、测量误差和外部有效性是否支撑作者结论；必要时调用 `academic-review-argument-audit` 检查 `construct -> measure` 和 `measure -> claim` 箭头是否成立。
7. 结果叙事一致性：调用 `manuscript-results-narrative-consistency`，使用 `references/empirical-paper-component-coverage.md` 检查作者目录体系中的理论机制、模型/公式、数据方法、主结果、机制、异质性、稳健性、拓展分析和结论是否被审稿模块覆盖并形成闭环；必要时调用 `academic-review-argument-audit` 检查 `result -> theory/contribution` 箭头是否成立。
8. 审稿素材组装：调用 `manuscript-review-material-assembly`，整理贡献、重大问题、次要问题、可执行修改建议、给编辑的判断依据和推荐意见理由；对“实际观察发现 vs 作者上升表述”“衡量标准是否匹配”“审稿段落是否讲清为什么推不出”等问题，调用 `academic-review-argument-audit` 输出 argument-validity issue 和段落草稿；输出 reviewer-owned materials，不替代最终提交文本。
9. 终稿前人工复核门：在正式起草或提交审稿意见前，检查关键段落和表格是否已人工核读，核心统计/模型/变量证据是否已回看，ScholarOne 实时页面、期刊政策提示、利益冲突、伦理/重复发表/数据异常风险是否已确认，author-facing 与 editor-facing 材料是否分开，最终推荐意见是否由审稿人承担。
10. 最终审稿文本撰写：调用 `manuscript-final-review-drafting` 作为总编排器，在第 8 步素材包和第 9 步 gate 基础上，先调用 `review-issue-priority-synthesizer` 综合排序 major/minor 问题，再起草 `Comments to the Author`、可选 `Confidential Comments to the Editors`、recommendation rationale 和 ScholarOne 字段映射；若用户要求多 Agent、草稿存在读者理解断点、或终稿准备进入 vNext，调用 `multi-agent-academic-review-qa` 做冷读者、技术清晰度、证据边界和可执行性复核；进入 paste-ready 前调用 `post-flight-review-verifier` 做证据、边界、背景桥和中英文一致性验收。若人工 gate 未完成，必须标注 `draft-not-ready-to-submit`。

路线纪律：

- 审稿是借稿件进入领域、更新自己的知识体系，再和作者进行同行对话；保持“感谢作者带来的风景，但认真校准地图”的语气：温柔、犀利、可证据化。
- 先做贡献链还原，再做质量判断。
- 论证有效性是横向验收能力：涉及“论据是否足以推出结论”的问题，调用 `workflow-argument-validity` 的审稿 adapter；本 workflow 只保存审稿业务路由和证据边界。
- 文献定位、方法识别、变量数据可以并行，但必须回填到同一份审稿台账。
- 边读边记录疑惑点和脆弱点：每个问题都应有 evidence location、issue type、status、severity、route 和 next action；不得只留在聊天记录或散文式摘要里。
- `notes/quick-read-contribution-chain.md` 负责还原作者声称；`notes/review-issue-ledger.md` 负责承接可核验的疑惑、断点和潜在审稿问题。
- AI 可以整理素材、矩阵和问题清单；最终提交的审稿文字和推荐意见由审稿人负责。
- 如果期刊政策限制 AI 使用，按期刊政策收紧任务范围。

## 编排层状态恢复与路由查重

在已有审稿项目中，编排层只负责轻量状态恢复、路由和去重提醒，不替代各子 Skill 的独立任务，也不要求每个子 Skill 在执行前全项目扫描。

触发场景：

- 用户问“这个之前谈过吗”“是否已经记录”“落到哪个文档了”；
- 用户问“接下来做什么”“目前完成到哪一步”“该调用哪个模块”；
- 用户追问变量、文献、识别、结果叙事或审稿素材中的某个具体疑点，需要判断应交给哪个子 Skill；
- 准备新增证据文件时，需要确认它属于哪个 workflow step 和哪个 issue id。

编排层状态恢复顺序：

1. 先读项目 `README.md` 的完成清单，确认当前 workflow 已完成哪些步骤。
2. 读取或检索 `notes/review-issue-ledger.md`，确认是否已有 issue id、状态和路由。
3. 只检索与当前问题直接相关的模块产物。例如：
   - 文献/gap/知识谱系问题：优先第 4 步产物；
   - 识别/因果/DAG/IV/PSM/DiD 问题：优先第 5 步产物；
   - 变量/数据/样本/口径/测量问题：优先第 6 步产物；
   - 理论-模型-结果-结论闭环问题：优先第 7 步产物；
   - major/minor/recommendation 组织问题：优先第 8 步产物。
   - 最终提交、ScholarOne 实时页面、期刊政策提示、人工核读、COI/伦理/重复发表、author/editor-facing 边界问题：优先第 9 步 gate 清单和第 8 步素材包。
   - 最终 author-facing / editor-facing 审稿文本、ScholarOne 字段草稿问题：优先第 10 步产物。
   - 最终草稿是否读得懂、技术推理是否讲清、是否需要多 Agent 交叉复核：优先第 10 步产物，并调用 `multi-agent-academic-review-qa`。
   - 最终草稿是否漏掉高优先级问题、是否可粘贴、是否越过证据边界：优先第 10 步 priority plan 和 post-flight verification，必要时调用 `review-issue-priority-synthesizer` 或 `post-flight-review-verifier`。
4. 若命中已有 issue 或结论，先告诉用户“这不是新问题，已有沉淀在 X”，再交给对应子 Skill 更新或解释。
5. 若无法判断归属，再做宽一点的 `rg` 检索；不要把宽检索作为每次默认动作。

职责边界：

- 子 Skill 负责本模块内的局部查重、证据补充和 issue 更新。
- 第 7 步负责跨模块检查理论、变量、方法、结果和结论是否一致。
- 第 8 步负责跨模块去重、合并、排序，并组装成审稿素材。
- 第 9 步负责提交前人工复核和责任边界确认，不重做第 3-8 步审查。
- 第 10 步负责问题排序、文本化、QA、post-flight 验收和表单映射，不新增未经证据支持的重大判断。
- 编排层不把“避免遗忘”变成所有子 Skill 的全项目扫描义务。

回答时按需区分：

- `已有结论`：项目中已经沉淀过；
- `本轮新增`：这次新查、新判断或新写入；
- `职责位置`：该问题属于哪个 workflow step；
- `遗漏原因`：若此前回答没有引用既有结论，应说明是编排层路由、子 Skill 局部查重，还是第 7/8 步全局整合没有执行到位。

## 会话捕捉协议

外部审稿和投稿前自审过程中，用户在对话里提出的质疑、困惑和反问，也属于审稿证据流的一部分。不要等到阶段结束才回忆整理。

当用户出现以下表达时，必须判断是否要进入 `notes/review-issue-ledger.md`：

- “这是什么意思”“怎么算”“看不懂”“作者有说明吗”；
- “是不是”“会不会”“是否成立”“是否可靠”；
- “这不就是……吗”“他到底是……还是……”；
- “这和前面矛盾吗”“这里是不是过度声称”；
- 指出变量、数据、文献、方法、表格、时间、口径、引用或概念的潜在问题。

处理顺序：

1. 先回答用户的直接问题，必要时回到原文证据。
2. 判断该问题是否影响贡献链、文献 gap、变量测量、识别、结果叙事或审稿意见。
3. 若影响，立即新增或更新 `notes/review-issue-ledger.md`；若暂时无法写文件，在回复中明确标记为 `pending ledger item`。
4. 在回复末尾简短说明：已记录到哪个 issue id，或为什么只作为普通解释不入账。

去重规则：

- 如果新质疑属于已有 issue，更新该 issue 的 `observed concern`、`next action` 或状态，不新建重复条目。
- 如果新质疑使问题升级，例如从 clarification 变成 major-candidate，应更新 `severity` 并保留升级理由。
- 如果后续核验证明疑虑解除，状态改为 `resolved`，不要删除原 issue。

## 决策纪律

- 不把单篇论文经验写成通用规则。
- 不把具体稿件、审稿意见正文、作者身份或期刊系统敏感信息写入 workflow。
- 写作建议和审稿判断必须回到贡献链和证据链。
- 对不确定的领域知识、方法判断或引用准确性，标注需核实。
