---
name: observe-browser-runtime
description: 在经过授权的 JS/browser 逆向任务中，基于父级 evidence ledger 对浏览器运行时行为做最小观测和可恢复 hook。用于 setInterval/setTimeout 注册观测、Function/eval 动态代码构造观测、XMLHttpRequest open/send 请求观测、axios request/response interceptor 观测、Object.defineProperty 属性读写观测、document.cookie get/set 观测、JSON.parse 入参观测、anti-debugger 初步定位、console trace、Playwright addInitScript 预注入和本地样本 forward-test。当前已由图灵 JS 的 setInterval debugger、Function(\"debugger\")、XHR LoginPost、property/cookie/JSON.parse、axios 巨潮接口样本验证；fetch/webpack/wasm 仍是候选能力，不得宣称已验证。
---

# Observe Browser Runtime

## 适用场景

使用本 Skill 前，先由父级 `reverse-workflow-orchestrator` 完成目标、授权边界、Green 和 evidence ledger。

适用：

- 浏览器页面或本地 HTML/JS 样本；
- 需要观测定时器注册、动态代码构造、XHR 请求、属性读写、cookie 读写、JSON.parse 或 anti-debugger 触发点；
- 静态分析已经看到 `debugger`、`setInterval`、`Function`、`eval`、`XMLHttpRequest`、`axios.interceptors`、`document.cookie`、`JSON.parse` 等候选；
- 需要用 Playwright `addInitScript` 在页面脚本执行前注入最小 hook。

不适用：

- Node-only 代码；
- wasm 主体分析；
- webpack 模块图恢复；
- fetch 等尚未在本 workflow forward-test 的场景，除非只作为探索性候选。

## 流程

1. 静态读取样本，确认候选触发点：
   - `debugger`;
   - `setInterval` / `setTimeout`;
   - `Function(...)`;
   - `eval(...)`;
   - `XMLHttpRequest.prototype.open/send`;
   - `axios.interceptors.request/response`;
   - `Object.defineProperty`;
   - `document.cookie`;
   - `JSON.parse`.
2. 建立最小运行时观测：
   - 优先用 Playwright `addInitScript` 预注入；
   - 只 hook 一个全局函数；
   - 记录 before/after、callbackName、delay、是否替换、页面状态。
3. 验证 Green：
   - 目标 hook 事件被捕获；
   - 页面或目标输出仍处于预期状态；
   - 输出 JSON 进入 TASK `outputs/`；
   - UAT 能独立读取结果并断言。
4. 写回 evidence ledger：
   - 静态线索；
   - 动态观测；
   - 复现阶梯层级；
   - 剩余未覆盖风险。

## 已验证模式

### setInterval(functionRef)

已在图灵 JS TASK01 验证。

用途：

```text
页面注册 setInterval(debug_func, 1000)
→ 预注入 hook 拦截注册
→ 记录 callbackName 和 delay
→ 返回占位 timer id，避免持续 debugger
```

### Function("debugger;")

已在图灵 JS TASK02 验证。

用途：

```text
页面调用 Function("debugger;")
→ 预注入 hook 包装 window.Function
→ 将 debugger 替换为 void 0
→ 记录 before/after
```

### XMLHttpRequest open/send

已在图灵 JS TASK03 验证。

用途：

```text
页面发起 XHR
→ 预注入 hook 包装 XMLHttpRequest.prototype.open/send
→ 记录 method/url/matched rule/body
→ 用可控响应验证页面状态
```

### axios request/response interceptor

已在图灵 JS TASK07 验证。

用途：

```text
请求经过 axios 封装层
→ request interceptor 观察/修改 config、headers、method、url
→ response interceptor 观察 status/data，并确认返回形态是否被改为 response.data
→ 与 XHR/fetch 底层观测互补
```

注意：真实接口可作为 primary Green，但外部示例端点不可用时要记录服务状态，不要偷偷换成 mock。

### Object.defineProperty 属性 get/set

已在图灵 JS TASK06 验证。

用途：

```text
目标值藏在对象属性读写过程中
→ 对目标对象和属性安装 get/set
→ 记录 prop/value/phase
→ 回到调用栈或上下游字段继续追踪
```

### document.cookie get/set

已在图灵 JS TASK06 验证。

用途：

```text
怀疑 JS 写入 cookie
→ 包装 document.cookie getter/setter
→ 记录写入值和读取时机
→ 与 HTTP Set-Cookie 区分
```

注意：HttpOnly cookie 无法被 JS 层 `document.cookie` 观测，需要走网络响应头证据。

### JSON.parse

已在图灵 JS TASK06 验证。

用途：

```text
怀疑密文或字符串在 JSON.parse 前后变成对象
→ 包装 JSON.parse
→ 记录 input 和解析后 keys
→ 用于定位响应解密或配置下发入口
```

## 证据边界

当前状态：

```text
structural-green / partial-forward-test-green
```

不得声称：

- 已覆盖全部 anti-debugger；
- 已覆盖 fetch；
- 已覆盖 webpack、wasm 或复杂混淆；
- 已形成完整 JS reverse workflow。

## 参考

需要代码片段和证据来源时读取：

- `references/browser-runtime-hook-snippets.md`
- `../../references/course-provenance.md`
