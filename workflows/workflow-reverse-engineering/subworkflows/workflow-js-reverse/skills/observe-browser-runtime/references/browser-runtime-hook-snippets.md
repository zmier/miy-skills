# Browser Runtime Hook Snippets

此文件记录 `observe-browser-runtime` 已验证和候选的浏览器运行时 hook 模式。

## 已验证：setInterval(functionRef)

证据：

```text
图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK01-Day05HookForwardTest
```

最小模式：

```js
await page.addInitScript(() => {
  window.__hookEvents = [];
  const originalSetInterval = window.setInterval;
  window.setInterval = function hookedSetInterval(callback, delay, ...args) {
    window.__hookEvents.push({
      type: "setInterval",
      callbackName: callback && callback.name ? callback.name : "<anonymous>",
      delay,
      suppressed: true,
    });
    return 0;
  };
});
```

适用：

- 定时器反调试；
- 需要证明某个函数被周期触发；
- 本地样本或可控页面。

风险：

- 抑制定时器可能改变业务逻辑；
- 只适合最小实验，不应长期保留。

## 已验证：Function("debugger;")

证据：

```text
图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK02-Day05FunctionDebuggerHook
```

最小模式：

```js
await page.addInitScript(() => {
  window.__functionHookEvents = [];
  const RawFunction = window.Function;
  function stripDebugger(code) {
    return String(code).replace(/\bdebugger\b\s*;?/g, "void 0;");
  }
  function HookedFunction(...args) {
    const index = args.length - 1;
    if (index >= 0) {
      const before = String(args[index] || "");
      const after = stripDebugger(before);
      if (before !== after) {
        window.__functionHookEvents.push({ type: "Function", before, after, replaced: true });
        args[index] = after;
      }
    }
    return RawFunction.apply(this, args);
  }
  HookedFunction.prototype = RawFunction.prototype;
  HookedFunction.toString = RawFunction.toString.bind(RawFunction);
  window.Function = HookedFunction;
  window.Function.prototype.constructor = HookedFunction;
});
```

适用：

- `Function("debugger")`;
- 通过构造器动态生成代码；
- 需要记录 before/after。

风险：

- 改写全局 `Function` 可能影响页面框架；
- 复杂场景要提供 restore 或缩小注入窗口。

## 已验证：XMLHttpRequest open/send

证据：

```text
图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK03-Day05XHRHookForwardTest
```

最小模式：

```js
await page.addInitScript(() => {
  window.__xhrHookEvents = [];
  const rawOpen = XMLHttpRequest.prototype.open;
  const rawSend = XMLHttpRequest.prototype.send;

  XMLHttpRequest.prototype.open = function hookedOpen(method, url, ...rest) {
    this.__hookRecord = {
      type: "XMLHttpRequest",
      method,
      url: String(url),
      matchedLoginPost: String(url).includes("LoginPost"),
    };
    window.__xhrHookEvents.push({ phase: "open", ...this.__hookRecord });
    return rawOpen.call(this, method, url, ...rest);
  };

  XMLHttpRequest.prototype.send = function hookedSend(body) {
    window.__xhrHookEvents.push({
      phase: "send",
      ...(this.__hookRecord || { type: "XMLHttpRequest" }),
      body: body == null ? null : String(body),
    });
    return rawSend.call(this, body);
  };
});
```

适用：

- 需要定位 XHR 的 method/url/body；
- 需要用运行时证据确认目标接口；
- 需要在不依赖真实服务端的情况下做本地 fixture UAT。

风险：

- 只覆盖 XHR，不覆盖 fetch/WebSocket；
- body 可能是 FormData、Blob、ArrayBuffer，需要后续按类型扩展。

## 候选：eval / string timer / fetch / cookie

这些模式尚未在本 workflow 中 forward-test。

处理原则：

- 可以在 TASK 中探索；
- 不应写成已验证能力；
- 一旦通过新 TASK，补充证据、UAT 和适用边界。
