---
date: 2026-07-17
type: provenance
status: active
scope:
  - workflow-video
---

# Source Registry

## 来源与迁移状态

| ID | 来源 | 证据类型 | 可支持的判断 | 不能支持的判断 | 迁移状态 |
|---|---|---|---|---|---|
| SRC-VIDEO-001 | `/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/J-260717-AI视频攻略.md` | 视频文字稿与内容理解 | 文档接口、角色分工、review loop、reference index、mode 与演化思想 | 不能证明具体平台执行成功，也不能证明全部规则适合本地项目 | draft-rule -> structural-green |
| CASE-VIDEO-001 | `/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/ai-three-schools-stickman/` | executed-capability / 完整生产试点 | 关键帧、托管、远程生成、断点续跑、技术 QC、视觉返修和交付链确实跑通 | 不能证明适用于其他风格、题材或 renderer | source-case-tested |
| PROJECT-VIDEO-001 | `/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/` | 真实系列项目 / forward-test host | 16 集、8 章、90–150 秒、系列连续性和批量生产可用于前向验证 | 当前尚未完成 TASK02–TASK06，不能宣称新 workflow 已前向跑通 | forward-test-pending |
| META-WORKFLOW-001 | `../workflow-tao/` | workflow 能力工程规范 | 父入口、orchestrator、构思日志、provenance、回归与迁移状态边界 | 不提供视频领域知识 | structural-green |

## 当前稳定度

```text
父结构：structural-green
教育类火柴人试点：source-case-tested
CH01 双集：forward-test-pending
跨题材通用性：pending
平台 adapters：pending
```

## 提升规则

- `raw-insight`：只在日志记录，不进入稳定 reference；
- `draft-rule`：可以进入 change proposal，不进入父入口强制协议；
- `structural-green`：结构已落地，但仍需真实前向样本；
- `forward-test`：在新项目/新批次中按合同执行并有比较证据；
- `stable`：至少跨项目或跨显著分支验证，且没有平台/题材污染。

## 边界

- 此 registry 只记录指针和抽象结论，不复制来源文件；
- 任何账号、密钥、cookie、签名 URL 或私有上传路径均不得写入；
- 项目实际回执、媒体和 rejected 资产继续由来源项目拥有；
- 若来源路径迁移，应更新指针，不把旧文件复制进 workflow。
