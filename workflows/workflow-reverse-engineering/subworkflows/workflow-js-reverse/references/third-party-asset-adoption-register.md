# Third-Party / Course Asset Adoption Register

## 原则

课程里出现的 Skill、MCP、浏览器、脚手架和通用脚本，不直接等于 workflow 能力。

采用顺序：

1. 登记来源和用途；
2. 在具体 TASK 中 forward-test；
3. 只把可迁移原则写入 workflow / Skill；
4. 工具本体保持 reference-only，除非后续明确要维护为本仓库资产；
5. 个案脚本留在 TASK 或课程资料中。

## 资产登记

| 资产 | 决策 | 对应 workflow 位置 | 说明 |
| --- | --- | --- | --- |
| web-protocol-recovery | reference-only | `replay-js-request` / `reproduce-js-crypto` / `deobfuscate-js-control-flow` | 路线完整但覆盖面太广，当前只吸收原则。 |
| wechat-miniapp-reverse | adopt-principles | `reverse-wechat-miniapp` | 小程序分支已吸收核心流程，工具启动细节作为参考。 |
| WMPFDebugger | reference-only | `reverse-wechat-miniapp` | 平台和依赖较重，不搬入 workflow。 |
| camoufox-js-reverse | reference-only | `observe-browser-runtime` / `replay-js-request` | 复杂浏览器指纹和动态页面工具路线，当前登记不迁入。 |
| cloakbrowser-reverse-mcp | reference-only | `observe-browser-runtime` / `analyze-webpack-runtime` / `analyze-wasm-runtime` | 动态素材采集和 MCP 路线参考。 |
| env-patch | adopt-principles | `execute-js-runtime` / `analyze-webpack-runtime` / `analyze-wasm-runtime` | 补环境原则已分散吸收。 |
| browser-hook-snippets | adopt-principles | `observe-browser-runtime` | hook 模式已通过 Day05/Day06 forward-test。 |
| ast-deobfuscate | reference-only | `deobfuscate-js-control-flow` | AST 专项尚未完整 forward-test，先登记。 |
| ruishu-reverse | reference-only | future anti-bot branch | 瑞数属于专项反爬大分支，不混入通用 JS 加密流程。 |

## 后续触发

当后续 TASK 命中以下条件，才考虑从 `reference-only` 升级：

- 同一工具路线被两个以上独立案例复用；
- 工具本体比现有 Skill 明显减少人工步骤；
- 能写出本地安装/运行/验证脚本；
- 有 UAT 证明迁移后不会污染通用 workflow。
