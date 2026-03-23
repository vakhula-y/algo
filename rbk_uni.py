import unittest

from blacredtree import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_view(self):
        self.pq.insert("A", 1)
        self.pq.insert("B", 10)
        self.pq.insert("C", 5)
        self.assertEqual(self.pq.view(), [("B", 10), ("C", 5), ("A", 1)])

    def test_peek_max(self):
        self.pq.insert("A", 2)
        self.pq.insert("B", 100)
        self.pq.insert("C", 50)
        self.assertEqual(self.pq.peek_max(), "B")
        self.assertEqual(len(self.pq.view()), 3)

    def test_delete_max(self):
        self.pq.insert("A", 10)
        self.pq.insert("B", 20)
        self.pq.insert("C", 15)
        self.assertEqual(self.pq.delete_max(), "B")
        self.assertEqual(self.pq.view(), [("C", 15), ("A", 10)])

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek_max())
        self.assertIsNone(self.pq.delete_max())
        self.assertEqual(self.pq.view(), [])

    def test_duplicate_priorities(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 5)
        self.pq.insert("C", 10)
        view = self.pq.view()
        self.assertEqual(view[0], ("C", 10))
        self.assertEqual(view[1][1], 5)
        self.assertEqual(view[2][1], 5)

    def test_large_dataset(self):
        import random
        priorities = list(range(1, 51))
        random.shuffle(priorities)
        for p in priorities:
            self.pq.insert(f"V{p}", p)
        self.assertEqual([item[1] for item in self.pq.view()], list(range(50, 0, -1)))

if __name__ == "__main__":
    unittest.main()
