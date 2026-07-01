# 非标准与 Native 包裹算法分流

## 定位

本 reference 属于 `reproduce-android-crypto`，用于判断一个“看起来像标准算法”的字段是否真的能在 Python/JavaScript 中直接复现。

如果算法外观像 MD5、SHA1、HMAC、AES、RC4、Base64，但常量、分段、编码表、盐、Key/IV、输出长度或运行时证据不一致，不要在复现层无限猜参数。先判断是否应回到 native oracle。

## 分流规则

| 现象 | 优先判断 | 下一步 |
| --- | --- | --- |
| 标准 Base64/CRC32/MD5/HMAC，输入、编码、盐明确 | 标准或参数化标准算法 | 留在 `reproduce-android-crypto`，按 comparison ladder 复现 |
| 输出形态像摘要，但标准实现始终不一致 | 可能有盐、常量魔改、分段或字符集差异 | 先排查 comparison ladder 的早期层 |
| 早期层一致但摘要/密文仍不一致 | 可能是 native 魔改或 OLLVM 包裹 | 回到 `hook-android-native` 建 oracle |
| Base64 表不是标准表或运行时生成 | 动态编码表 | Hook 表生成/使用点，保存表和输入输出 |
| RC4/AES 等对称算法输出不一致 | 可能是 Key schedule、IV、padding、分段或魔改 | 固定 key/iv/plaintext/ciphertext fixture，必要时 Stalker |
| OLLVM/控制流平坦化/指令替换痕迹明显 | 静态伪代码不可信 | 读取 `../../hook-android-native/references/native-trace-ollvm.md` |
| 静态出现 OpenSSL 常量、函数名或相似结构 | 只是算法候选，不是完成证据 | 结合数据流、xref 和运行时输入输出确认 |
| 编码表或 S-box 运行时生成 | 动态表或魔改算法 | dump 表来源、使用点和同次输入输出 |
| MD5/SHA1/HMAC 常量或 salt 异常 | 魔改摘要或组合算法 | 保存 salt、常量、分段、编码和 OLLVM 证据链 |
| 插件能解释部分 OLLVM 算法 | 平行解释工具 | 作为 confirmatory，不替代当前样本 primary 证据 |
| 外部复现成本过高但 App 内函数可稳定调用 | R2 黑盒调用可用 | 转 `../../export-frida-rpc/SKILL.md`，标记 `rpc-available` 而非 `reproducible` |

## 工作顺序

```text
先用 comparison ladder 排除普通差异
→ 固定同一次 fixture
→ 标准实现仍不一致
→ 检查 native/OLLVM 证据
→ Hook 输入、输出、表、key schedule 或 doFinal 窗口
→ 建 oracle
→ 再回到 reproduce-android-crypto 写外部实现
```

## 工具与证据边界

- OpenSSL 特征、标准常量和函数外观只形成候选；
- BPO、IDA 插件或自动识别工具属于 `confirmatory` 或 `exploratory`，不能单独作为算法 Green；
- Frida RPC 黑盒调用属于 R2：它证明可以借用 App 运行态生成结果，不证明 R3 纯外部复现完成；
- 若交付允许依赖 App 运行态，可以把 R2 作为阶段性工具；若交付要求脱离设备，必须继续做 native oracle 与外部实现。

## Green 边界

- `standard-reproducible`：标准库实现与同一 fixture 完全一致；
- `parameterized-standard`：标准算法加盐、排序、编码或模式差异已解释；
- `native-oracle-needed`：标准层无法解释，需回 native 取证；
- `native-oracle-green`：已取得输入、输出、常量/表或关键中间值；
- `nonstandard-reproducible`：外部实现与 native oracle 对拍一致。

不要因为算法名或输出长度像 MD5/AES 就标记为标准算法 Green。

## 看雪查字典入口

优先查看：

- 看雪第8章 课时2-3：Base64、CRC32、MD5；
- 看雪第8章 课时4-5：OLLVM_MD5、OLLVM_SHA1；
- 看雪第8章 课时6：HMAC；
- 看雪第8章 课时7-9：OLLVM_Base64、OLLVM_RC4、Frida Stalker OLLVM AES；
- 看雪第9章：非标准算法还原下；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。
