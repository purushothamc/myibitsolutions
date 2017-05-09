class Solution:
    def findLastInsertLocation(self, A, B):
        ln = len(A)
        start, end = 0, ln - 1
        result = -1
        while start <= end:
            mid = start + (end - start) / 2
            if B >= A[mid]:
                start = mid + 1
                result = mid
            elif B < A[mid]:
                end = mid - 1
        return result

    def findFirstInsertLocation(self, A, B):
        ln = len(A)
        start, end = 0, ln - 1
        result = -1
        while start <= end:
            mid = start + (end - start) / 2
            if B > A[mid]:
                start = mid + 1
            elif B <= A[mid]:
                result = mid
                end = mid - 1
        return result

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if not A:
            return [-1, -1]
        first = self.findFirstInsertLocation(A, B)
        last = self.findLastInsertLocation(A, B)
        if first == -1 and last == -1:
            return [-1, -1]
        return [first, last]