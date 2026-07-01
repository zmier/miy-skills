# Canonical Node Ledger

| node_id | label | type | depth | parent_id | child_ids | evidence_ids | source_links | status |
|---|---|---|---:|---|---|---|---|---|
| Y | 论文贡献成立 / 值得发表 | root-claim | 0 |  | X1; X2; P9 |  |  | complete |
| X1 | 问题有意义 | major-claim | 1 | Y | G1; G2; G3 |  |  | complete |
| X2 | 作者证明具体核心发现 | major-claim | 1 | Y | P1; P2; P3 |  |  | complete |
| P6 | 主结果支持核心发现 | middle-claim | 2 | X2 | P6.1; P6.2 |  |  | complete |
| P6.1 | 表4核心交互项显著为负 | subclaim | 3 | P6 |  | E-R4-1; E-R4-2 | [[manuscript#Table 4]] | complete |
| E-R4-1 | 表4列(1)：Peerdumy×POST = ... | minimal-evidence | 4 | P6.1 |  |  | [[manuscript#Table 4]] | needs-table-visual-qc |

## Status Values

```text
complete
needs-children
needs-evidence
needs-anchor
abstract-evidence-leaf
needs-table-visual-qc
```

