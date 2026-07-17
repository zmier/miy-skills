# TASK01 Log

## 2026-07-08 20:05 ReAct：从基金经理研究 TASK04 剥离 RESSET skill 工程

### Thought

RESSET interface-first replay、direct POST forward test、zip retrieval 和 Chaojiying preflight 都是 `$resset-download` 的技能工程问题。它们是在基金经理研究项目中被发现的，但不应长期留在该项目的 TASK04 下，否则后续其他项目复用 `$resset-download` 时找不到完整证据链。

### Action

在 `$resset-download` 目录下建立 task-driven 结构：

```text
tasks/TASK01-interface-first-replay/
```

并准备把基金经理研究 TASK04 的 interface replay feasibility 文档迁移到本任务作为 canonical 输出。

### Observation

已创建 `$resset-download` 侧 task-driven 结构：

```text
README.md
tasks/README.md
tasks/TASK01-interface-first-replay/TASK01-说明.md
tasks/TASK01-interface-first-replay/README.md
tasks/TASK01-interface-first-replay/acceptance-contract.md
tasks/TASK01-interface-first-replay/logs/log.md
tasks/TASK01-interface-first-replay/outputs/resset_direct_interface_replay_feasibility.md
```

`SKILL.md` 已新增“技能工程与任务证据”小节，指向 `tasks/TASK01-interface-first-replay/`，并明确未达成 acceptance contract 前不把 direct POST 或 browserless zip retrieval 写成默认路线。

已把原基金经理研究项目中的：

```text
tasks/TASK04-external-fund-data-inventory/outputs/resset_direct_interface_replay_feasibility.md
```

移动到：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/resset-download/tasks/TASK01-interface-first-replay/outputs/resset_direct_interface_replay_feasibility.md
```

项目侧 TASK04 README 已改为指向 `$resset-download` 技能任务，不再把该文档作为项目本地产物。

### Reflection

迁移后边界更清楚：基金经理研究 TASK04 只记录“发现了 RESSET interface-first 改进机会”，而 `$resset-download/tasks/TASK01-interface-first-replay/` 承担后续 direct POST、zip retrieval、Chaojiying preflight 依赖和 SKILL.md 反哺。后续只有 TASK01 达成 acceptance contract 后，才应把 experimental 或默认规则写入 `$resset-download/SKILL.md`。

## 2026-07-08 20:12 ReAct：Chaojiying 修复后恢复 RESSET forward test

### Thought

用户确认 `BUG-2026-07-08-chaojiying-preflight-runtime-readiness` 已修复。根据 issue fix-log，默认 `python3` 仍会结构化返回 `missing_dependency`，但 workflow `.venv` 下 `preflight --no-network --json` 可返回 `ready`，真实 `score` UAT 也通过。因此 RESSET direct POST forward test 可以恢复，但仍必须遵守：

```text
1. 自动识别前必须先跑 preflight；
2. 只允许单次授权 challenge；
3. 失败立即人工接力；
4. 不记录 CAPTCHA 结果、pass2、token 或敏感码。
```

### Action

本轮按四步推进：

```text
1. 用 handle-interactive-verification 的 workflow .venv 跑 Chaojiying preflight。
2. 检查当前 Chrome/CDP 中 RESSET WebVPN 登录态。
3. 尝试恢复 FDSHRCHG 单基金 smoke 的表页与验证码 challenge。
4. 在 preflight=ready 的前提下，做 direct POST / zip retrieval forward test；若 WebVPN 或验证码阻塞则按红灯分类回填。
```

### Observation

已用 workflow `.venv` 运行 Chaojiying preflight：

```text
status: ready
ready: true
network.attempted: false
python: 3.12.12
requests: 2.32.4
env: CHAOJIYING_USER / CHAOJIYING_PASS2 / CHAOJIYING_CODETYPE present
```

这说明 `BUG-2026-07-08-chaojiying-preflight-runtime-readiness` 的核心阻塞已解除，且自动识别前的本地运行时检查可作为 `$resset-download` 的默认前置步骤。

随后检查 Chrome/CDP 中的 RESSET WebVPN 页面：

```text
downloadTaskUser.action: still readable
existing tasks:
  - RESSET 基金_基金份额变动, 100%, csv, 0.333 MB, 3 rows
  - RESSET 股票_资产负债表, 100%, csv, 0.488 MB, 11477 rows
