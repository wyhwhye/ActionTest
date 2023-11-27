import unittest
from quickSort import quick_sort
import sys

sys.setrecursionlimit(10**4)


class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(quick_sort([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])

    def test_duplicate_elements(self):
        self.assertEqual(quick_sort([5, 2, 8, 1, 3, 2, 5]), [1, 2, 2, 3, 5, 5, 8])

    def test_negative_numbers(self):
        self.assertEqual(quick_sort([-5, 2, -8, 1, -3]), [-8, -5, -3, 1, 2])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            quick_sort([5, '2', 8, 1, 3])

    def test_large_list(self):
        # Test sorting a large list of numbers
        input_list = list(range(10 ** 3, 0, -1))
        expected_output = list(range(1, 10 ** 3 + 1))
        self.assertEqual(quick_sort(input_list), expected_output)

    def test_repeated_elements(self):
        # Test handling a list with many repeated elements
        input_list = [1] * 10 ** 3 + [2] * 10 ** 3
        expected_output = [1] * 10 ** 3 + [2] * 10 ** 3
        self.assertEqual(quick_sort(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
