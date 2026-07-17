# Acceptance Contract: RESSET Interface-First Replay

## Route Boundary

本任务只评估授权 WebVPN/RESSET 登录态下的请求复现，不绕过：

- WebVPN / RESSET 登录与权限；
- CAPTCHA；
- RESSET 下载中心；
- 单次任务创建限制；
- 用户授权边界。

## Green Definitions

| Check | Green | Evidence |
|---|---|---|
| `tableMetadataOk` | `dataSearch.jsp` GET 返回目标表名、记录数、日期范围、字段/表单信息 | saved HTML summary or stable Markdown |
| `downloadCenterListOk` | `downloadTaskUser.action` GET 返回完成任务列表和 `downloadtask(...)` 参数 | parsed task rows |
| `taskCreatedOk` | direct POST 或等价协议创建 `FDSHRCHG` 单基金小样本任务 | 下载中心出现新任务，状态达到 100% |
| `zipRetrievalOk` | `/verifyDownload?token=<tid>` 或 CDP-triggered navigation 保存 zip | response magic `PK`，`unzip -l` 清单通过 |
| `fallbackOk` | WebVPN 登录失效、验证码失败、接口跳转登录页时能明确回退 UI/人工 | log records route and reason |

## Red Classifications

| Red | Meaning | Required next step |
|---|---|---|
| `webvpn_session_red` | 请求跳 IDaaS 登录或 WebVPN 兼容性提示 | 刷新/重登；不要误判 RESSET endpoint |
| `captcha_preflight_red` | 超级鹰凭据/依赖/状态不可用 | 人工接力或修复 `$handle-interactive-verification` |
| `task_creation_red` | direct POST 被 RESSET 拒绝或任务创建失败 | 保存 response summary，降级 UI |
| `zip_retrieval_red` | `/verifyDownload` 返回登录页/HTML 而非 zip | 保持 browser download event |

## UAT

### UAT 1: Read-Only Replay

```text
GET dataSearch.jsp for FDINFO / FDSHRCHG
GET downloadTaskUser.action
```

Pass:

```text
status 200
no IDaaS login page
expected RESSET markers present
```

### UAT 2: Task Creation

```text
FDSHRCHG
FdCd=000001
EndDt=2023-12-31
csv zip
small field set
```

Pass:

```text
download center shows new task
status reaches 100%
row count plausible for one-fund smoke
```

### UAT 3: Zip Retrieval

Pass:

```text
saved file starts with PK
unzip -l lists RESSET_FDSHRCHG_1.csv
copyright pdf exists
download condition or data dictionary html exists
```
