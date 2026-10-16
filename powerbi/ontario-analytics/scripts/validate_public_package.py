"""Structural and publication checks. Does not execute Power Query/DAX/Desktop."""
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
model=read(ROOT/'Ontario.SemanticModel/model.bim')['model']
tables={t['name']:t for t in model['tables']}
assert len(tables)==9
assert len(model['relationships'])==10
assert sum(len(t.get('measures',[])) for t in tables.values())==13
for rel in model['relationships']:
    for side in ['from','to']:
        assert rel[side+'Table'] in tables
        assert rel[side+'Column'] in {c['name'] for c in tables[rel[side+'Table']]['columns']}
for entry,folder in [('Open-Dashboard.pbip','OntarioDashboard.Report'),('Ontario.pbip','Ontario.Report')]:
    assert read(ROOT/entry)['artifacts'][0]['report']['path']==folder
    report=ROOT/folder
    assert read(report/'definition.pbir')['datasetReference']['byPath']['path']=='../Ontario.SemanticModel'
    assert read(report/'definition/version.json')['version']=='2.0.0'
    page_order=read(report/'definition/pages/pages.json')['pageOrder']
    assert page_order==['Disease','Regional','Access']
    visuals=list(report.rglob('visual.json'))
    assert len(visuals)==26
    for page in page_order:
        assert (report/'definition/pages'/page/'page.json').is_file()
    for p in visuals:
        d=read(p)
        for state in d['visual'].get('query',{}).get('queryState',{}).values():
            for projection in state['projections']:
                field=projection['field'];is_measure='Measure' in field
                field=field.get('Measure',field.get('Column'))
                assert field is not None
                table=tables[field['Expression']['SourceRef']['Entity']]
                assert field['Property'] in {f['name'] for f in table.get('measures' if is_measure else 'columns',[])}

demo=read(ROOT/'demo/synthetic-data.json')
assert len(demo['indicators'])==8
assert {r['Geography'] for r in demo['pho']}=={f'Demo PHU {n:02d}' for n in range(1,30)}
assert all(r['Region'].startswith('Demo Health Region ') for r in demo['regionWait'])
html=(ROOT/'demo/index.html').read_text(encoding='utf-8')
assert 'SYNTHETIC DATA ONLY' in html
assert json.loads(re.search(r'const DATA=(.*?);\s*const \$',html,re.S)[1])==demo
assert not re.search(r'\bfetch\s*\(|XMLHttpRequest|https?://127\.0\.0\.1',html)
assert all((ROOT/'previews'/name).is_file() for name in ['Preview-01-Disease.png','Preview-02-PHU.png','Preview-03-Access.png'])
bad=[]
for p in ROOT.rglob('*'):
    if not p.is_file():continue
    if p.suffix.lower() in {'.xlsx','.xls','.csv','.pdf','.pbix','.pbit','.zip'} or '.pbi' in p.parts or '__pycache__' in p.parts:
        bad.append(str(p.relative_to(ROOT)))
    if p.suffix.lower() in {'.json','.md','.m','.dax','.py','.ps1','.html','.cmd','.pbip','.pbir','.bim','.pbism','.tmdl'}:
        text=p.read_text(encoding='utf-8')
        # Generic path/identifier guards; no private identifier values belong in source.
        forbidden=[':'+chr(92)+'Users'+chr(92),'One'+'Drive'+chr(92)]
        assert not any(token.lower() in text.lower() for token in forbidden),str(p)
        assert not re.search(r'student\s+(?:number|id)\s*[:#]',text,re.I),str(p)
assert not bad,f'Unexpected private/generated files: {bad}'
print('PASS: both complete reports, 3 pages each, 26 visuals each, 9 tables, 10 relationships, 13 measures, synthetic payload parity and publication guards.')
