---
name: csmar-download
description: 使用 Playwright MCP 在 CSMAR（国泰安）数据库中搜索、定位并下载数据表。适用于通过 WebVPN 访问 CSMAR 网页端，自动完成数据表查找、参数配置（时间区间/代码/字段/格式）和文件下载的场景。
---

# CSMAR 数据下载（Playwright MCP）

## 技能工程与来源追溯

本技能的稳定执行规则写在 `SKILL.md`。真实项目反哺、字段验证批次和迁移状态记录在：

```text
references/source-provenance.md
```

## 前置条件

1. 用户已通过 WebVPN（如江南书苑）登录 CSMAR，浏览器中可见 CSMAR 主页面
2. Playwright MCP 已连接
3. CSMAR 主页面嵌套在 WebVPN 的 iframe 中，所有页面操作先获取 iframe 上下文

若通过 `playwright-mcp` skill 的 `mcporter` 调用 Playwright MCP，先做运行环境确认：

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

如果看到 `mcp-chrome-*` 分叉目录，先确认当前运行的 Chrome 进程是否仍使用固定目录：

```bash
ps auxww | rg -i 'playwright|mcp-chrome|Google Chrome' | rg -v 'rg -i'
```

只要当前进程参数含 `--user-data-dir=/Users/narra/Library/Caches/ms-playwright/mcp-chrome` 且带 `--remote-debugging-port=9222`，历史分叉目录可先视为残留，不要误判当前会话跑偏。

注意：`playwright-mcp` 固定 profile 不等于用户日常 Chrome 的现有标签页。若用户要求检查“当前 Chrome TAB”，优先用 Chrome plugin；若 Chrome extension 不可用，可改用 `playwright-mcp` 打开同一 WebVPN URL 并验证固定 profile 中的登录态。

## 核心操作模式

CSMAR 页面结构：WebVPN 外壳 -> iframe -> CSMAR 实际内容。始终通过以下方式获取操作上下文：

```js
const frame = page.locator('iframe').contentFrame();
```

在 WebVPN 场景下，实际可能是双层 iframe 或 iframe 重载。更稳的做法是从 `page.frames()` 中寻找包含 CSMAR 搜索框、目标表或下载按钮的 frame：

```js
async function getCsmarFrame(page) {
  for (const frame of page.frames()) {
    const hasSearch = await frame
      .locator('input[placeholder="请输入关键字"]')
      .count()
      .catch(() => 0);
    if (hasSearch > 0) return frame;

    const body = await frame.locator('body').innerText().catch(() => '');
    if (body.includes('下载数据') || body.includes('四川大学本部')) return frame;
  }
  throw new Error('CSMAR frame not found');
}
```

`mcporter` 代码执行建议使用 JSON 参数，避免 `function` 或长代码被 shell 解析打断：

```bash
mcporter call playwright.browser_run_code_unsafe --args '{"code":"async (page) => { return page.url(); }"}'
```

若使用 `filename` 载入长脚本，Playwright MCP 常见允许目录是：

```text
/Users/narra/.codex/.playwright-mcp
/Users/narra/.codex
```

## 工作流程

### Phase 0：入口与登录态烟测

打开 WebVPN CSMAR 入口后，先确认是否真的可用，而不是停在过期会话或空 iframe：

```js
const frame = await getCsmarFrame(page);
const body = await frame.locator('body').innerText();

const offline = body.includes('账号已下线') || body.includes('重新登录');
const hasOrg = body.includes('四川大学本部') || body.includes('CSMAR');
const hasSearch = await frame.locator('input[placeholder="请输入关键字"]').count();
```

若出现 `账号已下线，请重新登录` 或 `用户未对系统做任何操作超过40分钟，账号已自动登出` 弹窗，优先刷新页面（相当于 `Cmd+R` 或 CDP `Page.reload`）。实测 WebVPN 场景下刷新常能直接恢复 CSMAR 登录态，点击弹窗里的 `重新登录` 反而可能停在首页但未恢复完整操作状态。

```js
await page.reload({ waitUntil: 'domcontentloaded' }).catch(() => {});
await page.waitForTimeout(8000);
const frame = await getCsmarFrame(page);
```

若刷新后仍未恢复，再尝试点击 `重新登录` 并等待 iframe 重载：

```js
const relogin = frame.getByText('重新登录');
if (await relogin.count()) {
  await relogin.first().click();
  await page.waitForTimeout(8000);
}
```

