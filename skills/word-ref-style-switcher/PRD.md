# Word 引文格式切换器 PRD

## 1. 背景

当前稿件原本采用编号制引文格式：

- 文中引用使用方括号编号，例如 `[1]`、`[2, 4, 5]`、`[33-37]`。
- 文末参考文献按编号排列，例如 `1. K. L. Alvin, R. J. Murphy, ...`。

现在稿件需要改投其他期刊，目标期刊要求改为作者-年份制：

- 文末参考文献按作者姓氏或作者首字母顺序排序。
- 文中引用改为 `(Author, Year)`、`(Author et al., Year)` 或多篇组合引用。

因此需要一个工具或 skill，帮助把 Word 稿件中的编号制参考文献自动转换为作者-年份制，并尽量减少人工逐条查改的工作量。

## 2. 用户当前困惑总结

用户的困惑主要不是“单条引用怎么写”，而是整篇稿件转换时存在多层不确定性：

1. 文末参考文献编号会因为按作者排序而整体变化，原来的 `[1]`、`[2]` 已经不能直接保留。
2. 文中引用不能只是把编号换成新编号，而是要根据每条参考文献抽取作者和年份，改成作者-年份格式。
3. 多篇引用的处理更复杂，例如 `[2, 4, 5]` 需要变成多个作者-年份条目的组合。
4. 连续编号范围如 `[33-37]` 需要先展开成 `[33, 34, 35, 36, 37]`，再逐条转换。
5. 文末作者排序规则需要明确：是按第一作者姓氏排序，还是按作者首字母排序；遇到同一作者同一年如何加 `a/b/c` 也需要定义。
6. Word 文档中可能存在普通文本引用、域代码引用、尾注/脚注、参考文献列表等不同结构，需要先识别稿件实际格式。
7. 转换后需要能校验：文中所有引用都能在文末找到对应文献，文末所有文献也确实被文中引用过。

## 3. 目标

构建一个“Word 引文格式切换器”，支持将英文论文稿件从编号制引用转换为作者-年份制引用。

核心目标：

- 读取 Word 文档中的文中编号引用和文末编号参考文献。
- 建立原始编号到参考文献信息的映射。
- 从文末参考文献中解析作者、年份、题名、期刊、卷期、页码等字段。
- 按目标期刊要求重新排序文末参考文献。
- 将文中 `[n]`、`[n, m]`、`[n-m]` 转换为作者-年份引用。
- 输出转换后的 Word 文档、转换报告和问题清单。

## 4. 非目标

第一版不强制解决以下问题：

- 不自动补全缺失 DOI、URL 或数据库元数据。
- 不自动判断目标期刊的全部细节格式，除非用户提供模板或规则。
- 不保证 100% 准确解析所有异常参考文献格式。
- 不直接改写正文语义，例如把 `Since ... was published in 1988 [1]` 自动改成更自然的叙述句，除非后续增加语义润色功能。
- 不处理 LaTeX/BibTeX 原稿，第一阶段聚焦 `.docx`。

## 5. 输入

### 5.1 必需输入

- 一个 `.docx` 稿件文件。
- 目标引用风格说明，至少包括：
  - 文中引用格式：例如 `(Alvin and Murphy, 1988)`。
  - 三位及以上作者格式：例如 `(Wang et al., 2008)`。
  - 多篇引用排序规则：按年份、按作者，或沿用文末排序。
  - 文末参考文献排序规则：按第一作者姓氏字母顺序。

### 5.2 可选输入

- 目标期刊 author guidelines。
- 目标期刊示例文章 PDF 或参考文献样例。
- 用户指定的特殊格式偏好，例如：
  - 两位作者用 `and` 还是 `&`。
  - 多篇引用之间用分号还是逗号。
  - 是否显示页码。
  - 同一作者同一年是否使用 `2020a`、`2020b`。

## 6. 输出

工具应输出：

- 转换后的 `.docx` 文件。
- 一份 Markdown 转换报告。
- 一份异常清单，列出需要人工确认的引用。
- 可选：导出的结构化参考文献数据，例如 `.json` 或 `.csv`。

