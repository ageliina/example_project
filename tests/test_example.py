#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 13:40:17

"""Unit test the example class."""

import unittest
from example_project.example import ExampleClass


class TestExampleClass(unittest.TestCase):
    def setUp(self):
        self.example_class = ExampleClass("foo", 42)

    def test_init(self):
        self.assertEqual(self.example_class.name, "foo")
        self.assertEqual(self.example_class.age, 42)
        self.assertGreaterEqual(self.example_class.seed, 0.0)
        self.assertLess(self.example_class.seed, 1.0)

    def test_name(self):
        self.assertEqual(self.example_class.name, "foo")

    def test_age(self):
        self.assertEqual(self.example_class.age, 42)

    def test_seed(self):
        self.assertGreaterEqual(self.example_class.seed, 0.0)
        self.assertLess(self.example_class.seed, 1.0)

    def test_show(self):
        self.assertTrue(self.example_class.show() is None)

    def test_add_name(self):
        self.assertEqual(self.example_class.add_name(self.example_class), "foofoo")

    def test_add_age(self):
        self.assertEqual(self.example_class.add_age(self.example_class), 84)
