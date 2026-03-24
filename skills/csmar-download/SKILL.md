---
name: csmar-download
description: 使用 Playwright MCP 在 CSMAR（国泰安）数据库中搜索、定位并下载数据表。适用于通过 WebVPN 访问 CSMAR 网页端，自动完成数据表查找、参数配置（时间区间/代码/字段/格式）和文件下载的场景。
---

# CSMAR 数据下载（Playwright MCP）

## 前置条件

1. 用户已通过 WebVPN（如江南书苑）登录 CSMAR，浏览器中可见 CSMAR 主页面
2. Playwright MCP 已连接
3. CSMAR 主页面嵌套在 WebVPN 的 iframe 中，所有页面操作先获取 iframe 上下文

## 核心操作模式

CSMAR 页面结构：WebVPN 外壳 -> iframe -> CSMAR 实际内容。始终通过以下方式获取操作上下文：

```js
const frame = page.locator('iframe').contentFrame();
```

## 工作流程

### Phase 1：搜索目标表

```js
const frame = page.locator('iframe').contentFrame();
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

注意：
- 直接搜“总市值”通常找不到合适的表，改用“个股回报率”。
- 搜“行业分类”时区分“年度表”（仅含分类标准版本编码）和“行业分类表”（含具体行业代码如 C26/K70）。

### Phase 2：进入目标表

```js
await frame.locator('td').filter({ hasText: '目标表名关键词' }).first().click();
await page.waitForTimeout(2000);
```

### Phase 3：配置下载参数

按顺序执行：时间区间 -> 代码选择 -> 字段选择 -> 输出格式。

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

## 批量下载模板

将 Phase 1-6 封装为可复用函数：

```js
async (page) => {
  const frame = page.locator('iframe').contentFrame();

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
