# Fix Log: miy-mail correspondence skill

## Summary

已将 correspondence 管理能力作为 `tools-skill` 的 sibling Skill 新建为 `miy-mail`，而不是并入 `tool-jira`。`tool-jira` 保持 issue / UAT / regression 工单语义，`miy-mail` 负责 Markdown 邮件、回复、会议 note 和 thread index。

## Modified Files

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/agents/openai.yaml`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/README.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/uat/TASK-miy-mail-smoke/emails/README.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/uat/TASK-miy-mail-smoke/emails/THREAD-20260708-csmar-data-confirmation/EMAIL-20260708-1600-to-data-colleague-csmar-data-confirmation.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/uat/TASK-miy-mail-smoke/emails/THREAD-20260708-csmar-data-confirmation/REPLY-20260708-1630-from-data-colleague-re-csmar-data-confirmation.md`

## Reproduction

原需求见：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/README.md
```

真实样例仍可作为参考：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/
```

## Validation

官方 Skill 结构校验：

```bash
PYTHONPATH='/Users/narra/.local/share/uv/tools/dvc/lib/python3.12/site-packages' python3 '/Users/narra/.codex/skills/.system/skill-creator/scripts/quick_validate.py' '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail'
```

结果：

```text
Skill is valid!
```

说明：系统默认 `python3` 和 Codex bundled Python 都缺少 `PyYAML`，直接运行 `quick_validate.py` 会报 `ModuleNotFoundError: No module named 'yaml'`。本次使用本机已有 uv dvc 环境中的 PyYAML 作为 `PYTHONPATH`，未安装或修改全局依赖。

## UAT / Acceptance Run

UAT fixture 输出路径：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/uat/TASK-miy-mail-smoke/emails/
```

执行内容：

```text
1. 创建 emails/README.md。
2. 创建 THREAD-20260708-csmar-data-confirmation/。
3. 创建 EMAIL-20260708-1600-to-data-colleague-csmar-data-confirmation.md。
4. 创建 REPLY-20260708-1630-from-data-colleague-re-csmar-data-confirmation.md。
5. README thread index 记录 initial item、latest item、status 和 next action。
```

验证命令：

```bash
'/Users/narra/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3' - <<'PY'
from pathlib import Path
root = Path('/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/uat/TASK-miy-mail-smoke/emails')
readme = root / 'README.md'
thread = root / 'THREAD-20260708-csmar-data-confirmation'
email = thread / 'EMAIL-20260708-1600-to-data-colleague-csmar-data-confirmation.md'
reply = thread / 'REPLY-20260708-1630-from-data-colleague-re-csmar-data-confirmation.md'
for path in [readme, email, reply]:
    assert path.exists(), path
readme_text = readme.read_text()
email_text = email.read_text()
reply_text = reply.read_text()
assert 'THREAD-20260708-csmar-data-confirmation' in readme_text
assert 'EMAIL-20260708-1600-to-data-colleague-csmar-data-confirmation.md' in readme_text
assert 'REPLY-20260708-1630-from-data-colleague-re-csmar-data-confirmation.md' in readme_text
assert '| Direction | outbound |' in email_text
assert '| Status | sent |' in email_text
assert '## Sendable Body' in email_text
assert '| Direction | inbound |' in reply_text
assert '| Reply to | EMAIL-20260708-1600-to-data-colleague-csmar-data-confirmation.md |' in reply_text
assert '## Extracted Commitments / Decisions' in reply_text
print('uat fixture validation passed')
PY
```

结果：

```text
uat fixture validation passed
```

## Acceptance Criteria

- [x] 明确该能力作为 sibling Skill 新建：`miy-mail`。
- [x] 提供 thread folder、email、reply、note 的命名规范。
- [x] 提供 outgoing email 和 inbound reply 的 Markdown 模板。
- [x] 提供 README thread index 更新规则。
- [x] 给出并执行 UAT 流程，记录 pass 标准和结果。

## Residual Risk

- `miy-mail` 目前是规则型 Skill，没有自动生成脚本；后续如果邮件归档量变大，可以再新增脚本辅助创建 thread、生成文件名和更新 README index。
