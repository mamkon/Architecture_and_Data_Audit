import importlib.util
from io import BytesIO
import json
from pathlib import Path
import unittest
import openpyxl

spec = importlib.util.spec_from_file_location('server', Path(__file__).with_name('server.py'))
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)


class SourceTests(unittest.TestCase):
    def test_pho_alignment_and_suppression(self):
        doc = {'geographies': [{'id': 'Public_Health_Units', 'features': [{'id': 'a', 'name': 'A'}, {'id': 'b', 'name': 'B'}], 'comparisonFeatures': [{'id': '1', 'name': 'Ontario'}], 'themes': [{'name': 'Asthma', 'indicators': [{'name': 'Rate', 'date': '2024', 'values': [2.5, '*'], 'comparisonValues': [3.1], 'associates': [{'name': 'supflag', 'values': ['NaN', '*'], 'comparisonValues': ['NaN']}]}]}]}]}
        rows = server.parse_pho(json.dumps(doc).encode())
        self.assertEqual([r['geography'] for r in rows], ['A', 'B', 'Ontario'])
        self.assertEqual(rows[0]['value'], 2.5)
        self.assertIsNone(rows[1]['value'])
        self.assertEqual(rows[1]['raw_value'], '*')
        doc['geographies'][0]['features'].pop()
        with self.assertRaises(ValueError):
            server.parse_pho(json.dumps(doc).encode())

    def test_cihi_ontario_only_and_units(self):
        w = openpyxl.Workbook(); s = w.active; s.title = 'Table 1'
        s.append(['Title']); s.append(['Reporting level', 'Province', 'Region', 'Indicator', 'Metric', 'Data year', 'Unit of measurement', 'Indicator result'])
        s.append(['Regional', 'Ontario', 'Toronto Region', 'Hip Replacement', '50th percentile', 2025, 'Days', 50])
        s.append(['Provincial', 'Ontario', 'n/a', 'Hip Replacement', '50th percentile', 2025, 'Days', 'n/a'])
        s.append(['Provincial', 'Alberta', 'n/a', 'Hip Replacement', '50th percentile', 2025, 'Days', 90])
        s.append(['Provincial', 'Ontario', 'n/a', 'Hip Replacement', '50th percentile', '2019Q3Q4', 'Days', 44])
        output = BytesIO(); w.save(output)
        rows = server.parse_cihi(output.getvalue())
        self.assertEqual(len(rows), 3); self.assertEqual(rows[0]['unit'], 'Days'); self.assertIsNone(rows[1]['value']); self.assertEqual(rows[2]['year'], '2019Q3Q4')
        s.cell(2, 1, 'Changed'); output = BytesIO(); w.save(output)
        with self.assertRaises(ValueError):
            server.parse_cihi(output.getvalue())

    def test_numeric_flags(self):
        for value in ['n/a', '*', 'NaN', None, float('nan'), True]:
            self.assertIsNone(server.numeric(value))
        self.assertEqual(server.numeric(0), 0)

    def test_unknown_filter_rejected(self):
        with self.assertRaises(ValueError):
            server.query('pho', 'records', {'url': 'http://example.com'})


if __name__ == '__main__':
    unittest.main()

