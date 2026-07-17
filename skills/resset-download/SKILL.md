---
name: resset-download
description: 使用 Playwright MCP 在 RESSET/锐思金融研究数据库中检索、定位并下载数据表。适用于通过 WebVPN 访问 RESSET，配置日期、代码、字段、输出格式，遇到验证码时优先使用授权的超级鹰单次候选识别，失败后通知用户接管，并从“下载中心”取回文件的场景。
---

# RESSET 数据下载（Playwright MCP）

## 技能工程与任务证据

本技能的稳定执行规则写在 `SKILL.md`。探索性接口复现、forward test、UAT 和后续 skill 反哺证据放在本技能目录的 `tasks/` 下。

当前任务：

```text
tasks/TASK01-interface-first-replay/
```

该任务承接从研究项目中剥离出来的 RESSET interface-first replay 证据。未达成 TASK acceptance contract 前，不把 direct POST 或 browserless zip retrieval 写成默认路线。

真实项目反哺、迁移状态和来源追溯记录在：

```text
references/source-provenance.md
```

## 前置条件

1. 用户已通过 WebVPN 打开 RESSET/锐思金融研究数据库，或允许在 Playwright MCP 固定 profile 中打开入口页。
2. Playwright MCP 已连接，优先用 `mcporter` 调用。
3. 若下载前出现验证码，默认使用 `$handle-interactive-verification` 中的超级鹰方案做**授权、低频、单次 challenge** 候选识别；识别失败或服务端不接受时，再交给用户人工填写。不要循环刷新验证码、批量调用第三方识别或记录验证码结果。

先确认 MCP 运行状态：

```bash
which mcporter && mcporter list
sed -n '1,160p' ~/.codex/config.toml
find /Users/narra/Library/Caches/ms-playwright -maxdepth 1 -type d \
  \( -name 'mcp-chrome*' -o -name 'playwright_chromiumdev_profile-*' \) | sort
```

当前推荐使用共享 Chrome profile：

```text
/Users/narra/Library/Caches/ms-playwright/mcp-chrome
```

注意：`playwright-mcp` 固定 profile 不等于用户日常 Chrome 的现有标签页。若用户要求检查“当前 Chrome TAB”，优先尝试 Chrome plugin；若 Chrome extension 不可用，再说明限制，并用 `playwright-mcp` 打开同一 WebVPN URL 验证固定 profile 中的登录态。

RESSET WebVPN 入口：

```text
https://https-esource-scu-edu-cn-443.webvpn.scu.edu.cn/https/443/com/resset/db/yitlink/common/main.jsp
```

## 页面结构

RESSET 是旧式 frameset 页面。实测主要结构如下：

```text
common/main.jsp
  mainFrame -> common/mainFrame.jsp?dbMsgId=4028818a2206ecbc012206edd0d10001&fromT=load
    menu -> common/menu.jsp?dbMsgId=4028818a2206ecbc012206edd0d10001&property=
    main -> db/main/mainPage.jsp 或 db/download/dataSearch.jsp
```

下载中心也是外层页面加 iframe：

```text
db/download/downloadTask.jsp
  mainFrame / #iResult -> db/download/downloadTaskUser.action
```

不要长期持有旧 frame 对象。点击表名、提交下载或进入下载中心后，frame 可能重载或 detach，必须重新从 `page.frames()` 查找。

## 控制方式边界：Playwright/CDP + 页面内 JS

RESSET 推荐控制方式是：用 Playwright MCP 或 Chrome DevTools Protocol 连接当前可用的 Chrome 登录态，再在页面上下文中执行站点自身前端逻辑和 DOM 操作。这里的 JS 是**页面内 JS**，不是绕过浏览器、脱离登录态直接请求后端接口。

允许的做法：

- 通过 Playwright/CDP 选择 RESSET 页面、frame 和下载中心页。
- 在页面上下文中触发 RESSET 自带函数，例如 `js_search()`、`changeDb()`、表单提交相关函数。
- 在 `menu`/`main` frame 中读取 DOM 链接、`dataSearch.jsp` 页面正文、表单 hidden 字段、记录数、时间范围和下载限制。
- 用 Playwright locator / 页面真实控件交互配置关键表单字段；`frame.evaluate()` 可用于读取状态、轻量字段勾选或站点自身函数调用，但日期、代码和上传文件状态必须用数据预览 canary 验证。
- 下载仍走真实 UI 链路：配置参数 -> 数据预览 canary -> 验证码 -> 点击“下载数据” -> “下载中心” -> 保存 zip。

