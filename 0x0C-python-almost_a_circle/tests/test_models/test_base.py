#!/usr/bin/python3
""" Defines testing methods"""
import unittest

class TestModels(unittest.TestCase):
    """ A class containg unit test methods"""
    def test_base(self):
        self.assertIsNotNone(id)

if __name__ == "__main__":
    unittest.main()
