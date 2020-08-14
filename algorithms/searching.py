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
