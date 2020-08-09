import unittest

from algorithms.sorting import InsertionSort


class InsertionSortTest(unittest.TestCase):

    @staticmethod
    def test_correctness():
        ins_sort = InsertionSort(array=[3, 2, 9, 4, 5, 8, 6, 1])
        assert ins_sort.sort(ascending=True), [1, 2, 3, 4, 5, 6, 8, 9]
        assert ins_sort.sort(), [1, 2, 3, 4, 5, 6, 8, 9]
        assert ins_sort.sort(ascending=False), [9, 8, 6, 5, 4, 3, 2, 1]


if __name__ == '__main__':
    unittest.main()
