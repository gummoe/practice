import unittest

from Sorting.quick_sort import quick_sort, partition, swap


class QuickSortTest(unittest.TestCase):

    def test_swap(self):
        test_input = [4, 5, 6]
        expected_result = [6, 5, 4]
        swap(test_input, 0, 2)

        self.assertEqual(test_input, expected_result)

    def test_partition(self):
        test_input = [8, 7, 1, 3, 5, 12, 35]
        expected_result = 4
        test_result = partition(test_input, 0, len(test_input) - 1)

        self.assertEqual(expected_result, test_result)

    def test_sorts_unordered(self):
        test_input = [10, 8, 5, 3, 1, 9, 4, 2, 6, 7]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_result = quick_sort(test_input, 0, len(test_input) - 1)

        self.assertEqual(expected_result, test_result)

    def test_sorts_ordered(self):
        test_input = [1, 3, 5, 7, 9]
        test_result = quick_sort(test_input, 0, len(test_input) - 1)

        self.assertEqual(test_input, test_result)

    def test_sorts_dupes(self):
        test_input = [2, 2, 2, 2, 2]
        test_result = quick_sort(test_input, 0, len(test_input) - 1)

        self.assertEqual(test_input, test_result)

    def test_sorts_single_item(self):
        test_input = [800]
        test_result = quick_sort(test_input, 0, len(test_input) - 1)

        self.assertEqual(test_input, test_result)

