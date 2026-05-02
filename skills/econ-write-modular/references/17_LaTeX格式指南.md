# 经济学论文 LaTeX 提示

用于撰写、排版和提交经济学论文的实用 LaTeX 指南。

## 文档结构

```latex
\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{setspace}\doublespacing  % 多数期刊要求双倍行距
\usepackage{amsmath,amssymb}
\usepackage{graphicx,float}
\usepackage{booktabs,threeparttable}
\usepackage{natbib}
\usepackage[hidelinks]{hyperref}
\usepackage{cleveref}
\usepackage{appendix}
```

## 必备宏包

| 宏包 | 用途 |
|---------|---------|
| `amsmath` | 对齐公式、多行数学表达 |
| `booktabs` | 专业表格横线 |
| `threeparttable` | 表格下方注释 |
| `natbib` | 作者-年份引用（经济学标准） |
| `siunitx` / `dcolumn` | 小数点对齐列 |
| `subcaption` | 子图（a）、（b）等 |
| `tikz` | 图示、博弈树、时间线 |
| `cleveref` | 智能交叉引用 |

## 表格格式

**使用 booktabs，永远不要使用 `\hline`。** 使用 `\toprule`、`\midrule`、`\bottomrule`，并完全避免竖线。

**回归表**：用 `threeparttable` 包裹，便于写注释：

```latex
\begin{table}[t]
\begin{threeparttable}
\caption{Effect of X on Y}\label{tab:main}
\begin{tabular}{lcc}
\toprule
 & (1) & (2) \\
\midrule
Treatment & 0.45*** & 0.38** \\
 & (0.12) & (0.15) \\
Controls & No & Yes \\
Observations & 5,000 & 5,000 \\
\bottomrule
\end{tabular}
\begin{tablenotes}\small
\item \textit{Notes:} Standard errors in parentheses. *** p<0.01.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

**用 `siunitx` 做小数点对齐**：使用 `S[table-format=1.3]` 作为列类型。对于多面板表格，用 `\midrule` 分隔面板，并用 `\multicolumn` 标注每个面板。

## 图形格式

- **总是使用 PDF** 矢量图，而不是 PNG/JPG。例外：照片或地图。
- **从 Stata 导出：** `graph export fig.pdf, replace`。从 R 导出：`ggsave("fig.pdf", width=6, height=4)`。从 Python 导出：`plt.savefig("fig.pdf", bbox_inches="tight")`。
- **用 `subcaption` 做子图：**

```latex
\begin{figure}[t]
\begin{subfigure}{0.48\textwidth}
  \includegraphics[width=\linewidth]{fig_a.pdf}
  \caption{Pre-period}\label{fig:pre}
\end{subfigure}\hfill
\begin{subfigure}{0.48\textwidth}
  \includegraphics[width=\linewidth]{fig_b.pdf}
  \caption{Post-period}\label{fig:post}
\end{subfigure}
\caption{Event study results}\label{fig:event}
\end{figure}
```

- 保持所有图形宽度一致（例如 `width=0.9\textwidth` 或固定 `width=5in`），以保证视觉一致性。

## 参考文献管理

**使用 `natbib`，配合 `\bibliographystyle{aer}` 或 `chicago`。** 这会生成作者-年份格式：`\citet{FF1993}` 生成 “Fama and French (1993)”，`\citep{FF1993}` 生成 “(Fama and French, 1993)”。

`biblatex` 搭配 `style=authoryear` 是另一种选择，但在经济学投稿中不如 `natbib` 常见。选择前检查目标期刊要求。

**工作论文：** 在 bib 条目中加入 `note = {NBER Working Paper No.\ 12345}`。投稿前更新为已发表版本。

## 数学格式

- 单行公式用 `equation`，多行公式用 `align`。避免使用 `eqnarray`。
- **只给会被引用的公式编号：** 对不编号公式使用 `\begin{equation*}` 或 `\nonumber`，只给用 `\eqref` 引用的公式编号。
- **符号惯例：** 拉丁字母表示可观测量/变量（$Y$, $X$, $D$），希腊字母表示参数（$\beta$, $\gamma$, $\varepsilon$）。首次使用时定义符号。

```latex
\begin{align}
Y_{it} &= \alpha + \beta D_{it} + \mathbf{X}_{it}'\gamma + \varepsilon_{it} \label{eq:main}
\end{align}
```

## 交叉引用

为每张表、每个图和每个公式设置标签。使用 `cleveref` 的 `\cref` 自动格式化：

```latex
\cref{tab:main}   % -> Table 1
\cref{fig:event}  % -> Figure 2
\cref{eq:main}    % -> eq. (1)
```

这可以避免全文中 “table 1” 与 “Table 1” 之类的不一致。

## 期刊投稿提示

| 期刊 | 关键要求 |
|---------|-----------------|
| AER | 12pt，双倍行距，图表放文末，匿名 |
| QJE | 类似 AER；在线附录作为单独 PDF |
| Econometrica | 自有 `ecta` 文档类；格式严格 |
| REStud | 可用 `restud` 类；图形放文末 |
| JPE | Chicago 风格参考文献；标准 article 类 |

**匿名投稿：** 删除作者姓名和会暴露身份的自引。谨慎使用 `\thanks{}`。添加 `\date{}` 以隐藏日期。

**字数统计：** 在命令行运行 `texcount paper.tex`。多数 top-5 期刊希望主文为 8,000--12,000 词。

**在线附录：** 创建单独文件（`appendix.pdf`），并设置自己的标题页。在主文中交叉引用：“see Online Appendix Table A1.”

## Beamer 报告

```latex
\documentclass{beamer}
\usetheme{metropolis}  % 干净、现代
\setbeamertemplate{navigation symbols}{}  % 移除导航杂物
```

- 每页幻灯片一个想法。谨慎使用 `\pause`。
- 在 `\appendix` 之后用一个 “Backup Slides” 页面标记备用页。
- 使用 `\hyperlink{backup1}{\beamerbutton{Detail}}` 从主报告链接到备用页。

## 常见问题

- **浮动体离正文太远：** 使用 `[t]` 或 `[!htbp]`；或者作为最后手段，使用 `\usepackage{float}` 配合 `[H]`。投稿时把所有表格/图形放到文末也能避免这个问题。
- **Overfull boxes：** 检查日志警告。宽表可以用 `\resizebox{\textwidth}{!}{...}`，或在 tabular 内用 `\small` 缩小字号。
- **表格太宽：** 重构表格（减少列数、缩短表头），而不是缩到不可读。必要时拆成多个面板。
- **引用缺失：** 运行 BibTeX/Biber，然后运行两遍 LaTeX。使用 `latexmk -pdf` 自动化构建链。
