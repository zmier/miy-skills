# RESSET direct interface replay feasibility

> 状态：technical feasibility assessment; partial Green
> 最近更新：2026-07-08 20:12
> 技能路线：`$workflow-js-reverse`
> 范围：评估是否可从 Playwright/CDP 页面控制升级为直接接口请求；本轮不提交新下载任务、不绕过验证码。
> Canonical location：`$resset-download/tasks/TASK01-interface-first-replay/outputs/`
> Origin：基金经理研究 `TASK04-external-fund-data-inventory` 中发现并迁移到技能任务。

## Executive Judgment

可以做成 **hybrid interface-first**，但暂不建议直接改成纯 browserless 接口下载。

当前证据支持：

- `dataSearch.jsp` 表页读取可以接口化：在 WebVPN/RESSET 登录态新鲜且 cookie/token 齐全时，Node `fetch` 可直接 GET 到表页 HTML。
- `downloadTaskUser.action` 下载中心列表可以接口化：同样在登录态齐全时，可直接 GET 到已有任务列表。
- 下载中心 HTML 暴露现有任务的 `downloadtask(id, tid, path)`，真实下载入口表现为 iframe navigation：`/verifyDownload?token=<tid>`。

当前还没有 Green：

- `dataSearch.action` 创建下载任务的 direct POST 尚未验证。该步骤受验证码、表单 hidden 字段、一次性状态和任务规模限制约束。
- `/verifyDownload?token=<tid>` 的 browserless GET 尚未 Green。Node GET 会跳 IDaaS 登录页；页面内 `fetch('/verifyDownload?...')` 会失败在 WebVPN `yit-proxy3.js` 包装层。实际 UI 下载使用 iframe/navigation，不是普通 XHR/fetch。
- WebVPN/SSO 新导航状态不稳定：已有 RESSET tab 可见且登录，但新开只读 `dataSearch.jsp` tab 已跳统一身份登录页。这说明需要把 WebVPN token/session lifecycle 纳入 ledger。

推荐结论：

```text
default: Playwright/CDP + 页面内 JS + 下载中心
experimental: interface-first read/list + UI/iframe fallback for captcha/task/zip
not yet: fully browserless batch downloader
```

## 2026-07-08 20:12 Forward-Test Update

用户确认 `BUG-2026-07-08-chaojiying-preflight-runtime-readiness` 已修复后，已恢复 forward-test 前置检查。

本轮新增证据：

```text
Chaojiying preflight:
  status: ready
  ready: true
  network.attempted: false

RESSET existing download center:
  downloadTaskUser.action still readable
  existing FDSHRCHG and BS_ALL tasks visible

RESSET new table navigation:
  FDSHRCHG main frame redirects to 四川大学统一身份认证
```

结论：

- Chaojiying 运行时已不再阻塞 `$resset-download` forward test。
- 本轮没有进入验证码 challenge，也没有调用识别接口。
- 当前阻塞是 WebVPN/SSO session lifecycle；恢复登录态后再继续 `FDSHRCHG` 单基金 direct POST smoke。

补充探测：

```text
20:24 no-submit table probe:
  second RESSET main tab was still inside RESSET search results before navigation
  navigating its main frame to FDSHRCHG dataSearch.jsp also redirected to 四川大学统一身份认证
  live form: absent
  verifyCode / verifyImg: absent
```

该结果把阻塞归因进一步收窄为新表页导航的 WebVPN/SSO 状态，而不是 Chaojiying、RESSET 下载中心列表或特定 tab。

## Request Construction Ledger

### 1. RESSET Main / Database IDs

| Item | Value |
|---|---|
| Runtime | WebVPN proxied browser runtime; RESSET old JSP frameset |
| Main URL | `https://https-esource-scu-edu-cn-443.webvpn.scu.edu.cn/https/443/com/resset/db/yitlink/common/main.jsp` |
| Stock dbMsgId | `4028818a2206ecbc012206edd0d10001` |
| Fund dbMsgId | `4028818a2206ecbc012206eedeb60003` |
| Bond dbMsgId | `4028818a2206ecbc012206ee43ed0002` |
| Financial statistics dbMsgId | `402881fa4195b29801419ca1fd650003` |

Evidence:

- Existing RESSET tabs still show `RESSET金融研究`, `下载中心`, `退出系统`, and database list.
- Top search form exposes `select[name="dbMsgId"]`, `input[name="queryMsg"]`, `searchScope=all`, `searchType=fuzzy`.

### 2. Table Metadata Page

Candidate request:

```text
GET /https/443/com/resset/db/yitlink/db/download/dataSearch.jsp

query:
  dlm=
  tableName=FDSHRCHG
  dbMsgId=4028818a2206ecbc012206eedeb60003
```

Green observed once with browser-derived cookies:

```text
FDSHRCHG dataSearch
status: 200
length: 84,000
markers:
  基金份额变动 FDSHRCHG
  数据开始日期 1998-04-07
  数据结束日期 2026-06-08
  总记录数 4,812,871
  更新频度 月更新
  验证码区域存在
```

Other Green examples:

```text
BS_ALL dataSearch
status: 200
length: 238,182
markers:
  资产负债表 BS_ALL
  总记录数 2,075,171

FDINFO dataSearch
status: 200
length: 130,414
markers:
  基金信息 FDINFO
  总记录数 32,514
```

Red / unstable condition:

```text
When WebVPN/SSO state is not fresh, the same GET redirects to:
https://https-id-scu-edu-cn-443.webvpn.scu.edu.cn/login

or to WebVPN compatibility tip:
https://webvpn.scu.edu.cn/?returnUrl=...
```