不默认采用的做法：

- 不用 Node/curl/fetch 直接拼后端下载接口。
- 不跳过验证码、下载中心或站内任务创建流程。
- 不把页面内 JS 扫描菜单误记为“直接接口请求”。

如果需要探索接口，只能作为单独的调研任务记录在 log 中，且不得绕开当前用户登录态、权限边界、验证码或 RESSET 下载中心规则。

### 接口直连当前状态

截至 `TASK01-interface-first-replay` 的 2026-07-08 forward test，RESSET 可以做 **hybrid interface-first**，但不能把纯 Node/curl/fetch browserless 下载写成默认路线。

已 Green / 可作为辅助读取：

- `dataSearch.jsp` 表页 HTML 在 WebVPN/RESSET 登录态新鲜、cookie/token 齐全时可直接读取，用于提取表名、字段、日期范围、记录数、hidden 字段和验证码区域。
- `downloadTaskUser.action` 下载中心列表在登录态新鲜时可直接读取，用于解析已有任务、状态、行数、文件大小和 `downloadtask(id, tid, path)` 参数。

未 Green / 不能默认：

- `dataSearch.action` 创建下载任务的 direct POST 尚未证明可稳定复刻。该步骤受当前验证码 challenge、hidden 字段、target frame、`js_search('download')` 设置的提交状态、一次性页面状态和任务规模影响。若页面内 `fetch(FormData)` 没有生成任务，优先回到页面原生 `js_search('download')`，不要把失败归因为 OCR。
- `/verifyDownload?token=<tid>` 的 browserless GET 尚未证明可直接拿到 zip。实测 Node GET 可能跳四川大学 IDaaS 登录页；页面内 `fetch('/verifyDownload?...')` 可能被 WebVPN `yit-proxy3.js` 包装层阻断。真实成功链路是 `downloadtask()` 创建 hidden iframe，用 navigation 触发下载，再由浏览器 download event/CDP 保存文件。
- WebVPN/SSO 状态不能只按“下载中心还能读”判断。旧 frameset、旧 iframe 或旧 tab 可读，不代表新表页导航、验证码 challenge 或下载提交仍处于有效会话。

默认执行判断：

```text
default: Playwright/CDP + 页面内 JS + 数据预览 canary + 验证码 + 下载中心 iframe/download event
allowed helper: interface-first 读取表页/下载中心列表
experimental only: direct POST 创建任务、browserless verifyDownload zip 保存
```

通用定位函数：

```js
function getRessetPage(page) {
  const pages = page.context().pages();
  return pages.find(p => p.url().includes('/resset/db/yitlink/common/main.jsp')) ||
    pages.find(p => p.url().includes('/resset/db/yitlink/')) ||
    page;
}

async function frameText(frame) {
  return await frame.locator('body').innerText({ timeout: 5000 }).catch(() => '');
}

async function findRessetFrame(page, predicate) {
  for (const frame of page.frames()) {
    const text = await frameText(frame);
    if (await predicate(frame, text)) return frame;
  }
  throw new Error('RESSET frame not found');
}

async function getMainDataFrame(page) {
  return await findRessetFrame(page, async (frame, text) =>
    frame.name() === 'main' ||
    frame.url().includes('/db/download/dataSearch.jsp') ||
    text.includes('下载数据') ||
    text.includes('常用数据表')
  );
}

function getDownloadTaskFrame(page) {
  return page.frames().find(f => f.url().includes('/db/download/downloadTaskUser.action'));
}
```

## Phase 0：登录态烟测

打开入口页后，先确认不是空壳、过期会话或无权限页：

```js
const resset = getRessetPage(page);
await resset.bringToFront();
await resset.waitForLoadState('domcontentloaded').catch(() => {});
await resset.waitForTimeout(3000);

const snapshot = [];
for (const frame of resset.frames()) {
  snapshot.push({
    name: frame.name(),
    url: frame.url(),
    text: (await frameText(frame)).slice(0, 1500)
  });
}
return snapshot;
```

可用性判据：