建议输出文件：

- `manuscript_author_year.docx`
- `reference_switch_report.md`
- `reference_parse_errors.csv`
- `reference_map.json`

## 7. 核心用户流程

1. 用户提供当前 Word 稿件。
2. 工具扫描文档，识别文末参考文献列表。
3. 工具解析原始编号和参考文献信息。
4. 工具扫描正文，识别所有编号制文中引用。
5. 工具建立编号引用到作者-年份引用的转换映射。
6. 工具按目标规则生成新的文末参考文献排序。
7. 工具替换正文中的编号引用。
8. 工具导出新文档和转换报告。
9. 用户根据异常清单人工复核。

## 8. 关键转换规则

### 8.1 文末参考文献解析

原始格式示例：

```text
1. K. L. Alvin, R. J. Murphy, “Variation in fibre and parenchyma wall thickness in culms of the bamboo Sinobambusa tootsik”, IAWA Journal 9 no.4 (1988) 353-361.
2. S. Y. Wang, M. H. Tsai, S. F. Lo, M. J. Tsai, “Effects of manufacturing conditions on the adsorption capacity of heavy metal ions by Makino bamboo charcoal”, Bioresource Technology 99 no.15 (2008) 7027-33.
3. D. S. Tai, C. L. Chen, J. S. Gratzl, “Chemistry of delignification during kraft pulping of bamboos”, Journal of Wood Chemistry and Technology 10 no.1 (1990) 75-99.
```

需要解析为：

```json
{
  "1": {
    "authors": ["Alvin, K. L.", "Murphy, R. J."],
    "year": "1988",
    "title": "Variation in fibre and parenchyma wall thickness in culms of the bamboo Sinobambusa tootsik",
    "journal": "IAWA Journal",
    "volume": "9",
    "issue": "4",
    "pages": "353-361"
  }
}
```

### 8.2 文末排序

默认排序规则：

1. 按第一作者姓氏字母顺序排序。
2. 第一作者相同，按第二作者姓氏排序。
3. 作者完全相同，按年份升序排序。
4. 同一作者组同一年，按题名字母顺序排序，并给年份加 `a`、`b`、`c`。

待确认点：

- 用户说“按作者首字母排序”，实际投稿规范可能是“按第一作者姓氏字母顺序排序”。需要在实现时允许用户确认或传入期刊规则。

### 8.3 文中单篇引用

原始：

```text
Since the first study on bamboo materials was published in 1988 [1], the field has undergone 38 years...
```

目标：

```text
Since the first study on bamboo materials was published in 1988 (Alvin and Murphy, 1988), the field has undergone 38 years...
```

如果一篇文献有三位及以上作者：

```text
(Wang et al., 2008)
```

### 8.4 文中多篇引用

原始：

```text
While bamboo charcoal proved effective in adsorbing pollutants [2, 4, 5], it paradoxically contributes...
```

目标示例：

```text
While bamboo charcoal proved effective in adsorbing pollutants (Wang et al., 2008; Author et al., 2010; Author and Author, 2012), it paradoxically contributes...
```

默认多篇排序规则：

1. 先按年份升序。
2. 年份相同则按第一作者姓氏排序。

但如果目标期刊要求按文末参考文献顺序排列，则应支持切换。

### 8.5 连续编号范围

原始：

```text
key research themes, and future directions in bamboo materials research [33-37].
```

处理步骤：

1. 展开为 `[33, 34, 35, 36, 37]`。
2. 分别查找每个编号对应的作者和年份。
3. 按目标规则排序。
4. 合并为作者-年份引用。

目标示例：

```text
key research themes, and future directions in bamboo materials research (Author, 2018; Author et al., 2019; Author and Author, 2020; Author et al., 2021; Author, 2022).
```

## 9. 需要识别的引用模式

工具需要识别以下正文引用模式：

- `[1]`
- `[1, 2]`
- `[1,2]`
- `[1, 2, 5]`
- `[1-3]`
- `[1, 3-5, 8]`
- `[33–37]`，包含 en dash
- `[33—37]`，包含 em dash
- 句尾引用：`... [1].`
- 句中引用：`... [1], ...`
- 同一句多个引用：`[1] ... [2, 3]`

