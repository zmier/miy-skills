---
name: handle-interactive-verification
description: 在课堂、自有系统或明确授权的低频 Android 测试中处理图片验证码、短信验证码、人工确认和短时 Token 等交互式验证关口，设计人机协作、fixture 回放、OCR 候选评估和时效/绑定记录。用于请求构造已完成但 G2 被一次性验证码或人工步骤阻塞的场景。不得用于批量绕过验证码、接管账号、滥用第三方打码平台或规避访问控制。
---

# 交互式验证关口处理

## 目标

把验证码从“算法字段”改建模为有生命周期的人机验证节点：

```text
challenge 获取
→ 图片/问题解析
→ 人工或授权识别
→ 服务端校验
→ 短信/Token 下发
→ 人工输入
→ 下游请求
```

## 工作流

1. 确认该验证关口属于授权范围，并限制次数。
2. 记录 challenge 请求、响应表示、会话/手机号/设备绑定和过期时间。
3. 优先选择人工接力；需要重复开发测试时再使用固定 fixture。
4. OCR 只作为候选建议，按 `references/verification-policy.md` 设置置信度和人工确认。
5. Base64 图片先验证 magic、尺寸和颜色模式，再交给 OCR。
6. 比较轻量 OCR、Tesseract、领域模型或内部授权服务，但不循环轰炸刷新 challenge。
7. 如果在授权环境中需要对比超级鹰，先运行 `scripts/chaojiying_client.py preflight --no-network --json`；只有 `status=ready` 时才做单次候选识别，其他状态立即切到人工接力。
8. 短信验证码、登录确认等必须由用户本人输入，不写入日志。
9. 服务端返回后记录成功/失败业务码、剩余时效和下游 Token。
10. Green 后把 Token/会话字段交给动态字段 Skill，并回到 G2。

## Green 条件

- 单次授权 challenge 被正确解析；
- 人工确认或授权识别结果被服务端接受；
- challenge、验证码和下游 Token 的绑定与时效已记录；
- 敏感码未落盘；
- 无无限重试或批量行为。

## 超级鹰脚本用法

脚本位置：

```bash
skills/handle-interactive-verification/scripts/chaojiying_client.py
```

凭据优先放在本地忽略文件，例如：

```bash
cp skills/handle-interactive-verification/.env.example \
  skills/handle-interactive-verification/.env.local
```

`.env.local` 入参：

```text
CHAOJIYING_USER=超级鹰账号
CHAOJIYING_PASS=超级鹰明文密码
# 或使用 CHAOJIYING_PASS2=密码 md5 小写值
# CHAOJIYING_SOFT_ID=软件 ID；官方 HTTP 文档说明可为空
CHAOJIYING_CODETYPE=1902
```

`CHAOJIYING_CODETYPE` 默认可不填；脚本默认使用 `1902`，即 4~6 位英文数字。

自动识别前必须先做本地 readiness 检查，不提交图片，也不访问超级鹰：

```bash
skills/handle-interactive-verification/scripts/chaojiying_client.py \
  preflight \
  --env-file skills/handle-interactive-verification/.env.local \
  --no-network \
  --json
```

`preflight` 输出 JSON，调用方按 `status` 分流：

| status | 处理 |
|---|---|
| `ready` | 依赖、凭据和默认识别类型可用；允许继续单次授权识别 |
| `missing_credentials` | 缺账号或密码/pass2；立即切到人工接力 |
| `missing_dependency` | 当前 Python 运行时缺 `requests` 或版本不满足项目要求；立即切到人工接力或改用项目 `.venv` |
| `invalid_env_shape` | `.env.local`、`pass2` 或 `codetype` 形状错误；修正前不访问第三方 |

`preflight` 的入参：

| 参数 | 作用 |
|---|---|
| `--env-file` | 读取本地忽略的凭据文件；文件缺失时不会报 traceback，会返回非 ready JSON |
| `--user` | 超级鹰账号；通常用 `CHAOJIYING_USER` |
| `--password` | 明文密码；脚本只检查是否存在，不输出值 |
| `--pass2` | 已计算好的 md5 小写密码；形状错误返回 `invalid_env_shape` |
| `--softid` | 软件 ID；官方 HTTP 文档说明可为空 |
| `--codetype` | 识别类型；默认 `1902` |
| `--no-network` | 显式声明本次检查不得访问第三方接口 |
| `--json` | 输出机器可读 JSON |

识别单张图片：

```bash
skills/handle-interactive-verification/scripts/chaojiying_client.py \
  --env-file skills/handle-interactive-verification/.env.local \
  recognize \
  --image /path/to/captcha.jpg \
  --ack-authorized
```

识别 Base64 图片文件：

```bash
skills/handle-interactive-verification/scripts/chaojiying_client.py \
  --env-file skills/handle-interactive-verification/.env.local \
  recognize \
  --image-base64-file /path/to/captcha-base64.txt \
  --ack-authorized
```

常用全局入参：

| 参数 | 作用 |
|---|---|
| `--env-file` | 读取本地忽略的凭据文件 |
| `--user` | 超级鹰账号；通常用 `CHAOJIYING_USER` |
| `--password` | 明文密码；脚本会转成官方 `pass2` |
| `--pass2` | 已计算好的 md5 小写密码 |
| `--softid` | 软件 ID；通常用 `CHAOJIYING_SOFT_ID` |
| `--dry-run` | 只校验入参，不访问第三方接口 |
| `--redact-result` | 输出时隐藏 `pic_str` |

`recognize` 入参：

| 参数 | 作用 |
|---|---|
| `--image` | 单张 bmp/jpg/jpeg/png 图片路径 |
| `--image-base64-file` | 单个 Base64 图片文本文件路径 |
| `--codetype` | 识别类型；默认 `1902` |
| `--str-debug` | 透传超级鹰 `str_debug` 字段 |
| `--ack-authorized` | 必填确认：本次为授权单次 challenge |

报错返分：

```bash
skills/handle-interactive-verification/scripts/chaojiying_client.py \
  --env-file skills/handle-interactive-verification/.env.local \
  report-error \
  --pic-id <recognize 返回的 pic_id> \
  --confirm-wrong-result \
  --ack-authorized
```

查题分：

```bash
skills/handle-interactive-verification/scripts/chaojiying_client.py \
  --env-file skills/handle-interactive-verification/.env.local \
  score
```

注意：`recognize` 和 `report-error` 都是第三方真实调用，必须显式 `--ack-authorized`。只允许单次授权候选识别，不做目录批量、循环刷新或自动绕过。

## 课程迁移判断

Day22 展示了 ddddocr、Tesseract、muggle_ocr 和第三方识别路线；课程原始笔记中的第三方打码平台示例包括云打码、超级鹰。Workflow 只记录它们作为课程来源信息，不采用“识别失败就无限刷新”或默认外包打码，而采用：

1. 人工接力；
2. 固定图片 fixture 评测；
3. 授权环境中的单次 OCR 候选；
4. 服务端业务码验收。

当前状态为 `learning`。

## 参考资料

- 安全与选择规则读取 `references/verification-policy.md`。
- 人工步骤复制 `assets/human-verification-manual.md`。
- 超级鹰单次候选识别脚本读取 `scripts/chaojiying_client.py`；凭据模板读取 `.env.example`，真实凭据放入本地忽略的 `.env.local` 后用 `--env-file` 显式加载。
- 超级鹰账号配置与官方入口读取 `references/chaojiying-account-note.md`；实际账号只放在本机 `.env.local`。