- 正文能看到 `RESSET金融研究`、`四川大学`、`下载中心`、`退出系统` 等登录后元素。
- 用户信息区域显示登录名，例如 `scu`，机构为 `四川大学`。
- 权限数据库列表包含目标库，例如 `股票`、`基金`、`债券`、`宏观统计` 等。
- 若看到登录页、账号下线或权限错误，先请用户重新登录 WebVPN/RESSET。

实测四川大学账号会显示正式机构用户，到期日类似 `2026-11-30`，并拥有 `股票`、`基金`、`宏观统计` 等多类库权限。

## Phase 1：定位目标表

优先从页面已有链接进入目标表；其次使用顶部搜索；最后才拼接直接 URL。

常见股票库表名：

| 目标数据 | RESSET 表名 | 物理表名 |
|---|---|---|
| 资产负债表 | 资产负债表 | `BS_ALL` |
| 利润表 | 利润表 | `IS_ALL` |
| 现金流量表 | 现金流量表 | `SCF_ALL` |
| 上市公司信息 | 上市公司信息 | `CINFO` |
| 月股票综合数据 | 月股票综合数据 | `MRESSTK` |
| 财务指标 | 财务指标 | `FININD` |
| 财务比率 | 财务比率 | `FINRATIO` |
| 年市值 | 年市值 | `YRMV` |
| 日股票综合数据 | 日股票综合数据 | `DRESSTK_2021_2025`、`DRESSTK_2026_` 等分段表 |

实测 `资产负债表` 的菜单链接可能是：

```text
db/download/dataSearch.jsp?dlm=12201&tableName=BS_ALL&dbMsgId=4028818a2206ecbc012206edd0d10001
```

但隐藏菜单链接经常不可见，直接 `locator.click()` 会失败。更稳的方式是点击 `main` frame 首页中的“常用数据表”可见链接：

```js
const resset = getRessetPage(page);
const main = await getMainDataFrame(resset);
await main.locator('a').filter({ hasText: '资产负债表' }).first().click();
await resset.waitForTimeout(3000);

const dataFrame = await findRessetFrame(resset, async (frame, text) =>
  frame.url().includes('/db/download/dataSearch.jsp') &&
  text.includes('资产负债表') &&
  text.includes('下载数据')
);
```

如果目标表不在首页常用数据表里，从 `menu` frame 抽取 href，而不是点击隐藏节点：

```js
const menu = resset.frames().find(f => f.name() === 'menu');
const links = await menu.locator('a').evaluateAll(els => els.map(a => ({
  text: (a.innerText || a.title || '').trim(),
  href: a.href,
  onclick: a.getAttribute('onclick')
})));
```

顶部搜索入口位于外层主页面，控件名通常为：

```text
select[name="dbMsgId"]
input[name="queryMsg"]
input/button value="搜 索"
```

搜索后同样重新获取 frame，再点击目标表结果。

## Phase 2：读取目标表状态

进入 `dataSearch.jsp` 后先读取表名、记录数、时间范围和权限状态：

```js
const dataFrame = await findRessetFrame(resset, async (frame, text) =>
  frame.url().includes('/db/download/dataSearch.jsp') &&
  text.includes('下载数据')
);

const body = await frameText(dataFrame);
if (body.includes('无权限') || body.includes('没有权限')) {
  throw new Error('RESSET table has no permission');
}
```

实测 `BS_ALL` 页面字段：

```text
资产负债表 BS_ALL
记录数：2,075,171
起始日期：1989-12-31
截止日期：2026-03-31
更新频率：月度
```

主要表单：

```text
form[name="myform"] action="db/download/dataSearch.action" target="resultFrame"
hidden: tableName, tableFullName, dbMsgId, dlm, hasNext, downloadNb
```

## Phase 3：配置下载参数

按顺序配置：日期口径 -> 代码筛选 -> 字段 -> 输出格式。

重要控件名：

```text
timeRange: 0=日期范围, 1=时间不限
beginDate / endDate
dateObject: 截止日期, 信息发布日期
cgRadio: c=代码输入, cg=代码组, cgb=概念板块
cSearchVar: 上市公司代码, 公司代码, 最新公司全称, A股股票代码, B股股票代码, H股股票代码, 上市标识
cValue
varCheck: 字段 checkbox
outputType: excel2007, excel, csv, csvutf, txt, stata17, stata12, ...
downType: Labels+Column, Labels, Column
zipType: zip
```

