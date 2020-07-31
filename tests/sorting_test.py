import unittest

from algorithms.sorting import InsertionSort


class InsertionSortTest(unittest.TestCase):

    def test_correctness(self):
        obj = InsertionSort(array=[21, 1, 4, 34, 87, 45, 67, 0, 12, 1, 65, 45])
        assert obj.sort(), [0, 1, 1, 4, 12, 21, 34, 45, 45, 65, 67, 87]


if __name__ == '__main__':
    unittest.main()
