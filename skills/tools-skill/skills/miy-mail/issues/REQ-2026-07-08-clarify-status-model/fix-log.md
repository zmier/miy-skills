# Fix Log: clarify status model

## Summary

已明确 `miy-mail` 中的两套状态模型：单条 `EMAIL` / `REPLY` / `NOTE` 文件只能使用 record status，`README.md` thread index 只能使用 thread status。已补充误用示例、迁移旧 correspondence 样例的 UAT 流程，并用 TASK03 CSMAR 样例副本完成验证。

## Modified Files

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/README.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/uat/TASK03-csmar-migrated/emails/README.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/uat/TASK03-csmar-migrated/emails/THREAD-20260708-csmar-fund-manager-data/EMAIL-20260708-1543-to-data-colleague-csmar-fund-manager-data-request.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/uat/TASK03-csmar-migrated/emails/THREAD-20260708-csmar-fund-manager-data/REPLY-20260708-1710-from-data-colleague-re-csmar-fund-manager-data.md`

## Reproduction

原需求见：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/README.md
```

真实样例来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/
```

真实项目样例未在本次修复中修改。

## Validation

官方 Skill 结构校验：

```bash
PYTHONPATH='/Users/narra/.local/share/uv/tools/dvc/lib/python3.12/site-packages' python3 '/Users/narra/.codex/skills/.system/skill-creator/scripts/quick_validate.py' '/Users/narra/.codex/skills/miy-mail'
```

结果：

```text
Skill is valid!
```

## UAT / Acceptance Run

UAT fixture 输出路径：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/uat/TASK03-csmar-migrated/emails/
```

执行内容：

```text
1. 复制真实 TASK03 emails/ 样例到 UAT fixture。
2. 升级 README index 为 Thread / Topic / Participants / Initial item / Latest item / Status / Next action。
3. 给 outbound email 补 Channel、record-level Status、Next action 和 ## Sendable Body。
4. 新增 synthetic REPLY 记录，Status 使用 received，Reply to 指向原始 EMAIL。
5. README thread Status 使用 replied，Latest item 指向 REPLY。
```

验证命令：

```bash
'/Users/narra/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3' - <<'PY'
from pathlib import Path
root = Path('/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/uat/TASK03-csmar-migrated/emails')
readme = root / 'README.md'
thread = root / 'THREAD-20260708-csmar-fund-manager-data'
email = thread / 'EMAIL-20260708-1543-to-data-colleague-csmar-fund-manager-data-request.md'
reply = thread / 'REPLY-20260708-1710-from-data-colleague-re-csmar-fund-manager-data.md'
record_statuses = {'draft', 'sent', 'received', 'recorded', 'superseded'}
thread_statuses = {'draft', 'waiting', 'replied', 'needs-followup', 'closed'}
for path in [readme, email, reply]:
    assert path.exists(), path
def metadata(path):
    data = {}
    for line in path.read_text().splitlines():
        if not line.startswith('|') or line.startswith('|---') or line.startswith('| Field'):
            continue
        parts = [part.strip() for part in line.strip('|').split('|')]
        if len(parts) == 2:
            data[parts[0]] = parts[1]
    return data
email_meta = metadata(email)
reply_meta = metadata(reply)
assert email_meta['Status'] in record_statuses
assert reply_meta['Status'] in record_statuses
assert email_meta['Status'] not in thread_statuses - record_statuses
assert reply_meta['Status'] not in thread_statuses - record_statuses
assert email_meta['Channel'] == 'email'
assert reply_meta['Channel'] == 'email'
assert 'Next action' in email_meta
assert 'Next action' in reply_meta
assert '## Sendable Body' in email.read_text()
assert reply_meta['Reply to'] == email.name
readme_text = readme.read_text()
assert '| Thread | Topic | Participants | Initial item | Latest item | Status | Next action |' in readme_text
assert reply.name in readme_text
assert '| replied | review returned inventory scope |' in readme_text
for forbidden in ['| sent |', '| received |', '| recorded |', '| superseded |']:
    assert forbidden not in readme_text
print('status model migration uat passed')
PY
```

结果：

```text
status model migration uat passed
```

## Acceptance Criteria

- [x] Add an explicit note that record status and thread status are separate state models.
- [x] Add a misuse example or short warning about not mixing the two status sets.
- [x] Add or reference a migration UAT for an existing correspondence sample.
- [x] Ensure the UAT pass standard checks both per-file metadata and README thread index.

## Residual Risk

- `miy-mail` 仍是规则型 Skill，没有自动迁移脚本；若后续旧 correspondence 样例较多，可以新增脚本批量检查 status 混用和 README index schema。
