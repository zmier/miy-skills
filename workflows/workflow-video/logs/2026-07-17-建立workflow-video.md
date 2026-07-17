---
date: 2026-07-17
type: conception-log
status: structural-green / forward-test-pending
scope:
  - workflow-video
---

# 建立 workflow-video：从视频 Harness 与火柴人微课试点抽父

## 来源

本 workflow 来自两类材料的交叉：

1. 视频内容理解稿：`/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/J-260717-AI视频攻略.md`；
2. 已完成生产案例：`/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/ai-three-schools-stickman/`；
3. 正在筹备的 16 集微课总项目：`/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/`；
4. 关于电影工业 Development、Pre-production、Production、Post、Distribution 和多次 Greenlight 的讨论。

本日志只保存抽象过程和边界，不复制对话全文、视频原稿、项目素材或任何凭据。

## 原始问题

```text
能否把“文档驱动的 AI 视频 Harness”与已经跑通的图像、托管、视频生成和 QC 流程，抽成一套可迁移 workflow？
它如何服务 16 集微课，而不吞掉项目自己的 TASK 管理？
```

## 关键洞见

视频理解稿提供的抽象方向：

- 文档可作为 agent/岗位之间的接口；
- 分镜、角色参考、动作描述和引用索引可以让上下游低耦合；
- 生产与审片需要相互独立的循环；
- 自动推进与人工逐步推进应是不同模式；
- workflow 演化应由项目证据提出、人工决定，而不是系统静默自改。

火柴人试点提供的执行证据：

- 角色/风格资产 -> 34 个关键帧 -> 公网 URL -> 远程视频任务 -> 下载 -> QC 的完整链路已真实执行；
- `shots.json`、`asset-map.json`、`video-jobs.json` 和 TASK 日志证明 manifest 与断点续跑有实际价值；
- 远程任务 `completed` 之后仍发现真人化、动漫化、意外文字和角色漂移，说明技术 QC 不能替代视觉审片；
- 反复改 prompt 无法解决某些高歧义构图，重做关键帧或移除触发元素更有效；
- 平台出现创建/查询限流，项目通过节流、并行轮询和回写状态完成恢复；
- rejected 版本保留在过程资产中，最终目录只接收通过版本。

## 方案分歧

### 方案 A：立即建立全套岗位 Skills

例如 series-bible、script-writer、storyboard、keyframe、renderer、reviewer、post 等。

拒绝原因：目前主要证据仍来自单一火柴人微课案例；提前拆分会把假设做成空 Skill，也难以确定真正的输入输出边界。

### 方案 B：先做 Agnes 专用流水线

拒绝原因：Agnes 是当前 renderer，不是视频生产的总模型。供应商绑定会污染父层，并限制后续 Seedance 或其他视频模型接入。

### 方案 C：建立最小父 workflow，执行中增量生长

采用。首版只包含：

- 父 `SKILL.md`；
- 一个 orchestrator；
- core loop 与 routing 两个稳定 reference；
- 一个项目合同模板；
- provenance、case card 和 forward-test plan。

## 最终结构决定

```text
workflow-video/
├── SKILL.md
├── agents/openai.yaml
├── skills/workflow-video-orchestrator/SKILL.md
├── references/core-loop.md
├── references/routing.md
├── templates/video-project-contract.md
├── logs/2026-07-17-建立workflow-video.md
├── provenance/source-registry.md
├── projects/CASE-260715-16集火柴人微课.md
└── tests/forward-test-plan.md
```

当前不建立 `scripts/`、`assets/`、`subworkflows/` 或平台 adapter。它们应由前向测试中的真实重复需求触发。

为保证 Codex 可按 `$workflow-video` 发现父入口，建立同名软链：

```text
/Users/narra/.codex/skills/workflow-video
-> /Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-video
```

## 已提升为结构规则

| 洞见 | 落点 | 状态 |
|---|---|---|
| 阶段门 + 返修循环 | `SKILL.md`、`references/core-loop.md` | structural-green |
| 文档驱动与单一事实源 | `references/core-loop.md` | structural-green |
| 生成路线与问题 owner 分离 | `references/routing.md` | structural-green |
| 技术、视觉、内容、连续性分层审片 | `SKILL.md`、`core-loop.md` | structural-green |
| 平台作为 adapter | `routing.md` | structural-green |
| 项目证据先留项目，再提演化建议 | `SKILL.md`、provenance | structural-green |

## 留在项目中的内容

- 火柴人角色和三色视觉规则；
- 16 集选题、教材证据和连续故事；
- Agnes 的密钥、请求 payload、限流实测和任务回执；
- 阿里云路径与公网 URL；
- 34 镜头关键帧、视频、rejected 版本和交付文件；
- CH01 双集的实际成本、合格率与编辑决定。

## 仍待验证

- 主轴是否同样适用于真人、产品宣传、访谈和非教育类视频；
- series bible、script/shot design、asset production、renderer review 是否值得拆成独立 child Skills；
- 动态分镜在 90–150 秒 AI 微课中的最低充分形式；
- 不同 renderer 的通用 job 状态与平台 adapter 合同；
- 自动 phase review 和 change proposal 的合适触发频率；
- 独立审片在不同项目规模下的最低成本方案。

## Forward test

先以 16 集微课的 CH01 双集测试：

```text
TASK02 系列圣经
-> TASK03 双集 Treatment / script / storyboard / animatic
-> TASK04 最小可恢复生产链
-> Gate 2 样片
```

测试通过也只证明“教育类系列火柴人微课分支”前向可用；其余类型仍保持 pending。
