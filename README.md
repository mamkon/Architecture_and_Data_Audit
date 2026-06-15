# Chronic Disease Burden and Healthcare Access Equity in Ontario

**CIND 820: Big Data Analytics Project**
Mamkon Mercy Oyeleke | Student Number: 501279489 | Toronto Metropolitan University

## Project Summary

This project investigates whether Ontario regions with the highest chronic
disease burden also face the greatest gaps in access to timely healthcare.
It combines two public datasets, chronic disease prevalence/incidence from
Public Health Ontario and wait times for priority procedures from the
Canadian Institute for Health Information, to identify regions where
burden and access constraints compound each other, supporting evidence-based
resource allocation by Ontario Health.

**Research questions:**
- **RQ1**: How do chronic disease prevalence/incidence rates vary across
  Ontario regions?
- **RQ2**: How have chronic disease-related hospitalizations and utilization
  changed over 2014–2023?
- **RQ3**: Do regions with the highest chronic disease burden also face the
  longest wait times for priority procedures?

## Datasets

| Dataset | Source | Licence | Access date |
|---|---|---|---|
| Chronic Disease Incidence and Prevalence Snapshot (2014–2023) | [Public Health Ontario](https://www.publichealthontario.ca/en/Data-and-Analysis/Chronic-Disease/Chronic-Disease-Incidence-Prevalence) | Open Government Licence, Ontario | May 2026 |
| Wait Times for Priority Procedures in Canada, 2025 (2008–2024) | [CIHI](https://www.cihi.ca/en/wait-times-for-priority-procedures-in-canada-2025) | CIHI non-commercial/research use | Jun 2026 |

## Repository Structure

```
Architecture_and_Data_Audit/
├── README.md
├── LICENSE
├── data/
│   ├── raw/                          # original downloaded files
│   └── processed/                    # cleaned/joined outputs
├── notebooks/
│   ├── 01_pho_eda.ipynb              # PHO profiling (Milestone 2)
│   ├── 02_cihi_eda.ipynb             # CIHI profiling (Milestone 2)
│   └── 03_pho_cihi_join_rq3.ipynb    # regional join + RQ3 preliminary test
├── outputs/
│   ├── figures/                      # 12 figures (fig1-fig12)
│   └── tables/                       # summary stats, RQ3 join table
├── reports/
│   └── CIND820_Milestone2_Interim_Report.pdf   # generated EDA/interim report
└── docs/
    ├── privacy_and_ethics_check.md
    ├── ai_use_declaration.md
    └── pipeline_diagram.png
```

## Generated EDA Report

The full Milestone 2 Interim Report, including the methodological rationale,
data profiling, RQ3 preliminary test, architecture diagrams, and reproducibility
section, is available as a PDF at
[`reports/CIND820_Milestone2_Interim_Report.pdf`](reports/CIND820_Milestone2_Interim_Report.pdf).
It was generated from the analysis in `notebooks/01_pho_eda.ipynb`,
`notebooks/02_cihi_eda.ipynb`, and `notebooks/03_pho_cihi_join_rq3.ipynb`.

## How to Run

Each notebook can be opened directly in Google Colab. The first code cell in
each notebook clones this repository when running in Colab, so the relative
`../data/raw/` and `../outputs/` paths resolve correctly without any manual
setup:

- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mamkon/Architecture_and_Data_Audit/blob/main/notebooks/01_pho_eda.ipynb) `01_pho_eda.ipynb`
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mamkon/Architecture_and_Data_Audit/blob/main/notebooks/02_cihi_eda.ipynb) `02_cihi_eda.ipynb`
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mamkon/Architecture_and_Data_Audit/blob/main/notebooks/03_pho_cihi_join_rq3.ipynb) `03_pho_cihi_join_rq3.ipynb`

Each notebook reads directly from `data/raw/` and is self-contained, but the
logical order is 01, then 02, then 03.

To run locally instead, from the `notebooks/` directory:

```bash
pip install pandas numpy matplotlib seaborn openpyxl jupyter
jupyter notebook
```

## Status (Milestone 2)

- ✅ PHO dataset fully profiled: 39,220 rows, 8 indicators, 37 geographies,
  2014–2023. Suppression rate 0.018%. Composite burden score built for all
  regions.
- ✅ CIHI dataset fully profiled: 18,956 rows, 14 indicators, 11 provinces,
  2008–2024. Ontario provincial trends and regional (Hip/Knee replacement)
  breakdown completed.
- ✅ **Key structural finding**: PHO's geography field includes 7 regional
  rollups (Central East, Central West, East, North East, North West, South
  West, Toronto) that map cleanly onto CIHI's 6 Ontario health regions
  (Central East + Central West → Central; South West → West). This mapping
  is the join key for RQ3.
- ✅ RQ3 preliminary test complete: composite chronic disease burden score
  vs. average Hip+Knee replacement wait time across Ontario's 6 regions,
  r = 0.61 (n = 6). North East Region is highest on both burden (0.88) and
  near-highest on wait time (142 days); Toronto Region is lowest on both
  (0.31 burden, 48 days).
- ⏳ Next (Milestone 3): extend the regional join across multiple years,
  test statistical significance with a larger effective sample, and explore
  whether the 28 individual PHU records can be approximately assigned to one
  of the 6 CIHI regions for finer-grained analysis.

## GenAI Declaration

See [`docs/ai_use_declaration.md`](docs/ai_use_declaration.md) for the full
AI use disclosure, including specific failure-mode mitigations applied this
milestone.

## Privacy and Ethics

See [`docs/privacy_and_ethics_check.md`](docs/privacy_and_ethics_check.md)
for the full privacy and ethics audit.

## References

Full reference list with APA citations is in Chapter 2 (Milestone 2 Interim
Report), section "References".
