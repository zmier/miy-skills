# Log

## 2026-06-18

- 创建顶层 `workflow-reverse-engineering` 容器。
- 将旧路径中的 `workflow-android-reverse` 复制到 `subworkflows/workflow-android-reverse/`。
- 迁移时排除 `.venv/`、`node_modules/`、`.pytest_cache/`，避免把可重建依赖缓存带入 workflow 知识资产。
- 暂不删除旧路径，避免打断历史课程笔记、TASK 和 Obsidian 链接。
- 创建 `workflow-js-reverse` 占位结构，等待图灵 JS 模块反哺。
- 执行迁移回归审计：识别历史证据引用与运行入口引用。
- 更新 `alib-miku-sync` 的 RPC 脚本默认 workflow 根目录到新路径。
- 在新 Android 子 workflow 下通过 `uv sync` 重建 `.venv`，并验证 Frida/requests 可导入。
- 完成 Android 子 workflow 第一轮资产审计，新增 `docs/android-asset-audit.md`，标注通用能力、Android 专属能力、可迁移但需平台适配的能力、工具迁移状态和清理债务。
- 完成父 workflow 第一批轻量通用层上提：新增平台路由、红灯分类、静态动态闭环、复现阶梯 4 份 reference，新增证据台账和 Mermaid 证据树 2 份 template，并将 `reverse-workflow-orchestrator` 从占位草案升级为结构可用的轻量编排 Skill。Android 子 workflow 本轮未改动。
- 创建 `workflow-js-reverse` 最小正式骨架，并新增 `observe-browser-runtime` Skill。该能力由图灵 JS Day05 两个 TASK 支撑：`setInterval(functionRef)` 注册层 hook 与 `Function("debugger;")` 动态构造层 hook。当前状态为 `minimal-structural-green / browser-runtime-hook-partial-green`，XHR/fetch/cookie/webpack/wasm 仍为候选，未写成已验证能力。
- 通过图灵 JS TASK03 验证 `XMLHttpRequest.prototype.open/send` 运行时观测，将 XHR method/url/body 观测补入 `observe-browser-runtime` 的已验证模式。fetch/cookie/webpack/wasm 仍为候选能力。