Interpretation:

- RESSET table page itself is replayable.
- WebVPN session construction is the hard outer layer.
- A direct client must extract and refresh WebVPN/RESSET cookies and likely localStorage state, not only RESSET `JSESSIONID`.

### 3. Download Task Creation

Candidate request from page and previous UI smoke:

```text
POST db/download/dataSearch.action
target/result frame: resultFrame
```

Important parameters to carry from page form:

```text
tableName
tableFullName
dbMsgId
dlm
hasNext
downloadNb
timeRange
beginDate
endDate
dateObject
cgRadio
cSearchVar
cValue / cSearchText / cSearchFile
varCheck
outputType
downType
zipType
verifyCode
```

Known constraints:

- `verifyCode` is required before task creation.
- Existing skill policy still applies: default one authorized Chaojiying attempt, failure manual.
- Full-table `FDSHRCHG` creation previously failed; single-fund smoke succeeded. Direct POST must start from the same single-fund smoke.

Status:

```text
requestConstructedOk: candidate only
realEndpointReachedOk: not tested in this round
taskCreatedOk: not tested in this round
```

Reason for not testing:

- Testing this endpoint would create a new RESSET server-side download task and requires a fresh captcha challenge. This should be a separate user-approved forward test.

### 4. Download Center List

Candidate request:

```text
GET db/download/downloadTaskUser.action
```

Green observed once with browser-derived cookies:

```text
status: 200
length: 16,344
markers:
  RESSET 基金_基金份额变动
  100%
  csv
  0.333 MB
  3 rows
  RESSET 股票_资产负债表
  100%
  csv
  0.488 MB
  11477 rows
```

Task row exposes:

```text
downloadtask(
  '7beed0ca13044cdda5d38833dd13b834',
  'c7f2c35e9bff433e84b4f7f1e7e94cf5',
  '/DOWNLOAD_FILE/FDSHRCHG_0fb426ac4d144eb6990bce74f2e88ac3/RESSET 基金_基金份额变动.zip'
)
```

Page function:

```text
downloadtask(id, tid, path):
  create hidden iframe
  iframe.src = '/verifyDownload?token=' + encodeURIComponent(tid)
  AJAX POST downloadTaskUser!upDate.action with { id }
```

Interpretation:

- Listing completed tasks is likely interface-replayable.
- Existing file metadata can be parsed without UI clicking.

### 5. Existing Zip Download

Candidate request:

```text
GET /verifyDownload?token=<tid>
```

Observed red:

```text
Node GET -> IDaaS login HTML, not zip
Browser page fetch('/verifyDownload?...') -> TypeError: Failed to fetch at yit-proxy3.js
```

Interpretation:

- Actual successful UI download is iframe/navigation based, not ordinary fetch.
- Browserless zip saving needs extra work:
  - capture exact network request produced by iframe navigation;
  - determine whether `yit-proxy3.js`, service worker, localStorage `x-yit-token`, `signCode`, or navigation-only behavior is required;
  - only call it Green when response starts with zip magic `PK`.

Until then, keep zip retrieval via browser download event or CDP download behavior.

## Dynamic State Ledger

Observed state in current WebVPN runtime:

```text
document.cookie:
  _bid
  HWWAFSESTIME
  HWWAFSESID
  csmenu
  comenu
  SYSTEM_INIT_FORMAT
  JSESSIONID
  yit_sw=true
  CLICKIT_SESSION
  goto

localStorage:
  signCode
  x-yit-token
  SearchHistory
  lastTime
  __path__full__

scripts:
  /yit-proxy3.js?v1.0.1
  /yit-analysis.js?v1.0.1
  RESSET base.js / jquery / bootstrap

browser features:
  serviceWorker = true
```

Request replay must treat WebVPN as part of the target system. RESSET cookies alone are insufficient.

## Recommended Forward Test

### Green 1: Read-Only Interface Probe

Goal:

```text
Use browser-derived cookies + localStorage state to GET:
  dataSearch.jsp?tableName=FDINFO
  dataSearch.jsp?tableName=FDSHRCHG
  downloadTaskUser.action
```

Pass criteria:

```text
tableMetadataOk: true
downloadCenterListOk: true
redirectToLogin: false
```

### Green 2: Single-Fund Task Creation Replay

Goal:

```text
POST FDSHRCHG single-fund smoke:
  FdCd=000001
  EndDt=2023-12-31
  small field set
  csv zip
```

Pass criteria:

```text
captchaAcceptedOk: true
taskCreatedOk: true
downloadCenterShowsTaskOk: true
no full-table task
```

This must remain user-authorized because it touches captcha and creates a server-side task.

### Green 3: Zip Retrieval

Goal:

```text
Save already-created completed zip through direct request or CDP-triggered iframe/navigation.
```

Pass criteria:

```text
zipResponseMagic: PK
contentDisposition filename matches RESSET zip
unzip lists data csv + copyright pdf + download condition html
```

## Suggested Skill Change After Green

Do not replace the current `$resset-download` default yet. Add an experimental mode only after Green 1 and at least one Green 2:

```text
mode: interface-first
1. Extract WebVPN/RESSET state from current Chrome/CDP.
2. Try read-only GET for table metadata and download center.
3. If redirect/login/tip appears, fallback to Playwright/CDP UI.
4. For task creation, use direct POST only for captcha-authorized small smoke first.
5. For zip retrieval, prefer direct /verifyDownload only after PK magic Green; otherwise browser download event.
```

Current recommendation:

```text
Use interface replay for metadata/listing acceleration.
Keep Playwright/CDP as the authoritative path for captcha, task creation, and zip saving.
```
