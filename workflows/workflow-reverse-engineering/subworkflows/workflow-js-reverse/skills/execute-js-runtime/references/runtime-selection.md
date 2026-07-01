# Runtime Selection

## 快速判断

| 红灯或需求 | 首选路线 | 说明 |
|---|---|---|
| 纯算法函数 | Node CLI | 最小、快、容易测 |
| Python 同步调用小函数 | execjs | 只适合同步函数 |
| Python 请求脚本要调用 JS | Python subprocess -> Node | 适合短任务和 batch |
| Promise 需要复用成接口 | Express / HTTP wrapper | 适合长驻服务化 |
| 需要 window/document/cookie/XHR | Browser runtime | 保留页面生命周期 |
| Promise 拿不到结果 | 显式 await + JSON stdout | 不读 pending Promise |
| 缺 navigator/screen/location | Browser 或补环境 | 先判断是不是算法必需 |
| webpack `__webpack_require__` | webpack 专项分支 | 不在本 Skill 里硬补 |
| wasm exports/imports | wasm 专项分支 | 需要处理内存与 glue |

## 常见失败

- Node 报 `window is not defined`：不要盲补，先判断是否应该留在 Browser。
- Python 解析 JSON 失败：stdout 混入 console log，应把日志打到 stderr 或写文件。
- execjs 拿不到 Promise：这是工具边界，不是 Promise 失败；改用 subprocess 或 wrapper。
- Promise 输出 `{}` 或 pending：外层没有 await。
- Browser 结果不稳定：页面脚本加载时机不对，需要 `waitForFunction` 或事件观测。
