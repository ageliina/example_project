#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 13:40:17

"""Unit test the example class."""

import unittest
from example_project.another import AnotherExampleClass


class TestAnotherExampleClass(unittest.TestCase):
    def setUp(self):
        self.another_example_class = AnotherExampleClass("foo")

    def test_init(self):
        self.assertEqual(self.another_example_class.name, "foo")

    def test_name(self):
        self.assertEqual(self.another_example_class.name, "foo")

    def test_show(self):
        self.assertTrue(self.another_example_class.show() is None)
