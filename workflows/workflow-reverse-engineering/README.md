---
date: 2026-06-18
type: workflow
status: migration-draft
---

# IP 代理
API Key：iploop_4ef2e1d1_06afa08fd7c5d9812a47a06ac262ce2f670fbd63

快速验证：curl -x "http://:iploop_4ef2e1d1_06afa08fd7c5d9812a47a06ac262ce2f670fbd63@proxy.iploop.io:8880" https://httpbin.org/ip

curl -x "http://:iploop_4ef2e1d1_06afa08fd7c5d9812a47a06ac262ce2f670fbd63@proxy.iploop.io:8880" \
  -H "X-Country: US" \
  https://httpbin.org/ip

代理url：https://platform.iploop.io/pages/dashboard.html


# Reverse Engineering Workflow

这是一个上位逆向工程 workflow 容器，用于承载跨平台逆向工程方法，以及 Android、JS、Windows、Unity 等平台子 workflow。

它不是单个 Skill。根目录负责组织 workflow 工程；可被 Codex 调用的执行单元放在 `skills/`；平台细节放在 `subworkflows/`。

## 当前结构

```text
workflow-reverse-engineering/
├── README.md
├── SKILL.md
├── ROADMAP.md
├── log.md
├── docs/
├── references/
├── templates/
├── skills/
│   └── reverse-workflow-orchestrator/
├── subworkflows/
│   ├── workflow-android-reverse/
│   └── workflow-js-reverse/
└── projects/
```

## 设计原则

1. workflow 是工程系统，Skill 是可调用执行单元。
2. 父 workflow 只承载跨平台共性，不吞掉平台子 workflow。
3. 子 workflow 保持平台专属细节和成熟结构。
4. TASK 记录个案证据，reference 记录稳定方法，template 记录可复用形态。
5. Radar 技术情报默认先进入 Radar/knowledge 层，只有经验证后才升级为 workflow 能力。

## 子 Workflow

- `subworkflows/workflow-android-reverse/`：从路飞课程项目迁移而来，当前为完整 Android 平台实现。
- `subworkflows/workflow-js-reverse/`：由图灵 JS 课程 forward-test 长出的 JS 平台实现，当前已覆盖 JS 运行时选择、浏览器 hook、请求复现、JS crypto、webpack、WASM、微信小程序、混淆到协议闭环，以及课程资产治理。

## 迁移状态

- Android workflow 已复制迁入，排除了 `.venv/`、`node_modules/`、`.pytest_cache/` 等可重建产物。
- 旧路径暂未删除，避免打断历史 Obsidian 链接和课程 TASK 引用。
- 后续可在确认无误后，把旧路径替换为指向新路径的软链，或保留旧路径作为课程历史快照。

## 审计文档

- [Android Workflow 资产审计](docs/android-asset-audit.md)：标注 Android 资产中的通用能力、Android 专属能力、可迁移但需平台适配的能力，以及当前工具迁移状态。

## 父级通用层

- [平台与运行时路由](references/platform-routing.md)
- [逆向红灯分类](references/red-light-taxonomy.md)
- [静态与动态闭环](references/static-dynamic-loop.md)
- [复现阶梯](references/reproduction-ladder.md)
- [证据台账模板](templates/evidence-ledger-template.md)
- [Mermaid 证据树模板](templates/mermaid-evidence-tree-template.md)
