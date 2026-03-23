import unittest
from binary_tree import BinaryTree, find_successor


class TestBinaryTreeSuccessor(unittest.TestCase):

    def setUp(self):
       
        self.root = BinaryTree(10)

        self.n5 = BinaryTree(5, parent=self.root)
        self.n15 = BinaryTree(15, parent=self.root)

        self.root.left = self.n5
        self.root.right = self.n15

        self.n3 = BinaryTree(3, parent=self.n5)
        self.n7 = BinaryTree(7, parent=self.n5)

        self.n5.left = self.n3
        self.n5.right = self.n7

        self.n20 = BinaryTree(20, parent=self.n15)
        self.n12 = BinaryTree(12, parent=self.n20)

        self.n15.right = self.n20
        self.n20.left = self.n12

    def test_successor_of_7(self):
        result = find_successor(self.root, self.n7)
        self.assertEqual(result.value, 10)

    def test_successor_of_5(self):
        result = find_successor(self.root, self.n5)
        self.assertEqual(result.value, 7)

    def test_successor_of_10(self):
        result = find_successor(self.root, self.root)
        self.assertEqual(result.value, 15)

    def test_successor_of_20(self):
        result = find_successor(self.root, self.n20)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