恢复后重新获取 frame，不要沿用旧 frame 对象：

```js
const frame = await getCsmarFrame(page);
```

最低可用性判据：

- 页面正文包含机构名，例如 `四川大学本部1`
- 能定位到搜索框 `input[placeholder="请输入关键字"]`
- 轻量检索能返回 `表结果`

### Phase 1：搜索目标表

```js
const frame = await getCsmarFrame(page);
const searchBox = frame.locator('input[placeholder="请输入关键字"]');
await searchBox.click();
await searchBox.fill('关键词');
await searchBox.press('Enter');
await page.waitForTimeout(2000);

// 切换到"表结果"标签查看数据表列表
await frame.locator('text=表结果').first().click();
await page.waitForTimeout(1000);

// 获取搜索结果
const rows = await frame.locator('table tbody tr').allTextContents();
```

搜索关键词选择经验：

| 目标数据 | 推荐关键词 | 目标表名 | 物理表名 |
|---|---|---|---|
| 公司基本信息 | 上市公司基本信息 | 上市公司基本信息年度表 | - |
| 行业分类（含行业代码） | 行业分类 | 上市公司行业分类表（日度） | - |
| 资产负债表 | 资产负债表 | 资产负债表 | FS_Combas |
| 利润表 | 利润表 | 利润表 | FS_Comins |
| 现金流量表 | 现金流量表 | 现金流量表(直接法) | FS_Comscfd |
| 股利分配（每股） | 现金股利 | 股利分配 | FI_T11 |
| 现金分红总额 | 分红 | 分公司现金分红与盈利对比表 | - |
| 总市值 | 个股回报率 | 年个股回报率文件 | TRD_Year |
| 产权性质 | 产权性质 | 中国上市公司股权性质文件 | EN_EquityNatureAll |
| 日频个股回报率 | 日个股回报率文件 | 日个股回报率文件 | TRD_Dalyr |
| 日频市场基准 | 综合日市场回报率文件 | 综合日市场回报率文件 | TRD_Cndalym |

注意：
- 直接搜“总市值”通常找不到合适的表，改用“个股回报率”。
- 搜“行业分类”时区分“年度表”（仅含分类标准版本编码）和“行业分类表”（含具体行业代码如 C26/K70）。
- 搜索结果行通常需要点击目标表名列中的 `span.link`，而不是整行。经验代码：`await frame.locator('table tbody tr').first().locator('span.link').nth(1).click()`。
- 若已知 `databaseId/tbId`，可直接导航 iframe 的 `src`，比重复搜索更稳。例如季度财务报表常见为 `databaseId=37&tbId=224/225/226`。

### Phase 2：进入目标表

```js
await frame.locator('table tbody tr').first().locator('span.link').nth(1).click();
await page.waitForTimeout(2000);
```

进入后先做权限确认：

```js
const tableBody = await frame.locator('body').innerText();
if (tableBody.includes('无权限')) throw new Error('CSMAR table has no permission');
if (!tableBody.includes('已购买')) {
  console.warn('未看到已购买字样，继续前建议人工核验权限状态');
}
```

实测资产负债表入口：

```text
databaseId=37&tbId=224
物理表名：FS_Combas
页面提示：资产负债表 — 资产负债表已购买
```

### Phase 3：配置下载参数

按顺序执行：时间区间 -> 代码选择 -> 字段选择 -> 输出格式。

代码选择优先级：

1. **全代码下载，本地筛选**：适合权限足、后续复用价值高、或者代码导入不稳定的任务。选择 `全部代码` 后下载原始全量数据，再用本地样本池按 `Stkcd` 筛选。
2. **代码导入**：适合数据体量过大、全代码不可接受时。CSMAR 模板要求 TXT/XLS/XLSX，TXT 口径为**纯代码列表、无表头、每行一个证券代码**，例如：

```text
000002
000003
000011
```

如果上传 CSV 且带表头，常见报错是 `文件格式不正确`。可先点 `模板下载` 获取 `代码模版.zip`，其中包含 `Codetemplate.txt/xls/xlsx/readme.txt`。

