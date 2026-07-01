---
date: 2026-06-18
type: reference
status: structural-green
scope:
  - workflow-reverse-engineering
---

# 静态与动态闭环

## 核心判断

静态分析回答“可能在哪里、代码大概怎么写”，动态观测回答“运行时到底发生了什么”。

二者要闭环：

```text
静态定位候选
→ 动态观测实参/返回/调用时机
→ 回到静态解释上游和分支
→ 用 fixture 校正复现
```

不能把静态猜测当作运行时证据，也不能只拿 hook 输出而不解释来源。

## 典型循环

1. 从目标线索进入：URL、字段名、错误码、字符串、函数名、导出符号、bundle 片段。
2. 静态定位候选：调用点、构造链、算法函数、bridge、native 边界。
3. 动态观测候选：实参、返回值、中间值、调用堆栈、触发时机、运行时类型。
4. 回填证据台账：候选是否命中，是否产生新待解字段。
5. 构造最小复现：外部脚本、运行态 RPC、离线 harness 或其他交付形态。
6. 用 UAT / Smoke / Unit 判断 Green。

## 平台工具映射

| 抽象动作 | Android 例子 | JS 例子 |
| --- | --- | --- |
| 静态找入口 | JADX 搜 URL/字段/调用链 | 搜 bundle、source map、webpack module |
| 动态观测 | Frida Hook Java/Native | DevTools breakpoint、Hook fetch/XHR/WebSocket/函数 |
| 调用栈辅助 | Java stack trace、native backtrace | JS call stack、async stack、initiator |
| 边界定位 | JNI、so、RPC bridge | WebCrypto、wasm、worker、service worker |
| 离线复现 | Python、Unidbg、Java wrapper | Node、浏览器自动化、jsdom、wasm runtime |

## 什么时候偏静态

- 目标字符串、字段名或函数名可搜索；
- 代码结构清晰；
- 需要理解上游来源和分支；
- hook 成本高或会改变行为；
- 需要做可迁移的算法复现。

## 什么时候偏动态

- 静态调用链过长；
- 参数来自运行态状态、缓存、随机数、设备态或用户态；
- 代码被混淆但运行路径明确；
- 需要确认真实输入输出；
- 静态工具反编译结果不可信。

## 常见误区

- 看到静态函数名就认为已经复现；
- hook 到返回值就不追输入和触发条件；
- 把一个样本的动态值写成通用规则；
- 离线复现失败时只怀疑算法，不检查环境态；
- 只保存最终响应，不保存中间 fixture。

