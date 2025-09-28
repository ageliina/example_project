#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 13:40:17

"""Unit test the example class."""

import unittest
from example_project import table


class TestTable(unittest.TestCase):
    def test_read_test_table(self):
        my_table = table.read_test_table()
        self.assertEqual(my_table["a"][0], 1)
        self.assertEqual(my_table["b"][1], 5)
        self.assertEqual(my_table["c"][2], 9)

    def test_write_test_latex_table(self):
        expected = "".join(open("data/tests/table/test_table.tex.frozen"))
        table.write_test_latex_table()
        got = "".join(open("data/tests/table/test_table.tex"))
        self.assertEqual(expected, got)
