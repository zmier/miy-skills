# 技术雷达反哺

## 适用场景

当资料来源不是一门课程或一个训练营，而是官方文档、开源工具 release、GitHub issue、论文、安全社区文章、会议资料或真实工程博客时，使用技术雷达反哺。

典型触发：

- 用户问某个课程知识在 2025/2026 是否过时；
- 真实项目遇到新系统、新工具版本或新防护导致 workflow 失效；
- 需要定期检索 Frida、Unidbg、eBPF、ART、FART、SVC/syscall、VMP、OLLVM、网络通道等方向的新资料；
- 希望把外部技术进展转成领域 workflow 的分支参考、工具链更新或路线选择规则。

## 与课程反哺的区别

| 维度 | 课程反哺 | 技术雷达反哺 |
| --- | --- | --- |
| 来源 | 老师案例、课件、代码、视频转写 | 官方文档、论文、release、issue、工程文章 |
| 基线 | 课程案例和教师路线 | 现有 workflow 与真实红灯 |
| 核心问题 | 课程知识如何工程化 | 新技术是否改变 workflow |
| 风险 | 抄答案、污染 Skill 主流程 | 追热点、过度升级、把未验证资料写成能力 |
| 常见状态 | `structural-green / forward-test-pending` | `radar-recorded / structural-green / forward-test-pending` |

## 主流程

```text
确定观察主题
→ 检索权威资料
→ 归类资料角色
→ 判断影响的 workflow 红灯
→ 用双价值四象限筛选
→ 先落入 Radar 知识层
→ 再决定是否升级 workflow / Skill
→ 更新 provenance / radar log
→ 必要时开 forward-test TASK
```

技术雷达的默认落点是 Radar，而不是领域 workflow。只有当资料满足“明确影响某个红灯、能给出可迁移动作、不会让主流程变重、最好已有真实案例或 forward-test 计划”时，才进入 workflow 或子 Skill。否则先沉淀为 `radar-recorded`、`watchlist` 或 `hypothesis`。

## 资料优先级

优先级从高到低：

1. 官方文档、AOSP 文档、工具官方 release；
2. 论文、会议材料、可复现实验项目；
3. 维护活跃的开源项目、issue、PR；
4. 安全社区技术文章；
5. 零散博客、论坛讨论、未复现传闻。

资料越靠后，越不能直接写成 workflow 规则，只能作为线索或探索性参考。

## 英文安全社区与博客线

英文社区和博客适合追踪实战技巧、工具组合、会议材料和工程趋势，但必须分层采信。

### 可靠来源分层

1. 官方标准与平台基线：
   - OWASP MASVS / MASTG：移动安全测试方法、术语和检查点基准；
   - Android Developers / AOSP / Android Security Bulletin：Android 平台、ART、权限、系统安全、eBPF、MTE、版本差异。
2. 高质量移动安全公司与研究博客：
   - Corellium：移动虚拟化、Android/iOS 逆向、设备环境和动态分析；
   - 8kSec：移动逆向、Frida、native library、fuzzing 和 exploitation；
   - HTTP Toolkit：抓包、SSL pinning、Frida 网络分析；
   - Fortinet Threat Research：Android malware、packer、unpacking、Frida 动态分析；
   - Pentest Partners：移动、BLE、IoT 场景下的 Frida 和实战逆向。
3. 会议与 workshop：
   - RE//verse、Black Hat、DEF CON、Virus Bulletin、A-Mobile；
   - 适合追踪二进制分析、反调试、mobile exploitation、Android malware、packer 和动态分析前沿。
4. 聚合与社区线索：
   - Awesome Android Reverse Engineering、Reddit r/netsec、Talk::Overflow、个人 Substack、Medium；
   - 只能作为线索入口，不能直接作为 workflow 规则来源。

### 采信规则

- 官方和标准文档可以作为平台基线，但不直接给出逆向操作 Green。
- 安全公司和会议材料可以作为实战参考，但仍要检查日期、目标 Android 版本、工具版本、设备/root 前提和是否有可复现代码。
- 聚合列表、Reddit、Medium、Substack 默认标记为 `community-signal`，必须经官方文档、GitHub 项目、论文或本地实验交叉验证。
- 任何“万能绕过”“通用脚本”“一键脱壳”都先标记为 `hypothesis`，不能直接进入 Skill 主流程。
- 若文章绑定具体 App、样本、host、token、固定类名或固定偏移，只能进入 Radar/TASK 证据，不能复制到通用 Skill。

### 适合跟踪的主题

- Frida / Objection / LSPosed / Zygisk / KernelSU / APatch 生态变化；
- SSL pinning、Cronet、OkHttp、mPaaS/mobilegw、小程序 bridge 网络通道；
- Android packer、FART、dex dump、ART 定制、JADX 失败和修复；
- anti-Frida、anti-debug、emulator/root 检测、SVC/syscall、硬件断点；
- eBPF、whole-system tracing、Binder 观测和 kernel observability；
- native library fuzzing、Ghidra/IDA/Binary Ninja、Stalker/Trace、Unidbg/Unicorn/AndroidNativeEmu。

