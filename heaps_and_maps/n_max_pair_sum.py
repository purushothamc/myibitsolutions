import heapq
from itertools import product
import Queue as Q

class value_ordered(object):
    def __init__(self, value, start, end):
        self.val = value
        self.start = start
        self.end = end

    def __cmp__(self, other):
        return self.val < other.val

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solveOne(self, A, B):
        x = product(A, B)
        h = []
        for pair in x:
            h.append(sum(pair))
        heapq._heapify_max(h)
        print heapq._nlargest(len(A), h)

    def solve(self, A, B):
        h = []
        cnt = 0
        #A = sorted(A, reverse=True)
        #B = sorted(B, reverse=True)
        d = dict()

        for x in product(A, B):
            sum_pair = sum(x)
            h.append(sum_pair)
        heapq._heapify_max(h)
        return heapq._nlargest(len(A), h)

    def solveTwo(self, A, B):
        if not A or not B:
            return []
        h, d = [], {}
        A.sort()
        B.sort()
        q = Q.PriorityQueue()
        q.put(value_ordered(A[-1] + B[-1], len(A)-1, len(B)-1))
        d[(len(A) - 1, len(B) - 1)] = True
        index = 0

        while index < len(A):
            popped = q.get()
            i, j = popped.start, popped.end
            h.append(popped.val)
            if not d.get((i-1, j), None):
                q.put(value_ordered(A[i-1] + B[j], i-1, j))
                d[(i-1, j)] = True
            if not d.get((i, j-1), None):
                d[(i, j-1)] = True
                q.put(value_ordered(A[i] + B[j-1], i, j-1))
            index += 1

        return h

A = [ 7, 17, 0, 0, 21, 49, 19, 49, 42, 15, 13, -45, -43, 23, 12, 7, -23, 22, -1, -27, -38,
      6, 45, 23, 20, -37, 24, -14, 45, -14, -19, -46, 5, -16, 4, -24, -17, 26, 27, -25, -9,
      42, 32, -2, -33, 47, -44, -6, -29, -43, -30, -17, 13, 17, -44, -17, 30, -18, -28, -23,
      18, -45, -18, 25, -11, -12, -49, -25, -36, -19, 0, -42, -27, 35, 6, -9, 32, -36, 35, -47,
      -29, -45, -14, -14, -26, 44, -28, 6, -24, -6, 34, -4, -1, 18, -29 ]

B = [ -9, -44, 24, 16, 23, -45, 18, 31, -21, -45, 39, -28, 37, 6, 9, -8, -21, -33, -20, 16, -9,
      -26, -10, 48, -48, 34, 32, -2, 35, 0, -29, 28, -42, 46, -6, 31, 3, 15, -36, 32, 20, -46,
      6, -40, 10, -34, -46, 39, -17, -15, -43, 24, 9, -3, 22, -36, -19, -44, 12, 19, -42, -14,
      -3, -33, -18, -6, 0, -13, 11, 15, 22, 33, 19, -22, -5, 31, -6, 0, 20, 27, 35, 28, -46, 46,
      27, 26, -40, 11, -15, -25, -20, -7, 11, -21, -38 ]

C = Solution()
#print C.solve(A, B)
#C.solveOne(A, B)
print C.solveTwo(A, B)