```

但把 `main` frame 导航到 `FDSHRCHG` 表页后，该 frame 被重定向到四川大学统一身份认证：

```text
main frame URL: https://https-id-scu-edu-cn-443.webvpn.scu.edu.cn/frontend/login
visible markers:
  - 四川大学统一身份认证
  - 扫码登录
  - 短信登录
  - 账号登录
```

因此本轮未进入 RESSET 表页验证码 challenge，也未调用 Chaojiying 识别，不存在新的验证码结果或敏感凭据需要记录。

当前 acceptance 状态：

```text
chaojiyingPreflightOk: true
webvpnSessionFreshForExistingDownloadCenter: partial true
webvpnSessionFreshForNewTableNavigation: false
captchaChallengeReached: false
directPostTaskCreatedOk: not attempted
browserlessZipRetrievalOk: not attempted
```

### Reflection

本轮阻塞点已经从“Chaojiying runtime readiness”转移为“WebVPN/SSO session lifecycle”。`$resset-download` 可以吸收的稳定规则是：下载前默认先跑 Chaojiying preflight；preflight Green 后才进入单次授权 CAPTCHA；若 RESSET 新导航跳到统一认证，则应先要求恢复 WebVPN/RESSET 登录态，不应把该状态误判为验证码失败或接口失败。

direct POST forward test 仍需在用户重新恢复 RESSET/WebVPN 登录态后继续。恢复后优先沿 `FDSHRCHG` 单基金 smoke 规模测试，不做全表大任务。

## 2026-07-08 20:24 ReAct：改用仍在站内的 RESSET tab 做 no-submit 表页探测

### Thought

Chrome/CDP 中存在两个 RESSET 主 tab。一个 tab 的 `main` frame 已重定向到四川大学统一身份认证；另一个 tab 仍停留在 RESSET 站内检索结果页，下载中心 iframe 也仍能读取已有任务。这说明 WebVPN 状态不是全局完全失效，而是不同 frame/tab 的导航状态不一致。可以先用仍在站内的 tab 做只读 `FDSHRCHG` 表页探测，确认是否还能回到下载表单页；该操作不提交下载任务、不触发验证码识别。

### Action

用 CDP 对仍在站内的 RESSET tab 导航 `main` frame 到：

```text
db/download/dataSearch.jsp?dlm=&tableName=FDSHRCHG&dbMsgId=4028818a2206ecbc012206eedeb60003
```

只检查 frame URL、正文标记、表单和验证码区域是否出现。若跳统一认证，则回填为 WebVPN/SSO 阻塞；若表页可见，再进入单基金 smoke 参数构造，但仍先不提交。

### Observation

只读导航已执行，未提交任何下载任务，也未触发验证码识别。

导航前目标 tab 状态：

```text
title: RESSET金融研究
top url: common/main.jsp
main frame: db/table/searchMsgSolrList.jsp
download center: still readable in another tab
```

导航 `main` frame 到 `FDSHRCHG` 表页后：

```text
requested:
  db/download/dataSearch.jsp?dlm=&tableName=FDSHRCHG&dbMsgId=4028818a2206ecbc012206eedeb60003

actual main frame:
  https://https-id-scu-edu-cn-443.webvpn.scu.edu.cn/frontend/login

visible markers:
  - 四川大学统一身份认证
  - 扫码登录
  - 账号登录
```

未出现：

```text
FDSHRCHG
基金份额变动
下载数据
verifyCode
verifyImg
```

因此本轮没有可供 direct POST 构造的 live form，也没有验证码 challenge。

### Reflection

这次把两个 RESSET 主 tab 都验证了：旧外壳、菜单或下载中心的可读性不足以代表新表页导航可用；只要目标表页跳 IDaaS，接口化和 UI 下载都应先暂停，等待用户恢复 WebVPN/RESSET 登录态。

下一次用户完成登录后，应从本条 ReAct 后继续：先重新打开/刷新 RESSET main page，再只读进入 `FDSHRCHG` 表页，若能看到 `下载数据` 和 `#verifyImg`，再进入 Chaojiying preflight 已 Green 的单次授权 CAPTCHA 路线。

