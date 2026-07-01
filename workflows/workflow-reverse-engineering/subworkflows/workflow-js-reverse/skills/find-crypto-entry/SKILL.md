---
name: find-crypto-entry
description: 在经过授权的 JS 逆向任务中定位加密、签名、token、登录密码加密等入口函数。用于从浏览器调试线索、静态源码、bundle、请求字段或本地 oracle 中识别候选函数、输入参数、关键常量、输出字段和上下游证据；适合 RSA/AES/DES/MD5/HMAC/国密等算法复现前的入口定位。当前已由图灵 JS TASK05 的 DCN RSA 样本验证；真实接口 replay 和复杂 webpack/wasm 入口仍需后续专项 TASK 继续验证。
---

# Find Crypto Entry

## 适用场景

先由父级 workflow 明确目标字段和 Green，再使用本 Skill 定位入口。

适用：

- 请求字段明显是加密、签名或 token；
- 登录密码、分页参数、header、body 中存在非明文字段；
- 静态代码中出现 `encrypt`、`sign`、`token`、`RSA`、`AES`、`MD5`、`HMAC` 等线索；
- 已有本地 JS/Python oracle，需要整理入口证据。

不直接负责：

- 完整算法重写；
- webpack 模块恢复；
- wasm 分析；
- 真实接口 replay。定位入口后交给对应复现 Skill。

## 流程

1. 从目标字段倒推候选词：
   - 字段名：`sign`、`token`、`password`、`pwd`、`encrypt`、`cipher`；
   - 算法词：`RSA`、`AES`、`DES`、`MD5`、`SHA`、`HMAC`、`SM2`、`SM3`、`SM4`。
2. 静态定位候选函数：
   - 函数名；
   - 入参；
   - 返回值；
   - 关键常量，如 key、iv、public exponent、modulus、salt。
3. 动态或 oracle 验证：
   - 用本地样本输入运行；
   - 输出形态应和目标字段一致；
   - 若只能结构验证，明确标记 `structural-green`。
4. 写入口证据台账：
   - 入口函数；
   - 参数来源；
   - 常量来源；
   - 输出字段；
   - 尚未证明的 replay 边界。

## 完成标准

最小 Green：

- 找到入口函数；
- 找到输入参数和输出字段；
- 至少找到一项关键常量或依赖函数；
- 能用本地 oracle 生成预期形态输出；
- 不把真实接口 replay 与入口定位混为一谈。

## 证据模板

```text
目标字段:
入口函数:
输入参数:
关键常量:
依赖函数:
输出形态:
本地 oracle:
未完成边界:
```

## 当前状态

```text
structural-green / crypto-entry-forward-test-green
```

已由 TASK05 验证：

- JS 入口：`encryptPassword(password)`；
- Python oracle：`dcn_rsa_encrypt(password)`；
- 常量：RSA public exponent 和 modulus；
- 输出：非空十六进制密文。
