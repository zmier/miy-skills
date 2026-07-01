# Paper Writing Review Workflow Roadmap

## R0：种子结构

- [x] 建立 workflow 根目录。
- [x] 建立 orchestrator Skill 草案。
- [x] 建立质量系统 reference v0.1。

## R1：共享质量系统

- [ ] 完善 paper-quality-system。
- [ ] 定义写作 / 审稿共同质量维度。
- [ ] 定义 contribution chain ledger。
- [x] 建立 skill registry / capability map，区分 implemented、seed、candidate 和 external Skills。

## R2：子 Skill 拆分

- [x] 列出首个共享基础设施子 Skill：`scholar-pdf-markdown-restoration`。
- [x] 建立快速通读与贡献链还原子 Skill：`manuscript-quick-reconstruction`。
- [x] 建立文献定位与知识谱系子 Skill：`manuscript-literature-genealogy`。
- [ ] 标注已有 Skills、待新增 Skills 和领域适配 Skills。
- [ ] 明确写作方向与审稿方向的路由差异。
- [x] 登记共享 audit Skill 候选：research question、literature gap、theory mechanism、identification、data measurement、results narrative、citation quality、academic expression。
- [x] 登记技术推理清晰度候选：`technical-reasoning-clarity-audit`，先作为第 10 步 post-pass，待跨场景复用后再拆 Skill。

## R3：模板与回归

- [ ] 创建 writing-ledger template。
- [x] 创建 manuscript-audit-ledger template。
- [x] 创建 quick-read-contribution-chain template。
- [x] 创建 literature-positioning-genealogy template。
- [ ] 创建 review-report template。
- [ ] 回填 `PROJECT-260618-元Workflow工程` TASK02。

## R4：真实审稿实践回流

- [x] 使用 `J-260607-EMFT-2026-0709` 建立 field practice 回流任务。
- [x] 将审稿台账字段沉淀为模板。
- [x] 将审稿项目目录结构沉淀为模板。
- [ ] 将 review-project-intake 等子 Skill 候选纳入共享子 Skill 清单。
- [x] 将 EMFT PDF 还原需求沉淀为 `scholar-pdf-markdown-restoration` 子 Skill。
- [x] 将外部审稿十模块沉淀为 `paper-workflow-orchestrator` 的编排路线。
- [x] 将“终稿前人工复核门”沉淀为审稿素材组装之后、正式提交之前的 workflow gate。
- [x] 将“最终审稿文本撰写”沉淀为终稿前人工复核门之后的第 10 步 seed Skill。
- [x] 将最终审稿问题优先级综合沉淀为共享子 Skill：`review-issue-priority-synthesizer`。
- [x] 将多 Agent / 冷读者终稿 QA 沉淀为共享子 Skill：`multi-agent-academic-review-qa`。
- [x] 将最终审稿 post-flight 验收沉淀为共享子 Skill：`post-flight-review-verifier`。
