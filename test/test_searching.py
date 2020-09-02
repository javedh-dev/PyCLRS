import unittest

from algorithms.searching import LinearSearch, BinarySearch


class LinearSearchTest(unittest.TestCase):

    @staticmethod
    def test_accuracy():
        ls = LinearSearch(array=[3, 1, 2, 4, 5, 6, 7, 9, 8, 0])
        assert ls.search(9), 7
        assert ls.search(12), -1


class BinarySearchTest(unittest.TestCase):

    @staticmethod
    def test_accuracy():
        ls = BinarySearch(array=[3, 1, 2, 4, 5, 6, 7, 9, 8, 0])
        assert ls.search(9), 7
        assert ls.search(12), -1


if __name__ == '__main__':
    unittest.main()
