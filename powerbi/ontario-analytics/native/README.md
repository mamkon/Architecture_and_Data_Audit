# Ontario Analytics — verified native Power BI report

## Open your report

The privately delivered PBIX contains actual historical data. No PBIX, source workbooks or cached observations are distributed in this public folder. Obtain your own authorized copies before refresh.

**Editable project:** open `Ontario.pbip` or `Ontario-Professional.pbip`. Both reference `OntarioProfessional.Report` and `Ontario.SemanticModel`. Keep the entire folder structure together. Desktop saved the active semantic model in its supported TMDL format under `Ontario.SemanticModel/definition/`; the original BIM and complete working packages are preserved in the private backup.

If the package is moved, close the PBIP first, run `Configure-Source-Folder.ps1`, reopen and choose **Refresh → Schema and data**. If opening the PBIX at a new location, use **Transform data → Edit parameters → SourceFolder** to point to this package's `input` folder, ending in a backslash. The configuration script updates the PBIP source, not the embedded PBIX copy. An initial project load may require a full refresh before measure visuals render. No sign-in or external API is required for local source imports.

## Three genuine native pages

1. **Disease Overview:** indicator/year slicers, Ontario and unweighted PHU-median rate cards, change since 2014, PHU coverage, native historical trend and yearly table, and a DAX narrative.
2. **PHU Comparisons:** 29-PHU ranking, a native analytics reference line bound dynamically to the selected Ontario rate, available-rate/gap/confidence-interval table, comparison cards and contextual narrative. Rankings and tables can scroll; hover a bar for rate, reference, gap, interval and rank. A selected bar cross-filters other visuals; click it again to clear.
3. **Healthcare Access:** procedure/year slicers, median/P90/benchmark cards, native trend chart, regional chart/table and explanatory narrative. Regional estimates are available for hip and knee replacement where published; missing results are not zero.

Use the bottom page tabs, or Ctrl+click the native page navigator buttons while editing in Desktop. Charts, cards, tables, slicers and navigation are actual Power BI objects; no chart image is used as a native visual.

## What was verified in Desktop

On 2026-10-16, the project was opened, actual Excel sources were loaded, all three final pages rendered, selected measures were compared to source calculations, the year slicer and narrative recalculation were exercised, and the `.pbix` was saved through Desktop. `Verification.json` records the checks and limits. This is spot verification, not a claim that every possible filter combination was tested.

Private spot checks compared disease rates, PHU coverage, reference gaps and procedure waits with the supplied source workbooks. The detailed numerical check record remains in the private delivery; this public source folder does not publish those observations.

## Model, sources and accuracy

The original 13 DAX measures, ten valid relationships and analytical transformations are preserved. Additional report measures and two intentionally disconnected source-specific year selectors bring the active model to 44 measures and eleven tables. Historical trend axes remain independent of the comparison-year selector. The Excel imports infer real sheet dimensions and project the eight CIHI columns early to avoid the workbook's oversized formatting range.

PHO source: historical chronic-disease snapshot, 2014–2023, age-standardized rates for both sexes. Rates are per 100,000; the unweighted median of PHUs is not the Ontario population rate. Incidence and prevalence are distinct measures.

CIHI source: 2025 wait-times workbook, 2008–2024. Report facts use April–September periods only; FY/Q3Q4 are excluded from comparisons. Medians and 90th percentiles are separate statistics. Benchmark percentages refer to procedure-specific publisher standards. No PHU-to-CIHI geographic join, new prediction, causal claim or individual patient wait forecast is implied.

Original publisher pages: https://www.publichealthontario.ca/en/data-and-analysis/chronic-disease/chronic-disease-incidence-prevalence and https://www.cihi.ca/en/wait-times-for-priority-procedures-in-canada-2025.

## Public source and browser companion

This public folder preserves the complete native report definitions and active model schema, transformations and DAX. It excludes publisher observations, workbooks, model cache, PBIX, real-data previews and machine-specific paths. The private package is separate. Put authorized workbooks under `input/` using the exact filenames referenced in Power Query, then configure SourceFolder and refresh.

[Browser companion](https://mamkon.github.io/ontario-analytics/): synthetic initial values, with local-only authorized actual-data JSON import. This is not a live Power BI connection. See the parent [publication review](../docs/DATA-AND-PUBLICATION.md) before any public real-data release. No publisher endorsement is implied.
