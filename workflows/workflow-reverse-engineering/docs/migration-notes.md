# Migration Notes

## 源路径

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/路飞-JS与安卓逆向/workflow-android-reverse
```

## 新路径

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse
```

## 迁移策略

本次采用“复制迁移 + 暂不删除旧路径”的策略。

原因：

- 旧目录可能被课程 TASK、Obsidian 双链、miku 脚本或历史文档引用；
- Android workflow 已经较成熟，不应在迁移时同时重构；
- 新父 workflow 仍处于 `migration-draft` 状态，需要先完成审计。

## 排除项

以下目录在初次复制迁移时未迁移：

- `.venv/`：Python 虚拟环境，可由 `pyproject.toml` 重建；
- `node_modules/`：Node 依赖，可由 `package-lock.json` 重建；
- `.pytest_cache/`：测试缓存。

2026-06-18 回归审计时，已在新 Android 子 workflow 下通过 `uv sync` 重建 `.venv/`，用于 miku RPC 脚本和 Frida/mitmproxy 运行。`node_modules/` 仍保持未重建，待实际需要 Mermaid CLI 或 Node 脚本时再执行 `npm ci`。

## 后续决策

完成迁移审计后再决定：

1. 保留旧目录作为课程历史快照；
2. 将旧目录改为软链，指向新路径；
3. 更新旧路径下的 README，提示新位置；
4. 更新相关脚本、Skill、文档中的硬编码路径。

当前决策：暂不删除旧路径，也不立即软链替换。旧路径作为历史课程证据快照保留；新的运行入口默认使用 `Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse`。
