---
name: reproduce-android-crypto
description: 在经过授权的 Android 请求复现任务中，根据 JADX 算法链和 Frida 运行时 fixture，用 Python 等价实现参数排序、签名、编码、填充和对称加密，并对中间值与最终字节进行逐级比较。用于已定位 Java 算法且输入、盐、Key、IV 和目标密文可获得的课堂靶场或自有应用。不得用于未授权访问、批量指标操纵或真实凭据滥用。
---

# Android 算法与正文复现

## 目标

把“看起来是相同算法”提升为“固定输入得到相同中间值和最终字节”，并输出能够脱离 App 重复运行的最小实现。若输入字段采用格式等价或随机替代值，明确区分“当前可用”和“真实生成链已复现”。

## 工作流

1. 读取静态构造链和运行时 JSONL fixture。若 fixture 来自 `crypto-probe`，先按 `references/crypto-probe-fixtures.md` 筛选行为窗口、算法类型、调用栈、输入输出长度和 key/iv/mode 关系；探针事件只能作为 Unit/G1 候选，不能单独证明请求构造链完整。
2. 列出参数集合、排序规则、空值规则和字符集。
3. 对替代字段读取 `references/substitute-validation.md`，记录真实性要求、替代公式、绑定风险和验证范围。
4. 先复现参数明文。
5. 时间、随机数或 UUID 参与时提供可注入参数；禁止拿两次随机输出直接比较。
6. 再复现签名输入和签名结果。
7. 再拼接完整加密前明文。
8. 明确 Key/IV 是文本字节、Hex 解码值还是截断值。
9. 复现 padding、mode 和最终密文。
10. 按 `references/comparison-ladder.md` 从上到下比较。
11. 检查课程文档中的输入、时间、随机段和输出是否来自同一次 fixture；不自洽样例只作算法说明。
12. 只有同一 fixture 密文字节完全一致才判定算法 A 级。
13. 先将离线结果标记为 G1；若上层目标要求完整重发，再构造包含必要请求头的完整请求执行一次 G2。
14. G2 前先载入一份 App 原始成功请求，用外部实现重算 sign、密文或关键派生值；不一致时停止网络请求并报告 G1 首差。
15. G2 默认不自动重试，必须保存请求 manifest、HTTP 状态和业务响应；失败也原样记录。
16. 预检一致但返回 TFS、风控或环境拒绝时，输出“运行态/设备态/传输上下文待归因”，不得无证据修改已通过的算法。
17. 替代值通过网络验证时只标记 `substitute-valid`，不得据此宣称字段真实生成链已复现。
18. 如果算法外观像 MD5/SHA1/HMAC/AES/RC4/Base64 但常量、分段、编码表、salt、Key/IV 或输出长度与标准实现不一致，且上游 native 静态证据提示 OLLVM/控制流平坦化/指令替换/字符串加密，不要在本 Skill 内继续盲猜；回到 `hook-android-native/references/native-trace-ollvm.md` 建立 native oracle。需要补课程语境时，查看 workflow 顶层 `../../references/kanxue-course-directory-index.md` 中看雪第5章和第8-9章。
19. 对标准算法、参数化标准算法、native 魔改算法和 OLLVM 包裹算法的分流，读取 `references/nonstandard-native-crypto.md`；只有同一 fixture 的早期层级一致后，才把差异归因到 native 魔改或 OLLVM。

## 编排交接

由总编排调用时：

- 接收 Mermaid 中的 Unit、G1 或 G2 红灯，以及固定输入和 Green 条件；
- 先写失败测试，再实现最小规则，并从首个差异层级修正；
- Unit 通过后更新对应字段，不能提前把整条请求标为完成；
- G1 与 G2 必须分别保存证据并分别更新终点链；
- 目标要求 UAT 时，G2 通过后仍将 `NEXT` 交回总编排执行最终验收。

## 输出

- 可执行 Python 脚本；
- 脱敏 fixture 与本地原始 fixture 的边界说明；
- 参数明文、sign、完整明文和 ciphertext 的比较报告；
- 单元测试与课堂 evaluation；
- 不能一致时的首个差异层级。
- 替代字段的适用前提、验证范围和未验证绑定。
- G1/G2 状态；若执行 G2，保存完整请求清单和响应证据。
- 原始成功请求预检结果，以及 G2 失败属于算法、显式 HTTP、状态绑定还是运行/传输上下文。

## 完成标准

- A：同一运行时 fixture 的参数明文、sign、完整明文和密文字节全部一致。
- B：动态输入不同，但固定课堂 fixture 精确一致，且当前运行时结构一致。
- C：算法链已实现，但缺少必要运行时输入，明确阻塞字段。

能力标签另行记录：

- `substitute-valid`：替代输入在声明范围内可用；
- `reproducible`：真实输入生成规则可重建；
- `validated`：真实重建值与 App 或 fixture 一致。

## 参考资料

- 分层比对见 `references/comparison-ladder.md`。
- 从算法探针事件进入复现时读取 `references/crypto-probe-fixtures.md`。
- 使用随机标识或格式等价值时读取 `references/substitute-validation.md`。
- 标准算法疑似被 OLLVM 或魔改 native 包裹时，读取 `../hook-android-native/references/native-trace-ollvm.md`；需要课程参考时查看 workflow 顶层 `../../references/kanxue-course-directory-index.md` 的看雪第5章、第8-9章。
- 判断标准算法、参数化标准算法、native 魔改算法和 OLLVM 包裹算法时，读取 `references/nonstandard-native-crypto.md`。