## 2026-07-08 20:21 ReAct：用户重新登录后恢复 FDSHRCHG smoke

### Thought

用户回复“好了”，表示 RESSET/WebVPN 登录态已恢复。本轮从 20:24 的阻塞点继续：先验证 Chrome/CDP 中是否有可用 RESSET tab，再只读进入 `FDSHRCHG` 表页；若表单和验证码区域出现，按 `$resset-download` 的规则先跑 Chaojiying no-network preflight，再做单次授权候选识别或人工接力。为了降低服务器任务规模，仍以单基金 smoke 为目标，不做全表大下载。

### Action

计划顺序：

```text
1. 读取当前 Chrome tabs 和 RESSET frame tree，确认登录态。
2. 导航到 FDSHRCHG dataSearch.jsp，只读检查表页与表单。
3. 构造单基金、少字段、csv、zip 的 smoke 参数。
4. preflight=ready 后，仅对当前 challenge 做一次超级鹰候选识别；失败则人工接力。
5. 提交任务后检查下载中心，若任务完成再验证下载入口。
```

### Observation

用户重新登录后，Chrome/CDP 中 `79A9...` RESSET 主 tab 已恢复为站内页面：

```text
top title: RESSET金融研究
markers:
  - 下载中心
  - 退出系统
  - 股票
  - 基金
  - 债券
  - 宏观统计
```

只读进入 `FDSHRCHG` 成功：

```text
main frame URL:
  db/download/dataSearch.jsp?dlm=&tableName=FDSHRCHG&dbMsgId=4028818a2206ecbc012206eedeb60003

markers:
  - 基金份额变动
  - FDSHRCHG
  - 下载数据
  - 验证码 / verifyCode
  - 数据开始日期 1998-04-07
  - 数据结束日期 2026-06-08
  - 总记录数 4,812,871
```

已把 smoke 参数收紧为：

```text
tableName: FDSHRCHG
tableFullName: 基金份额变动
dateObject: dList_EndDt / 截止日期
beginDate: 2026-06-08
endDate: 2026-06-08
cSearchVar: FdCd / 基金代码
cValue: 000001
fields:
  - FdCd
  - FdNm
  - EndDt
  - StartShr
  - BuyShr
  - RedeShr
  - ShrEnd
  - ShrChg
outputType: csv
downType: Labels+Column
zipType: zip
```

验证码前置检查：

```text
captcha image: 100x30 JPEG, saved to local transient path
chaojiying preflight: ready
recognize: err_no=0, pic_id present, candidate length=4
```

验证码候选未写入日志、未写入文件、未展示给用户。

随后尝试用页面内 `fetch(FormData)` 直接 POST 到：

```text
db/download/dataSearch.action
```

但 CDP 返回体没有带回可验收的 `submit` payload；事后只读检查显示：

```text
resultFrame: about:blank
downloadTaskUser.action: status 200, but no new FDSHRCHG task row observed
verifyCode input: empty
```

因此本轮不能判为 `directPostTaskCreatedOk=true`。

已按“默认超级鹰，失败人工”的规则切换人工接力，并通过 `$feishu-notify` 发送提醒：

```text
title: RESSET 需要人工验证码
action: 请用户在当前 Chrome 的 RESSET 表页手动填写验证码，填好后回复继续
```

### Reflection

本轮 Green 的部分是：WebVPN/RESSET 登录态恢复、`FDSHRCHG` 表页打开、表单参数构造、Chaojiying preflight 和单次授权识别。未 Green 的部分是：页面内 direct POST 没有形成可验证的新下载任务。

由于已经对当前 challenge 做过一次授权识别，不能继续自动重复调用第三方识别。下一步等待用户手动填写验证码；用户确认后，优先用页面原生 `js_search('download')` 提交，以验证 RESSET UI 任务创建链路，再回到下载中心检查任务行。direct POST 作为 experimental 继续保留在 TASK01，不写入默认 SKILL 路线。

