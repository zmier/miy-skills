---
name: analyze-macho-static
description: 对授权 Mac App 的 Mach-O、dylib、framework、helper 或 XPC service 做静态分析，识别架构、依赖、导入导出、字符串、ObjC 元数据、Swift 符号、网络/加密/Keychain/IPC 入口和 patch/harness 候选。
---

# Analyze Mach-O Static

## 工作流

1. 从 `inspect-mac-app-bundle` 接收二进制清单和候选目标。
2. 确认架构：arm64、x86_64、universal binary、Rosetta 运行差异。
3. 建立依赖图：系统 framework、第三方 framework、embedded dylib、plugin、XPC service。
4. 搜索字符串和符号：URL、host、path、selector、class、Keychain、CFNetwork、NSURLSession、WKWebView、XPC、crypto。
5. 识别 ObjC class/selector、Swift demangle 候选、C/C++ 导出和 stripped 情况。
6. 对候选函数建立证据卡：地址、符号、调用关系、输入输出猜测、动态验证计划。
7. 对 GUI/图表/动态列表目标，额外建立 MVC/MVVM/渲染分层链路：
   - controller / delegate / data source；
   - parser / adapter / property builder / view-model；
   - model item / dictionary / array / record；
   - view / layer / render / draw / fill / color；
   - visible range / offset / length / total / cache。
8. 若静态证据不足，交给 `analyze-objc-swift-runtime`、`hook-mac-app-frida` 或 `trace-mac-app-lldb`。

## Selector 分层提示

静态分析时，类似以下命名通常提示不同层级：

```text
业务/模型层: data, model, item, record, quote, ohlc, kline, date, id, code
适配/属性层: parser, parse, property, range, axis, location, length, adapter
控制层: controller, dataSource, delegate, reload, update
渲染层: draw, render, layer, plot, fill, color, stroke, cell
```

第三方 framework 中的 `draw*`、`fillForIndex:`、`cellFor*` 等方法常是渲染终点，只能证明“某个可见 index 被画了”，不能直接证明业务日期、ID 或对象身份。若发现 visible offset、range、length、total 等字段，必须在动态阶段验证 local index 是否会随滚动、缩放、懒加载或数据补全变化。

## Green

```text
staticTargetLocated=true
candidateFunctionOrClass=<name/address>
evidenceSource=[strings/symbols/xrefs/imports]
runtimeValidationPlanDeclared=true
uiLayeringMapDeclared=true/false
```

静态定位只算候选，不替代运行态 oracle 或业务 UAT。
