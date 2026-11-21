"""Проверки состава выгрузки без привязки к порядку строк."""

import unittest

from export_rows import export_rows


class ExportTests(unittest.TestCase):
    def test_export_preserves_own_records_and_their_multiplicity(self):
        rows = [("A", 12), ("B", 80), ("A", 7), ("A", 12)]
        self.assertCountEqual(export_rows(rows, "A"), [7, 12, 12])

    def test_export_without_own_records_is_empty(self):
        self.assertEqual(export_rows([("B", 80)], "A"), [])
