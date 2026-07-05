---
name: lark
description: 飞书/Lark 总路由 Skill。用于读取或操作飞书文档、云盘、表格、多维表格、任务、消息、日历、会议纪要等。先按用户意图路由到 vendors/larksuite-cli/skills/lark-* 官方子 skill；常用：lark-doc 读取/编辑飞书文档，lark-drive 文件/权限/评论，lark-sheets 表格，lark-base 多维表格，lark-task 任务。需要本机安装 lark-cli 并完成授权。
status: local-umbrella / routes-to-vendor-submodule
source: ../../vendors/larksuite-cli
---

# Lark / Feishu Umbrella Skill

本 Skill 是本地伞型入口，负责把飞书/Lark 相关请求路由到官方 `larksuite/cli` 仓库中的领域 Skill。

官方仓库作为 submodule 放在：

```text
../../vendors/larksuite-cli/
```

官方领域 Skill 位于：

```text
../../vendors/larksuite-cli/skills/lark-*/SKILL.md
```

## 前置条件

本 Skill 只提供 agent 操作指引。真正执行飞书操作还需要本机有 `lark-cli`：

```bash
npx @larksuite/cli@latest install
lark-cli --help
```

首次使用或权限不足时，按官方 `lark-shared` 指引配置与授权。

## 必读规则

执行任何飞书操作前，必须先读取：

```text
../../vendors/larksuite-cli/skills/lark-shared/SKILL.md
```

然后根据任务类型读取对应领域 Skill：

| 用户意图 | 读取 |
|---|---|
| 读取、创建、更新飞书文档 / Docx / Wiki 文档 | `../../vendors/larksuite-cli/skills/lark-doc/SKILL.md` |
| 云盘文件、文件夹、导入导出、复制、权限、评论 | `../../vendors/larksuite-cli/skills/lark-drive/SKILL.md` |
| 电子表格读取、写入、追加、导出 | `../../vendors/larksuite-cli/skills/lark-sheets/SKILL.md` |
| 多维表格 / Base 表、字段、记录、视图 | `../../vendors/larksuite-cli/skills/lark-base/SKILL.md` |
| 任务、任务列表、提醒、子任务 | `../../vendors/larksuite-cli/skills/lark-task/SKILL.md` |
| 即时消息、群聊、消息搜索、文件上传下载 | `../../vendors/larksuite-cli/skills/lark-im/SKILL.md` |
| 日历、日程、忙闲、会议室 | `../../vendors/larksuite-cli/skills/lark-calendar/SKILL.md` |
| 会议记录、会议纪要、转录 | `../../vendors/larksuite-cli/skills/lark-minutes/SKILL.md`、`../../vendors/larksuite-cli/skills/lark-vc/SKILL.md` |
| 邮件 | `../../vendors/larksuite-cli/skills/lark-mail/SKILL.md` |
| 通讯录 | `../../vendors/larksuite-cli/skills/lark-contact/SKILL.md` |
| Wiki 知识空间和节点 | `../../vendors/larksuite-cli/skills/lark-wiki/SKILL.md` |
| 审批 | `../../vendors/larksuite-cli/skills/lark-approval/SKILL.md` |
| OKR | `../../vendors/larksuite-cli/skills/lark-okr/SKILL.md` |
| 开放平台 API 探索 | `../../vendors/larksuite-cli/skills/lark-openapi-explorer/SKILL.md` |

如果任务涉及文档内嵌的表格、多维表格、画板、附件或评论，按领域 Skill 的路由说明继续读取对应 Skill，不要只凭本总入口猜参数。

## 常用路由

### 飞书文档

用户给出飞书文档 URL、Wiki URL、doc token，或要求读取/整理 coauthor 飞书文档内容时：

1. 读取 `lark-shared/SKILL.md`。
2. 读取 `lark-doc/SKILL.md`。
3. 若只是读取，继续按 `lark-doc` 要求读取 `references/lark-doc-fetch.md`。
4. 执行 `lark-cli docs +fetch --doc "<URL或token>"`，按官方 Skill 选择 scope/detail。

### 飞书表格 / 多维表格

用户给出 spreadsheet/base URL 或文档中嵌入 `<sheet>` / `<bitable>`：

1. 读取 `lark-shared/SKILL.md`。
2. 读取 `lark-sheets/SKILL.md` 或 `lark-base/SKILL.md`。
3. 使用对应 `lark-cli sheets ...` 或 `lark-cli base ...` 命令。

### 文件、评论、导入导出

用户要复制文档、导出文件、处理评论或云盘权限时：

1. 读取 `lark-shared/SKILL.md`。
2. 读取 `lark-drive/SKILL.md`。
3. 优先使用官方 Skill 推荐的 shortcut。

## 安全边界

- 不输出 appSecret、accessToken、refreshToken 等密钥。
- 写入、删除、覆盖、权限变更等操作前必须确认用户意图。
- 高风险操作遇到官方 CLI 的 confirmation gate 时，必须等待用户明确同意后再加 `--yes`。
- 授权链接和 device code 不缓存；需要授权时重新生成。
- 文件路径参数遵守官方 `lark-shared` 规则，优先相对路径和 stdin。

## 本地维护

更新 upstream：

```bash
git -C ../../vendors/larksuite-cli pull --ff-only
git add ../../vendors/larksuite-cli
```

如果官方未来发布 `skills/lark/` umbrella Skill，可考虑用官方 umbrella 替换本地入口。
