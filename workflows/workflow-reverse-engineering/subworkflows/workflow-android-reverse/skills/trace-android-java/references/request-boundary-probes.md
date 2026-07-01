# 请求边界运行时探针

用于已经确认 URL 或业务动作，但还不知道 OkHttp Header、Body、sign、data、Base64/加密路径在哪里构造的场景。

## 选择顺序

| 红灯 | 优先探针 | 说明 |
|---|---|---|
| 不知道 App 装了哪些网络拦截器 | `okhttp-interceptor-probe.js` | 先定位 Header/sign/重试/风控所在层 |
| 代理抓包不可见或证据不足，但怀疑使用 OkHttp | `assets/upstream-okhttplogger-frida/` | 原样纳入的完整 OkHttpLogger，上游支持 find/hold/history/resend |
| 字段先进入 `Map/TreeMap/HashMap` | `map-put-probe.js` | 过滤 `data/sign/token/body/params` 等 key，并打印栈 |
| 怀疑某层走 Base64 或编码封装 | `base64-probe.js` | 只证明编码边界，不证明加密算法完整 |
| `sign/token/密文` 算法入口未知，疑似 Java 标准 Crypto API | `frida-crypto-probe.js` | Hook MessageDigest/Mac/Cipher/Key/IV 等固定 API，输出候选 JSONL fixture |
| 只知道调用者，不知道数据 | 调用栈 + 参数 Hook | 栈证明控制流，参数证明数据流 |

## 使用规则

1. 模板必须复制到 TASK 目录，不在 skill assets 中直接改。
2. 每次只回答一个问题：有哪些拦截器、OkHttp 请求/响应是什么、哪个 key 被写入、Base64 输入输出是什么。
3. 默认只打印摘要、长度、hex/base64 片段和调用栈，避免泄露完整 Token/Cookie。
4. 观察到运行时值只能标 `observed`；能稳定重复取值才标 `hook-available`。
5. 如果 Hook 点过宽导致噪声，先用 host/path、key 白名单或调用栈中的包名前缀过滤。
6. 原样调用旧实现并返回旧结果，不改变 App 行为。
7. 使用 upstream OkHttpLogger 的 `history()` 或 `resend(index)` 前，必须在 TASK 中声明实验目的、授权边界和可能副作用。

## 交接

- 发现拦截器类名：回到 JADX/静态链，查 Header/sign 添加逻辑。
- 发现 OkHttp request/response：脱敏后写入候选矩阵；若要重放，先走 `analyze-android-traffic` 的低频单变量实验规则。
- 发现 Map key：把 key 作为请求树叶子追加到 `request-construction-ledger.md`。
- 发现 Base64 输入输出：转 `reproduce-android-crypto` 建立 Unit fixture。
- 发现 crypto-probe 候选事件：先筛选行为窗口、调用栈和字段形态，再转 `reproduce-android-crypto` 建立 Unit/G1 fixture。
- 发现证书/Pinning 拦截器：转 HTTPS MITM 或 Pinning 诊断分支。