## 2026-07-08 20:29 ReAct：用户要求核验超级鹰返回候选

### Thought

用户询问“为什么超级鹰没通过”，并要求查看超级鹰接口返回的码。根据 `$handle-interactive-verification` 规则，验证码候选不能写入聊天、日志或文件；但可以在当前授权页面中把候选值回填到 `#verifyCode`，由用户在浏览器里查看。需要区分两件事：超级鹰接口是否返回成功，以及 RESSET 服务端是否接受该验证码并创建任务。

### Action

对当前 RESSET `FDSHRCHG` 页面重新截取当前 `#verifyImg`，先运行 no-network preflight；若 ready，则做一次用户明确要求的候选识别，并只把候选值填入页面 `#verifyCode`。日志只记录 `err_no`、`err_str`、候选长度和是否填入，不记录候选文本。

### Observation

已对当前页面重新截图并调用超级鹰：

```text
page: 基金份额变动 FDSHRCHG
captcha: 100x30 JPEG
preflight.status: ready
preflight.network.attempted: false
chaojiying.err_no: 0
chaojiying.err_str: OK
pic_id_present: true
pic_str_len: 4
page_fill.ok: true
verifyCode fieldLen: 4
```

候选值已填入当前 RESSET 页面 `#verifyCode` 输入框；未写入聊天、日志或文件。

### Reflection

本次验证说明“超级鹰没通过”的表述需要修正：超级鹰接口侧是通过的，返回了 4 位候选，并已成功回填页面。上一轮未形成下载任务，更可能是 `fetch(FormData)` direct POST 路线没有完整复刻 RESSET 原生 `js_search('download')` 的提交/iframe 行为，或响应处理被 WebVPN/页面脚本链路吞掉；不能归因为 Chaojiying OCR 失败。

下一步若用户确认页面验证码已可见，可用页面原生按钮/`js_search('download')` 提交，而不是继续 direct fetch。

## 2026-07-08 20:31 ReAct：用页面原生提交测试 FDSHRCHG smoke

### Thought

用户要求“点下一步测试下”。当前验证码候选已由上一轮填入页面 `#verifyCode`，不需要也不应重复调用第三方识别。本轮目标是验证 RESSET 原生 UI/iframe 提交流程是否能创建下载任务，而不是继续 direct POST 实验。

### Action

读取当前页面 `#verifyCode` 是否非空；若非空，重新确认 smoke 参数仍为 `FDSHRCHG` 单基金、单日、少字段，然后在页面上下文调用原生 `js_search('download')`。提交后观察：

```text
1. resultFrame URL / text；
2. 是否出现下载提交弹窗或验证码错误；
3. 下载中心列表是否出现新的 RESSET 基金_基金份额变动任务。
```

### Observation

已执行页面原生提交测试。

提交前状态：

```text
verifyCode length: 4
tableName: FDSHRCHG
beginDate / endDate: 2026-06-08 / 2026-06-08
cSearchVar: FdCd
cValue: 000001
selectedFields:
  - FdCd
  - FdNm
  - EndDt
  - StartShr
  - BuyShr
  - RedeShr
  - ShrEnd
  - ShrChg
outputType: csv
downType: Labels+Column
zipType: zip
```

调用：

```text
window.js_search('download')
```

页面函数执行后已设置：

```text
targetAction: download
cSearchText: 000001
initFormat: csv
fileHeadFormat: Labels+Column
zipFormat: zip
```

页面/站点返回：

```text
alert: 创建下载失败，请重试！
resultFrame: about:blank
downloadTaskUser.action: 200
new FDSHRCHG task row: not observed
```

因此本轮 `nativeUiTaskCreatedOk=false`，没有进入下载中心新任务轮询或 zip 下载阶段。

### Reflection

页面原生链路已证明 `js_search('download')` 可以正常设置提交字段，但服务器侧没有创建任务。由于失败消息是通用的“创建下载失败，请重试！”，当前不能仅凭页面反馈区分是验证码候选未被服务端接受、`FDSHRCHG` 单基金参数组合有问题，还是 RESSET 对该表/字段/时间的任务创建有额外限制。