字段选择建议用字段名，而不是位置。低风险 smoke test 可只选少量字段：

关键输入优先使用真实控件交互，尤其是 `beginDate`、`endDate`、`dateObject`、`cSearchVar`、`cValue`、`cSearchFile`。实测 `FDNVRET` 中直接 `frame.evaluate()` 改 DOM value 会出现“可见值正确，但数据预览返回系统异常”的脏状态；用 `locator.fill()` / 真实点击从干净表页重填后，同一日期和代码条件可预览并下载。

```js
await dataFrame.locator('input[name="beginDate"]').fill('2023-03-10');
await dataFrame.locator('input[name="endDate"]').fill('2023-09-24');
await dataFrame.locator('select[name="dateObject"]').selectOption('dList_TrdDt');
await dataFrame.locator('select[name="cSearchVar"]').selectOption('FdCd');
await dataFrame.locator('textarea[name="cValue"], input[name="cValue"]').fill('000051 000216 000834');
```

`frame.evaluate()` 仍可用于字段勾选、输出格式 radio、快照读取等低风险动作，但提交前必须通过 `3.2 下载前数据预览 canary`。

```js
await dataFrame.evaluate((cfg) => {
  const setRadio = (name, value) => {
    const el = document.querySelector(`input[name="${name}"][value="${value}"]`);
    if (el) el.checked = true;
  };
  const setValue = (name, value) => {
    const el = document.querySelector(`[name="${name}"]`);
    if (el) el.value = value;
  };

  setRadio('timeRange', '0');
  setValue('beginDate', cfg.beginDate);
  setValue('endDate', cfg.endDate);
  setValue('dateObject', cfg.dateObject);

  setRadio('cgRadio', 'c');
  setValue('cSearchVar', cfg.codeVar);
  setValue('cValue', cfg.codeValue || '');

  document.querySelectorAll('input[name="varCheck"]').forEach(cb => {
    cb.checked = cfg.fields.includes(cb.value);
  });

  setRadio('outputType', cfg.outputType);
  setRadio('downType', cfg.downType);
  setRadio('zipType', 'zip');
}, {
  beginDate: '2023-12-31',
  endDate: '2023-12-31',
  dateObject: '截止日期',
  codeVar: '上市公司代码',
  codeValue: '',
  fields: ['CompanyCode', 'ComCd', 'LComNm', 'ReportType', 'EndDt'],
  outputType: 'csv',
  downType: 'Labels+Column'
});
```

如果需要全字段，可点击页面按钮 `全选字段`，或将所有 `input[name="varCheck"]` 设为 checked。

### 3.1 大批量代码：文本文件上传优先试验

部分 RESSET 表在第 2 步查询条件中提供文本文件上传控件，常见控件名为：

```text
input[name="cSearchFile"]
form[name="myform"] enctype="multipart/form-data"
```

当目标代码池较大、手工填入 `cValue` 可能超长时，优先读取页面示例或帮助文本，确认该表是否支持文本文件。若支持，可先尝试 all-in-one 文本文件上传，再准备分批 fallback。

通用策略：

```text
1. 生成 code file：纯代码，无表头；按页面要求选择“一行空格分隔”或“一行一个代码”。
2. 同时生成 chunk plan：例如每 500/1000 个代码一批，作为服务器拒绝 all-in-one 时的备用计划。
3. 配置页面：timeRange/dateObject/date range/cSearchVar/fields/outputType/downType/zipType。
4. 上传文件到 cSearchFile；提交前在页面上下文读取表单快照。
5. 快照至少记录：cSearchVar、cValue 是否为空、cSearchFile 文件名与大小、varCheck 数量、日期范围和输出格式。
6. all-in-one 如果成功，保留 fallback chunk 文件但不执行；如果服务器拒绝、任务失败或下载中心没有新任务，再切换 chunk plan。
```

Playwright 上传示例：

```js
const fileInput = dataFrame.locator('input[name="cSearchFile"]');
if (await fileInput.count()) {
  await fileInput.setInputFiles('/path/to/codes.txt');
}
```

不要把一次 all-in-one 成功泛化为所有 RESSET 表都支持大文本上传。每张表都要先检查控件、示例规则、任务创建结果和下载中心记录。

