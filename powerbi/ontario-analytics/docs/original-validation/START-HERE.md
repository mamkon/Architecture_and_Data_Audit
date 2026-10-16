# Automated Ontario dashboard & report

## Start here

1. Extract the full ZIP to a short local folder, such as C:\PowerBI\Ontario. Keep all folders together.
2. Install Python 3.10+ if needed, then run `python -m pip install -r requirements.txt` in that folder.
3. Double-click Start-Dashboard.cmd, or run `python serve.py`. Keep the terminal running. The browser opens http://127.0.0.1:8770/.
4. The dashboard and server check the two input workbooks every 60 seconds. Replace files inside input/ using the same filenames and sheet/header structure. After a successful reload the dashboard updates and Automated-Report.html/PDF are regenerated. Browser filters are retained where still valid.
5. Use Open automated report in the header, then Download refreshed PDF report. Report snapshots use the newest year available in each source separately.

An unavailable or changing source causes an explicit error; a browser that already has data marks it STALE DATA instead of presenting it as freshly loaded. New sessions receive an error until source loading succeeds. Files are validated for eight PHO indicators and 29 PHUs; changes to the source geography/schema need review rather than silent acceptance. Automatic refresh does not automatically download new publisher releases or retrain the original model.

## Native Power BI report

Run Configure-Source-Folder.ps1 once after extraction, then open Ontario.pbip in Power BI Desktop and select Refresh. Alternatively, set SourceFolder in Power Query > Edit parameters to input/ with its full path and a trailing backslash. The semantic model reads the Excel workbooks directly; it does not depend on generated CSVs.

The Power BI report retains three editable pages. Select one indicator/procedure and year for regional comparisons. Clear Year for full trends. Blank measures prevent summing or averaging incompatible rates and medians.

The local browser automation does NOT make Power BI Desktop auto-refresh. Desktop refresh remains an explicit action. Scheduled Power BI Service refresh is not configured; a service setup needs an appropriate workspace, source/gateway access, credentials and an approved schedule. No scheduled task, service account or public deployment has been created.

## Publisher colours

PHO pages: purple #693A77, blue #0F80A7 and teal #008184.
CIHI pages: teal #00A199, dark teal #29585F and orange #ED7024.
These values were observed in the publishers' own web styles/logo. See PublisherColours.json for exact URLs. They are not a claimed complete brand manual. The report is independent research; no affiliation or endorsement is implied.

For native Power BI, import OntarioTheme.json through View > Themes > Browse for themes. Core chart defaults and text colours are also set in the report definition. Publisher/source labels and contrasting colours distinguish series; colour is not the only source identifier.

## Data definitions

The supplied historical files cover PHO 2014–2023 and CIHI 2008–2024. All source rows remain in the preserved-source CSVs. Report facts use age-standardized rates, both sexes, and individual PHUs; provincial PHO aggregates remain separate. CIHI report facts use April–September periods only; FY/Q3Q4 remain in the source extract. Missing/suppressed values are not zero-filled.

No PHU/CIHI geographic join is assumed. Rates and medians are nonadditive. The source file and chart definitions, not refresh timestamps, establish the data period. No school details, student number or personal contact details are included; authorship is retained. Originals outside this package remain unchanged.

## Verification limits

Source parsing and HTTP routes were tested with the supplied workbooks, including metadata-change reload and failure recovery. Native report JSON files pass Microsoft schema checks. Power Query/M refresh, DAX execution and native visual rendering have not been executed in Power BI Desktop here. The HTML dashboard is a browser companion, not a Power BI export. Its tab/filter/calculation behaviour is tested separately.

Nothing is published online. 127.0.0.1 works only on the computer running the server. Source redistribution permissions remain a separate prerequisite for public data hosting.
