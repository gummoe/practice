import unittest

from Stacks_and_Queues.stack import Stack


class StackTest(unittest.TestCase):

    def test_is_empty_is_true(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

    def test_is_empty_is_false(self):
        stack = Stack()
        stack.stack = [1, 2, 3]

        self.assertFalse(stack.is_empty())

    def test_pop_empty(self):
        stack = Stack()

        self.assertIsNone(stack.pop())

    def test_pop_not_empty(self):
        stack = Stack()
        stack.stack = [1, 2, 3]

        self.assertEqual(1, stack.pop())
        self.assertEqual(2, len(stack.stack))

    def test_push(self):
        stack = Stack()

        stack.push(1)
        self.assertEqual(stack.stack[0], 1)

        stack.push(2)
        self.assertEqual(stack.stack[0], 2)

    def test_peek_is_empty(self):
        stack = Stack()

        self.assertIsNone(stack.peek())

    def test_peek_is_not_empty(self):
        stack = Stack()
        stack.stack = ['bananas']

        self.assertEqual('bananas', stack.peek())
