# Browser Runtime Hook Snippets

详见：

```text
skills/observe-browser-runtime/references/browser-runtime-hook-snippets.md
```

本文件作为 workflow 级入口，方便从 JS 子 workflow 根目录发现该能力。

当前已验证：

- `setInterval(functionRef, delay)` 注册层观测；
- `Function("debugger;")` 动态构造层观测。
- `XMLHttpRequest.prototype.open/send` 请求 method/url/body 观测。

当前未验证：

- fetch；
- cookie/storage；
- webpack runtime；
- wasm；
- 复杂混淆。
