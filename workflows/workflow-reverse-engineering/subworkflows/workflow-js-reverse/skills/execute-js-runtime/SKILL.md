---
name: execute-js-runtime
description: 在经过授权的 JS 逆向任务中选择和验证 JavaScript 执行位点。用于判断代码应在 Node CLI、Python subprocess 调 Node、Python execjs 同步调用、Express/HTTP wrapper、浏览器 Playwright runtime 中执行；适合纯 JS 算法、Promise 异步结果桥接、Python 主流程复用 JS、以及需要 window/document/cookie/XHR/page lifecycle 的浏览器逻辑。当前已由图灵 JS TASK04 的 Node/Python/Browser runtime baseline 与 TASK08 的 execjs/subprocess/express 桥接样本验证；webpack、wasm、复杂补环境仍需各自专项 Skill 继续处理。
---

# Execute JS Runtime

## 适用场景

先由父级 `reverse-workflow-orchestrator` 定义目标、授权边界、证据台账和 Green，再使用本 Skill 选择 JS 执行位点。

使用本 Skill：

- 需要把 JS 算法从页面或 bundle 中抽出来运行；
- 需要在 Python 主流程里复用 JS 函数；
- 需要验证 Promise/async 结果是否能稳定返回；
- 不确定代码应该放在 Node、execjs、Python subprocess、Browser 还是 HTTP wrapper 中。

不直接处理：

- webpack 模块恢复；
- wasm imports/exports 和内存交互；
- 复杂浏览器补环境；
- 反调试 hook。此类任务先路由到对应专项 Skill 或 reference。

## 路线选择

### Node CLI

选 Node 当：

- 代码是纯函数或算法；
- 不依赖 `window`、`document`、`navigator`、`cookie`、XHR/fetch 生命周期；
- 目标是快速验证摘要、加密、编码、参数拼接。

完成标准：

- 输出 JSON；
- 同步结果和 Promise 结果都显式返回；
- 错误走 stderr 或非零退出码。

### Python subprocess -> Node

选 Python subprocess 当：

- Python 是主控流程；
- 只需要短生命周期调用 JS；
- 暂不需要长驻 Node 服务或浏览器上下文。

完成标准：

- Node 只向 stdout 打印一份 JSON；
- Python 解析 JSON 后再进入后续请求或测试；
- 记录 Node 代码路径、输入参数和 stdout 证据。

### Python execjs

选 `execjs` 当：

- JS 函数是同步函数；
- Python 主流程只需要短小计算结果；
- 不涉及 Promise、setTimeout、网络请求或浏览器对象。

完成标准：

- 确认 runtime 是 Node.js(V8)；
- 用 `ctx.call(...)` 或 `ctx.eval(...)` 返回同步值；
- Promise 任务不要强塞给 `execjs`，改走 subprocess 或 HTTP wrapper。
- 如果 JS 内部有 `require("./module.js")`，先切换 Python 进程 cwd 到 JS 文件目录，或改写为绝对 require；否则 `execjs` 会按调用进程目录解析相对模块。

### Express / HTTP Wrapper

选 Express wrapper 当：

- JS 任务是 Promise/async；
- Python 或其他调用方需要稳定 HTTP 接口；
- 同一个 JS 逻辑会被多次调用，长驻服务比反复启动 Node 更合适。

完成标准：

- wrapper 返回 JSON；
- 端口、输入参数和生命周期可控；
- 本地课程服务不得误当生产服务暴露。

### Browser Runtime

选 Browser 当：

- 代码依赖 `window`、`document`、DOM、cookie、XHR/fetch、localStorage、页面脚本加载顺序；
- 需要用 Playwright `page.evaluate`、`addInitScript` 或页面事件观测；
- 需要保留页面生命周期才能得到正确结果。

完成标准：

- 页面状态和 JS 返回值都进入 TASK 输出；
- 明确哪些浏览器对象被使用；
- 如果只是为了绕过缺失环境，要记录补环境项，不把它混成算法本身。

## Promise 纪律

- Node 顶层用 async IIFE 包住并 `await`；
- Browser 用 `page.evaluate(async () => ...)`；
- Python subprocess 只读取已完成后的 stdout JSON；
- `execjs` 只用于同步函数；
- Express wrapper 用 HTTP JSON 承接 Promise 结果；
- 不把 pending Promise、console 日志或页面肉眼状态当作 Green。

## 证据输出

每个 runtime baseline 至少输出：

```json
{
  "runtime": "node | node-via-python | browser",
  "syncResult": "...",
  "promiseResult": "...",
  "usedBrowserObjects": ["window", "document"]
}
```

参考模板：

- `../../templates/node-runtime-baseline/run.js`

## 当前状态

```text
structural-green / runtime-baseline-forward-test-green
```

已由 TASK04 验证：

- Node CLI 同步与 Promise 结果；
- Python subprocess 调 Node 并解析 JSON；
- Playwright Browser runtime 访问 `window/document` 并返回 Promise 结果。

已由 TASK08 验证：

- Python `execjs` 同步调用；
- Python subprocess 调 Node 执行带参 Promise；
- Express wrapper 返回 Promise 结果。
