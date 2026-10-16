# Local generated data — not distributed

`refresh_data.py` creates validated CSV exports here when run with authorized local workbooks. The Power BI semantic model imports the Excel inputs directly. Generated extracts, cached browser data and reports stay local and are ignored by Git. Synthetic public demonstration data lives separately in `demo/`.
