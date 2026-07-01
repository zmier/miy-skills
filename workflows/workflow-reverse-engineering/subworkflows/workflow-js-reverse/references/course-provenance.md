# Course Provenance

## 图灵 JS 逆向 2622 期 Day05

来源项目：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/图灵JS/PROJECT-图灵JS课程反哺ReverseWorkflow
```

### TASK01-Day05HookForwardTest

- 课程材料：Day05-hook 技术 / `1.1.普通调试模式.html`
- 验证能力：`setInterval(functionRef, delay)` 注册层 hook
- 证据角色：primary forward-test
- 迁移状态：`partial-forward-test-green`
- 影响文件：
  - `skills/observe-browser-runtime/SKILL.md`
  - `skills/observe-browser-runtime/references/browser-runtime-hook-snippets.md`

### TASK02-Day05FunctionDebuggerHook

- 课程材料：Day05-hook 技术 / `1.3.构造器debugger.html`
- 验证能力：`Function("debugger;")` 动态代码构造 hook
- 证据角色：assisted-comparison forward-test
- 迁移状态：`partial-forward-test-green`
- 影响文件：
  - `skills/observe-browser-runtime/SKILL.md`
  - `skills/observe-browser-runtime/references/browser-runtime-hook-snippets.md`

### TASK03-Day05XHRHookForwardTest

- 课程材料：Day05-hook 技术 / `7.xhr-hook脚本.js`
- 验证能力：`XMLHttpRequest.prototype.open/send` 请求 method/url/body 观测
- 证据角色：assisted-comparison forward-test
- 迁移状态：`partial-forward-test-green`
- 影响文件：
  - `skills/observe-browser-runtime/SKILL.md`
  - `skills/observe-browser-runtime/references/browser-runtime-hook-snippets.md`

### TASK06-Day05CookieAndDefinePropertyHook

- 课程材料：Day05-hook 技术 / `4.defineProperty的简单使用.js` / `6.同花顺cookie-hook脚本.js` / `3.字符串转对象hook脚本.js`
- 验证能力：`Object.defineProperty` 属性 get/set、`document.cookie` get/set、`JSON.parse` 入参和 key 观测。
- 证据角色：property-cookie-parse forward-test。
- 迁移状态：`property-cookie-parse-forward-test-green`。
- 影响文件：
  - `skills/observe-browser-runtime/SKILL.md`
  - `README.md`
  - `SKILL.md`

## 清洗说明

- 未把教师脚本原样纳入 Skill 主流程；
- 只抽取可迁移的 hook 模式、证据要求和边界；
- 保留课程来源用于追溯；
- fetch/webpack/wasm 尚未 forward-test，不写入已验证能力。

## 图灵 JS 逆向 2622 期 Day20

### TASK21-Day20WasmBindgenEnvPatch

- 课程材料：Day20 AI 逆向 Wasm-2 / 荔枝网 wasm 逆向 / `wasm_signer.js` / `gdtv_sign.wasm`。
- 验证能力：wasm-bindgen/webpack wrapper 型 WASM signer、最小浏览器环境补齐、固定 Node runtime、荔枝网真实接口 replay。
- 证据角色：wasm-bindgen env patch real endpoint forward-test。
- 迁移状态：`wasm-bindgen-env-patch-real-endpoint-green`。
- 影响文件：
  - `skills/analyze-wasm-runtime/SKILL.md`
  - `SKILL.md`

### 清洗说明

- 未把荔枝网固定业务字段、设备 ID 或完整老师脚本写入通用 Skill；
- 只抽取“保留 wrapper、提取 wasm side asset、补 browser env、冻结 Node runtime、真实 endpoint oracle”的可迁移规则；
- 本机复现显示 `PATH` 中不同 Node 会导致 OOM、空 stdout 或成功输出，因此 Node 绝对路径需要进入证据台账。

## 图灵 JS 逆向 2622 期 Day21

### TASK22-Day21WechatMiniappReverse

- 课程材料：Day21 微信小程序 AI 逆向 / 百达屋 / `request_samples.json` / `main.py` / `wechat-miniapp-reverse` Skill。
- 验证能力：微信小程序 request sample 签名 parity、WMPF 运行时特征识别、百达屋真实接口 replay。
- 证据角色：wechat miniapp protocol forward-test。
- 迁移状态：`wechat-miniapp-protocol-forward-test-green`。
- 影响文件：
  - `skills/reverse-wechat-miniapp/SKILL.md`
  - `SKILL.md`

### 清洗说明

- 未把百达屋固定酒店数据、登录 token 或业务细节写入通用 Skill；
- 老师提供的 `wechat-miniapp-reverse` 和 WMPFDebugger 作为工具路线参考，不原样并入主流程；
- 只抽取“小程序独立分支、request sample parity、AppService/WebView/WMPF 证据、真实 endpoint oracle”的可迁移规则。

## 图灵 JS 逆向 2622 期 Day22

### TASK23-Day22ObfuscationAndQingchuang

- 课程材料：Day22 AI 逆向 JavaScript 混淆技术 1 / 青创网 / `main.js` / `main.py` / 逆向分析报告。
- 验证能力：混淆入口到协议闭环、bootstrap 材料提取、AES 请求包装、RSA-SHA1 签名、自定义签名变换、响应 `Result` 解密、真实接口 replay。
- 证据角色：obfuscation to protocol forward-test。
- 迁移状态：`obfuscation-to-protocol-forward-test-green`。
- 影响文件：
  - `skills/deobfuscate-js-control-flow/SKILL.md`
  - `skills/reproduce-js-crypto/SKILL.md`
  - `skills/replay-js-request/SKILL.md`
  - `SKILL.md`

### 清洗说明

- 未把青创网固定商品数据、当前 bootstrap 值或业务字段写入通用 Skill；
- 老师提供的 web-protocol-recovery 资产进入后续资产审计，不在本条直接全量迁入；
- 只抽取“混淆不是终点，必须闭环到 bootstrap/request envelope/response decrypt/business oracle”的可迁移规则。

## 图灵 JS 逆向 2622 期 Asset Audit

### TASK24-CourseProvidedSkillAssetAudit

- 课程材料：Day02/Day05/Day09/Day16/Day17/Day18/Day21/Day22 中散落的 Skills、MCP、脚手架和工具包。
- 验证能力：课程资产分类、路径存在性审计、adoption register。
- 证据角色：course asset governance forward-test。
- 迁移状态：`course-asset-register-green`。
- 影响文件：
  - `references/third-party-asset-adoption-register.md`
  - `SKILL.md`

### 清洗说明

- 未全量迁入任何老师大包；
- `web-protocol-recovery`、WMPFDebugger、Camoufox、CloakBrowser、ruishu-reverse 等保持 reference-only；
- `env-patch`、`browser-hook-snippets`、`wechat-miniapp-reverse` 只吸收已通过 TASK 验证的原则。

## 图灵 JS 逆向 2622 期 Regression

### TASK25-JSWorkflowRegressionAndTransfer

- 课程材料：TASK01-TASK24 输出、JS workflow、Skill 主体、provenance、asset register。
- 验证能力：课程反哺后的 workflow 回归、Skill 去个案污染、能力状态可追溯。
- 证据角色：workflow regression and transfer test。
- 迁移状态：`js-workflow-regression-green`。
- 影响文件：
  - `SKILL.md`
  - `skills/*/SKILL.md`
  - `references/course-provenance.md`
  - `references/third-party-asset-adoption-register.md`

### 清洗说明

- 通用 Skill 主体不写课程个案名；
- 课程个案证据留在 TASK、provenance、asset register；
- workflow 只保留路线、分支和 Green 状态。

## 图灵 JS 逆向 2622 期 Day01-Day03

### TASK04-Day01-03JSRuntimeBaseline

- 课程材料：Day01 JS 基础、Day02 JS 基础、Day03 浏览器调试技巧 1。
- 验证能力：Node CLI、Python subprocess 调 Node、Playwright Browser runtime 三种 JS 执行位点。
- 证据角色：runtime baseline forward-test。
- 迁移状态：`runtime-baseline-forward-test-green`。
- 影响文件：
  - `skills/execute-js-runtime/SKILL.md`
  - `skills/execute-js-runtime/references/runtime-selection.md`
  - `templates/node-runtime-baseline/run.js`

### 清洗说明

- 未把课程真实站点请求作为 Green；
- 只抽取 runtime selection、Promise await、JSON stdout 这些可迁移规则；
- 真实站点 replay 留给后续算法和协议恢复 TASK。

## 图灵 JS 逆向 2622 期 Day04

### TASK05-Day04BrowserDebugAndCryptoEntry

- 课程材料：Day04 浏览器调试技巧 2 / `dcn_rsa_try.js` / `dcn_rsa_try.py`。
- 验证能力：从 JS/Python 样本定位 RSA 加密入口、关键常量和本地 oracle。
- 证据角色：crypto-entry structural forward-test。
- 迁移状态：`crypto-entry-forward-test-green`。
- 影响文件：
  - `skills/find-crypto-entry/SKILL.md`
  - `skills/find-crypto-entry/references/entry-ledger-template.md`

### 清洗说明

- 未把 DCN 固定 modulus 或真实站点地址写入通用 Skill；
- 只抽取“目标字段 -> 候选词 -> 入口函数 -> 常量 -> oracle”的可迁移流程；
- 真实登录接口 replay 不作为本 TASK Green。

## 图灵 JS 逆向 2622 期 Day06

### TASK07-Day06RequestInterceptorAndAxios

- 课程材料：Day06 JS 调试技巧 1 / XHR、axios 拦截器、巨潮接口请求脚本。
- 验证能力：axios request/response interceptor、`URLSearchParams` 表单请求、真实巨潮接口返回字段观测。
- 证据角色：axios interceptor real endpoint forward-test。
- 迁移状态：`axios-interceptor-real-endpoint-green`。
- 影响文件：
  - `skills/observe-browser-runtime/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 未把巨潮固定业务数据写入通用 Skill；
- 只抽取 request wrapper/interceptor 的证据模式；
- `httpbin.org/get` 当前不可用，作为外部服务状态记录，不作为主 Green。

## 图灵 JS 逆向 2622 期 Day07

### TASK08-Day07PythonNodeBridge

- 课程材料：Day07 JS 调试技巧 2 / Python 执行 JS、Promise、Express 示例。
- 验证能力：`execjs` 同步调用、Python subprocess 执行 Promise、Express wrapper 返回 Promise 结果。
- 证据角色：python-node-bridge forward-test。
- 迁移状态：`python-node-bridge-forward-test-green`。
- 影响文件：
  - `skills/execute-js-runtime/SKILL.md`
  - `skills/execute-js-runtime/references/runtime-selection.md`

### 清洗说明

- 未把七麦真实业务参数作为本 TASK Green；
- 只抽取 Python/Node/Express 桥接方法；
- `express` 本地安装仅用于课程复现，不作为生产服务配置。

## 图灵 JS 逆向 2622 期 Day08

### TASK09-Day08QimaiMinimalReplay

- 课程材料：Day08 JS 调试技巧 3 / `1.七麦数据.js` / `3.七麦数据.py`。
- 验证能力：调用 JS `get_analysis(page)` 生成七麦 `analysis` 参数，并按课程请求访问真实七麦 `rank/offline` 接口。
- 证据角色：small protocol replay real endpoint forward-test。
- 迁移状态：`js-request-replay-forward-test-green`。
- 影响文件：
  - `skills/replay-js-request/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 未把七麦固定 cookies、业务响应数据或目标站业务规则写入通用 Skill；
- 只抽取“已定位 JS 参数算法 -> 桥接执行 -> 请求构造 -> 真实 endpoint oracle”的可迁移流程；
- 真实响应返回 `code=10000`、`msg=成功`，但该业务结果只保留在 TASK 输出中。

## 图灵 JS 逆向 2622 期 Day09

### TASK10-Day09DigestAlgorithmBasics

- 课程材料：Day09 摘要算法 1 / MD5、SHA、HMAC、myToken。
- 验证能力：MD5/SHA/HMAC 的 JS/Python parity，myToken `code/timestamp` 耦合，以及真实 myToken 接口请求。
- 证据角色：digest crypto reproduction and real endpoint forward-test。
- 迁移状态：`js-crypto-digest-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `skills/replay-js-request/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 未把 myToken 业务数据写入通用 Skill；
- 只抽取摘要算法 parity、字段形态、salt 拼接、timestamp 同源这类可迁移规则；
- `crypto-js` 已作为本项目本地依赖固定，不依赖用户目录上层 `node_modules`。

## 图灵 JS 逆向 2622 期 Day10

### TASK11-Day10DigestRealCases

- 课程材料：Day10 摘要算法 2 / 宝钢 `x-signature` / 企查查 dynamic header entry。
- 验证能力：宝钢 `Content-Md5`、canonical string、`HmacSHA1(...).toUpperCase()`、真实内容列表接口 replay。
- 证据角色：digest real-case request signature forward-test。
- 迁移状态：`js-request-signature-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `skills/replay-js-request/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 宝钢固定业务字段、响应正文只保留在 TASK 输出；
- 只抽取 canonical string、body serialization、header signature、real endpoint oracle 这些可迁移规则；
- 企查查当前作为候选入口报告保留：课程脚本完成 dynamic header key，value 分支未在本 TASK 作为 Green。

## 图灵 JS 逆向 2622 期 Day11

### TASK12-Day11DESAndRuishuAsset

- 课程材料：Day11 对称加密 1 / DES JS/Python 示例 / 瑞数最新 Skill 包。
- 验证能力：DES-CBC-PKCS7 在 JS `crypto-js` 与 Python `Crypto.Cipher.DES` 中输出一致，并可解密回原文。
- 证据角色：symmetric crypto parity forward-test。
- 迁移状态：`js-symmetric-des-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 老师 JS 样本演示 ECB，Python 样本演示 CBC；本 TASK 为 parity 明确统一成 CBC 合约。
- 瑞数 Skill 包只登记为 `asset-adoption-candidate`，不标记为已 forward-test。
- 不把瑞数大包原样搬入 JS workflow；后续需要单独走资产审计与专项 TASK。

## 图灵 JS 逆向 2622 期 Day12

### TASK13-Day12SymmetricCryptoCases

- 课程材料：Day12 对称加密 2 / 自然科学 DES 响应解密 / AES 基础 / 建筑市场 AES。
- 验证能力：自然科学接口真实返回 DES-ECB-Base64 密文，Python 解密为 JSON；AES-CBC-PKCS7 JS/Python parity。
- 证据角色：encrypted response decrypt forward-test。
- 迁移状态：`js-response-decrypt-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 自然科学接口真实返回 HTTP 200，解密 JSON 含 `code/data/message`，`data` 下含 `resultsData`。
- 建筑市场接口当前返回 HTTP 403，记录为 endpoint/anti-bot 红灯，不标记为 replay Green。
- AES 先作为 JS/Python parity fixture；真实建筑市场解密需后续处理 403 红灯。

## 图灵 JS 逆向 2622 期 Day13

### TASK14-Day13AsymmetricAndModifiedAlgorithm

- 课程材料：Day13 非对称加密 1 / RSA 基础 / 吉林产权魔改算法。
- 验证能力：RSA 公钥加密私钥解密 roundtrip；吉林产权自定义 encode/decode；真实接口请求与响应解密。
- 证据角色：asymmetric and modified algorithm forward-test。
- 迁移状态：`js-asymmetric-modified-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- `node-rsa` 当前包导出形态与课程脚本不同，需要兼容 `default` / named export；
- 吉林产权变量命名类似 `aes`，但实际为自定义算法，不能归为标准 AES；
- 真实响应解密后含 `results/token/reqDate/resDate`，业务细节只保留在 TASK 输出。

## 图灵 JS 逆向 2622 期 Day14

### TASK15-Day14LoginEncryptAndBirdReport

- 课程材料：Day14 非对称加密 2 / 登录 RSA / 观鸟记录 / AI 实现观鸟记录。
- 验证能力：登录 RSA 字段形态；观鸟记录 RSA 请求体、MD5 header 签名、AES 响应解密；bootstrap session 后真实接口 replay。
- 证据角色：hybrid request crypto and bootstrap session forward-test。
- 迁移状态：`js-hybrid-request-crypto-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `skills/replay-js-request/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 直接使用课程 JS 请求观鸟接口出现 read timeout；
- AI collector 先访问 visited/generate 获取 session/cookie 后真实请求成功；
- AI 代码只作为平行实现，证明来自真实 endpoint 与 UAT，不来自“AI 写了代码”本身。

## 图灵 JS 逆向 2622 期 Day15

### TASK16-Day15AsyncStackAndMinmetals

- 课程材料：Day15 非对称加密 3 / 异步栈 / 控制流 / 五矿集团。
- 验证能力：控制流与 Promise 异步栈作为入口定位证据；五矿集团公钥接口、MD5 sign、timeStamp、RSA 分块加密 param、真实采购接口 replay。
- 证据角色：async/control-flow entry location and RSA block replay forward-test。
- 迁移状态：`js-control-flow-minmetals-forward-test-green`。
- 影响文件：
  - `skills/deobfuscate-js-control-flow/SKILL.md`
  - `skills/reproduce-js-crypto/SKILL.md`
  - `skills/replay-js-request/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- AI 分析报告和 client 是平行实现；Green 来自真实五矿 endpoint 与 UAT；
- 控制流样例用于说明入口隐藏在 dispatcher/runtime wrapper 中，不等于完整 AST 反混淆；
- 五矿业务响应细节只保留在 TASK 输出。

## 图灵 JS 逆向 2622 期 Day16

### TASK17-Day16WebpackBasicAndCamoufoxAssetAudit

- 课程材料：Day16 webpack 打包方式 1 / webpack 基本结构 / webpack 逆向问题 / 36氪登录加密 / Camoufox 迁移包 / 医保局 webpack 资产。
- 验证能力：识别 webpack loader、挂全局、打印模块调用日志、通过 module id 获取 exports、调用 36氪 `window.loader(490).JSEncrypt` 输出 RSA 密文。
- 证据角色：webpack runtime entry recovery forward-test。
- 迁移状态：`webpack-loader-forward-test-green`。
- 影响文件：
  - `skills/analyze-webpack-runtime/SKILL.md`
  - `skills/analyze-webpack-runtime/references/webpack-entry-ledger-template.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- webpack 被沉淀为“入口路由层”，不直接等同算法层；
- 36氪固定公钥与业务手机号只保留在 TASK 输出，不写入通用 Skill；
- Camoufox 迁移包和医保局 webpack 只登记为候选资产/候选案例，不把未 forward-test 的内容标绿。

## 图灵 JS 逆向 2622 期 Day17

### TASK18-Day17WebpackRealProtocolReplay

- 课程材料：Day17 webpack 打包方式 2 / 医保局 / 凤凰云智。
- 验证能力：webpack 模块导出请求封装，生成医保局 `x-tif-*` 头与加密 body，真实请求 endpoint 并解密响应；凤凰云智 webpack RSA 工具链本地输出密文。
- 证据角色：webpack runtime + real protocol replay forward-test。
- 迁移状态：`webpack-real-protocol-forward-test-green`。
- 影响文件：
  - `skills/analyze-webpack-runtime/SKILL.md`
  - `skills/reproduce-js-crypto/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- 医保局是真实 endpoint replay Green：HTTP 200、响应解密、业务结构三者同时满足；
- 凤凰云智只作为本地 webpack/RSA 输出形态 Green，未标记真实接口 replay；
- 动态 headers 与 body 必须同源生成，不能把老师抓包中的固定 `x-tif-*` 头当成通用解法。

## 图灵 JS 逆向 2622 期 Day18

### TASK19-Day18SMAndWebProtocolRecovery

- 课程材料：Day18 SM 国密系列 / SM 基础 / 行行查 / `web-protocol-recovery` Skill 资产。
- 验证能力：SM3/SM4 JS/Python parity；行行查真实接口响应密文解密；JS webpack helper 与 Python gmssl 解密一致；协议恢复资产审计。
- 证据角色：SM crypto parity and encrypted response protocol recovery forward-test。
- 迁移状态：`sm-and-web-protocol-forward-test-green`。
- 影响文件：
  - `skills/reproduce-js-crypto/SKILL.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- `sm-crypto` 安装在项目本地 Node 依赖中，`gmssl` 安装在 `Writer/.venv`；
- 行行查只请求第一页做 UAT，避免大规模采集；
- `web-protocol-recovery` 只吸收纯协议交付、证据门禁、工具分层等原则，不把其 Camoufox/CloakBrowser 依赖原样写入当前 JS workflow 主线。

## 图灵 JS 逆向 2622 期 Day19

### TASK20-Day19WasmImportsExports

- 课程材料：Day19 AI 逆向 WASM 1 / WebAssembly 实例化 / imports 与 exports 分析 / 码上爬。
- 验证能力：Node `WebAssembly.instantiate` 调用 wasm exports；Python `pywasm` 调用同一 exports；固定输入同参同结果；`encrypt.wasm` 输出接入码上爬真实接口参数。
- 证据角色：wasm runtime and endpoint replay forward-test。
- 迁移状态：`wasm-import-export-forward-test-green`。
- 影响文件：
  - `skills/analyze-wasm-runtime/SKILL.md`
  - `skills/analyze-wasm-runtime/references/wasm-ledger-template.md`
  - `README.md`
  - `SKILL.md`

### 清洗说明

- `pywasm==1.0.8` 安装到 `Writer/.venv`；
- WASM 被定义为本地 helper/side asset，不是默认浏览器黑箱；
- 邯郸公示 AI 报告作为复杂网关协议资产登记，不作为 TASK20 WASM 基础 Green。