下一步建议走两个分支之一：

```text
1. 人工填一个新验证码后用相同参数再点一次，隔离 OCR 候选问题；
2. 换成此前已 Green 的 BS_ALL smoke 参数复测，隔离 FDSHRCHG 表/参数问题。
```

在未隔离前，不把 `FDSHRCHG` 自动下载写入 `$resset-download/SKILL.md` 的稳定路线。

## 2026-07-08 20:36 ReAct：恢复 FDSHRCHG 页面供人工验证码测试

### Thought

用户指出当前看到的是 RESSET `common/main.jsp` 首页，而不是 `FDSHRCHG` 表页。需要恢复内部 `main` frame 到 `FDSHRCHG dataSearch.jsp`，并把 smoke 参数重新配置好，让用户手动填写新验证码测试。

### Action

激活当前 RESSET Chrome tab，导航内部 `main` frame 到：

```text
db/download/dataSearch.jsp?dlm=&tableName=FDSHRCHG&dbMsgId=4028818a2206ecbc012206eedeb60003
```

页面打开后重新设置：

```text
dateObject=dList_EndDt
beginDate=endDate=2026-06-08
cSearchVar=FdCd
cValue=000001
fields=FdCd,FdNm,EndDt,StartShr,BuyShr,RedeShr,ShrEnd,ShrChg
outputType=csv
downType=Labels+Column
zipType=zip
verifyCode empty
```

### Observation

已恢复目标页面。虽然 Chrome 顶层 tab 仍显示 `common/main.jsp` / `RESSET金融研究`，但内部 frameset 的 `main` frame 已是：

```text
db/download/dataSearch.jsp?dlm=&tableName=FDSHRCHG&dbMsgId=4028818a2206ecbc012206eedeb60003
```

当前确认：

```text
markers:
  - 基金份额变动
  - FDSHRCHG
  - 数据开始日期
  - 数据结束日期
  - 总记录数

captchaPresent: true
captchaSize: 100x30
verifyCode length: 0
```

smoke 参数已恢复：

```text
beginDate / endDate: 2026-06-08 / 2026-06-08
cSearchVar: FdCd
cValue: 000001
selectedFields: FdCd,FdNm,EndDt,StartShr,BuyShr,RedeShr,ShrEnd,ShrChg
outputType: csv
downType: Labels+Column
zipType: zip
```

### Reflection

这是 frameset 页面造成的视觉误导：顶层地址栏一直是 `common/main.jsp`，但实际业务页在内部 `main` frame。用户现在可以直接在页面下方验证码区域手动填写新验证码并点击“下载数据”，或填好后回复继续由自动化点击。

## 2026-07-08 20:39 ReAct：人工验证码同样创建失败

### Thought

用户反馈手动填写验证码后也返回“创建下载失败”。这基本排除 Chaojiying OCR 候选问题，下一步应把故障归因转向 `FDSHRCHG` 表、参数组合、记录匹配或 RESSET 对该表的任务创建限制。

### Action

记录人工验证码结果，并对当前 `FDSHRCHG` 页面做只读诊断：读取 smoke 参数、表单关键字段、隐藏限制字段、页面记录数和可能的校验/下载限制文本。不再调用验证码识别，也不再提交下载。

### Observation

用户确认字段全选是人工操作，不应作为主因。

只读诊断显示当前 `FDSHRCHG` 表单关键状态：

```text
form.action: db/download/dataSearch.action
form.target: resultFrame
form.enctype: multipart/form-data
tableName: FDSHRCHG
dbMsgId: 4028818a2206ecbc012206eedeb60003
dlm: 303
tableRecordsValue: 4,812,871
servertype: 1
dateObject: dList_EndDt
beginDate / endDate: 2026-06-08 / 2026-06-08
cSearchVar: FdCd
cValue / cSearchText: 000001 / 000001
targetAction: download
assignLines: -1
outputType: csv
downType: Labels+Column
zipType: zip
```

