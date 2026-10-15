# Original-source Ontario data connector

A local read-only JSON API and browser explorer using PHO's actual InstantAtlas JSON resource and CIHI's official 2026 release workbook. These are publisher downloads, not documented official REST APIs. The adapter supplies a consistent API over them. No API key is needed.

## Run

From the repository root with Python 3.10+:

```
python -m pip install -r live_api/requirements.txt
python live_api/server.py
```

Open http://127.0.0.1:8765. The first request downloads and validates the source. Source records are cached in memory for 24 hours; restarting clears the cache. It does not poll continuously, retrain models, or change the original analysis. A failed refresh returns 502 instead of silently serving old results. The explorer clears prior results before each request.

## API

- `/health`: process status, not upstream availability.
- `/v1/sources`: publisher pages, fixed downloads, release labels and methodology link.
- `/v1/pho/options`: indicators, measures, geography IDs/names, years.
- `/v1/pho/records?indicator=Prevalence%20of%20asthma&measure=Age-standardized%20rate%20(both%20sexes)&geography_id=3895&year=2024`
- `/v1/cihi/options`: indicators, metrics, Ontario regions and years.
- `/v1/cihi/records?indicator=Hip%20Replacement&metric=50th%20percentile&region=Toronto%20Region&year=2025`

Responses include the source, retrieval timestamp, count and records. `value: null` means the published value was missing, suppressed or nonnumeric; `raw_value` retains the published marker. PHO confidence intervals/suppression flags and CIHI units are preserved. No zero-filling, geography joins, predictions or causal claims are added. Read PHO technical notes for units and changing disease definitions, and CIHI methodology for reporting periods and regional definitions.

CIHI's `year` is the original reporting-period label, retained as a string, including `2019FY` and `2019Q3Q4`. These must not be collapsed into a single calendar year or averaged together. PHO's `year` is a calendar-year integer. All filters compare their string representations exactly.

## Source differences and release changes

The existing research used PHO 2014–2023 and CIHI 2008–2024. The verified downloads now cover PHO 2015–2024 and CIHI 2008–2025. They must not be mixed into the original findings without revalidation. Download URLs are pinned to verified resources, not guessed dynamically; inspect new releases before updating constants and release labels. PHO's dashboard resource has no stability guarantee. Schema validation intentionally fails if feature lengths or CIHI headers change.

## Public hosting is not configured

This server binds only to localhost. GitHub Pages cannot execute Python. No production API URL, hosting account, CORS proxy, keys or public data mirror is fabricated. The existing portfolio and project notebooks remain unchanged. A public endpoint and portfolio integration can follow after selecting hosting and confirming redistribution rights.

PHO's website terms restrict copying/redistribution except as permitted; the general personal non-commercial download permission is not a blanket licence to republish its data. This connector does not redistribute downloaded data in Git or add a public cache. CIHI also has source-specific terms. Confirm appropriate permission/licensing before deploying a public data service. Do not assume the historical repository's licence statement applies to the current release.

Sources:
- https://www.publichealthontario.ca/en/data-and-analysis/chronic-disease/chronic-disease-incidence-prevalence
- https://www.publichealthontario.ca/en/About/Terms-of-Use
- https://www.cihi.ca/en/wait-times-in-canada-2026
- https://www.cihi.ca/en/about-cihi/terms-of-use

