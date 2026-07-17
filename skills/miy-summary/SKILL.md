---
name: miy-summary
description: Summarize work for any specified calendar date from local file creation/modification evidence, classify files by project root (with TASKxx kept as project-internal tasks), separate unassigned skill/tool activity, and create or update an all-day Feishu calendar recap. Use when the user asks for a daily work summary, date-based activity review, or to push such a recap to Feishu Calendar.
---

# miy-summary

按指定日期把工作区中的文件活动整理成“项目级 Summary + 有记录的小时线”，然后推送到飞书日历的全天日程。

## 1. 证据与分类

1. 日期必须是 `YYYY-MM-DD`；所有时间判断使用 `Asia/Shanghai`。日期边界和时间戳转换必须通过系统命令或脚本完成，不要凭心算。
2. 先阅读 `task-driven-project-manager` 的 SKILL.md，理解项目根目录与 `tasks/TASKxx-*` 的关系。TASKxx 是项目内部任务，不得在 Summary 中写成独立项目。
3. 从本技能的 `scripts/scan_day.py` 扫描工作区：

   ```bash
   python3 <miy-summary-skill-dir>/scripts/scan_day.py \
     --root <workspace-root> --date YYYY-MM-DD --timezone Asia/Shanghai
   ```

   脚本同时检查创建时间和最后修改时间，输出 JSON。默认排除 `.git`、`node_modules`、虚拟环境、缓存和 `__pycache__`。
4. 项目分类规则：`03 Projects/<project-root>/...` 归入该项目；路径中 `tasks/TASKxx-*` 只作为该项目的任务维度。其他路径统一归为“项目外/未归属项目”，并根据有限的路径/文件名信息提取主题：`00 信息/miy-skills/...` 写成“技能/工作流维护：<技能名>”，`00 信息/工具/...` 写成“工具维护：<工具名>”，其他路径使用前两级目录或文件名概括；只有无法可靠判断时才写“其他”。
5. “做了什么”必须以文件路径、文件名和变更时段为证据。没有文件变更只能写“未检测到文件变更记录”，不能推断用户没有工作。

## 2. Summary 写法

描述顶部必须先写项目级总结，结构如下：

```text
【Summary】
YYYY-MM-DD 主要推进 N 个项目：
1. <项目名>｜<项目级目标/阶段概括>。其中 TASKxx 是项目内部任务。

项目外/未归属项目的文件：
- <数量> 个 <技能/工作流> 文档：<用途概括>
- <数量> 个工具/配置文件：<维护概括>

文档活动统计：<项目内 Markdown>；<项目外 Markdown>；全工作区创建/更新总数，以及同日创建并更新数。

项目外文件必须尽量按上述主题概括，不能把所有文件压成“项目外/未归属项目（N个）”。
```

如果只有一个项目，也要明确写“1 个项目”；不要把 TASK00、TASK08 等列成项目。若没有项目外文件，写“未发现项目外文件”。

## 3. 按小时写法

- 只展示脚本报告中实际有变更文件的小时；合并相邻小时可以使用 `HH:00–HH:59` 或 `HH:00–HH:59、HH:00–HH:59`。
- 每行先写项目名，再写项目内部 TASKxx 及活动概括；项目外活动写推断出的技能/工具/目录主题，不要只写“项目外/未归属项目”。
- 可附文件数量，但不要把数量误写成工作时长。
- 推荐顺序：时间升序；Summary 后再放 `【按小时】`。

## 4. 推送飞书日历

用户明确要求“推送/更新到飞书日历”时，使用 `lark-calendar` 技能，并遵守其前置要求：先读 `lark-shared/SKILL.md`、`references/lark-calendar-schedule-meeting.md`，以及实际使用的 `+agenda`、`+create`/`+update` 参考文档。

1. 先用 `calendar +agenda --as user --start YYYY-MM-DD --end <next-date> --format json` 定位主日历、检查同日是否已有同名总结日程，并取得 `organizer_calendar_id`。
2. 日程标题默认 `YYYY-MM-DD工作总结`；描述使用上面的 Summary + 按小时文本。全天日程使用底层 `calendar events create/patch` 的 `start_time.date` 与 `end_time.date` 字段，不要用 18:00–18:30 伪装全天。单日全天请求按 API 约定传入同一日期；返回值可能将结束日期显示为次日。
3. 同日已有本技能创建的总结日程时，沿用唯一 `event_id` 做 patch，只更新描述；不要重复创建。没有则创建新的全天日程。写入时 `need_notification: false`，避免给自己发送通知。
4. 历史日期是回顾记录，不是预约会议；用户明确要求时可以按全天回顾处理。若 API 拒绝历史日期，不要擅自改到今天，报告错误并请用户决定。
5. 写入后等待至少 2 秒，再用 `+agenda` 查询同日，核验标题、全天 `start_time/end_time` 与描述已落地。

## 5. 边界

- 不读取文件正文来臆测工作内容，除非路径和文件名不足以概括活动且用户授权进一步阅读。
- 不把工具、技能、同步配置的修改冒充研究项目产出。
- 不泄露令牌、授权链接或私有协作者信息。
- 若用户只要求总结、不要求推送，则输出总结但不写飞书；若用户要求推送，则完成写入并核验。
