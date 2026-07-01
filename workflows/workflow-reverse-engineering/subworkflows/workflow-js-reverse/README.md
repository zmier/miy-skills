---
date: 2026-06-18
type: subworkflow
status: minimal-structural-green / browser-runtime-hook-partial-green / js-request-replay-green / js-crypto-digest-green
---

# JS Reverse Workflow

这是 `workflow-reverse-engineering` 下的 JS 逆向子 workflow。

当前不是完整 JS 逆向体系，而是从图灵 JS forward-test 中长出来的最小骨架。

## 当前已验证能力

### JS Runtime Execution

承载 Skill：

```text
skills/execute-js-runtime/SKILL.md
```

已 forward-test 的场景：

- Node CLI 同步函数与 Promise 结果；
- Python subprocess 调 Node 并解析 stdout JSON；
- Playwright Browser runtime 访问 `window/document` 并返回 Promise 结果。
- Python `execjs` 同步调用；
- Express wrapper 返回 Promise 结果。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK04-Day01-03JSRuntimeBaseline
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK08-Day07PythonNodeBridge
```

### Browser Runtime Observation

承载 Skill：

```text
skills/observe-browser-runtime/SKILL.md
```

已 forward-test 的场景：

- `setInterval(functionRef, delay)` 注册层观测与拦截；
- `Function("debugger;")` 动态代码构造观测与替换。
- `XMLHttpRequest.prototype.open/send` 请求 method/url/body 观测。
- `axios.interceptors.request/response` 请求封装层观测。
- `Object.defineProperty` 属性 get/set 观测。
- `document.cookie` get/set 观测。
- `JSON.parse` 入参和结果 key 观测。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK01-Day05HookForwardTest
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK02-Day05FunctionDebuggerHook
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK03-Day05XHRHookForwardTest
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK06-Day05CookieAndDefinePropertyHook
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK07-Day06RequestInterceptorAndAxios
```

### Crypto Entry Location

承载 Skill：

```text
skills/find-crypto-entry/SKILL.md
```

已 forward-test 的场景：

- 从 JS/Python 样本中定位 RSA 登录密码加密入口；
- 提取 public exponent、modulus 等关键常量；
- 用本地 oracle 验证输出为目标形态。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK05-Day04BrowserDebugAndCryptoEntry
```

### JS Request Replay

承载 Skill：

```text
skills/replay-js-request/SKILL.md
```

已 forward-test 的场景：

- 从课程 JS 调用 `get_analysis(page)` 生成七麦 `analysis` 参数；
- 用 Python `execjs` 桥接 JS 算法；
- 按课程 Python 请求参数访问真实 `https://api.qimai.cn/rank/offline`；
- 分开记录算法构造、请求构造、HTTP 到达、JSON 返回四类 Green。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK09-Day08QimaiMinimalReplay
```

### JS Crypto Reproduction

承载 Skill：

```text
skills/reproduce-js-crypto/SKILL.md
```

已 forward-test 的场景：

- MD5、SHA1/SHA224/SHA256/SHA384/SHA512 的 JS/Python 输出一致性；
- HMAC-MD5/HMAC-SHA 系列的 JS/Python 输出一致性；
- myToken `code = MD5(timestamp + "9527" + timestamp.substr(0, 6))`；
- 动态 timestamp 同源约束；
- myToken 真实接口 JSON 返回。
- 宝钢 `Content-Md5 + canonical string + HmacSHA1` header signature；
- 宝钢真实内容列表接口 JSON 返回。
- DES-CBC-PKCS7 的 JS/Python parity 与解密回原文；
- 瑞数 Skill 包资产识别，但未 forward-test。
- 自然科学 DES-ECB-Base64 真实响应解密为 JSON；
- AES-CBC-PKCS7 的 JS/Python parity；
- 建筑市场 AES endpoint 403 红灯记录。
- RSA 公钥加密/私钥解密 roundtrip；
- 吉林产权魔改 encode/decode 与真实 endpoint 响应解密；
- JS 包导出形态差异红灯。
- 观鸟记录 RSA body + MD5 sign + AES response hybrid crypto；
- bootstrap session 后真实 endpoint replay；
- AI 辅助实现的证据边界。
- Promise/控制流 dispatcher 下的入口定位证据；
- 五矿集团 RSA 分块加密 param 与真实采购接口 replay。
- SM3/SM4 的 JS/Python parity；
- 行行查真实响应密文的 JS helper 与 Python gmssl 双路径解密一致性。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK10-Day09DigestAlgorithmBasics
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK11-Day10DigestRealCases
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK12-Day11DESAndRuishuAsset
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK13-Day12SymmetricCryptoCases
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK14-Day13AsymmetricAndModifiedAlgorithm
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK15-Day14LoginEncryptAndBirdReport
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK16-Day15AsyncStackAndMinmetals
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK19-Day18SMAndWebProtocolRecovery
```

