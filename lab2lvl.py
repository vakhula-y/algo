def max_hamsters(S, C, hamsters):
    left, right = 0, C
    answer = 0

    while left <= right:
        k = (left + right) // 2

        if k == 0:
            left = 1
            continue

        costs = []
        for H, G in hamsters:
            costs.append(H + G * (k - 1))

        costs.sort()
        total_food = sum(costs[:k])

        if total_food <= S:
            answer = k
            left = k + 1
        else:
            right = k - 1

    return answer



if __name__ == "__main__":

   
    S1 = 7
    C1 = 3
    hamsters1 = [[1, 2], [2, 2], [3, 1]]

    result1 = max_hamsters(S1, C1, hamsters1)
    print("Приклад 1:")
    print("S =", S1)
    print("C =", C1)
    print("hamsters =", hamsters1)
    print("Результат:", result1)
    print()

   
    S2 = 19
    C2 = 4
    hamsters2 = [[5, 0], [2, 2], [1, 4], [5, 1]]

    result2 = max_hamsters(S2, C2, hamsters2)
    print("Приклад 2:")
    print("S =", S2)
    print("C =", C2)
    print("hamsters =", hamsters2)
    print("Результат:", result2)
    print()

    
    S3 = 2
    C3 = 2
    hamsters3 = [[1, 50000], [1, 60000]]

    result3 = max_hamsters(S3, C3, hamsters3)
    print("Приклад 3:")
    print("S =", S3)
    print("C =", C3)
    print("hamsters =", hamsters3)
    print("Результат:", result3)
    print()

   
    import unittest

    class TestHamsters(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(max_hamsters(S1, C1, hamsters1), 2)

        def test_example_2(self):
            self.assertEqual(max_hamsters(S2, C2, hamsters2), 3)

        def test_example_3(self):
            self.assertEqual(max_hamsters(S3, C3, hamsters3), 1)

    unittest.main()
