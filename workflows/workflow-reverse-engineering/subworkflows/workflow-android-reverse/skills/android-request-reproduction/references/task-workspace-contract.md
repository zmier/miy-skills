# 需求 TASK 工作区契约

每个具体请求复现需求必须拥有独立 TASK 工作区。总编排 Skill 负责创建、更新和关闭工作区；子 Skills 只完成其中一个阶段，并把证据写回工作区。

## 物理归属

- TASK 必须创建在对应课程、案例或业务项目目录内，不得创建在 `workflow-android-reverse/` 根目录。
- 跨多个 Day 的知识迁移任务放在这些课程资料的共同上级目录，例如 `笔记包/TASK-Day21-23知识迁移/`。
- Evaluation、日志、fixture、案例测试、专用 Hook、复现脚本和构建产物属于 TASK。
- Workflow 只接收抽象后的 Skill、通用脚本、模板、依赖和不读取具体 TASK 的中性测试。
- Workflow 可以链接 TASK 证据，但不得复制证据，也不得让 `make test` 反向依赖某个课程 TASK。

## 最小结构

```text
TASK-需求名/
├── README.md
├── TASK-总-需求名.md
├── 00-工作流状态.yaml
├── acceptance-contract.md               # 从 Skill asset 复制；定义 UAT/G2/G1
├── request-construction-ledger.md  # 从 Skill asset 复制；含路线矩阵的持续主轴
├── evaluations/                    # 案例前向评测；模板来自 Skill asset
├── tests/
│   ├── smoke/
│   ├── unit/
│   ├── e2e/
│   ├── uat/
│   └── fixtures/
├── tasks/
│   ├── TASK01-目标与边界/
│   ├── TASK02-采集窗口/          # 含人类抓包操作手册
│   ├── TASK03-候选接口/
│   ├── TASK04-对照验证/          # 含人类验证操作手册
│   ├── TASK05-目标接口/
│   └── TASK06-最小重放与路由/   # 可含参数归约清单和实验
├── evidence/{raw,sanitized}/
├── logs/LOG.md
└── final_outputs/
```

可以增加 JNI、Native、Unidbg 等后续阶段，但不得省略目标边界、证据、结论依据和恢复动作。

## 文件职责

- `README.md`：人类入口、边界和证据规则。
- `TASK-总-*.md`：阶段状态、依赖和人工关口。
- `00-工作流状态.yaml`：机器与总编排 Skill 的当前状态。
- `acceptance-contract.md`：从 `assets/acceptance-contract-template.md` 复制，先定义 UAT、G2、G1、路线和完成边界。
- `request-construction-ledger.md`：从 `assets/request-construction-ledger-template.md` 复制，保存终点链、目标 URL、路线矩阵、Mermaid 核心控制面、测试状态、字段能力、按路线必要性、证据和下一动作。
- `evaluations/`：使用 `assets/evaluation-template.md` 记录具体案例对 Skill 的前向评测。
- `tests/smoke/`：设备、代理、进程、Frida、类加载和脚本环境检查。
- `tests/unit/`：单个字段、算法、编码、加密和边界 fixture。
- `tests/e2e/`：G1 离线等价与 G2 受控端到端记录或脚本。
- `tests/uat/`：最终业务或研究交付的人工验收记录。
- `tests/fixtures/`：带来源、版本、时间与环境的固定输入和 App 输出。
- `tasks/*/outputs/`：各阶段整理后的中间产物。
- `tasks/TASK02-采集窗口/human-operation-manual.md`：人类执行的目标化抓包步骤。
- `tasks/TASK04-对照验证/validation-operation-manual.md`：基于候选生成的下一轮最小验证步骤。
- `tasks/TASK06-最小重放与路由/parameter-inventory.md`：目标请求参数分类与必要性状态。
- `tasks/TASK06-最小重放与路由/minimization-operation-manual.md`：人类逐项执行的删减实验。
- `evidence/raw/`：本地原始证据，不提交敏感流量。
- `evidence/sanitized/`：可链接、可共享的脱敏证据。
- `logs/LOG.md`：过程、失败尝试和决策。
- `final_outputs/`：通过人工关口的接口卡、fixture 和最终交付。

## 状态推进

1. 先写观察，再写假设。
2. 为采集、候选和实验分配稳定编号。
3. 子 Skill 完成后先同步更新请求构造依赖台账的 Mermaid 图、测试矩阵、路线矩阵和节点表，再更新阶段 output、工作流状态和日志。
4. 所有“已确认”结论必须引用证据编号。
5. 未通过人工关口时不得进入下游阶段。
6. 人类操作必须由版本化手册驱动；人类反馈先原样记录，再由 AI 解释。
7. 每个新 TASK 必须对应 Mermaid 中的红灯、失败测试或未运行关口，并写明 Green 条件。
8. 任何工具调用前，先把唯一 `NEXT` 指向本轮 TASK；完成后依据证据重新计算。

## Skill 交接

子 Skill 返回时至少写明：

- TASK 工作区和目标阶段；
- 对应 Mermaid 红灯与测试 ID；
- 输入证据；
- 新观察与证据；
- Green 条件是否达到；
- 更新的文件；
- 当前置信度与唯一阻塞；
- 下一 Skill 及完成条件。

`capture-android-traffic` 通常写入抓包操作手册、采集索引和脱敏样本；`analyze-android-traffic` 通常写入候选矩阵、验证操作手册、实验日志和目标接口卡；`minimize-android-request` 写入参数清单、删减实验和最小请求卡；后续分析 Skills 从 `handoff.md` 接续。

所有子 Skills 还必须更新 `request-construction-ledger.md` 中自己处理的节点。阶段文件保留细节，台账保留跨阶段的当前真相。

## Python 环境

- 临时校验、一次性数据检查和文档辅助脚本统一使用 `Writer/.venv`。
- 不为纯 Markdown、Shell 或无 Python 运行依赖的 Skill 创建空虚拟环境。
- 当某个 Skill 需要可重复执行的 Python 工作流时，在该 Skill 或其工程目录中创建独立 `.venv`，并同时提供：
  - `pyproject.toml`；
  - Python 版本与依赖说明；
  - 初始化、安装和运行命令；
  - 必要的 lock 文件；
  - 忽略 `.venv/` 的版本控制规则；
  - 对应 unit、e2e 或 UAT 测试。
- 不使用临时 `uv --with`、系统 Python 或全局 `pip` 代替上述环境约定。