```js
// 1. 设置起始日期
const startInput = frame.locator('input[placeholder="请选择"]').first();
await startInput.click({ clickCount: 3 });
await startInput.fill('2010-12-31');
await startInput.press('Enter');
await page.waitForTimeout(500);

// 2. 设置结束日期
const endInput = frame.locator('input[placeholder="请选择"]').nth(1);
await endInput.click({ clickCount: 3 });
await endInput.fill('2023-12-31');
await endInput.press('Enter');
await page.waitForTimeout(500);

// 3. 选择"常用代码"（默认全部 A 股约 5800+）
await frame.getByRole('radio', { name: '常用代码' }).click();
await page.waitForTimeout(500);

// 或选择"全部代码"，适合先下载全量后本地筛选
await frame.getByRole('radio', { name: '全部代码' }).click();
await page.waitForTimeout(500);

// 4. 字段全选
await frame.locator('text=全选').first().click();
await page.waitForTimeout(500);

// 5. 选择 CSV 格式
await frame.getByRole('radio', { name: 'CSV格式（*.csv）' }).click();
await page.waitForTimeout(500);
```

### Phase 4：发起下载

```js
await frame.getByRole('button', { name: '下载数据' }).click();
await page.waitForTimeout(3000);
```

点击后 CSMAR 会打开一个新标签页显示下载确认页面。

注意：部分环境中 Playwright 当前页会自动变成下载确认页，新标签页顺序不稳定。稳妥做法是点击后检查 `page.context().pages()`，并用当前页和其他页的 URL/body 判断哪个是 `sdownload.html`。

### Phase 5：在新标签页保存文件

```js
// 切换到最新的标签页（下载确认页）
const tabs = await page.context().pages();
// 或使用 mcp_playwright_browser_tabs 切换到最后一个 tab

// 等待下载链接出现（链接文本格式为"表名+数字"）
await page.waitForTimeout(3000);
const allLinks = await page.locator('a').allTextContents();
// 找到类似 "资产负债表141806298" 的链接

// 下载并保存
const downloadPromise = page.waitForEvent('download', { timeout: 120000 });
await page.locator('a').filter({ hasText: '表名关键词' }).click();
const download = await downloadPromise;
await download.saveAs('/目标路径/文件名.zip');
```

关键：下载确认页中的链接文本不是纯表名，而是“表名 + 数字 ID”（例如 `资产负债表141806298`），`filter({ hasText: })` 匹配表名前缀即可。

稳妥定位下载确认页：

```js
const pages = page.context().pages();
const downloadPage =
  pages.find(p => p.url().includes('sdownload')) ||
  pages[pages.length - 1];

await downloadPage.waitForTimeout(3000);
const links = await downloadPage.locator('a').allTextContents();
```

如果 `browser_tabs select` 对当前 `mcporter` 会话返回假性错误，可直接用 Playwright 页面对象切换或关闭：

```js
const main = page.context().pages()
  .find(p => p.url().includes('csmar/data/yitlink') && !p.url().includes('sdownload'));
if (main) await main.bringToFront();

for (const p of page.context().pages().filter(p => p.url().includes('sdownload'))) {
  await p.close().catch(() => {});
}
```

补充：
- `download.saveAs()` 在包含中文、空格、括号的长路径上偶尔会报 `ENOENT`，但 MCP 通常已经把文件保存到默认目录。
- 默认下载目录常见为 `/Users/narra/.codex/.playwright-mcp/`，文件名会将括号替换为连字符，例如 `资产负债表211708672-仅供哈佛大学使用-.zip`。
- 若 `saveAs` 失败，先检查默认下载目录，再 `cp` 到项目目录。

### Phase 5.5：验证批次与字典样本模式

当 CSMAR 不是主数据源，而是用于校验、备源或字段 crosswalk 时，不必一开始追求所有大表全量下载。推荐使用 validation batch：

```text
small/master table: full download + DES dictionary
large/panel table: clearly bounded sample window + DES dictionary
raw zip: source of truth
parsed CSV/Parquet: derived artifact
```

执行要点：

- 每个验证批次都保存原始 zip，不只保存解压后的 CSV。
- 优先保留 CSMAR 自带 `[DES][csv].txt` 或数据字典文件；字段含义不只靠页面截图或人工记忆。
- 小型 master、manager、subject 表可尝试全字段全量；大型月度、日度、持有人或交易类表先用研究相关窗口做 sample，等变量口径确认后再扩全量。
- 下载后立即写批次台账，至少记录：

```text
source_database
source_table
download_batch_id
download_time
query_range
code_filter
field_list
zip_path
zip_members
encoding
row_count
download_page_record
status
notes
```