当前页面没有暴露更具体的错误码，只有通用的“创建下载失败，请重试！”。

### Reflection

字段全选可暂时排除。更高概率的原因是日期口径：页面“数据结束日期 2026-06-08”不等于 `EndDt=2026-06-08` 对 `FdCd=000001` 必然有记录，也不代表该日期适合创建下载任务。已有项目邮件和旧 console 线索都指向 `FdCd=000001 + EndDt=2023-12-31` 曾作为成功 smoke/讨论样本；下一步应把日期改回 `2023-12-31`，由用户手填新验证码后测试。

## 2026-07-08 20:41 ReAct：复原此前成功的 FDSHRCHG smoke

### Thought

用户询问“之前测试的时候能下载的那个，可以复现吗？” 现有证据显示此前成功样本是 `FDSHRCHG` 单基金 smoke：

```text
FdCd=000001
EndDt=2023-12-31
csv zip
download center: RESSET 基金_基金份额变动, 3 rows
CSV: 华夏成长混合A 申购、赎回、份额变化记录
```

因此应复原这组参数，而不是继续使用 `2026-06-08`。

### Action

在当前 `FDSHRCHG` 页面恢复参数：

```text
dateObject: dList_EndDt
beginDate / endDate: 2023-12-31 / 2023-12-31
cSearchVar: FdCd
cValue: 000001
fields:
  - FdCd
  - FdNm
  - StartDt
  - EndDt
  - StartShr
  - BuyShr
  - RedeShr
  - ShrEnd
  - ShrChg
  - RtShrChg
  - DivReinvt
  - ShiftIn
  - ShiftOut
outputType: csv
downType: Labels+Column
zipType: zip
verifyCode: empty
```

不提交、不调用验证码识别，等待用户手填验证码后复现。

### Observation

页面已设置为此前成功样本参数，验证码框为空，验证码图片存在。

### Reflection

这组参数应优先用于隔离：如果它能创建任务，则 `2026-06-08` 是失败主因；如果它仍失败，再排查当前 RESSET 会话、验证码或表任务创建状态变化。

## 2026-07-08 20:47 ReAct：WebVPN 重新入口后用超级鹰复测 FDSHRCHG 成功样本

### Thought

用户反馈：此前手填仍失败，但从四川大学 WebVPN 页面重新进入 RESSET 后就可以下载。这说明前面失败高概率是 WebVPN/RESSET frame 会话状态脏了，而不是字段、日期或验证码本身。当前 Chrome 中出现新的 RESSET tab，应在这个新会话上复现此前成功样本，并用超级鹰单次候选填码测试。

### Action

计划：

```text
1. 使用当前新 RESSET tab。
2. 进入 FDSHRCHG 表页。
3. 配置此前成功样本：FdCd=000001, EndDt=2023-12-31, csv zip, 小字段集。
4. 跑 Chaojiying no-network preflight。
5. 截取当前验证码，单次 recognize，回填 #verifyCode。
6. 调用页面原生 js_search('download')。
7. 检查弹窗/resultFrame/下载中心任务。
```

### Observation

复测成功。

环境：

```text
new RESSET tab id: CF7DA2FBFC17DF0CBD4427187188E4AA
entry: user re-entered RESSET from Sichuan University WebVPN page
```

配置参数：

```text
tableName: FDSHRCHG
beginDate / endDate: 2023-12-31 / 2023-12-31
cSearchVar / cValue: FdCd / 000001
fields:
  - FdCd
  - FdNm
  - StartDt
  - EndDt
  - StartShr
  - BuyShr
  - RedeShr
  - ShrEnd
  - ShrChg
  - RtShrChg
  - DivReinvt
  - ShiftIn
  - ShiftOut
outputType: csv
downType: Labels+Column
zipType: zip
```

验证码路线：

```text
preflight.status: ready
captcha image: 100x30
chaojiying.err_no: 0
chaojiying.err_str: OK
pic_id_present: true
pic_str_len: 4
verifyCode filled: length 4
```

页面原生提交：

