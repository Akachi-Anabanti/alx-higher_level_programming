#!/usr/bin/python3

"""Test module"""
import unittest
from models.base import Base

class BaseTest(unittest.TestCase):

    def test_public_instance(self):
        base = Base()
        base_0 = Base();
        base_2 = Base(3);
        self.assertEqual(base.id, 1)
        self.assertEqual(base_0.id, 2)
        self.assertEqual(base_2.id, 3)

