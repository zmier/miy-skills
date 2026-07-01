# 壳与动态加载诊断

支持加壳假设的组合证据：

- JADX 只看到少量代理 Application/ClassLoader；
- Manifest Application 指向 wrapper/stub；
- APK 含 `libshell*`、`libjiagu*` 或可疑加密 `.dat`；
- 运行时能使用业务类，但静态 Dex 中不存在；
- 业务类在启动或功能触发后由新 ClassLoader 出现。

不能单独作为结论：

- 类名短；
- JADX 报少量错误；
- APK 包含很多 so；
- 搜不到一个关键词。

这些也可能来自混淆、多 Dex、跨平台框架或关键词选择不当。