### 3.2 下载前数据预览 canary

下载前必须先跑一次页面自身的“数据预览”作为 canary。表单快照只能证明 DOM 值看起来正确，不能证明 RESSET 旧式 frameset、hidden state、上传文件状态、target frame 和 WebVPN 会话能被服务器接受。

默认门槛：

```text
配置参数 -> 点击“数据预览” -> 预览有响应且不是“系统异常” -> 再进入验证码/下载
```

如果“数据预览”无反应、返回“系统异常”、跳登录页、弹权限错误、或结果 iframe 没有可解释响应，立即停止，不要继续验证码或点击“下载数据”。这类失败优先判断为表单状态脏、导航方式不对、上传控件状态不被站点接受、hidden 字段不完整、frame 已 detach，或当前 Playwright 操作的 tab/frame 与用户实际可用页面不是同一个。

预览 smoke test 示例：

```js
async function previewCanary(resset, dataFrame) {
  const previewButton = dataFrame.locator('input[type="button"][name="dataShow"][value*="数据预览"]');
  await previewButton.waitFor({ timeout: 10000 });
  await previewButton.click();
  await resset.waitForTimeout(5000);

  const popupText = await dataFrame.locator('#downloadPopup')
    .innerText({ timeout: 2000 })
    .catch(() => '');

  const frameSnapshots = [];
  for (const frame of resset.frames()) {
    const text = await frame.locator('body').innerText({ timeout: 2000 }).catch(() => '');
    if (frame.name() === 'resultFrame' ||
        frame.url().includes('dataSearch.action') ||
        text.includes('系统异常') ||
        text.includes('预览') ||
        text.includes('没有符合条件')) {
      frameSnapshots.push({
        name: frame.name(),
        url: frame.url(),
        text: text.replace(/\s+/g, ' ').slice(0, 1200),
      });
    }
  }

  const joined = [popupText, ...frameSnapshots.map(x => x.text)].join(' ');
  if (joined.includes('系统异常')) {
    throw new Error('RESSET preview returned 系统异常; rebuild form before download');
  }
  if (!joined.trim()) {
    throw new Error('RESSET preview had no observable response; do not download');
  }

  return { popupText, frameSnapshots };
}
```

Green 判据：

```text
1. 预览按钮点击后有明确响应；
2. 结果不是“系统异常”；
3. 不跳 WebVPN/统一身份认证/权限错误；
4. 对正式下载任务，预览结果应与预期筛选方向一致：有样本时看到数据行；若预期可能无记录，至少要看到站点返回的可解释“无记录/没有符合条件数据”。
```

Red 处理：

```text
1. 不提交下载，不进入验证码；
2. 重新从 RESSET 页面真实入口、菜单或用户当前可预览的 tab 进入表页；
3. 重新配置表单，少用直接 frame.goto；必要时让用户在能预览的页面上保留焦点，由 Playwright 读取并复用该 frame；
4. 对文本文件上传场景，先用小规模手工代码输入做预览 smoke，再切回 cSearchFile 上传；
5. 把预览失败文本、frame URL、form hidden 字段和用户可预览页面差异写入 task log。
```

## Phase 4：验证码识别与人工兜底

RESSET 下载提交前可能出现验证码区域：

```text
#verifyCode
#verifyImg
refreshCode()
```

默认路线：

```text
数据预览 canary green -> no-network preflight -> 授权单次 challenge -> 截取 #verifyImg -> 超级鹰候选识别 -> 回填 #verifyCode -> 提交下载
失败/空结果/服务端拒绝 -> 飞书通知用户人工填写 -> 用户回复后继续
```

### 4.1 默认：超级鹰单次候选识别

使用 `$handle-interactive-verification` 的超级鹰脚本，安全边界如下：

- 仅限当前用户授权的 RESSET/WebVPN 会话和当前单次下载 challenge。
- 必须显式传入 `--ack-authorized`。
- 凭据放在本地忽略文件或环境变量中，不写入 skill、日志或项目文件。
- `recognize` 只调用一次；不做目录批量、不循环刷新验证码、不自动轰炸重试。
- 输出建议加 `--redact-result`；若需要回填 `pic_str`，仅在内存/当前命令输出中短暂使用，不落盘。
- 若服务端返回验证码错误，可在人工确认确实识别错误后，用返回的 `pic_id` 执行一次 `report-error`。