### Webpack Runtime Entry Recovery

承载 Skill：

```text
skills/analyze-webpack-runtime/SKILL.md
```

已 forward-test 的场景：

- 识别 webpack loader；
- 把 loader 挂到全局；
- 打印模块调用日志；
- 通过 `window.loader(490)` 获取 36氪登录加密模块导出对象；
- 从导出对象中取 `JSEncrypt` 并执行 RSA 加密。
- 通过医保局 webpack 模块生成 `x-tif-*` 头与加密 body；
- 访问真实医保局 endpoint 并解密响应为业务 JSON。
- 通过凤凰云智 webpack 模块取 RSA 工具链并完成本地密文输出。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK17-Day16WebpackBasicAndCamoufoxAssetAudit
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK18-Day17WebpackRealProtocolReplay
```

### WASM Runtime Analysis

承载 Skill：

```text
skills/analyze-wasm-runtime/SKILL.md
```

已 forward-test 的场景：

- Node `WebAssembly.instantiate` 调用 `Wasm.wasm`；
- Python `pywasm.load` 调用同一导出函数；
- 同参同结果 parity；
- `encrypt.wasm` 输出接入码上爬真实接口参数。

证据来源：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow/tasks/TASK20-Day19WasmImportsExports
```

## 候选能力

以下能力只作为候选，尚未在本 workflow 中 forward-test：

- fetch / WebSocket hook；
- localStorage / sessionStorage 观测；
- vite / rollup bundle 识别；
- source map 与混淆还原；
- AST 分析与转换；
- JS sign 参数定位与复现；
- 更多真实站点 replay 与业务 oracle；
- 复杂 crypto 算法完整重写；
- DES/AES/RSA/SM 等后续算法族完整复现；
- CryptoJS / WebCrypto；
- 浏览器补环境；
- Node / JSDOM / Playwright / VM 隔离执行；
- anti-debugger、控制流平坦化、字符串数组混淆；
- 请求 replay 与 oracle 验证。

## 目录

```text
workflow-js-reverse/
├── README.md
├── SKILL.md
├── references/
│   ├── browser-runtime-hook-snippets.md
│   └── course-provenance.md
├── templates/
├── skills/
│   ├── execute-js-runtime/
│   ├── analyze-webpack-runtime/
│   ├── analyze-wasm-runtime/
│   ├── deobfuscate-js-control-flow/
│   ├── find-crypto-entry/
│   ├── replay-js-request/
│   ├── reproduce-js-crypto/
│   └── observe-browser-runtime/
└── tests/
```

## 使用原则

1. 先用父级 `reverse-workflow-orchestrator` 定义目标、证据台账、红灯和 Green。
2. 确认为 JS/browser runtime 后，再进入本子 workflow。
3. 先用 `execute-js-runtime` 判断代码应在 Node、Python subprocess 还是 Browser 运行。
4. 已验证能力可以直接用；候选能力必须在 TASK 中 forward-test 后再升级。
5. 不把 Android 的 Frida/JADX/Unidbg 工具链迁入 JS 默认流程。
6. 不把课程脚本原样写入通用 Skill；课程来源记录在 `references/course-provenance.md`。
