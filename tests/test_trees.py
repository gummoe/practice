import unittest

from Trees.tree_node import TreeNode
from Trees.tree_traversals import (
    in_order_traversal,
    pre_order_traversal,
    post_order_traversal
)


def construct_balanced_tree():
    """
            5
       3        7
     2   4    6   8

    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.left = TreeNode(6)
    return root


class TreesTest(unittest.TestCase):

    def test_in_order_traversal(self):
        test_input = construct_balanced_tree()
        expected_result = [2, 3, 4, 5, 6, 7, 8]
        test_result = in_order_traversal(test_input)

        self.assertEqual(expected_result, test_result)

    def test_pre_order_traversal(self):
        test_input = construct_balanced_tree()
        expected_result = [5, 3, 2, 4, 7, 6, 8]
        test_result = pre_order_traversal(test_input)

        self.assertEqual(expected_result, test_result)

    def test_post_order_traversal(self):
        test_input = construct_balanced_tree()
        expected_result = [2, 4, 3, 6, 8, 7, 5]
        test_result = post_order_traversal(test_input)

        self.assertEqual(expected_result, test_result)

