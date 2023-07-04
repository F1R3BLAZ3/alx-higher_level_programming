#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test for an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test for a list with a single element"""
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_numbers(self):
        """Test for a list with positive numbers"""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test for a list with negative numbers"""
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test for a list with mixed positive and negative numbers"""
        result = max_integer([-5, 10, -2, 8, -3])
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
