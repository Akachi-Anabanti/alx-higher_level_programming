#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class"""
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_isinstance_list(self):
        self.assertIsNone(max_integer(""))
        self.assertRaises(TypeError, max_integer, [1, 2, 'a'])

    def test_returns_int(self):
        self.assertIsInstance(max_integer([1, 2, 3, 4]), int)

    def test_returns_str(self):
        self.assertIsInstance(max_integer("a"), str)

    def test_returns_float(self):
        self.assertIsInstance(max_integer([1, 1.2, 2.3]), float)
