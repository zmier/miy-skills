# Regression Audit

## 2026-06-18 迁移回归审计

## 审计范围

本轮审计目标：

- 确认新 `workflow-reverse-engineering` 容器可读；
- 确认 Android 子 workflow 复制完整；
- 找出旧 `workflow-android-reverse` 路径的运行型引用；
- 区分历史证据引用和需要迁移的运行入口；
- 不批量改写课程 TASK 日志和历史输出。

## 文件完整性

新路径：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering
```

Android 子 workflow：

```text
subworkflows/workflow-android-reverse/
```

校验结果：

- Android 子 workflow 中 `SKILL.md` 数量：30；
- 初次复制时排除了 `.venv/`、`node_modules/`、`.pytest_cache/`；
- 后续已在新路径通过 `uv sync` 重建 `.venv/`；
- 新 `.venv` 中已验证 `frida==16.0.19`、`requests==2.32.4` 可导入；
- `node_modules/` 仍未重建，后续只有在需要 Mermaid CLI 或 Node 脚本时再执行 `npm ci`。

## 旧路径引用分类

### 历史证据引用

课程 TASK、日志、UAT、输出 JSONL、旧案例 README 中存在大量旧路径引用。

处理策略：

- 不批量修改；
- 这些文件记录当时的真实执行环境，属于历史证据；
- 若强行改写，会污染 TASK 证据和时间线；
- 后续只在新的 TASK 和 workflow 文档中使用新路径。

### 运行入口引用

发现 `alib-miku-sync` 中以下脚本默认指向旧路径：

- `scripts/android-rpc-progress.sh`
- `scripts/android-rpc-adaptive-probe.sh`
- `scripts/android-rpc-auto-dashboard.sh`
- `scripts/install.sh`

处理结果：

- 已将默认 `ALIB_ANDROID_REVERSE_WORKFLOW_ROOT` 改为新路径；
- 仍保留环境变量覆盖能力；
- 已更新当前运行时配置：

```text
~/Library/Application Support/alib-sync/config.env
```

使其指向新 Android 子 workflow。

## 旧路径处理决策

当前不删除旧路径，也不立即替换为软链。

原因：

- 旧目录仍被大量课程历史文件引用；
- 某些进行中的真实项目输出里记录了旧 `.venv` 路径；
- 直接软链替换会改变旧路径语义，不利于区分“历史快照”和“新 workflow”；
- 当前最稳妥的是保留旧路径作为历史快照，新工作默认使用 `miy-skills/workflows` 下的新路径。

未来可选策略：

1. 旧路径保留为历史快照，并添加迁移提示 README；
2. 当确认没有进行中的任务依赖旧 `.venv` 后，删除旧 `.venv/node_modules` 以节省空间；
3. 若用户更重视无缝兼容，可将旧 `workflow-android-reverse` 替换为指向新路径的软链，但需要先备份旧目录。

## 当前状态

```text
migration-draft / runtime-default-updated / regression-partial-green / asset-audit-structural-green
```

未完成项：

- 未批量更新历史课程文档；
- 未重建 `node_modules/`；
- 未把旧路径替换为软链；
- 未安装 `reverse-workflow-orchestrator` 到 `.codex/skills`；
- 未完成父级 `references/` 与 `templates/` 上提。

已完成项：

- 已完成 Android 通用/专属/可迁移能力审计表：`docs/android-asset-audit.md`。
