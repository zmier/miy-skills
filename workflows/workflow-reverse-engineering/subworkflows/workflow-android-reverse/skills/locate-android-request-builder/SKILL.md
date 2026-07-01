---
name: locate-android-request-builder
description: 使用 JADX 等静态分析工具，在经过授权的 Android APK 中从目标接口 URL、Path、字段名或请求类型出发，定位 Retrofit/OkHttp 请求声明、调用点、RequestBody 构造、明文字段拼装、签名与编码转换链。用于参数归约已确定请求体或动态字段是唯一阻塞，需要回答“这个二进制正文在哪里生成、输入是什么、下一步该 Hook 哪个 Java 方法”。不得用于未授权应用、凭据提取或访问控制规避。
---

# Android 请求构造链定位

## 目标

从已确认的网络接口建立一条可引用的静态证据链：

```text
接口 Path
→ 网络声明
→ 调用点
→ RequestBody 构造
→ 明文字段拼装
→ sign
→ 编码或加密函数
→ Java 运行时观察点
```

## 输入

- TASK 工作区和已确认目标接口；
- APK 路径、版本与包名；
- 成功请求样本及 Content-Type；
- 参数归约结论；
- 可用 JADX 版本。

目标接口未确认时返回 `analyze-android-traffic`；参数阻塞未收敛时返回 `minimize-android-request`。

## 工作流

1. 记录 APK 哈希与 JADX 版本。
2. 使用当前稳定版 JADX；旧版无法处理大型 APK 时升级，不沿用失败的课程旧版。
3. 将反编译产物写入 TASK 的受控分析目录，不覆盖 APK，并从版本管理中排除大体积产物。
4. 优先用 CLI 生成可检索证据，同时用 GUI 支持人类跟课浏览。
5. 按 `references/jadx-search-funnel.md` 搜索完整 Path，再逐步缩短关键词。
6. 识别 Retrofit/OkHttp 声明，记录方法、注解、Body 类型与拦截器。
7. 查找该网络方法的用例，定位传入 `@Body` 的对象。
8. 追踪 `RequestBody.create`、工厂方法或序列化器的正文参数。
9. 找到返回 `byte[]`、`ByteString` 或不透明对象的方法，记录真实类名、方法名和签名。
10. 向上记录业务输入，向下记录 sign、压缩、编码和加密调用。
11. 区分“推测语义”和“代码直接证据”。
12. 只有出现方法体缺失、反编译异常或控制流无法验证等证据时，才按回退阶梯切换另一反编译器或 Smali。
13. 输出静态链路卡与下一运行时观察点。

## 编排交接

由总编排调用时：

- 接收 Mermaid 中具体字段或不透明外层的红灯；
- 静态搜索只围绕该节点的 Green 条件展开；
- 将定位到的类、方法、签名和代码位置作为证据侧枝写回图与节点表；
- `located` 不能写成 `reproducible` 或 `validated`；
- 需要真实实参时，把 `NEXT` 交给 `trace-android-java`，并写明要观察的唯一问题。

## 混淆规则

- 保留 APK 中真实类名和方法名；JADX 反混淆别名只作阅读辅助。
- Hook、搜索 Smali 或运行时定位时使用真实符号。
- 单字母或短方法名不是失败；通过调用关系、参数类型、常量与返回值恢复职责。
- 只有静态调用关系不足时，才路由 `trace-android-java`。

## 输出

默认写入：

```text
tasks/TASK07-JADX定位/
├── jadx-search-log.md
├── request-builder-chain.md
└── outputs/runtime-handoff.md
```

至少记录：

- APK 与工具版本；
- 搜索词及命中位置；
- 网络声明；
- 调用点；
- 正文构造方法及真实签名；
- 已恢复的输入字段；
- sign 与编码/加密函数；
- 尚不确定的分支；
- 推荐 Hook 点和下一 Skill。

## 完成标准

- A：静态证据完整连接接口 Path 到正文生成方法，并明确算法调用。
- B：已定位正文生成 Java 方法和输入，但某个算法实现需运行时确认。
- C：只定位到网络声明或调用点，明确缺少的 Dex、反编译质量或运行时类型证据。

只搜索到 URL 字符串不算完成。

## 参考资料

- 执行 JADX 搜索和记录证据时读取 `references/jadx-search-funnel.md`。
- 当前反编译结果不足、课程要求切换 GDA 或工具版本时读取 `references/decompiler-fallback.md`。
