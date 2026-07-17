# CSMAR 基金经理相关数据需求确认邮件草稿

| Field | Value |
|---|---|
| Thread | THREAD-20260708-csmar-fund-manager-data |
| Direction | outbound |
| Channel | email |
| From | 研究设计同学 |
| To | 数据同学 |
| CC | none |
| Date | 2026-07-08 15:43 Asia/Shanghai |
| Subject | CSMAR 基金经理/基金层外部数据可用性与字段需求确认 |
| Related task | TASK03-research-design-v0 |
| Reply to | none |
| Status | sent |
| Next action | wait for reply |

## Sendable Body

主题：CSMAR 基金经理/基金层外部数据可用性与字段需求确认

你好，

我们这边基于支付宝「基金经理请回答」数据的 TASK03 research design v0 已经形成了第一版：现有支付宝问答宽表可以先支持“沟通努力”和“回答策略”这些平台内近端反应分析；但如果要进一步做 fund flow / performance / manager career 相关设计，就需要接入 CSMAR 的基金经理、基金和基金公司层数据。

想请你先帮忙做一个小型 inventory，不急着全量拉数：先确认 CSMAR 里哪些表可用、字段覆盖如何、时间范围到哪里、哪些字段适合导出。确认后我们再按优先级做派生表。

## 1. 研究上最需要的 CSMAR 数据

### P0：进入 flow / performance 设计必须有

1. 基金经理主表

希望确认是否有这些字段：

```text
manager_code / manager_id
manager_name
gender
birth_year / age
education / degree / school / major
career_background / resume
fund_company_code
fund_company_name
manager_start_date
manager_end_date
current_status
source_table_name
```

重点是：CSMAR 是否有稳定的基金经理唯一 ID，以及同名基金经理如何区分。

2. 基金经理-基金任职表

希望确认：

```text
manager_code
fund_code
fund_name
fund_company_code
fund_company_name
tenure_start_date
tenure_end_date
is_current_manager
is_lead_manager / manager_role
co_manager_count
```

这个表是连接支付宝回答主体、基金代码和后续 flow/performance 的核心。

3. 基金基础信息表

希望确认：

```text
fund_code
fund_name
fund_company_code
fund_company_name
fund_type
investment_type
active_or_passive
share_class
inception_date
termination_date
benchmark_code / benchmark_name
management_fee
custody_fee
```

后续可能需要限定主动权益、偏股混合、债基、指数基金等样本。

4. 净值、收益和业绩表

希望确认是否有日频或月频：

```text
fund_code
date
nav
adjusted_nav
daily_return
monthly_return
benchmark_return
excess_return
```

如果 CSMAR 有现成风险调整收益、alpha、排名或同类分位，也请一并确认字段。

5. 规模、份额和 fund flow 相关表

希望确认：

```text
fund_code
date / quarter / month
total_net_assets
shares_outstanding
subscription
redemption
net_subscription
fund_flow
```

如果没有直接 flow 字段，也请确认是否可以用规模、份额、净值收益构造近似 flow。

### P1：机制、异质性和控制变量很有用

1. 基金公司主表 / 公司规模

```text
fund_company_code
fund_company_name
company_aum
company_fund_count
company_manager_count
company_rank
ownership_type
```

2. 持有人结构

```text
fund_code
report_date
individual_holder_ratio
institutional_holder_ratio
holder_count
top_holder_ratio
```

如果能拿到个人投资者占比，这对解释支付宝平台沟通反应很重要。

3. 持仓和风格暴露

```text
fund_code
report_date
stock_holding_ratio
bond_holding_ratio
cash_ratio
top10_holding_ratio
industry_exposure
```

4. 基金公告 / 经理变更 / 产品事件

```text
fund_code
event_date
event_type
announcement_title
manager_change_flag
fee_change_flag
purchase_restriction_flag
dividend_flag
```

### P2：如果方便可作为扩展

```text
fund_rating
fund_awards
star_rating
risk_rating
sales_channel_information
marketing_or_advertising_events
```

这些不是当前主线必须，但如果 CSMAR 里有现成表，可以先登记。

## 2. 和支付宝数据的匹配需求

支付宝宽表目前有：

```text
manager_name
inst_name
answer_author_public_id
answer_author_user_id
answer_create_time
question_id
answer_id
```

希望 CSMAR 侧最后能给出一个匹配候选表，字段大致为：

```text
alipay_manager_name
alipay_inst_name
answer_author_public_id
csmar_manager_code
csmar_manager_name
csmar_fund_company_code
csmar_fund_company_name
match_confidence
ambiguity_flag
ambiguity_reason
notes
```

需要特别注意：

- 同名基金经理；
- 基金公司简称、历史名称和品牌名；
- 支付宝展示主体可能是基金经理本人，也可能是基金公司/运营账号；
- 匹配最好结合回答日期，看该基金经理在当时是否任职。

## 3. 时间范围建议

支付宝回答时间范围约为：

```text
2023-05-09 到 2026-06-26
```

CSMAR 如果可行，建议至少取：

```text
2020-01-01 到 CSMAR 当前可用最新日期
```

原因是我们可能需要构造回答前 3/6/12/24 个月的历史收益、规模、flow 和经理任职经验。

## 4. 希望先返回的 inventory

第一步不需要直接交付所有数据。可以先帮忙确认一个字段清单：

```text
csmar_inventory_fund_manager_related.md
```

里面最好包括：

- 可用 CSMAR 模块 / 表名；
- 每张表的关键字段；
- 数据时间范围；
- 频率（日频、月频、季度、事件级）；
- 是否能导出；
- 是否有中文字段名或字段字典；
- 你判断的 P0 / P1 / P2 可得性；
- 可能的缺口或权限限制。

## 5. 如果字段可用，后续希望形成的派生表

后续如果可行，我们希望形成这些研究用表：

```text
csmar_fund_manager_master.csv
csmar_fund_manager_fund_tenure.csv
csmar_fund_basic.csv
csmar_fund_daily_returns.csv
csmar_fund_month_panel.csv
csmar_fund_company_master.csv
csmar_fund_holdings_quarterly.csv
csmar_holder_structure.csv
match_candidates_alipay_manager_to_csmar.csv
csmar_variable_dictionary.md
csmar_coverage_report.md
```

其中最关键的是：

```text
match_candidates_alipay_manager_to_csmar.csv
csmar_fund_manager_fund_tenure.csv
csmar_fund_month_panel.csv
```

## 6. 这批数据会支持的研究设计

有了 CSMAR 后，我们可以把现在的支付宝平台内设计扩展成：

1. 基金经理沟通努力是否预测后续 fund flow。
2. 非工作时间回答是否在短窗口内对应更强申购/赎回变化。
3. 回答策略是否在过往业绩差、回撤大或投资者关注高时更重要。
4. 这种关系是否随基金类型、公司规模、个人投资者占比、基金经理任职经验而变化。

这些设计都需要先确认经理-基金-时间的可连接性，所以 inventory 阶段最重要的是“能不能稳定匹配”和“外部数据频率够不够”。

谢谢！辛苦你先帮我们看一下 CSMAR 里哪些能拿、哪些需要调整口径。