脚本路径：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py
```

推荐 Python：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python
```

凭据文件模板：

```bash
cp '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.example' \
  '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local'
```

`.env.local` 典型字段：

```text
CHAOJIYING_USER=超级鹰账号
CHAOJIYING_PASS=超级鹰明文密码
# 或 CHAOJIYING_PASS2=密码 md5 小写值
CHAOJIYING_SOFT_ID=软件 ID
CHAOJIYING_CODETYPE=1902
```

识别前必须先做 no-network preflight；只有 `status=ready` 才继续截图和识别。非 ready 时不要等到验证码环节才失败，直接走人工兜底：

```bash
'/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python' \
  '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py' \
  preflight \
  --env-file '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local' \
  --no-network \
  --json
```

preflight 判据：

```text
ready -> 可继续单次授权 challenge
missing_credentials / missing_dependency / invalid_env_shape -> 飞书通知用户人工填写
```

先从页面截图验证码图片：

```js
const codeInput = dataFrame.locator('#verifyCode');
if (await codeInput.count()) {
  const value = await codeInput.inputValue();
  if (!value.trim()) {
    await dataFrame.locator('#verifyImg').screenshot({
      path: '/Users/narra/.codex/.playwright-mcp/resset_verify.jpg'
    });
  }
}
```

识别单张图片：

```bash
'/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python' \
  '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py' \
  --env-file '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local' \
  recognize \
  --image '/Users/narra/.codex/.playwright-mcp/resset_verify.jpg' \
  --codetype 1902 \
  --ack-authorized \
  --redact-result
```

返回 JSON 中的 `pic_str` 是候选验证码，`pic_id` 用于确认为错时返分。回填候选值：

```js
const candidate = '<pic_str from chaojiying>';
const codeInput = dataFrame.locator('#verifyCode');
await codeInput.fill(candidate);
```

如果 RESSET 提交后明确返回验证码错误，且超级鹰结果确认为错，可返分一次：

```bash
'/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/.venv/bin/python' \
  '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/scripts/chaojiying_client.py' \
  --env-file '/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/skills/handle-interactive-verification/.env.local' \
  report-error \
  --pic-id '<pic_id from recognize>' \
  --confirm-wrong-result \
  --ack-authorized
```

### 4.2 失败兜底：人工接力

若没有超级鹰凭据、脚本报错、候选为空、页面没有 `#verifyImg`、或服务端不接受验证码，则通知用户，并停止自动点击下载：

```bash
'/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/feishu-notify/scripts/send-notify.sh' \
  'RESSET 需要人工验证码' \
  'RESSET 超级鹰识别不可用或未通过。请在浏览器中填写验证码后，回复我继续。' \
  --feishu
```

用户填好验证码并回复后，重新读取 `#verifyCode`，确认非空再继续：

```js
const codeInput = dataFrame.locator('#verifyCode');
if (await codeInput.count()) {
  const value = await codeInput.inputValue();
  if (!value.trim()) throw new Error('RESSET captcha is empty; wait for user');
}
```

## Phase 5：提交下载任务

点击页面上的“下载数据”按钮，或调用页面函数：

```js
const downloadButton = dataFrame.locator('input[type="button"][name="search"][value*="下载数据"]');
await downloadButton.click();
await resset.waitForTimeout(5000);
```

提交成功后会出现 `#downloadPopup`：

```text
下载提醒
下载已提交！请进入“下载中心”查看。
下载编号：RESSET 股票_资产负债表
关闭
进入下载中心
```

点击 `#popupGotoBtn` 进入下载中心：

```js
const popupText = await dataFrame.locator('#downloadPopup').innerText({ timeout: 15000 });
const gotoBtn = dataFrame.locator('#popupGotoBtn');
await gotoBtn.click();
await resset.waitForTimeout(3000);
```

`进入下载中心` 通常会打开新标签页：

```text
db/download/downloadTask.jsp
```

## Phase 6：从下载中心保存文件

下载中心外层只有标题和面包屑，真实任务列表在 iframe `downloadTaskUser.action` 中。必须进入该 frame：

