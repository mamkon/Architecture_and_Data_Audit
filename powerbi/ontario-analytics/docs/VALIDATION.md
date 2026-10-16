# Validation status

## Current package checks

Run `python scripts/validate_public_package.py` from this folder. It checks both PBIP references; both three-page report definitions and their visual files; native model field/measure references; the nine-table, ten-relationship and thirteen-measure structure; the content-version marker; synthetic demo provenance; and the absence of prohibited data/cache files and known private path/identifier patterns in the presentation folder.

Run `node scripts/test_demo.cjs` to exercise initial rendering, all three tabs, disease/year selection, procedure selection, missing synthetic values and absent regional results in a lightweight DOM harness. This checks browser logic, not real-browser layout or accessibility conformance. Three preview PNGs were generated from the same synthetic JSON.

## Retained historical validation

`original-validation/Validation.json` records original workbook hashes, historical row counts and source-grain checks. `original-validation/Validation.md` and `START-HERE.md` are preserved provenance, not current public opening instructions. Microsoft report-schema checks previously passed, but did not catch the incorrect content-version value later corrected to 2.0.0. The separate `definition.pbir` entry version remains 4.0.

## Explicit limits

Native Power Query refresh, DAX execution, successful Desktop materialization of all three pages and end-to-end real-source refresh have not been verified here. The screenshot supplied before this organization task showed a blank native canvas. Opening the corrected project in Desktop and confirming each report tab remains necessary. The public demo is synthetic and is not an API deployment, real-time health data, model prediction or native Power BI screenshot. Power BI Service scheduled refresh is not configured.
