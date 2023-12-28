#!/usr/bin/python3

"""Test module"""
import unittest
from models.base import Base

class BaseTest(unittest.TestCase):

    def test_public_instance(self):
        base = Base()
        assert(base.id == 1)