- 做 zip QC 时不要只看文件存在。至少检查 zip member、CSV header、编码、行数、字段数、日期范围和关键字段非空率。
- 若普通 CSV parser 出现 bad-length rows，先判断是否来自长文本字段中的换行或引号。此类问题不等于下载失败；在 QC 报告里标记为 parser limitation，并把 raw zip 和 DES 字典保留为 source of truth。
- 验证批次的完成状态通常是 `structural-green / forward-test-pending`：它证明当前项目可用于 cross-check，不等于所有表、所有年份、所有字段都已全量 validated。

### Phase 6：返回主页面继续下一个表

```js
// 切回 CSMAR 主搜索页面的标签
// mcp_playwright_browser_tabs select index=1（通常是主页面）
```

## 常见陷阱与解决方案

### 1. iframe 上下文丢失

CSMAR 所有内容在 iframe 内。如果直接用 `page.locator()` 或 snapshot 中的 ref 操作，常见结果是找不到元素。

解决：始终先用 `page.locator('iframe').contentFrame()` 获取 frame 并在 frame 上操作。复杂操作优先 `mcp_playwright_browser_run_code`。

### 2. 大文件下载导致 MCP 断连

财务报表类数据（资产负债表、利润表）压缩后可达 50-140MB，下载耗时较长，可能导致 Playwright MCP 连接超时断开（`Connection closed`）。

解决：
- 为 `waitForEvent('download')` 设置较长 timeout（至少 120000ms）。
- 断连后重连，原浏览器标签页通常仍保留，可直接在下载确认页继续。
- 若下载确认页仍在，无需重新配置参数。

### 3. 搜索结果中表名相似难以区分

例如搜“行业分类”会出现“行业分类年度表”和“行业分类表”，前者只有分类标准版本编码，后者才有具体行业代码。

解决：进入表后检查字段列表是否包含目标字段：

```js
const fields = await frame.locator('[class*="field"] div[class*="item"]').allTextContents();
```

### 4. 下载确认页链接获取时机

新标签页打开后，下载链接可能需要几秒才渲染完成。直接用 snapshot 有时看不到链接。

解决：用 `run_code` 配合 `waitForTimeout(3000)` 后再通过 `page.locator('a').allTextContents()` 获取全部链接文本并筛选。

### 5. "全选"按钮定位

字段区域的“全选”在不同表中位置可能不同。`frame.locator('text=全选').first()` 通常命中字段全选；若页面存在多个“全选”（例如代码区也有），根据上下文调整定位。

### 6. 页面浮层遮挡与常规 click 失效

CSMAR 页面右侧服务栏、最近搜索浮层、消息框可能拦截 Playwright 常规点击，报错类似 `intercepts pointer events`。

解决：

```js
await frame.evaluate(() => {
  document.querySelectorAll('.full-screen-model, .fixed-service')
    .forEach(el => el.style.display = 'none');
  document.querySelectorAll('.el-message-box__wrapper .el-button--primary, .el-message-box__wrapper .el-message-box__close')
    .forEach(el => el.click());
  document.querySelectorAll('.el-dialog__wrapper .el-dialog__headerbtn')
    .forEach(el => el.click());
});
```

若仍被遮挡，可改用 DOM 直点：

```js
const domClickByText = async (selector, text) => frame.evaluate(({ selector, text }) => {
  const els = [...document.querySelectorAll(selector)];
  const el = els.find(x => (x.innerText || '').trim().includes(text));
  if (el) { el.click(); return true; }
  return false;
}, { selector, text });
```

字段精确选择可用：

```js
const domClickExactField = async (text) => frame.evaluate((text) => {
  const items = [...document.querySelectorAll('.set-body-inner-item')];
  const item = items.find(el => (el.innerText || '').trim() === text);
  if (item) { item.click(); return true; }
  return false;
}, text);
```

### 7. 权限与数据库入口切换

CSMAR 镜像/入口不同，权限可能不同。实践中同一任务在一个入口显示 `无权限`，切换到另一个入口后显示 `已购买`。

建议：
- 先读取页面正文，确认目标表是否出现 `已购买` 或 `无权限`。
- 记录当前域名和学校/机构名，避免后续复现时混用。
- 若用户切换数据库，不要沿用旧页面状态，先重新验证关键表权限。

### 8. 日频数据的 5 年限制与站内打包

`日个股回报率文件` 页面明确提示：`每次最多查询下载 5 年内数据`。长区间需要拆段。

