---
name: feishu-notify
description: 通过 Writer 中已有的 scholar-kit 通知工具给用户发送飞书推送或 macOS 本机通知。用于长任务完成、环境红灯、需要人工登录/确认、实验失败、后台采集异常、等待用户操作、定时状态通报，或用户明确要求“飞书通知我”“给人类通报”“发推送”“notify me”时。默认复用 Writer/.pytools/scholar-kit/scripts/notify.py，不在 Skill 中保存密钥或真实 token。
---

# Feishu Notify

## 目标

在需要把后台状态告诉人类时，优先复用已有通知工具：

```text
Writer/.pytools/scholar-kit/scripts/notify.py
```

本 Skill 只负责“何时通知、怎么调用、如何不刷屏”。不要在 Skill 中复制飞书密钥、webhook、用户 ID、业务 token 或真实响应。

## 快速调用

首选脚本：

```bash
scripts/send-notify.sh "标题" "正文" --feishu
```

常用例子：

```bash
scripts/send-notify.sh "MIKU 等待人类操作" "Big-Knife 已执行，请确认登录与目标页面状态。" --feishu
scripts/send-notify.sh "长任务完成" "采集任务已结束，请查看 batch-report.md。" --feishu
scripts/send-notify.sh "本机提醒" "这是一条只发 macOS 通知的提醒。"
```

发送带按钮的飞书交互卡片：

```bash
scripts/send-card.py "需要你确认" "任务已经暂停，请处理后点按钮。" \
  --button-text "我处理好了" \
  --reply-text "收到，继续推进。"
```

如果直接调用底层工具：

```bash
/Users/narra/Documents/alib/Writer/.venv/bin/python \
  /Users/narra/Documents/alib/Writer/.pytools/scholar-kit/scripts/notify.py \
  "正文" --title "标题" --feishu
```

## 通知判断

只在“人类需要知道或介入”的节点通知：

- 长任务完成、失败或进入人工门；
- 环境红灯、自动修复失败、设备离线、App crash；
- 需要登录、验证码、授权确认、进入目标页面；
- 后台任务暂停、冷却到期、等待用户下一步；
- 用户明确要求发送通知。

不要把高频状态变化都发飞书。进度条、每轮成功、每条请求结果应留在 dashboard、log 或状态文件里。

## 消息形态

底层 `scholar_kit.utils.notify` 当前支持几种形态：

| 形态 | 适用 | 入口 |
|---|---|---|
| macOS banner | 本机轻提醒 | `notify.py "正文" --title "标题"` |
| macOS alert | 本机阻塞式确认 | `notify.py "正文" --title "标题" --alert` |
| 飞书普通卡片 | 异步通知，无需反馈 | `notify.py "正文" --title "标题" --feishu` |
| 飞书按钮卡片 + 自动回复 | 人类点按钮后自动回一条文本 | `scripts/send-card.py ... --reply-text "收到"` |
| 飞书按钮卡片 + Python callback | 当前 Python 进程保持运行，点击按钮后执行回调 | 直接用 `feishu_notify(callback=...)` |
| 飞书关键词回复 callback | 用户回复某个关键词触发回调 | `register_keyword_callback(...)` |

按钮卡片有两个层级：

```text
轻量确认：只需要按钮 + reply_text，适合“我看到了”“继续吧”；
进程回调：需要当前 Python 进程保持运行并启动 Feishu WebSocket listener，适合让按钮点击真正唤醒等待中的自动化流程。
```

长跑任务默认优先用轻量确认。只有自动化确实需要“点按钮后继续执行”，才使用 callback 模式。

## 接收按钮与回复

底层 scholar-kit 已经支持通过 Feishu WebSocket listener 接收事件：

```text
scholar_kit.utils.notify._listener.FeishuEventListener
ensure_feishu_event_listener(...)
```

可接收两类交互：

- 飞书卡片按钮点击；
- 用户回复关键词。

但要注意边界：

```text
“能收到按钮事件” ≠ “某个业务工具已经能被按钮控制”。
```

如果要让 miku、采集器或其他后台任务响应飞书按钮，应额外设计一个业务侧 command listener 或 command queue，把按钮事件转换为稳定命令：

```text
start / stop / probe / repair / clear-cooldown / acknowledge / resume
```

不要把真实业务动作直接散落在通知 callback 里；推荐让 callback 只写入命令队列，由业务 supervisor 自己读取、校验、执行和记录日志。

## 限频原则

长跑任务必须避免通知刷屏：

```text
同类 key 默认 5-10 分钟内只通知一次；
环境红灯开始、修复成功、修复失败可以分 key；
业务冷却中的周期性状态不应每轮通知；
需要人工介入的状态可以强制通知一次。
```

如果业务脚本已有自己的限频器，优先使用业务脚本的通知入口，不要在外层再包一层重复通知。

## 安全纪律

- 不打印或落盘飞书密钥、webhook、App Secret、用户 token、authorization、cookie、device id。
- 通知正文默认写摘要，不写完整原始响应。
- 如果需要携带路径，优先给本地文档路径、报告路径、log 路径。
- 如果通知失败，不要让主任务因为通知失败而失败；记录 warning 并继续。

## 验证

先做不发飞书的本机 smoke：

```bash
scripts/send-notify.sh "通知 smoke" "这是一条本机 smoke 测试。"
```

确认需要飞书时再加：

```bash
scripts/send-notify.sh "飞书 smoke" "这是一条飞书 smoke 测试。" --feishu
```

交互卡片 smoke：

```bash
scripts/send-card.py "飞书按钮 smoke" "请点按钮确认。" \
  --button-text "收到" \
  --reply-text "收到确认。"
```

如果失败，检查：

```text
Writer/.venv/bin/python 是否存在；
Writer/.pytools/scholar-kit/scripts/notify.py 是否存在；
当前环境是否能访问飞书 API；
FEISHU_* 环境变量或 scholar-kit 默认配置是否可用。
```
