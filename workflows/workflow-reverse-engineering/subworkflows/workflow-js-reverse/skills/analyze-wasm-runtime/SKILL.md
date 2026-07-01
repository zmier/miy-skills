# analyze-wasm-runtime

## 适用场景

当 JS 逆向任务中出现 `.wasm` 文件、`WebAssembly.instantiate`、`WebAssembly.instantiateStreaming`、`instance.exports`、`memory`、`imports`、`exports`，且目标字段由 WASM 导出函数参与生成时，使用本 Skill。

## 总原则

WASM 优先当作“本地 helper / side asset”处理，而不是默认当作浏览器黑箱。

处理顺序：

1. 找到 wasm 文件来源；
2. 枚举 imports/exports；
3. 判断是“裸导出函数”还是“wasm-bindgen / webpack wrapper”；
4. 裸导出函数：用固定输入调用导出函数；
5. wrapper 型：保留原 JS wrapper，提取 wasm side asset，补最小浏览器环境后调用 wrapper 暴露函数；
6. 冻结 Node runtime，记录 `node -v` 与 `node` 绝对路径；
7. 在 Node 和 Python 至少一条路径跑通；
8. 能双路径时做同参同结果 parity；
9. 再把输出接入真实请求；
10. 用 endpoint 或响应解密结果做 oracle。

## Node 执行

```js
const fs = require("fs");
const bytes = fs.readFileSync("./target.wasm");
const { instance } = await WebAssembly.instantiate(bytes, imports);
console.log(Object.keys(instance.exports));
console.log(instance.exports.encrypt(1, 123456));
```

## Python 执行

优先使用课程已验证的 `pywasm`：

```python
import pywasm

vm = pywasm.load("./target.wasm")
result = vm.exec("encrypt", [1, 123456])
```

## wasm-bindgen / wrapper 型执行

如果目标站把 WASM 包在 webpack/wasm-bindgen wrapper 里，不要一开始就丢掉 wrapper。优先沿用原 wrapper，因为：

- 字符串编码、内存分配、异常处理通常在 wrapper 中；
- 真实导出函数可能不是最终业务函数；
- wrapper 可能负责 `WebAssembly.instantiate`、module cache、header entries 转换。

处理模板：

```text
原站 JS wrapper
  -> 提取内联或远程 wasm side asset
  -> 安装最小 browser env: window/self/location/document/HTMLElement/XMLHttpRequest
  -> 固定 Node runtime
  -> 调用 wrapper export
  -> 生成 headers/params
  -> 请求真实 endpoint
```

Node runtime 要作为证据的一部分。遇到同一脚本在不同 Node 下表现不同，例如：

- `RuntimeError: unreachable`
- 空 stdout 且 exit code 为 0
- `FATAL ERROR: invalid table size Allocation failed - JavaScript heap out of memory`

先固定一个已验证的 `NODE_BIN` 绝对路径，再继续补环境。不要只靠 `PATH` 中的 `node`，因为 Python subprocess、shell、IDE 可能解析到不同版本。

## 证据台账

每个 wasm TASK 至少记录：

- wasm 文件路径和来源；
- imports 需求；
- exports 列表；
- 目标导出函数；
- 固定输入；
- Node/Python 输出；
- 是否接入真实请求；
- endpoint oracle；
- 未解决的 memory/string/env/import 红灯。

## 常见红灯

| 红灯 | 现象 | 处理 |
| --- | --- | --- |
| 缺 imports | instantiate 报导入缺失 | 记录模块名/函数名，补最小 stub |
| 字符串在 memory | 导出函数参数是指针 | 分析 memory 写入/读取 |
| 浏览器 API 耦合 | wasm 初始化依赖 fetch/window | 先下载 wasm，再本地 instantiate |
| wasm-bindgen wrapper | 裸 wasm 可加载但业务函数不可用 | 保留原 wrapper，补最小浏览器对象 |
| Node/V8 差异 | 同脚本 OOM、空 stdout、unreachable | 固定 `NODE_BIN`，把 runtime 纳入 ledger |
| 输出只本地可算 | 无真实接口验证 | 只标局部 Green，不标 replay Green |

## 课程来源

具体课程证据记录在：

`../../references/course-provenance.md`