实践经验：
- `2018-01-01` 至 `2022-12-31` 全代码关键字段约 500 万条，压缩包约 133MB，站内打包约数分钟。
- `2023-01-01` 至最新全代码关键字段约 428 万条，压缩包约 116MB。
- 站内显示 `正在生成数据压缩包` 时不要重复点击下载，等待链接出现后再点最终下载。

等待下载链接模板：

```js
const start = Date.now();
while (Date.now() - start < 360000) {
  const links = await page.locator('a').allTextContents();
  const hit = links.find(t => t.includes('日个股回报率文件'));
  if (hit) break;
  await page.waitForTimeout(10000);
}
```

### 9. 字段少选优先于全字段

全字段下载虽然省事，但日频大表很容易导致打包慢、下载慢、后续清洗慢。若研究变量明确，优先保留最小必要字段。

示例：DID/CAR 日频个股常用字段：

- `Stkcd`
- `Trddt`
- `Clsprc`
- `Dsmvosd`
- `Dsmvtll`
- `Dretwd`
- `Dretnd`
- 可比收盘价
- `Markettype`
- `Trdsta`

季度 DID 常用字段：

- `FS_Combas`：`A001000000`、`A002000000`、`A002101000`、`A002201000`、`A001110000`、`A001111000`、`A001123000`、`A001101000`、`A003000000`
- `FS_Comins`：`B001101000`、`B002000000`、`B001300000`、`B001212000`、`B001302000`
- `FS_Comscfd`：`C001000000`

### 10. 低风险下载烟测

正式批量下载前，可用资产负债表做小样本烟测，验证“检索 -> 进入表 -> 配置 -> 生成下载页 -> 实际下载”全链路：

- 表：`资产负债表` / `FS_Combas` / `databaseId=37&tbId=224`
- 时间：`2023-12-31` 至 `2023-12-31`
- 代码：`常用代码`
- 字段：默认已选 4 个字段即可，不必全选
- 格式：`CSV格式（*.csv）`

成功标志：

- 下载确认页 URL 包含 `sdownload.html`
- 页面显示 `下载表名 资产负债表`
- 页面显示类似 `资产负债表155843919.zip`
- 链接文本为 `资产负债表 + 数字 ID`
- zip 内含 `FS_Combas.csv` 与 `FS_Combas[DES][csv].txt`

实测样例：`2023-12-31` 单期、常用代码、默认 4 字段生成约 276KB zip，共约 10640 条记录。不同日期和账号权限下编号会变化，以页面显示为准。

## 批量下载模板

将 Phase 1-6 封装为可复用函数：

```js
async (page) => {
  const frame = await getCsmarFrame(page);

  // 搜索
  const searchBox = frame.locator('input[placeholder="请输入关键字"]');
  await searchBox.click();
  await searchBox.fill('${keyword}');
  await searchBox.press('Enter');
  await page.waitForTimeout(2000);
  await frame.locator('text=表结果').first().click();
  await page.waitForTimeout(1000);

  // 进入目标表
  await frame.locator('td').filter({ hasText: '${tableName}' }).first().click();
  await page.waitForTimeout(2000);

  // 配置参数
  const startInput = frame.locator('input[placeholder="请选择"]').first();
  await startInput.click({ clickCount: 3 });
  await startInput.fill('${startDate}');
  await startInput.press('Enter');
  await page.waitForTimeout(500);

  const endInput = frame.locator('input[placeholder="请选择"]').nth(1);
  await endInput.click({ clickCount: 3 });
  await endInput.fill('${endDate}');
  await endInput.press('Enter');
  await page.waitForTimeout(500);

  await frame.getByRole('radio', { name: '常用代码' }).click();
  await page.waitForTimeout(500);
  await frame.locator('text=全选').first().click();
  await page.waitForTimeout(500);
  await frame.getByRole('radio', { name: 'CSV格式（*.csv）' }).click();
  await page.waitForTimeout(500);

  // 发起下载
  await frame.getByRole('button', { name: '下载数据' }).click();
  await page.waitForTimeout(3000);
};
```

在新标签页保存文件：

```js
async (page) => {
  await page.waitForTimeout(3000);
  const downloadPromise = page.waitForEvent('download', { timeout: 120000 });
  await page.locator('a').filter({ hasText: '${tableNamePrefix}' }).click();
  const download = await downloadPromise;
  await download.saveAs('${savePath}');
};
```
