#!/usr/bin/python3
"""Test rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def test_triangle_instance(self):
        r1 = Rectangle(10, 2, id=1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        with self.assertRaises(AttributeError):
            r1.__width
        with self.assertRaises(TypeError):
            Rectangle(None, None)
