# analyze-webpack-runtime

## 适用场景

当目标 JS 被 webpack 打包，算法入口不是直接暴露的函数，而是藏在模块加载器、模块 id、导出对象中时，使用本 Skill。

典型信号：

- 看到 `!function(e){...}(...)` 自执行模块包；
- 存在 `modules[id].call(module.exports, module, module.exports, require)` 形态；
- 存在 `t[id].exports`、`installedModules`、`__webpack_require__`、`webpackJsonp`、`chunk`；
- 业务代码通过数字或字符串模块 id 加载，例如 `loader(490)`；
- 算法类或函数挂在导出对象上，例如 `loader(490).JSEncrypt`。

## 总原则

webpack 通常不是算法本身，而是入口路由层。处理顺序是：

1. 识别 loader；
2. 暴露 loader；
3. 打印模块调用日志；
4. 根据模块 id 获取 exports；
5. 从 exports 中找到目标函数、类或常量；
6. 再交给 `reproduce-js-crypto` 或 `replay-js-request` 继续复现。

关键判断：如果模块导出的是请求封装函数，不要停在“能调用函数”。要继续验证它是否同时生成 headers/body/cookies 所需字段，并用真实 endpoint 或明确 oracle 证明可用。

## 操作流程

### 1. 识别 loader

优先找类似结构：

```js
function n(id) {
  if (cache[id]) return cache[id].exports;
  var module = cache[id] = { exports: {} };
  modules[id].call(module.exports, module, module.exports, n);
  return module.exports;
}
```

如果模块容器是数组，模块 id 多为数字；如果模块容器是对象，模块 id 可以是字符串或 hash。

### 2. 暴露 loader

在 loader 定义后挂到全局：

```js
window.loader = n;
```

Node 环境可先补：

```js
window = global;
```

### 3. 打模块调用日志

在 loader 入口增加日志：

```js
console.log("模块加载 -> ", id);
```

这一步用于回答两个问题：

- 目标动作触发了哪些模块；
- 哪个模块最可能导出加密函数或参数生成函数。

### 4. 取导出对象

如果已知模块 id：

```js
const mod = window.loader(490);
console.log(Object.keys(mod));
```

如果导出对象里有目标类：

```js
const rsa = new mod.JSEncrypt();
rsa.setPublicKey(publicKey);
const cipher = rsa.encrypt(plainText);
```

### 5. 处理运行环境红灯

如果 loader 初始化时触发浏览器环境检测：

- 先观察 webpack 自身是否主动调用检测模块；
- 能注释初始化调用的，先注释做最小复现；
- 不能注释的，补 `window`、`navigator`、`location` 等最小环境；
- 仍然大量依赖真实浏览器时，转到浏览器自动化或 Camoufox/Playwright 方案。

### 6. 接真实协议

当 webpack 模块导出请求封装能力时，台账要拆开记录：

- `moduleExportOk`：能取到模块导出对象；
- `fieldGenerationOk`：能生成目标字段，如 `x-tif-*`、`encData`、`signData`；
- `timestampCouplingOk`：headers/body 中的时间戳、nonce、sign 使用同一轮值；
- `realEndpointReachedOk`：真实 endpoint 返回 HTTP 200/业务可识别响应；
- `responseDecryptOk`：如果响应加密，能用同一模块或等价实现解密；
- `businessShapeOk`：明文包含预期业务结构。

如果只有本地密文输出，例如 RSA 加密字符串，只能标记本地算法/形态 Green，不能写成真实 replay Green。

## 输出物

每个 webpack TASK 至少输出：

- loader 位置和形态；
- 目标模块 id；
- 目标模块 exports 的 key；
- 调用目标函数所需的最小参数；
- 是否进入算法复现层；
- 是否有未解决的浏览器环境红灯。

## 课程来源

具体课程证据与文件路径记录在：

`../../references/course-provenance.md`
