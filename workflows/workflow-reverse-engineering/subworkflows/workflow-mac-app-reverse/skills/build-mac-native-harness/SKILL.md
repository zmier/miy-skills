---
name: build-mac-native-harness
description: 在授权 Mac App 逆向任务中，为 Mach-O、dylib、framework、C/C++/ObjC/Swift 函数构建本机离线 harness，验证固定输入 parity、依赖补齐、环境变量、bundle resource、Keychain/文件依赖和调用副作用。
---

# Build Mac Native Harness

## 触发条件

- 静态或动态分析已定位候选函数、类、framework 或 dylib；
- 目标可以在授权范围内被本机加载、链接或通过小型宿主调用；
- 需要把 M2 运行态 oracle 提炼为 M3 离线函数。

## 工作流

1. 记录目标二进制、架构、依赖、签名和资源路径。
2. 用固定输入建立 App 运行态 oracle，包含输入、输出、错误和副作用。
3. 选择 harness 形态：C/ObjC/Swift 小程序、Python ctypes、Node native addon、lldb expression 或动态加载 dylib。
4. 补齐最小依赖：framework search path、bundle resource、环境变量、working directory、locale、timezone。
5. 若函数依赖 Keychain、sandbox container、network、XPC 或 App singleton，优先记录 `runtimeDependencyBlocked`，不要伪造离线 Green。
6. 做固定输入 parity，再接真实请求或业务动作验证。

## Green

```text
harnessBuildOk=true
fixedInputParityOk=true
runtimeDependencyBlocked=false
sideEffectsDeclared=true
businessGreenSeparatelyVerified=true/false
```

M3 harness Green 不自动等于 M1/M4 业务 Green。

