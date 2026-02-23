from typing import List
import unittest

def snake(matrix):

    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result: List[int] = []

    for i in range(m):
        if i % 2 == 0:

            for j in range(n):
                result.append(matrix[i][j])

        else:
            for j in range(n-1, -1, -1):
                result.append(matrix[i][j])

    return result
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
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print("Snake result:", snake(matrix))
    print("\nRunning tests\n")

    unittest.main()
