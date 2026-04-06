import unittest
from flood_fill import flood_fill

class TestFloodFill(unittest.TestCase):

    def test_standard_fill(self):
        matrix = [
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'X'],
            ['X', 'X', 'X']
        ]
        expected = [
            ['C', 'C', 'C'],
            ['C', 'C', 'X'],
            ['X', 'X', 'X']
        ]
        result = flood_fill([row[:] for row in matrix], 0, 0, 'C')
        self.assertEqual(result, expected)

    def test_same_color(self):
        matrix = [
            ['G', 'G'],
            ['G', 'G']
        ]
        result = flood_fill([row[:] for row in matrix], 0, 0, 'G')
        self.assertEqual(result, matrix)

    def test_walled_off_area(self):
        matrix = [
            ['W', 'B', 'W'],
            ['B', 'W', 'B'],
            ['W', 'B', 'W']
        ]
        expected = [
            ['W', 'B', 'W'],
            ['B', 'R', 'B'],
            ['W', 'B', 'W']
        ]
        result = flood_fill([row[:] for row in matrix], 1, 1, 'R')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
