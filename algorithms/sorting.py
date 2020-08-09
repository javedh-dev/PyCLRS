# INSERTION-SORT(A) --> Ascending
# 1 for j = 2 to A.length
# 2     key = A[j]
# 3     // Insert A[j]  into the sorted sequence A[1..j-1].
# 4     i = j - 1
# 5     while i >= 0 and A[i] > key
# 6         A[i+1] = A[i]
# 7         i = i + 1
# 8     A[i+1] = key

# INSERTION-SORT(A) --> Descending
# 1 for j = A.length -1 to 1
# 2     key = A[j]
# 3     // Insert A[j]  into the sorted sequence A[1..j-1].
# 4     i = j + 1
# 5     while i <= A.length and A[i] > key
# 6         A[i-1] = A[i]
# 7         i = i + 1
# 8     A[i-1] = key

class InsertionSort:

    def __init__(self, array):
        self.__array = array

    def sort(self, ascending=True):
        n = len(self.__array)
        if ascending:
            for j in range(1, n):
                key = self.__array[j]
                i = j - 1
                while i >= 0 and self.__array[i] > key:
                    self.__array[i + 1] = self.__array[i]
                    i -= 1
                self.__array[i + 1] = key
        else:
            for j in range(n - 1, -1, -1):
                key = self.__array[j]
                i = j + 1
                while i < n and self.__array[i] > key:
                    self.__array[i - 1] = self.__array[i]
                    i += 1
                self.__array[i - 1] = key
        return self.__array
