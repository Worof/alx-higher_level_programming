#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        """Test case when max integer is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test case when max integer is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test case when max integer is in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test case with only one element in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test case with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test case with both positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_all_same_numbers(self):
        """Test case where all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

if __name__ == '__main__':
    unittest.main()