```js
const center = page.context().pages().find(p => p.url().includes('downloadTask.jsp'));
await center.bringToFront();
await center.waitForTimeout(3000);

const taskFrame = getDownloadTaskFrame(center);
if (!taskFrame) throw new Error('download task iframe not found');

const rows = await taskFrame.locator('tr').evaluateAll(trs => trs.map((tr, i) => ({
  i,
  text: (tr.innerText || '').replace(/\s+/g, ' ').trim()
})));
```

任务完成行的实测格式：

```text
1 07-08 16:20:38 RESSET 股票_资产负债表 100% csv 0.488 11477 下载
```

若状态不是 `100%`，等待后刷新/重查。任务链接只在站内保存 48 小时。

保存文件：

```js
const button = taskFrame.locator('button').filter({ hasText: /下载/ }).first();
await button.waitFor({ timeout: 15000 });

const downloadPromise = center.waitForEvent('download', { timeout: 60000 });
await button.click();
const download = await downloadPromise;
await download.saveAs('/Users/narra/.codex/.playwright-mcp/resset_download.zip');
```

实测下载按钮的 onclick 类似：

```text
downloadtask('e4c713ce04e246b1a1f6e1562966914b',
             '34c11c13b0814ea3b67da49e0accb8c7',
             '/DOWNLOAD_FILE/BS_ALL_.../RESSET 股票_资产负债表.zip')
```

下载后用系统工具验证：

```bash
ls -lh /Users/narra/.codex/.playwright-mcp/resset_download.zip
unzip -l /Users/narra/.codex/.playwright-mcp/resset_download.zip | sed -n '1,80p'
```

BS_ALL smoke test 成功样本应包含：

```text
RESSET_BS_ALL_1.csv
RESSET_CopyrightNotice_cn.pdf
BS_ALL_下载条件.html
```

### 6.1 同名任务精确定位

下载中心可能同时存在同一张表的多个历史任务，例如 pilot、重试批次、年度批次和 all-in-one 批次。不要只按表名点击第一个“下载”按钮。

稳妥定位规则：

```text
target = 数据集名称 + 下载时间/序号 + 100% 状态 + 行数/大小（如已知）
button = 目标行内 onclick 包含目标物理表名前缀的 downloadtask(...)
```

读取行和按钮时注意：旧 RESSET 下载中心的 DOM 可能有一个外层 `tr` 包住整张列表。应优先识别真实任务行文本，或用按钮的 `closest('tr').innerText` 与目标时间戳匹配。

示例：

```js
const targetTime = 'MM-DD HH:mm:ss';
const rows = await taskFrame.locator('tr').evaluateAll((trs) =>
  trs.map((tr, i) => ({
    i,
    text: (tr.innerText || '').replace(/\s+/g, ' ').trim(),
  }))
);
const targetRow = rows.find(row =>
  row.text.includes('RESSET 基金_基金份额变动') &&
  row.text.includes(targetTime) &&
  row.text.includes('100%')
);
```

下载按钮的 `onclick` 可解析出：

```text
downloadtask(id, tid, path)
```

把 `id`、`tid/token`、`path`、目标行文本和本地保存路径写入 TASK-local metadata，便于后续审计。不要把真实 token 写入通用 Skill 或公开报告。

### 6.2 download event 失败后的受限取回兜底

首选仍然是点击下载按钮并等待浏览器 `download` event。但在 WebVPN/隐藏 iframe/站内 CDN 场景下，真实下载可能由 `downloadtask()` 创建 hidden iframe 触发，Playwright 的 `download` event 偶尔不触发。

只有在以下条件同时满足时，才可使用页面上下文 token 兜底：

```text
1. 下载任务已经通过真实 UI、验证码和下载中心创建；
2. 下载中心目标行状态为 100%；
3. 已按目标行精确解析出 downloadtask(id, tid, path)；
4. browser download event 超时或不可用；
5. 取回结果经过 content-type / content-length / zip magic 验证。
```

兜底示例：

```js
const result = await taskFrame.evaluate(async (token) => {
  const response = await fetch(`/verifyDownload?token=${encodeURIComponent(token)}`, {
    credentials: 'include',
  });
  const buffer = await response.arrayBuffer();
  return {
    status: response.status,
    url: response.url,
    headers: Object.fromEntries(response.headers.entries()),
    bytes: Array.from(new Uint8Array(buffer)),
  };
}, taskToken);
```

保存前必须验证：

