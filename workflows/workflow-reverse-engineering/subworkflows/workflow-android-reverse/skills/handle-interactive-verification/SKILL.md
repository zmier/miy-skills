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
7. 短信验证码、登录确认等必须由用户本人输入，不写入日志。
8. 服务端返回后记录成功/失败业务码、剩余时效和下游 Token。
9. Green 后把 Token/会话字段交给动态字段 Skill，并回到 G2。

## Green 条件

- 单次授权 challenge 被正确解析；
- 人工确认或授权识别结果被服务端接受；
- challenge、验证码和下游 Token 的绑定与时效已记录；
- 敏感码未落盘；
- 无无限重试或批量行为。

## 课程迁移判断

Day22 展示了 ddddocr、Tesseract、muggle_ocr 和第三方识别路线。Workflow 中不采用“识别失败就无限刷新”或默认外包打码，而采用：

1. 人工接力；
2. 固定图片 fixture 评测；
3. 授权环境中的单次 OCR 候选；
4. 服务端业务码验收。

当前状态为 `learning`。

## 参考资料

- 安全与选择规则读取 `references/verification-policy.md`。
- 人工步骤复制 `assets/human-verification-manual.md`。
