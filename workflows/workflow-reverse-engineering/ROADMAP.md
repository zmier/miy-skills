# Roadmap

## Phase 1：容器化迁移

- [x] 创建 `workflow-reverse-engineering` 顶层容器。
- [x] 将 `workflow-android-reverse` 复制到 `subworkflows/workflow-android-reverse/`。
- [x] 排除 `.venv/`、`node_modules/`、`.pytest_cache/` 等可重建产物。
- [x] 创建顶层 README、workflow、Roadmap、log。
- [x] 创建 JS 子 workflow 占位结构。

## Phase 2：迁移审计

- [x] 统计 Android 子 workflow 文件、Skill、reference、template。
- [x] 检查旧路径硬编码引用。
- [x] 更新 miku RPC 运行脚本的默认 workflow 根目录。
- [x] 在新 Android 子 workflow 下重建 `.venv`。
- [ ] 判断是否需要把旧路径替换为软链。
- [x] 更新元 Workflow 工程 TASK05 的迁移状态。

## Phase 3：抽象父 Workflow

- [x] 审计 Android workflow 的通用/专属/可迁移能力。
- [x] 将第一批稳定通用内容上提到 `references/` 和 `templates/`。
- [x] 编写 `skills/reverse-workflow-orchestrator/SKILL.md` 的轻量编排版。
- [x] 定义父 workflow 与 subworkflow 的初始调用关系。
- [x] 用 JS 子 workflow 的真实案例 forward-test 父级抽象。

## Phase 4：JS 子 Workflow

- [x] 盘点图灵 JS 模块笔记与代码。
- [x] 创建 `workflow-js-reverse` 的初始 workflow 和 skills。
- [x] 选择 1-2 个 JS 案例进行课程驱动反哺。
- [x] 用 JS 子 workflow 反向校验父 workflow 抽象是否合理。
- [x] 用 XHR 案例扩展 JS browser runtime 观测分支。
- [x] 用 JS runtime baseline 案例补齐 Node / Python subprocess / Browser 执行位点选择分支。
- [x] 用 Day04 RSA 样本补齐 JS 加密入口定位分支。
- [x] 用 Day05 property/cookie/JSON.parse 样本补齐浏览器运行时值来源观测分支。
- [x] 用 Day06 axios/巨潮接口样本补齐请求封装层 interceptor 观测分支。
- [x] 用 Day07 execjs/subprocess/express 样本补齐 Python-Node-JS 桥接分支。
- [ ] 继续用 cookie/fetch 或 webpack 案例扩展 JS 子 workflow 的第二批能力分支。
