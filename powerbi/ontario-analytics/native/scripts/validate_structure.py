"""Check editable native source structure. Does not run Desktop in CI."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
report=R/'OntarioProfessional.Report';model=R/'Ontario.SemanticModel/definition'
pages=json.loads((report/'definition/pages/pages.json').read_text(encoding='utf-8'))
assert pages['pageOrder']==['Disease','Regional','Access']
assert len(list(report.rglob('visual.json')))==38
tables={p.stem:p.read_text(encoding='utf-8') for p in (model/'tables').glob('*.tmdl')}
assert len(tables)==11
assert sum(len(re.findall(r'(?m)^\tmeasure ',s)) for s in tables.values())==44
assert len(re.findall(r'(?m)^relationship ',(model/'relationships.tmdl').read_text(encoding='utf-8')))==10
for p in report.rglob('visual.json'):
 d=json.loads(p.read_text(encoding='utf-8'))
 assert d['visual']['visualType'] not in ['image']
 for state in d['visual'].get('query',{}).get('queryState',{}).values():
  for projection in state.get('projections',[]):
   f=projection['field'];kind='measure' if 'Measure' in f else 'column';f=f.get('Measure',f.get('Column'))
   table=f['Expression']['SourceRef']['Entity'];name=f['Property'];assert table in tables
   pattern=r'(?m)^\t'+kind+r" (?:'"+re.escape(name)+r"'|"+re.escape(name)+r')(?:\s|=|$)'
   assert re.search(pattern,tables[table]),(table,name)
for p in R.rglob('*'):
 if p.is_file():
  assert p.suffix.lower() not in ['.xlsx','.csv','.pbix','.abf','.zip']
  if p.suffix.lower() in ['.tmdl','.json','.m','.dax','.md','.ps1']:
   s=p.read_text(encoding='utf-8');assert not re.search(r'[A-Z]:\\Users\\',s,re.I),str(p)
print('PASS: 3 native pages, 38 native visuals, 11 tables, 10 relationships, 44 measures and source-only publication guards.')
