# RESSET Download Skill Engineering

本目录维护 `$resset-download` 技能本体及其可复现工程证据。

## 入口

- 技能说明：`SKILL.md`
- 任务列表：`tasks/README.md`
- 当前重点任务：`tasks/TASK01-interface-first-replay/`
- 相关外部 issue：`../../workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/issues/BUG-2026-07-08-chaojiying-preflight-runtime-readiness/README.md`

## 当前判断

截至 2026-07-08：

- `$resset-download` 默认路径仍是 Playwright/CDP 控制 Chrome 登录态，配合页面内 JS、验证码、下载中心和浏览器下载事件。
- RESSET 接口化方向已形成独立任务：只读 `dataSearch.jsp` 表页和 `downloadTaskUser.action` 下载中心列表具备 interface replay 潜力。
- `dataSearch.action` direct POST 创建下载任务、`/verifyDownload?token=...` browserless zip 保存尚未 Green。
- 验证码自动路线依赖 `$handle-interactive-verification` 的超级鹰 preflight；当前已向该 skill 提 issue，避免把凭据/依赖缺口误判为 RESSET 接口失败。

## Task-Driven 结构

```text
resset-download/
├── SKILL.md
├── README.md
├── agents/
└── tasks/
    ├── README.md
    └── TASK01-interface-first-replay/
        ├── TASK01-说明.md
        ├── README.md
        ├── acceptance-contract.md
        ├── docs/
        ├── inputs/
        ├── outputs/
        ├── cache/
        ├── scripts/
        └── logs/
            └── log.md
```

## 工作规则

- 技能正文只写已稳定的执行规则。
- 探索性接口 replay、外部 WebVPN 状态、验证码 preflight、UAT 证据先进入 `tasks/`。
- 每个任务用 `logs/log.md` 记录 ReAct 过程，用 `outputs/` 保存稳定 Markdown 证据。
- 只有当 TASK 的 acceptance contract 达成后，才把规则反哺进 `SKILL.md`。
