---
date: 2026-07-17
type: reference
status: structural-green / forward-test-pending
scope:
  - workflow-video
---

# Video Production Core Loop

## 单一主轴

视频项目的通用主轴不是某个模型调用，而是：

```text
意图 -> 锁定 -> 拆解 -> 生产 -> 审核 -> 修复 -> 再锁定 -> 交付 -> 反哺
```

每个阶段都用同一状态机：

```text
pending
-> in-progress
-> review-ready
-> accepted | revise | rejected | blocked-with-reason | awaiting-human
```

外部服务自己的 `queued / in_progress / completed / failed` 只能作为执行状态，不能替代内容验收状态。

## 阶段合同

| 阶段 | 必答问题 | 最小产物 | Green |
|---|---|---|---|
| 0 Intake | 做什么、给谁看、模式和权限是什么？ | 项目合同、现状诊断 | 范围、规格、工具权限、预算/额度边界明确 |
| 1 Development | 为什么值得做，讲什么、不讲什么？ | brief、内容来源、受众与目标 | `content-greenlight` |
| 2 Creative pre-production | 谁在什么世界里，以何种叙事讲？ | series/visual bible、Treatment、连续性规则 | 创意假设可执行，重大分歧已决定 |
| 3 Script & shot design | 旁白、动作、节奏和画面如何对应？ | script、storyboard、shot manifest、animatic 或等价时长预演 | `script-lock` 与 `animatic-lock` |
| 4 Assets | 哪些资产冻结、复用、生成或后期制作？ | reference index、角色/场景/关键帧资产、asset map | 采用版本、别名、来源和路径可追溯 |
| 5 Render | 每个镜头由什么引擎生成，如何恢复？ | job manifest、raw outputs、错误与重试记录 | 目标项全部有状态，无静默丢失和重复任务 |
| 6 Review | 文件能播吗？画面对吗？知识对吗？ | technical QC、visual/content/continuity review ledger | 每项 accepted 或有明确返修/阻塞原因 |
| 7 Post | 画面、声音、字幕和包装是否锁定？ | rough/fine cut、picture lock、音频字幕与母版 | `picture-lock` 后完成 delivery QC |
| 8 Delivery & learning | 交付是否完整，哪些经验可迁移？ | delivery manifest、复盘、change proposal | `delivery-accepted`；个案与稳定规则分离 |

## 文档驱动接口

各岗位/Skill 通过文件合同交接，避免依赖同一长对话的隐含记忆：

```text
内容来源 -> brief / script
创意开发 -> series bible / treatment
镜头设计 -> shot manifest
资产生产 -> reference index / asset map
外部生成 -> job manifest / raw artifacts
审片 -> review ledger / repair instruction
后期 -> picture-lock manifest / delivery manifest
```

交接文件至少包含：

- stable id；
- 上游 source id / version；
- 负责人或语义 owner；
- 状态与最后更新时间；
- 采用稿路径；
- 审核结论与未解决问题。

## 锁定与返工

锁定不是永久禁止修改，而是让修改成本可见：

| 锁定点 | 修改触发 |
|---|---|
| content-greenlight | 重新选择受众、学习目标或内容边界 |
| script-lock | 旁白主张、故事动作或总时长发生实质变化 |
| animatic-lock | 镜头顺序、时长、构图或生成路线发生实质变化 |
| pilot-production-greenlight | 模型、风格、预算或合格率假设被样片推翻 |
| picture-lock | 画面剪辑结构改变，导致声音/字幕/包装连锁返工 |
| delivery-accepted | 交付版本被替换或平台规格改变 |

返工应回到最早的真实故障层：

```text
事实错 -> 内容/剧本
隐喻错 -> treatment/storyboard
构图歧义 -> keyframe/shot design
运动错 -> motion instruction/render adapter
文字错 -> deterministic post
编码错 -> media pipeline
```

不要只在最下游不断换提示词。

## Review Ledger 最小字段

```text
item_id
artifact_version
review_dimension: technical | visual | content | continuity | delivery
severity: critical | major | minor | note
finding
evidence_path_or_timestamp
disposition: accept | revise | reject | awaiting-human
repair_owner
repair_route
recheck_status
```

## 批量放量条件

进入 `batch-execution` 前至少确认：

- 代表性样片覆盖主要人物、场景、动作和知识表达类型；
- 资产与镜头 ID 稳定；
- 任务可断点恢复，重跑不会制造不受控重复任务；
- 限流、超时、等待、失败和人工验证可被区分；
- 技术 QC 与视觉抽帧/内容检查已经真实执行；
- 返修可以定位到内容、镜头、资产、引擎或后期中的一个 owner；
- 成本、时间和失败率在项目可接受边界内。

## 阶段复盘

每个主要 Gate 后做一次短复盘：

```text
what-was-planned
what-actually-happened
failure-patterns
project-only-fixes
candidate-workflow-rules
evidence-needed-before-promotion
```

只有最后两项形成 change proposal，不能把完整项目复盘直接粘进父 Skill。