## 可调用的情报适配器

技术雷达本身只负责编排和判断，不应把所有检索逻辑写进本 Skill。根据资料类型调用已有适配器：

- 学术论文、预印本、英文研究资料：优先调用 `scholar-kit-openalex-search`，用 OpenAlex 检索候选论文，再按相关性、时间、可复现性和 workflow 影响做二轮筛选。
- 跨数据源学术检索：若需要 OpenAlex、WoS、CNKI 协同，由 `scholar-kit-literature-search` 或相应 scholar-kit 分支负责编排。
- 工具 release、GitHub issue、官方文档和安全社区文章：使用联网检索、GitHub、官方文档或项目仓库作为来源，不交给 OpenAlex。
- 英文社区和博客：先按“官方基线 / 高质量研究博客 / 会议材料 / 社区线索”分层，再决定是否进入 Radar、watchlist、TASK 或 workflow-candidate。

OpenAlex 适合发现论文和预印本线索，但不等于完整技术雷达。工程可用性仍要回到官方仓库、release、issue、复现实验和当前 workflow 的 forward-test。

### OpenAlex 论文雷达用法

调用 `scholar-kit-openalex-search` 时，把它当成“论文候选池生成器”，而不是 workflow 变更证据。

推荐做法：

1. 先用宽主题词形成候选池，例如 `Android app unpacking eBPF`、`mobile app hardening Android reverse engineering`、`Android anti debugging anti analysis reverse engineering`。
2. 避免只搜工程黑话。`FART`、`unidbg`、`OLLVM Android`、`Frida bypass` 等词在 OpenAlex 中可能召回很弱，因为论文标题和摘要常使用更学术的表达。
3. 对同一主题做两组词：
   - 工程词：贴近社区和工具名；
   - 学术词：贴近论文表达，例如 `packed Android applications`、`anti runtime analysis`、`binary obfuscation`、`dynamic security analysis`。
4. 把检索结果先写入 Radar 文档和 `.bib/.json` 候选池，标记为 `paper-candidate-pool`。
5. 只在完成二轮筛选后，才判断是否影响 workflow：
   - 论文是否解决真实 `X -> ✅`？
   - 是否有代码、数据、可复现实验或后续引用？
   - 是否只是概念综述，还是能给出可执行路线？
   - 是否需要 GitHub、arXiv 原文、项目主页或官方文档交叉验证？
6. OpenAlex 能检索到部分 arXiv / 预印本，但若目标是最新 arXiv 追踪或 arXiv ID 精准检索，应补用 arXiv API、RSS、Semantic Scholar、论文主页或项目仓库。

OpenAlex 结果的典型状态：

- `radar-recorded`：已记录论文信号，但暂不改 workflow；
- `watchlist`：值得定期跟踪引用、开源实现、复现实验；
- `structural-green`：Radar 文档、候选池、判断和来源都已落盘；
- `forward-test-pending`：可能影响 workflow，但需要真实案例验证；
- `validated`：只有在新案例上完成迁移验证后才能使用。

## 落点判断

- 默认落点：Radar 目录、候选池、watchlist、技术雷达总结。
- 影响默认主流程：只有在多个来源一致、已有 forward-test 或明确平台变更时才修改。
- 影响分支路线：写入相关 Skill 的 `references/`，标明触发红灯和回到 workflow 的动作。
- 影响工具链版本：写入环境准备 Skill、Makefile、安装说明或 compatibility reference。
- 只影响用户理解：写入技术雷达目录、课程索引、知识卡片或 README。
- 尚不能验证：写入 radar log，标记 `watchlist` 或 `hypothesis`。

## 技术雷达不能做的事

- 不能把“最新”当成“必须采用”。
- 不能把单篇文章或单个 issue 写成通用能力。
- 不能因为某工具出现新 release 就修改所有相关 Skill。
- 不能把未在新案例上验证的路线标成 `validated`。
- 不能让主 workflow 因高级低频资料变重。

## 定时检索建议

定时检索不是为了追热点，而是为了维护 workflow 的有效性。

建议：

- 月度轻量检索：工具 release、Android 官方平台变化、关键 issue；
- 季度深度检索：论文、预印本、会议、安全社区、开源项目横评；论文和预印本可调用 `scholar-kit-openalex-search` 形成候选池；
- 红灯即时检索：某个真实任务遇到工具失效、平台不兼容或新防护。

每次检索至少落盘：

- 日期；
- 检索主题；
- 关键来源；
- 新发现；
- 影响的 Skill 或 workflow 分支；
- 是否需要修改；
- 是否需要 forward-test；
- 下次观察点。

## 完成标准

一次技术雷达反哺至少满足：

1. 资料来源和检索日期明确；
2. 已区分官方、论文、release、issue、博客等来源类型；
3. 已说明它影响哪个 workflow 红灯；
4. 已说明为什么修改或不修改 Skill；
5. 若修改 Skill，已保留来源追溯；
6. 若未验证，明确标记 `forward-test-pending` 或 `watchlist`；
7. 没有把外部资料直接伪装成当前 workflow 的已验证能力。
