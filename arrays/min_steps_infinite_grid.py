#!/bin/env/python

class Solution:
    def __init__(self):
        pass

    def coverPoints(self, X, Y):
        distance = 0
        s1, s2 = len(X), len(Y)
        if s1 <= 1 or s2 <= 1:
            return 0
        for i, j in zip(xrange(1, s1), xrange(1, s2)):
            distance += max(abs(X[i]-X[i-1]), abs(Y[j]-Y[j-1]))
        return distance

P = Solution()
print P.coverPoints([0,2,4],[1,3,5])