```text
js_search('download')
targetAction: download
cSearchText: 000001
initFormat: csv
fileHeadFormat: Labels+Column
zipFormat: zip
```

结果：

```text
page markers:
  - 下载已提交
  - 下载编号
  - 进入下载中心

download center:
  time: 07-08 20:48:50
  dataset: RESSET 基金_基金份额变动
  status: 100%
  format: csv
  size: 0.333 MB
  rows: 3

download saved:
  /Users/narra/.codex/.playwright-mcp/RESSET 基金_基金份额变动.zip
  bytes: 349527

zip contents:
  - RESSET_FDSHRCHG_1.csv
  - RESSET_CopyrightNotice_cn.pdf
  - FDSHRCHG_数据词典.html
```

CSV 验证：

```text
FdCd: 000001
FdNm: 华夏成长混合A
EndDt: 2023-12-31
rows: 3
contains: StartShr, BuyShr, RedeShr, ShrEnd, ShrChg, RtShrChg
```

### Reflection

关键结论：同样的成功样本参数与超级鹰路线，在用户从四川大学 WebVPN 入口重新进入后的新 RESSET 会话中 Green。这说明此前“创建下载失败，请重试！”主要不是字段全选、验证码 OCR、或 `FDSHRCHG` 样本参数问题，而是 WebVPN/RESSET frameset 会话状态脏了。

稳定执行建议：

```text
若已知 Green 参数 + 正确验证码仍返回“创建下载失败，请重试！”，不要在脏 frameset 中反复提交；
应从四川大学 WebVPN 入口重新进入 RESSET，再重新打开目标表页和配置参数。
```

本轮满足 TASK01 中 `FDSHRCHG` 单基金 UI-equivalent task creation + zip retrieval 的 Green 证据；direct POST browserless 仍未 Green，不能升级为默认路线。

## 2026-07-08 20:58 ReAct：把 direct browserless 困难点反哺到 SKILL

### Thought

用户追问当前 `$resset-download/SKILL.md` 是否已经沉淀 “Node/curl/fetch 直接 POST 后端、绕过真实页面状态和下载中心” 的困难点。核对后发现：SKILL 已经写入了稳定边界，即默认使用 `Playwright/CDP + 页面内 JS + 下载中心`，不默认使用 Node/curl/fetch 直连；但具体困难机理仍主要保留在 TASK01 feasibility/log 中，不利于下次执行时快速判断。

### Action

补充 `$resset-download/SKILL.md` 的“控制方式边界”小节，把 direct browserless 的当前状态写成可执行判断：

```text
1. 表页 HTML 与下载中心列表可 interface-first 读取；
2. dataSearch.action 创建任务 direct POST 尚未 Green；
3. verifyDownload?token 的 browserless GET 尚未 Green；
4. 默认路线仍是页面内 JS + iframe/download event；
5. 纯 browserless 只能作为 TASK01 实验路线。
```

### Observation

已在 `$resset-download/SKILL.md` 的“控制方式边界：Playwright/CDP + 页面内 JS”后新增“接口直连当前状态”小节。新增内容明确：

```text
已 Green / 可辅助读取：
  - dataSearch.jsp 表页 HTML
  - downloadTaskUser.action 下载中心列表

未 Green / 不能默认：
  - dataSearch.action direct POST 创建下载任务
  - verifyDownload?token browserless GET 保存 zip
  - 仅凭旧下载中心可读不能判断 WebVPN/SSO 新导航有效

默认：
  - Playwright/CDP + 页面内 JS + 验证码 + 下载中心 iframe/download event
```

核对后，SKILL 中没有写入验证码候选、第三方识别敏感结果或绕过权限/验证码/下载中心的执行建议。

### Reflection

这次反哺后，`$resset-download/SKILL.md` 已经不仅记录“不要默认直连”，也记录了为什么不能默认直连、哪些接口可作为辅助读取、哪些仍属于 TASK01 实验路线。后续执行 RESSET 下载时，默认路线仍是页面内 JS 和真实下载中心；只有当 TASK01 的 acceptance contract 对 direct POST 和 browserless zip retrieval 都达成 Green，才应再次升级 SKILL 默认规则。
