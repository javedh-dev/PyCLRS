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

# SELECTION SORT(A) --> Ascending
# 1 for j=1 to A.length-1
# 2     swappable_index = j
# 3     for i=j to A.length-1
# 4         if A[i] < A[swappable_index]
# 5             swappable_index = i
# 6     Swap A[j] and A[swappable_index]

# SELECTION SORT(A) --> Descending
# 1 for j=1 to A.length-1
# 2     swappable_index = j
# 3     for i=j to A.length-1
# 4         if A[i] > A[swappable_index]
# 5             swappable_index = i
# 6     Swap A[j] and A[swappable_index]


class SelectionSort:

    def __init__(self, array):
        self.__array = array

    def sort(self, ascending=True):
        n = len(self.__array)
        for j in range(0, n-1):
            swappable_index = j
            if ascending:
                for i in range(j, n):
                    if self.__array[i] < self.__array[swappable_index]:
                        swappable_index = i
            else:
                for i in range(j, n):
                    if self.__array[i] > self.__array[swappable_index]:
                        swappable_index = i
            temp = self.__array[swappable_index]
            self.__array[swappable_index] = self.__array[j]
            self.__array[j] = temp
        return self.__array
