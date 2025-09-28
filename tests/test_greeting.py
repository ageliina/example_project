#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 13:40:17

"""Unit test the example class."""

import unittest
from example_project import greeting


class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting.greeting("00:00"), "Good night!")
        self.assertEqual(greeting.greeting("06:15"), "Good morning!")
        self.assertEqual(greeting.greeting("12:34"), "Good day!")
        self.assertEqual(greeting.greeting("23:20"), "Good evening!")
        self.assertRaises(ValueError, greeting.greeting, "foobarbaz")
        self.assertRaises(ValueError, greeting.greeting, "99:99")
