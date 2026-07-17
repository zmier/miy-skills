---
date: 2026-07-17
type: forward-test-plan
status: pending
mode: executed-capability
scope:
  - workflow-video
  - CASE-260715
---

# Forward Test Plan：CH01 双集

## 目的

验证 `workflow-video` 能否在不替换现有项目管理的前提下，指导 16 集火柴人微课从系列圣经推进到第 1 章双集样片 Gate。

本文件是测试合同草案，不代表测试已经执行。

## 被测对象

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-video
```

## 测试项目

```text
/Users/narra/Documents/alib/Writer/03 Projects/260715-微课
```

候选样片：

- `CH01-E01`：三大流派；
- `CH01-E02`：数据飞轮。

## Baseline

代理 baseline：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260715-微课/ai-three-schools-stickman
```

baseline 证明一条具体生产链跑通，但存在：

- 先有 4 分钟脚本与 34 镜头，尚未验证 90–150 秒系列双集；
- 角色/连续故事没有在整季 series bible 中冻结；
- visual drift 多在生成后发现；
- 当前证据主要绑定 Agnes 与火柴人场景。

## 测试范围

```text
TASK02 系列圣经
-> TASK03 CH01 双集 Treatment、script、storyboard、animatic
-> TASK04 最小执行管线
-> 少量代表性镜头
-> 双集样片
-> 独立审片
-> Gate 2 决策
```

## Required mode fields

```yaml
mode: pilot-execution
expected_steps:
  - diagnose existing project contracts
  - map workflow stages to TASK02-TASK04
  - lock series and visual rules
  - produce CH01 double-episode script/shot artifacts
  - run representative image/video generation
  - execute technical and visual/content review
  - record Gate 2 decision
allowed_external_tools: to be declared by project owner at run time
forbidden_external_tools: any undeclared paid generation or public publishing
pending_outputs_allowed: true, only with machine-readable awaiting-human or blocked-with-reason state
completion_standard_for_this_mode: Gate 2 evidence package is complete; batch production is not required
```

## Smoke target

至少满足：

1. 不重建或复制项目现有 README、Roadmap 和 TASK 体系；
2. 项目合同、episode、shot、asset、job、review 和 delivery 语义 owner 唯一；
3. 两集均在 90–150 秒范围内完成可审时长预演；
4. 样片覆盖角色连续性、知识图解、主角表演和确定性文字/图形路线；
5. 外部任务可区分 queued、completed、failed、awaiting-human 与 rejected-after-review；
6. 技术 QC 与视觉/内容/连续性审片分别产出证据；
7. 未过 Gate 2 不批量生成剩余 14 集；
8. 项目中不落盘密钥，workflow 中不出现项目凭据；
9. 返修能够定位到剧本、分镜、资产、renderer 或后期 owner；
10. 项目发现先写 project evidence，workflow 只接收经批准的 change proposal。

## Contamination check

- Agnes 的 payload、帧数和限流不得进入父 workflow 稳定协议；
- 火柴人角色和三色编码不得变成跨项目强制规则；
- 教育类知识审核不得污染非教育视频的父路由；
- 电影工业术语可以作为 Gate 语言，但不得强迫低风险单支视频生产完整电影制片文书。

## 结果文件（执行时创建）

```text
tests/runs/YYYY-MM-DD-ch01-double-episode/
├── task-contract.md
├── outputs/log.md
├── outputs/result.md
├── regression-comparison.md
└── pass-fail.md
```

若条件允许，应由不继承本次构思讨论的独立执行者完成；否则明确记录测试不纯净，并保持 `forward-test-pending`。

## Pass / Fail

Pass：

- smoke target 全部满足；
- 双集样片或机器可读的合理等待态真实产生；
- 与 baseline 相比没有丢失任务恢复、资产追溯和多层 QC；
- workflow 使上游锁定和下游返修 owner 更清晰；
- Gate 2 有明确 accepted / revise / reject 结论。

Fail：

- 需要读取本次构思对话才能执行；
- 父 workflow 泄漏单一平台或火柴人案例细节；
- 项目结构被重复搭建；
- 把 route-only 或远程 `completed` 宣称为成片通过；
- 未通过样片审片即进入批量生成；
- 返修原因无法回到明确 owner。