## 10. 需要人工复核的情况

以下情况应进入异常清单，不建议静默转换：

- 文中引用编号在文末参考文献中不存在。
- 文末参考文献编号重复。
- 参考文献缺少年份。
- 参考文献作者解析失败。
- 同一编号对应的参考文献跨多段，无法稳定识别边界。
- 文中出现类似 `[Figure 1]`、`[Table 2]`、`[Equation 3]` 的非参考文献方括号内容。
- 文献实际作者为机构作者，例如 `World Bank`、`FAO`。
- 同一作者同一年多篇文献需要区分 `a/b/c`。
- 引用是叙述式引用，可能更适合 `Alvin and Murphy (1988)` 而非 `(Alvin and Murphy, 1988)`。

## 11. Word 文档处理要求

### 11.1 格式保留

转换后应尽量保留：

- 段落结构。
- 字体、字号、斜体、粗体。
- 标题层级。
- 表格和图注。
- 文末参考文献所在章节标题。

### 11.2 引用替换粒度

优先只替换正文中的编号引用文本，不大范围重写段落。

如果 Word 中的引用由域代码、EndNote、Zotero、Mendeley 等插件生成，应先检测并提示：

- 是否转为纯文本后再处理。
- 是否保留域代码并通过文献管理器切换样式。

## 12. 转换报告要求

转换报告至少包含：

- 输入文件名。
- 输出文件名。
- 识别到的参考文献总数。
- 识别到的文中引用总数。
- 成功转换的引用数量。
- 未转换或需复核的引用数量。
- 文末参考文献排序前后映射表。
- 编号到作者-年份的映射表。
- 异常列表。

示例映射：

| 原编号 | 作者-年份 | 文末新排序位置 | 状态 |
| --- | --- | --- | --- |
| 1 | Alvin and Murphy, 1988 | 1 | 成功 |
| 2 | Wang et al., 2008 | 24 | 成功 |
| 33 | Author et al., 2019 | 7 | 需复核：作者解析不确定 |

## 13. 验收标准

第一版可接受标准：

- 能处理普通 `.docx` 中的纯文本编号制引用。
- 能正确解析形如 `1. Author, “Title”, Journal volume no.issue (year) pages.` 的文末参考文献。
- 能替换正文中的 `[n]`、`[n, m]`、`[n-m]`。
- 能按第一作者姓氏字母顺序重排文末参考文献。
- 能生成转换报告。
- 对解析失败的条目不强行猜测，而是写入异常清单。

建议准确率目标：

- 对格式统一的参考文献，字段解析成功率不低于 95%。
- 对文中编号引用，识别召回率不低于 98%。
- 对无法确认的情况，宁可标记复核，不做静默错误替换。

## 14. 未来增强

后续可增加：

- 支持直接读取和写入 CSL 样式。
- 支持从 DOI、Crossref、OpenAlex 补全参考文献元数据。
- 支持自动生成 BibTeX、RIS、EndNote XML。
- 支持叙述式引用识别，例如将 `Alvin and Murphy (1988)` 与括号式引用区分。
- 支持按目标期刊 PDF 样例自动推断引用格式。
- 支持中文 GB/T 7714 与 APA、Harvard、Chicago author-date 等格式互转。

## 15. 待用户确认问题

实现前建议确认：

1. 目标期刊的具体引用格式是什么？是否有 author guidelines 链接或示例文章？
2. 文中两位作者写作 `and` 还是 `&`？
3. 三位及以上作者是否一律写 `et al.`？
4. 多篇引用在同一括号内按年份排序，还是按作者排序？
5. 文末参考文献是否需要保留编号？通常作者-年份制不保留编号。
6. 当前 Word 文档中的引用是纯文本，还是 Zotero/EndNote/Mendeley 域代码？
7. 是否允许工具把文档中的引用全部转为纯文本？
8. 是否需要同时输出 BibTeX 或 RIS，方便后续进入文献管理器？

