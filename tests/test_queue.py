import unittest

from Stacks_and_Queues.queue import Queue


class QueueTest(unittest.TestCase):

    def test_is_empty_is_true(self):
        queue = Queue()

        self.assertTrue(queue.is_empty())

    def test_is_empty_is_false(self):
        queue = Queue()
        queue.queue = [1, 2, 3]

        self.assertFalse(queue.is_empty())

    def test_remove_empty(self):
        queue = Queue()

        self.assertIsNone(queue.remove())

    def test_remove_not_empty(self):
        queue = Queue()
        queue.queue = [1, 2, 3]

        self.assertEqual(1, queue.remove())
        self.assertEqual(2, len(queue.queue))

    def test_add(self):
        queue = Queue()

        queue.add(1)
        self.assertEqual(queue.queue[0], 1)

        queue.add(2)
        self.assertEqual(queue.queue[1], 2)

    def test_peek_is_empty(self):
        queue = Queue()

        self.assertIsNone(queue.peek())

    def test_peek_is_not_empty(self):
        queue = Queue()
        queue.queue = [34]

        self.assertEqual(34, queue.peek())
