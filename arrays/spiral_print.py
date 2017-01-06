#!/bin/env/python


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def printSpiral(A):
        result = []
        rows, cols = len(A), len(A[0])
        top, right, bottom, left = 0, cols-1, rows-1, 0
        direction = 0
        while top <= bottom and left <= right:
            if direction is 0:
                for k in xrange(left, right+1):
                    result.append(A[top][k])
                top += 1
                direction = 1
            elif direction is 1:
                for k in xrange(top, bottom+1):
                    result.append(A[k][right])
                right -= 1
                direction = 2
            elif direction is 2:
                for k in xrange(right, left-1, -1):
                    result.append(A[bottom][k])
                bottom -= 1
                direction = 3
            elif direction is 3:
                for k in xrange(bottom, top-1, -1):
                    result.append(A[k][left])
                left += 1
                direction = 4
            direction %= 4
        return result

P = Solution()
print P.printSpiral([[1,2,3],[4,5,6],[7,8,9]])