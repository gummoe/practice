import unittest

from Sorting.merge_sort import merge_sort, merge


class MergeSortTest(unittest.TestCase):

    def test_merge(self):
        right = [1, 2, 3]
        left = [4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        test_result = merge(left, right)

        self.assertEqual(expected_result, test_result)

    def test_sorts_unordered(self):
        test_input = [10, 8, 5, 3, 1, 9, 4, 2, 6, 7]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_result = merge_sort(test_input)

        self.assertEqual(expected_result, test_result)

    def test_sorts_ordered(self):
        test_input = [1, 3, 5, 7, 9]
        test_result = merge_sort(test_input)

        self.assertEqual(test_input, test_result)

    def test_sorts_dupes(self):
        test_input = [2, 2, 2, 2, 2]
        test_result = merge_sort(test_input)

        self.assertEqual(test_input, test_result)

    def test_sorts_single_item(self):
        test_input = [800]
        test_result = merge_sort(test_input)

        self.assertEqual(test_input, test_result)

