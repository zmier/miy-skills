---
name: prepare-unidbg-toolchain
description: 准备和验证 Unidbg 离线执行环境。用于 Android so 算法需要脱离真机运行、课程资料包含 unidbg 工程、需要检查 JDK/Maven wrapper、处理中文或空格路径导致资源加载失败、运行官方 SignUtil smoke，或建立 desktop-only Unidbg TASK 时使用。
---

# Prepare Unidbg Toolchain

## 适用场景

- 已定位加密逻辑在 so 中，准备走 Unidbg 离线执行。
- 当前不能触碰真机、代理或 Frida，但可以使用 APK/so/课程资料包。
- 需要验证本机能否编译并运行 Unidbg 最小样例。

## 工作流

1. 建立 TASK 级 `desktop-only` 验收契约，明确禁止 `adb/frida/reqable/mitmproxy/socksdroid`。
2. 读取 `references/emulation-route-selection.md`，先判断当前目标更适合 Unicorn、AndroidNativeEmu 平行参考，还是默认 Unidbg。
3. 先读取或创建 TASK 级 `inputs/resource-manifest.yaml`。资源本体不放入 Skill；Skill 只记录获取、校验、解压和放置规则。
4. 按 manifest 获取资源：
   - 公开第三方资源优先使用官方 GitHub、Release、包管理器或项目文档指定来源；
   - 老师课程资料、靶 APK、靶 so、课堂示例代码只从授权本地资料包或人工提供路径获取；
   - 若公开来源不可用，可按 manifest 中的 fallback 使用本地缓存或课程包，但必须记录来源差异。
5. 对下载或复制到 TASK 的资源计算 `sha256`，与 manifest 记录对照；首次填入 hash 时在日志说明来源和时间。
6. 检查 JDK，优先 JDK 8；若 Maven 报 `No compiler is provided`，显式设置完整 JDK：
   ```bash
   export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_301.jdk/Contents/Home"
   export PATH="$JAVA_HOME/bin:$PATH"
   ```
7. 优先使用课程包、公开源码或项目自带 wrapper，例如 `./mvnw`，不要先要求全局 Maven/Gradle。
8. 资料包中文路径提取失败时，不依赖中文路径文本匹配；按成员后缀匹配 `unidbg-*.zip`。
9. 构建：
   ```bash
   ./mvnw -q -pl unidbg-android -am -DskipTests package
   ./mvnw -q -pl unidbg-android -am -Dmaven.test.skip=false test-compile
   ./mvnw -q -pl unidbg-android -Dmaven.test.skip=false dependency:build-classpath -Dmdep.outputFile=target/test-classpath.txt -DincludeScope=test
   ```
10. 运行官方 smoke，例如 `com.anjuke.mobile.sign.SignUtil`。

## 资源契约

不要把 Unidbg 源码包、老师课程 zip、APK、so 或大体积示例工程打包进 Skill。按资源类型处理：

| 资源类型 | 示例 | 推荐处理 |
|---|---|---|
| 公开第三方资源 | Unidbg、JADX、Frida、mitmproxy | 在 manifest 记录官方来源、版本、获取命令和 sha256 |
| 课程授权资源 | 老师资料包、靶 APK、靶 so、课堂代码 | 在 manifest 记录本地期望路径、授权来源和 sha256，不上传到 Skill |
| 小型通用脚手架 | wrapper 模板、Makefile 片段、补环境片段 | 可放入 Skill 的 `assets/` 或 `scripts/` |
| 个案 fixture | 某次抓包、某个输出、某个 APK 的固定参数 | 留在对应 TASK 的 `inputs/`、`outputs/` 或 `tests/fixtures/` |

manifest 至少包含：

```yaml
resources:
  - id: unidbg
    kind: third-party-open-source
    preferred_source: https://github.com/zhkl0228/unidbg
    recommended_version: "0.9.7"
    fallback_source: "授权课程资料包中的 unidbg-0.9.7.zip"
    expected_path: inputs/course-provided/unidbg-0.9.7.zip
    sha256: "<fill-after-first-verified-copy>"
    restore_strategy: "优先官方来源；不可用时使用授权本地资料包"

  - id: target-apk
    kind: course-fixture
    preferred_source: "授权课程资料包"
    expected_path: inputs/course-provided/<target>.apk
    sha256: "<fill-after-first-verified-copy>"
    restore_strategy: "从本地课程资料包复制；缺失时请求人工补齐"
```

换环境时按顺序恢复：

```text
读取 resource-manifest.yaml
→ 检查 expected_path 是否存在
→ 缺公开资源：按 preferred_source 获取
→ 缺课程资源：从授权本地资料包或人工提供路径复制
→ 计算 sha256 并比对
→ 解压到 inputs/extracted/
→ 复制运行副本到 ASCII workdir
→ 执行 smoke
```

## 路径规则

Unidbg 0.9.x 在路径包含中文、空格或其他非 ASCII 字符时，可能把 resource URL 编码后的路径当普通文件路径使用，导致 `android/sdkXX/lib/liblog.so` 等资源明明存在却 `FileNotFoundException`。

处理顺序：

1. 先确认资源实际存在；
2. 不优先使用软链，Java 可能 canonicalize 回真实路径；
3. 复制运行工作副本到 ASCII 路径，例如 `/tmp/<task>-unidbg-work/unidbg-0.9.7`；
4. TASK 中记录原路径、运行副本路径和原因。

## 工具层补丁规则

有些红灯来自 Unidbg 版本或运行器本身，而不是目标 App，例如：

- 中文/空格路径导致 resource URL 编码问题；
- JNI 签名 parser 对某类裸参数描述符不兼容；
- pid、`/proc` 路径或 runner 随机性影响重复运行；
- Maven/JDK/classpath 与课程版本不一致。

处理规则：

1. 先用官方或课程 sample 证明工具链基础可运行；
2. 再用目标样例证明红灯出现在工具层，而不是 ABI、JNI 签名、参数包装或缺少 `JNI_OnLoad`；
3. 只修改 TASK 的 ASCII 运行副本或缓存源码，不修改全局 Unidbg、系统 JDK 或 Skill 资源；
4. 记录补丁文件、原始报错、最小改动和回归命令；
5. 补丁后至少重跑当前目标和一个 smoke，确认没有把工具问题误归因到目标 App；
6. 该类记录写成 `tooling-gap`，不要写成目标 App 的补环境。

## Green

- `./mvnw -version` 可用；
- `unidbg-android` 编译通过；
- 至少一个官方样例、授权课程样例或 TASK-local smoke 有稳定输出；
- `inputs/resource-manifest.yaml` 已记录本轮必需资源、来源、恢复策略和 hash 状态；
- 若存在工具层补丁，补丁仅限 TASK 运行副本，且已记录原始错误、改动和回归结果；
- 日志确认没有触碰真机链路。

## 迁移状态

- 已覆盖 JDK/Maven wrapper、ASCII 工作副本、资源 manifest 和 tooling-gap 记录。
- 具体样例输出、固定 runner 调整和课程资源路径保留在 TASK 与能力注册表，不写入通用 Skill 主体。

## 参考资料

- 选择 Unicorn、AndroidNativeEmu 或 Unidbg 时读取 `references/emulation-route-selection.md`。