```text
HTTP status = 200
content-type 包含 application/zip 或实际 bytes 是 zip
前 4 字节 zip magic = 504b0304
本地 zipinfo/unzip 可读
```

该兜底只用于“已完成下载中心任务的文件取回”，不能用于绕过验证码、创建任务、下载未授权数据或替代页面提交链路。

### 6.3 多 CSV zip 的下载后 QC

大批量 RESSET zip 可能拆成多个 CSV member。QC 要流式读取全部 CSV，而不是只看第一个 member。

最低 QC：

```text
zip members
zip size and magic
encoding
CSV member count
header/field count per CSV
total rows across CSV members
bad-length rows
download-center row count match
date min/max for target date field
unique code count and out-of-filter code count if code filter was used
important categorical distributions, e.g. StatPd
```

若上传了代码文件，QC 要比较：

```text
uploaded code count
codes with rows
codes without rows
codes outside uploaded set
```

代码无记录不自动视为下载失败；可能是该期间无观测、停牌/终止、表本身无对应记录或过滤口径导致。应在 QC 报告中列出数量和样例，交给下游研究口径判断。

## 已验证的低风险 smoke test

用于确认 RESSET 检索、验证码、提交任务、下载中心链路是否可用：

```text
数据库：RESSET 股票
表：资产负债表 / BS_ALL
日期：2023-12-31 到 2023-12-31
日期口径：截止日期
代码：不限
字段：CompanyCode, ComCd, LComNm, ReportType, EndDt
格式：csv
字段标题：Labels+Column
压缩：zip
```

实测结果：

```text
下载编号：RESSET 股票_资产负债表
下载中心状态：100%
大小：约 0.488 MB
数据量：11477 条
建议文件名：RESSET 股票_资产负债表.zip
```

## 常见坑

- Chrome plugin 不可用时，`playwright-mcp` 无法直接控制用户日常 Chrome 的现有标签；要在固定 profile 中打开同一 URL 并验证登录态。
- MCP 的 open tabs 摘要有时显示当前页仍是 CSMAR；不要依赖摘要，始终用 `page.context().pages().find(p => p.url().includes(...))` 选择 RESSET/下载中心页。
- 隐藏菜单链接不要强点。优先点 `main` frame 的可见常用表链接，或从 `menu` frame 抽取 href 后用站点自身导航函数。
- `dataSearch.jsp` 直接 `goto` 可能被 frameset 重置回首页；导航后重新获取 `main` frame 并用正文确认。
- 已有下载中心可读不等于新表页导航登录态可用。若 `main` frame 跳到 `四川大学统一身份认证`、`扫码登录`、`短信登录` 或 `账号登录`，先请用户恢复 WebVPN/RESSET 登录态，再继续 direct POST 或验证码流程。
- 下载前必须先点“数据预览”做 canary。若预览无反应或提示“系统异常”，不要继续验证码或下载；优先重建表页、改用真实菜单入口或用户当前可预览的 tab/frame，再重新填表。表单 DOM 值正确不等于服务器接受该表单状态。
- 直接 `frame.evaluate()` 改 `beginDate` / `endDate` / `cValue` 等关键输入，可能造成 RESSET 前端 hidden state 与 DOM value 不一致。优先使用 `locator.fill()`、真实 select/click 和真实菜单入口；若已经出现“系统异常”，不要在同一页面继续补救，先重开目标表页并重新填。
- 若已知 Green 参数和正确验证码仍提示 `创建下载失败，请重试！`，优先怀疑 WebVPN/RESSET frameset 会话状态脏了。不要在同一脏页面反复提交；让用户从四川大学 WebVPN 入口重新进入 RESSET，再重新打开目标表页和配置参数。实测 `FDSHRCHG` 的 `FdCd=000001`、`EndDt=2023-12-31` 在重新进入后可正常创建 3 行任务。
- 验证码默认使用 `$handle-interactive-verification` 的超级鹰方案做授权、低频、单次候选识别；失败后再由用户人工填写。不要批量调用、循环刷新或把验证码结果写入日志。
- 点击下载提交后只是在服务器创建任务；真正文件在“下载中心”的 `downloadTaskUser.action` iframe 中。
- 下载链接站内保留 48 小时，下载成功后尽快保存到本地项目目录或 `.playwright-mcp` 工作目录。
