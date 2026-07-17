# 2026-07-14 Research Zhihu Post：来源案例与 Skill 设计

## 来源

- 来源类型：真实项目反哺 / 对话洞见 / 写作更新实践；
- 来源案例：`CASE-260521 基金经理研究`；
- 直接案例：TASK07 知乎同行稿从只覆盖 TASK07-9 的 1,184 行旧稿，重构为吸收 TASK08--TASK11 后续证据的 340 行外部可读稿；
- 项目材料仍由来源项目保存，Skill 不复制领域数据、具体样本记录或协作者信息。

## 原始问题

用户指出，“写知乎贴”不仅为了给网友看，也能迫使研究者从不了解内部背景的外部人视角重新审视研究进展。旧稿在后续证据不断增加后暴露出：

1. 按 TASK 时间追加，研究主线越来越难懂；
2. 旧候选机制虽已被后续检验削弱，仍占据正文主叙事；
3. 英文缩写、变量名和任务号承担了过多解释；
4. 星号、经济意义、机制和因果容易被混写；
5. 本地稿与飞书稿需要同源更新和回读验证。

## 方案分歧

### 方案 A：只增强 task-driven 的 peer brief

优点是已有结构接近；缺点是它面向单个 subagent 工作包，无法承担多个 TASK 的研究主叙事重组，也不拥有研究结论阶梯。

### 方案 B：创建通用 project-explainback 父 Skill

优点是可能适用于软件、数据和研究项目；缺点是当前只有一个研究案例完整验证，按 `workflow-tao` 不应过早抽父。

### 方案 C：在 workflow-research 下创建 research-zhihu-post

最终采用。它让“知乎贴”保留真实发布用途，同时把外部视角审计定义为同一能力的默认内核。

## 单一语义 owner

```text
research-zhihu-post
  owner：完整研究解释、陌生同行审计、旧结论更新和知乎稿输出；

task-driven-project-manager
  consumer：决定触发、文件位置、subtask/phase 验收；

research-brainstorm
  consumer：把稿件和开放问题用作共同 brief；

research-roadmap
  consumer：链接最新解释稿和被修正路线；

workflow-tao
  meta owner：single semantic owner、mode 和 forward-test 规则。
```

## 模式决定

采用三种模式：

```text
outside-view-audit
peer-discussion-draft
publish-ready
```

这样既不把内部审计误当作公开授权，也不把真正的知乎发布降格为一个隐喻。

## 稳定规则与案例边界

提升为稳定结构：

- 先冻结证据截止日期；
- 更新旧稿前做 evidence reconciliation；
- 旧结论被削弱时修改原段，不只在末尾追加；
- 正文按研究认识演进，而非 TASK 流水账组织；
- 分开统计事实、经济含义、机制相容和因果；
- 运行零私有上下文与公开安全审计；
- 把暴露出的困惑回写 roadmap / TASK00 / brainstorm；
- 平台同步后回读关键节点。

留在来源案例：

- 基金经理回答与申购赎回的具体结果；
- TASK08--TASK11 的系数、样本与领域解释；
- 飞书文档 token、项目绝对路径和协作者通信。

## 迁移状态

```text
structural-green
source-case-tested
independent-forward-test-pending
```

本案例证明该结构在一个长期研究项目中有效，但参与了规则提炼。下一次独立研究项目应检验：模式选择、陌生读者审计、旧稿修正和 roadmap 回写是否无需依赖本案例也能成立。

## 追加实践：公式与白话双层表达

### 触发

来源项目的对外稿已经能够说明四层排查结论，但出现了新的陌生读者缺口：部分层级只有结果表，没有公式；第三层虽有公式，其他层级的比较对象和估计量仍要靠项目成员口头补充。用户提出“公式给同行快速看，围绕公式的解释给网友看”。

### 现场发现

1. 同行需要公式快速确认估计对象，但公式不能承担全部解释；
2. 公式若只放在 Q&A，正文证据与方法会脱节；
3. 主规格为季度固定效应、经理固定效应仅为稳健性时，若把后者写入公式却搭配前者系数，会制造规格错配；
4. 精确分组内最近邻匹配不能因为“匹配”二字被简称为 PSM；
5. 原始共同量的算术分解成立，不代表 `log(1+C)` 的回归系数可以相加；层级差异要检验系数差，而不是比较星号；
6. Markdown 同步飞书时，LaTeX 命令后的换行可能被吞，曾将 `\\qquad` 与下一行 `H_0` 拼成错误命令，因此必须回读平台版本。

### Skill 化

本轮将这些现场发现去案例化后写入：

- `SKILL.md`：新增“公式与白话双层表达”及 specification-result binding；
- `references/outside-reader-audit.md`：新增公式位置、规格绑定、方法命名、变换边界和平台渲染审计；
- `assets/research-zhihu-post-template.md`：为主结果、替代解释、层级分解与正式差异检验预留双层表达结构。

具体基金系数、样本数量、平台文档 token 和项目路径继续留在来源案例，不进入通用规则。

### 迁移状态

```text
structural-green
source-case-tested
independent-forward-test-pending
```

本次修改已在来源稿上完成闭环，但仍需在一个新的研究主题中验证：不同模型类型下，双层表达能否保持简洁而不把文章写成方法附录。

### 验证

使用工作区既有 `.venv` 运行 `skill-creator/scripts/quick_validate.py`，返回：

```text
Skill is valid!
```

本轮只确认结构与来源案例回归，未把状态升级为独立前向验证通过。
