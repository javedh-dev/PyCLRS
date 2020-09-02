# LINEAR SEARCH(A,n)
# 1 for i=1 to A.length
# 2     if A[i] equals n then return i
# 3 return -1

class LinearSearch:

    def __init__(self, array):
        self.__array = array

    def search(self, n):
        for i in range(0, len(self.__array)):
            if self.__array[i] == n:
                return i
        return -1


class BinarySearch:

    def __init__(self, array):
        self.array = sorted(array)

    def search(self, n):
        flag = True
        high = len(self.array)-1
        low = 0
        while flag:
            if high < low:
                return -1
            mid = (high + low) // 2
            if self.array[mid] == n:
                return mid
            elif self.array[mid] > n:
                high = mid - 1
            else:
                low = mid + 1
        return -1
