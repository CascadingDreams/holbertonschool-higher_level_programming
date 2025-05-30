#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test list with single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-1]), -1)

    def test_positive_integers(self):
        """Test list with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_integers(self):
        """Test list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-10, -5, -1]), -1)

    def test_mixed_integers(self):
        """Test list with positive and negative integers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-5, -2, 3, 1]), 3)
        self.assertEqual(max_integer([10, -5, 15, -10]), 15)

    def test_duplicate_integers(self):
        """Test list with duplicate integers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 3, 5]), 5)
        self.assertEqual(max_integer([-2, -2, -2]), -2)

    def test_max_at_beginning(self):
        """Test when max integer is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([100, 50, 25]), 100)

    def test_max_at_end(self):
        """Test when max integer is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([25, 50, 100]), 100)

    def test_max_in_middle(self):
        """Test when max integer is in the middle"""
        self.assertEqual(max_integer([1, 10, 2]), 10)
        self.assertEqual(max_integer([5, 1, 100, 2, 3]), 100)

    def test_two_elements(self):
        """Test list with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([2**31 - 1, 2**30]), 2**31 - 1)

    def test_zero_in_list(self):
        """Test lists containing zero"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([0, -1, -2]), 0)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_float_numbers(self):
        """Test with float numbers (if function supports them)"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.1, 1.2, 1.0]), 1.2)

    def test_long_list(self):
        """Test with a longer list"""
        long_list = list(range(100))
        self.assertEqual(max_integer(long_list), 99)

        # Reverse order
        reverse_list = list(range(99, -1, -1))
        self.assertEqual(max_integer(reverse_list), 99)

    def test_identical_elements(self):
        """Test list where all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([-3, -3, -3]), -3)


if __name__ == '__main__':
    unittest.main()
