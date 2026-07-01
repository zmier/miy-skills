---
name: reverse-workflow-orchestrator
description: 编排跨平台逆向工程 workflow。用于定义授权边界、目标、UAT Green 与证据台账，判断目标属于 Android、JS、Hybrid、Windows、Unity 或 unknown 运行时，再按红灯分类路由到平台子 workflow，并维护静态/动态闭环、复现阶梯、Radar 与迁移状态。适用于把成熟 Android workflow 抽象为父 workflow、接入 JS 逆向流程、或处理混合 WebView/小程序/native bridge 场景。
---

# Reverse Workflow Orchestrator

这是 `workflow-reverse-engineering` 的总编排 Skill。

当前状态：`structural-green / not-installed / forward-test-pending`

## 核心流程

1. 定义目标、授权边界和 UAT Green。
2. 判断平台与运行时。需要细分时读取 `references/platform-routing.md`。
3. 用 `templates/evidence-ledger-template.md` 建立证据台账。
4. 用 `templates/mermaid-evidence-tree-template.md` 维护待解节点树。
5. 按红灯分类判断下一步。需要细分时读取 `references/red-light-taxonomy.md`。
6. 在静态分析和动态观测之间循环校正。需要细分时读取 `references/static-dynamic-loop.md`。
7. 按复现阶梯选择交付形态。需要细分时读取 `references/reproduction-ladder.md`。
8. 路由到对应平台子 workflow。
9. 把可复用发现沉淀到 TASK / reference / template / Skill，并标注迁移状态。

## 路由规则

- Android：进入 `subworkflows/workflow-android-reverse/`。
- JS：进入 `subworkflows/workflow-js-reverse/`。当前为待建设状态，先用父级模板约束证据，再从图灵 JS 案例 forward-test。
- Hybrid / WebView / 小程序 / native bridge：标为 `hybrid`，先同时判断 JS 侧 bridge 和平台 native 容器，不要仅按页面表象路由。
- Windows / Unity：当前只保留父级抽象和未来子 workflow 入口，不伪造已验证能力。
- Unknown：先使用父级证据台账和红灯分类，直到能确定运行时。

## 平台边界

父 workflow 只写跨平台共性：

- 目标与 Green；
- evidence ledger；
- red-light taxonomy；
- static-dynamic loop；
- reproduction ladder；
- Radar 与迁移状态。

父 workflow 不写平台细节：

- 不把 Frida/JADX/Unidbg 作为 JS 默认工具；
- 不把 DevTools/AST/Node 作为 Android 默认工具；
- 不把一次 Android 成功经验直接升级成跨平台规则；
- 不把课程案例路径、固定 App、固定字段或固定脚本写入主流程。

## 迁移状态

- `structural-green`：结构、reference、template、Skill 路由已自洽。
- `forward-test-pending`：尚未在新平台案例验证。
- `forward-test-green`：已在未参与提炼的新案例中通过预设 Green。

没有 forward-test 时，只能声称“可作为抽象候选”，不能声称“已跨平台验证”。
