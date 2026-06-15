# Privacy and Ethics Check

CIND 820: Big Data Analytics Project
Mamkon Mercy Oyeleke | Student Number: 501279489

## Personal Health Information

Both datasets used in this project are fully aggregated at the population
level. Neither dataset contains individual patient names, health card
numbers, dates of birth, postal codes, or any other directly identifiable
attributes. No personal health information as defined under Ontario's
Personal Health Information Protection Act (PHIPA) is present in either
dataset. The privacy risk of this project is assessed as low.

Having now worked directly with both datasets at the row level (39,220 PHO
rows, 18,956 CIHI rows), this assessment is confirmed: every row is an
aggregate count, rate, or wait-time statistic at the geography-year-indicator
level, with no individual-level fields anywhere in either file.

## Sensitive Attributes

The PHO dataset includes breakdowns by age group and sex. In this aggregated
context these are analytical dimensions, not sensitive identifiers. Neither
dataset includes race, ethnicity, income level, or immigration status. Where
socioeconomic or equity context is introduced in interpretation, it draws on
published literature (see Chapter 2, section 2.1) rather than being derived
from the datasets themselves.

## Equity and Ethical Framing

Regional analysis of disease burden and healthcare access carries a risk of
stigmatizing specific communities or regions if findings are communicated
without adequate context. This project commits to equity-informed
interpretation throughout: regional differences are framed as indicators of
systemic resource distribution, not as reflections of community behaviour.
No causal claims are made beyond what the data can support. Correlations
(e.g., the r = 0.61 burden-vs-wait-time relationship across Ontario's six
health regions) are explicitly described as preliminary signals based on a
small sample (n = 6), not statistical findings.

## Licensing

| Dataset | Licence | Attribution required |
|---|---|---|
| PHO Chronic Disease Incidence and Prevalence Snapshot | Open Government Licence, Ontario | Yes |
| CIHI Wait Times for Priority Procedures, 2025 | CIHI non-commercial/research use | Yes |

Both licences explicitly permit academic and research use. No ethics board
approval is required for publicly available, aggregated government data at
this level of analysis.
