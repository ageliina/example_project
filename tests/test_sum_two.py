#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 13:40:17

"""Unit test the example class."""

import unittest
import sum_two


class TestSumTwo(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(sum_two.sum_two(0, 0), 0)
        self.assertEqual(sum_two.sum_two(0, 1), 1)
        self.assertEqual(sum_two.sum_two(1, 1), 2)
        self.assertEqual(sum_two.sum_two(1, 4), 5)
        self.assertEqual(sum_two.sum_two(5, 6), 11)

    def test_errors(self):
        self.assertRaises(TypeError, sum_two.sum_two, 1, "foo")
        self.assertRaises(TypeError, sum_two.sum_two, 1, None)
        self.assertRaises(TypeError, sum_two.sum_two, 1, {})
        self.assertRaises(TypeError, sum_two.sum_two, 1, [])
        self.assertRaises(TypeError, sum_two.sum_two, 1, 2, 3)
        self.assertRaises(TypeError, sum_two.sum_two, 1, 2, 3, 4)
