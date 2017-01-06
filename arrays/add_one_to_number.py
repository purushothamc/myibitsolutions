#!/bin/env/python


class Solution:
    def __init__(self):
        pass

    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        size = len(A)
        if size <= 0:
            return 1
        A.reverse()
        carry = 1
        for i in xrange(size):
            sum = A[i] + carry
            A[i] = sum % 10
            carry = sum / 10
        while carry > 0:
            A.append(carry % 10)
            carry /= 10
        while A:
            if A[-1] == 0: A.pop()
            else: break
        A.reverse()
        return A

P = Solution()
print P.plusOne([9, 9, 9, 9, 9])