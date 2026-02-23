import unittest
from lab1 import snake

class TestSnake(unittest.TestCase):

    def test_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5 ,6],
            [7, 8, 9]
        ]
        self.assertEqual(
            snake(matrix),
            [1, 2, 3, 6, 5, 4, 7, 8, 9]
        )
    def test_2x4(self):
        matrix = [
            [1,2,3,4],
            [5,6,7,8]
        ]
        self.assertEqual(
            snake(matrix),
            [1,2,3,4,8,7,6,5]
        )

    def test_1x5(self):
        matrix = [[1,2,3,4,5]]
        self.assertEqual(
            snake(matrix),
            [1,2,3,4,5]
        )

    def test_5x1(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        self.assertEqual(
            snake(matrix),
            [1,2,3,4,5]
        )

if __name__ == "__main__":
    unittest.main()
