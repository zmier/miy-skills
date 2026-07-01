---
name: ths-skill
description: 同花顺/THS 客户端本地数据与图表自动化的复合 Skill。用于在授权环境内路由同花顺相关任务，包括 K 线画线/标注 DrawLine XML 的读取、生成、清理与 UAT；父入口负责安全边界、任务路由、证据分层和完成标准，具体执行由内部子 skills 承接。
---

# THS Skill

## 定位

`ths-skill` 是一个中型复合 Skill：

```text
父入口：同花顺任务的边界、路由、证据协议和 Green 标准
子 skills：具体能力执行，例如 K 线 DrawLine 标注/画线自动化
references：稳定 schema、路径、market/period 映射和 UAT 规则
logs：从真实项目抽象出的构思和迁移边界
```

它来自一次授权 Mac App 靶场实践，不是通用金融交易自动化工具。默认只处理本机客户端的本地展示、研究标注、可恢复配置和离线文件，不触碰交易、下单、账户风控或服务端数据。

## 可用 Mode

### `diagnose-only`

适用：

```text
只需要判断同花顺数据在哪里、schema 是什么、某个任务该走哪条路线。
```

允许：

```text
读取本地文件；
列出候选路径；
输出计划、风险、pending UAT；
不写入目标 App 容器。
```

完成标准：

```text
说明候选路径、证据强度、下一步验证动作和不能下结论的部分。
```

### `local-write-uat`

适用：

```text
需要写入本地 DrawLine XML 或同类可恢复本地数据，并让 App 原生加载。
```

必须：

```text
先 dry-run；
写入前备份；
记录目标路径；
写入后使用 App 原生加载链路 UAT；
提供删除/恢复路径。
```

禁止：

```text
修改交易、下单、登录、风控或服务端数据；
把 UI 临时绘制伪装成持久化 Green；
在未备份时写入用户本地持久化文件；
把个案账号、token、cookie、完整敏感 raw 数据写入稳定 reference。
```

## 路由

当前子 skill：

```text
skills/ths-drawline-annotation/SKILL.md
```

路由规则：

| 用户目标 | 子 skill |
|---|---|
| 查看某支股票已有标注/画线 | `ths-drawline-annotation` |
| 脚本生成文字、标注气泡、矩形、水平线、上涨/下跌箭头 | `ths-drawline-annotation` |
| 删除脚本生成的测试标注 | `ths-drawline-annotation` |
| 判断 DrawLine XML 的路径、marketCode、periodCode、LineType | `ths-drawline-annotation` |
| 新的同花顺本地数据自动化任务 | 父入口先建 evidence note，再决定是否新增子 skill |

## 通用执行协议

1. 明确授权边界和目标股票/周期/图形类型。
2. 读取相关 `references/` 与子 skill。
3. 优先 dry-run 和 list，不直接写盘。
4. 写盘前必须自动备份或显式说明无法备份。
5. 写入后使用 App 原生加载路径 UAT，默认重启 App 为已确认加载动作。
6. 将项目个案证据留在 PROJECT/TASK；只有稳定规则提升到本 Skill 的 `references/`。
7. 若需要用户操作 App，使用 `feishu-notify` 通知。

## Red / Green

Red：

```text
taskBoundaryOk=false
targetPathKnown=false
schemaKnown=false
dryRunOk=false
backupOk=false
nativeLoadUatOk=false
cleanupOk=false
```

Green：

```text
taskBoundaryOk=true
targetPathKnown=true
schemaKnown=true
dryRunOk=true
backupOk=true
nativeLoadUatOk=true
cleanupOk=true
```

对新增图形类型，允许分层状态：

```text
structureDryRunGreen
nativeLoadUatGreen
cleanupGreen
```

不要把 `structureDryRunGreen` 写成 `nativeLoadUatGreen`。

## 当前稳定能力

```text
DrawLine XML 路径识别；
已有标注/画线 list；
文字工具 text 写入并完成 native load UAT；
标注 note、矩形 rect、水平线 hline、上涨/下跌箭头 dry-run 结构生成；
按 TextContent dry-run/remove 清理；
写入前自动备份。
```

## 参考

- `references/drawline-schema.md`
- `references/source-provenance.md`
- `logs/2026-06-29-ths-skill-from-mac-reverse-project.md`
