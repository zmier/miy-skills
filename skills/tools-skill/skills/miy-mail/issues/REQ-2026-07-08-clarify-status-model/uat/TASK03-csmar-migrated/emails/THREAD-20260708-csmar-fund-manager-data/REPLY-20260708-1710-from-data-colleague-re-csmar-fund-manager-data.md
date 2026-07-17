# Re: CSMAR 基金经理/基金层外部数据可用性与字段需求确认

| Field | Value |
|---|---|
| Thread | THREAD-20260708-csmar-fund-manager-data |
| Direction | inbound |
| Channel | email |
| From | 数据同学 |
| To | 研究设计同学 |
| CC | none |
| Date | 2026-07-08 17:10 Asia/Shanghai |
| Subject | Re: CSMAR 基金经理/基金层外部数据可用性与字段需求确认 |
| Related task | TASK03-research-design-v0 |
| Reply to | EMAIL-20260708-1543-to-data-colleague-csmar-fund-manager-data-request.md |
| Status | received |
| Next action | review returned inventory scope |

## Received Content

可以先确认 CSMAR 中基金经理主表、基金经理-基金任职表、基金基础信息、净值收益、规模份额等模块。fund flow 字段需要看库内是否有直接字段；如果没有，可能需要用规模、份额、净值和收益构造。

## Extracted Commitments / Decisions

- 数据同学会先返回 CSMAR 相关模块和字段 inventory。
- fund flow 可能需要构造，不保证有直接字段。

## Next Action

Review returned inventory scope and decide P0 export tables.
