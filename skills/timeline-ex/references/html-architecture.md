# Timeline-Ex HTML Architecture

## 1. 默认技术栈

首版使用：

```text
原生 HTML + CSS + JavaScript
vis-timeline 8.5.2
timeline-data.js
```

选择理由：

- `vis-timeline` 原生表达单点、时间范围、分组、缩放和今天标记；
- 原生 HTML/CSS 允许项目直接双击打开；
- 数据与视图分离后，Agent 可以安全更新节点而不改布局代码；
- 不需要 React、Node 构建或后端服务。

固定 CDN 版本：

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/vis-timeline@8.5.2/styles/vis-timeline-graph2d.min.css"
/>
<script src="https://cdn.jsdelivr.net/npm/vis-timeline@8.5.2/standalone/umd/vis-timeline-graph2d.min.js"></script>
```

需要完全离线时，将相同版本资源保存到项目 `assets/vendor/vis-timeline/` 并改用相对路径。不要无版本引用 `latest`。

## 2. 页面分区

推荐顺序：

```text
Hero / 当前批次
Summary cards / Gate 数、下一门槛、失败影响
Lifecycle chain / 箭线式状态转换
Chronological view / 真实时间轴
Gate register / 可搜索表格
Detail drawer / 节点详情与 Markdown 链接
```

时间轴回答“什么时候”；生命周期链回答“为什么能进入下一步”。两者共用 `timeline-data.js`，不要维护两份节点。

## 3. 视觉编码

默认：

```text
EVT  = 蓝色；
OBL  = 橙色；
GATE = 紫色；
OUT  = 绿色或红色，按结果语义选择；
tentative/window/conditional = 虚线边框；
exact/confirmed-window       = 实线边框；
today                        = 明显但不遮挡节点的竖线。
```

要求：

- 颜色、形状、文字标签至少使用两种信号；
- 文字和背景达到可读对比度；
- 节点短标题在默认缩放下可辨认；
- 近似时间不使用“已确认”视觉；
- 失败分支与当前主路线明显区分。

## 4. 短窗口显示

“月初”“下旬”等窗口在全程视图中可能太窄。允许把短于约 14 天的 range 以箱形里程碑放在近似中点，同时：

- 保留节点 `start/end`；
- 详情中展示 `displayTime` 原文；
- 页面声明箱形位置是可视化处理；
- 不因此修改节点时间语义。

## 5. 降级策略

如果 CDN 或脚本不可用：

- 生命周期链仍应由原生 HTML/JS 数据渲染或静态存在；
- Gate 表格和节点 Markdown 仍可访问；
- 页面显示明确错误提示；
- 不把空白画布误报为“无节点”。

## 6. 何时增加 G6

当以下情况同时出现时，增加 AntV G6 依赖视图：

- 节点超过约 20 个；
- 存在多条并行路线、回路或多种失败分支；
- 仅靠生命周期链无法看清 `creates / supersedes / pass / fail`；
- 用户明确需要像网络图一样缩放、选择和追踪边。

使用第二个标签页：

```text
[时间视图] [依赖网络] [Gate 清单]
```

G6 与时间轴必须读取同一组 `nodes/links`。不要为 G6 新建第二份手工数据。

## 7. 何时升级 React / Ant Design

只有在需要以下能力时升级：

- 在页面内创建或编辑节点；
- 多人协作和后端持久化；
- 复杂表单、权限、审批和通知；
- 多项目组合管理；
- 大量通用 UI 组件。

Ant Design 适合表格、筛选器、抽屉和表单，不是核心时间轴引擎。Tailwind 只负责样式，不负责时间布局或关系连线。不要为了“好看”先引入构建链。

## 8. 浏览器 UAT

至少验证：

```text
GIVEN timeline-data.js 包含有效节点
WHEN 打开 index.html
THEN vis-timeline 初始化且没有控制台错误

GIVEN 用户点击生命周期链或表格节点
WHEN 打开详情
THEN 抽屉标题、状态和 Markdown 链接与节点一致

GIVEN 用户选择 EVT/OBL/GATE/OUT 筛选
WHEN 时间轴重绘
THEN 只保留对应类型

GIVEN 当前视图过窄
WHEN 点击聚焦或查看全程
THEN 时间窗口切换且节点仍可识别
```

推荐用 Playwright 做浏览器检查，但不要为了一个静态项目新增永久测试工程；可使用已有工具环境临时验证。

## 9. 模板使用

复制 `assets/static-template/` 到目标 `docs/external-timeline/` 后：

1. 用项目节点替换示例 `timeline-data.js`；
2. 修改标题、摘要卡和视觉变量；
3. 添加实际节点 Markdown；
4. 检查相对路径；
5. 运行 JS 语法、数据完整性和浏览器 UAT；
6. 从项目 README 和 Roadmap 链接 `index.html`。
