# Typed Arrow Ledger

| arrow_id | from_node | to_node | primary_arrow_type | secondary_type | A-to-B relation | evidence_ids | external_need |
|---|---|---|---|---|---|---|---|
| A001 | X1 | Y0 | finding-contribution | gap-contribution | research motivation + gap to overall contribution | G1-G4 | yes |
| A002 | X2 | Y0 | finding-contribution | policy/contribution elevation | empirical finding to paper contribution | P1-P8 | yes |
| A003 | P9 | Y0 | finding-contribution | policy-implication | contribution/policy claims to overall worth | P9a-P9c | yes |
| A004 | G1 | X1 | institutional-context | policy-document | institutional facts to research importance | E-X1-POL-1; E-X1-POL-2; E-X1-EX-1 | yes |
| A005 | G2 | X1 | theory-motivation | mechanism-ambiguity | opposing mechanisms to research question | E-X1-MECH-1 to 3 | no |
| A006 | G3 | X1 | gap-contribution | citation-verification | cited literature to gap | E-CIT-GAP-* | yes |
| A007 | G4 | X1 | gap-contribution | contribution-positioning | gap to contribution | E-X1-CONTR-1; E-CIT-CONTR-* | yes |
| A008 | P1 | X2 | treatment-definition | construct-measure | treatment definition to X | P1a-P1c | yes |
| A009 | P2 | X2 | theory-mechanism | mechanism-claim | theory to expected X->Y direction | P2a-P2c | yes |
| A010 | P3 | X2 | construct-measure | construct-level-fit | KV proxy to disclosure quality | E-YDEF-*; E-DESC-1 | yes |
| A011 | P4 | X2 | sample-mechanism-fit | timing-fit | sample/window to DID spillover test | P4a-P4c | no |
| A012 | P5 | X2 | identification-causal | DID-method | design/tests to causal claim | P5a-P5c | yes |
| A013 | P6 | X2 | result-finding | construct-measure | coefficient to finding | P6a-P6b | no |
| A014 | P7 | X2 | mechanism-claim | mechanism-exclusion | mechanism tests to mechanism story | P7a-P7c | yes |
| A015 | P8 | X2 | robustness-threat | boundary-condition | robustness/boundary to finding scope | P8a-P8h | yes |
| A016 | P1a | P1 | treatment-definition | construct-definition | operational rule to active disclosure violation | E-XDEF-* | yes |
| A017 | P1b | P1 | treatment-timing | timing-fit | Peerdumy/POST to treatment timing | E-DID-* | no |
| A018 | P1c | P1 | sample-mechanism-fit | baseline-fit | exclusion rules to peer spillover scope | E-SAMPLE-3 to 5 | no |
| A019 | P2a | P2 | theory-mechanism | signal-theory | signal claim to mechanism | E-THEORY-SIGNAL-1; citations | yes |
| A020 | P2b | P2 | mechanism-claim | reputation-competition | reputation logic to mechanism | E-THEORY-REP-1; citations | yes |
| A021 | P2c | P2 | mechanism-claim | market-pressure | attention/supervision to mechanism | E-THEORY-PRESS-1; citations | yes |
| A022 | P4a | P4 | data-source | sample-design | sample period/data source to data basis | E-SAMPLE-1; E-SAMPLE-7 | no |
| A023 | P4b | P4 | sample-design | sample-mechanism-fit | rules to clean event sample | E-SAMPLE-2 to 6 | no |
| A024 | P4c | P4 | sample-statistic | reporting-qc | sample size/winsorization to sample clarity | E-SAMPLE-8; E-SAMPLE-9; E-DESC-2 | no |
| A025 | P5a | P5 | identification-causal | cluster-level-fit | model/FE/SE to estimation validity | E-MODEL-* | yes |
| A026 | P5b | P5 | identification-causal | pretrend-test | pretrend table to DID assumption | E-PRETREND-* | yes |
| A027 | P5c | P5 | identification-causal | staggered-did | stacked DID/Bacon to treatment heterogeneity threat | E-ROB-STACK-*; E-ROB-BACON-1 | yes |
| A028 | P6a | P6 | result-finding | statistical-result | table coefficient to main result | E-MAIN-1 to 4 | no |
| A029 | P6b | P6 | result-finding | numerical-interpretation | coefficient/mean ratio to economic magnitude | E-MAIN-5; E-DESC-1 | no |
| A030 | P7a | P7 | mechanism-claim | table-text-conflict | CAR/reputation split to reputation mechanism | E-MECH-CAR-*; E-MECH-REP-* | yes |
| A031 | P7b | P7 | mechanism-claim | proxy-validity | high attention groups to market pressure | E-MECH-PRESS-* | yes |
| A032 | P7c | P7 | mechanism-exclusion | null-result-reversal | nonsignificant/regulatory-distance evidence to excluding info transmission | E-MECH-INFO-* | no |
| A033 | P8a | P8 | robustness-threat | matching | matching/entropy to robustness | E-ROB-MATCH-* | yes |
| A034 | P8b | P8 | robustness-threat | policy-common-factor | excluding policy-affected industries to common-factor threat | E-ROB-COMMON-* | yes |
| A035 | P8c | P8 | robustness-threat | Oster/alt-measure/timing | Oster/DA/POST_Month to robustness | E-ROB-OSTER-*; E-ROB-ALT-* | yes |
| A036 | P8d | P8 | robustness-threat | placebo | placebo distribution to random/policy threat | E-ROB-PLACEBO-* | yes |
| A037 | P8e | P8 | boundary-condition | event-firm-status | leader status to stronger effect boundary | E-HET-LEADER-* | yes |
| A038 | P8f | P8 | boundary-condition | violation-type | self-involvement/severity to boundary | E-HET-OWN-*; E-HET-MON-* | no |
| A039 | P8g | P8 | construct-level-fit | boundary-condition | external finance dependence proxy to boundary | E-HET-RELY-*; E-CIT-RELY-1 | yes |
| A040 | P8h | P8 | construct-level-fit | boundary-condition | HHI competition proxy to boundary, including reverse low-competition sign | E-HET-COM-*; E-CIT-COM-* | yes |
| A041 | P9a | P9 | finding-contribution | literature-contribution | specific result to disclosure antecedents literature contribution | E-CONTR-1; E-CIT-CONTR-1 | yes |
| A042 | P9b | P9 | finding-contribution | spillover-literature-contribution | specific result to negative disclosure/peer spillover contribution | E-CONTR-2; E-CIT-CONTR-2; E-CIT-CONTR-3 | yes |
| A043 | P9c | P9 | policy-implication | regulatory-policy | empirical finding to policy recommendations | E-POLICY-1 to 3 | yes |
