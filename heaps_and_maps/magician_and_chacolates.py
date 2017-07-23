import Queue as Q

class ordered(object):
    def __init__(self, value):
        self.val = value

    def __cmp__(self, other):
        return self.val < other.val

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        if not B or not A:
            return 0
        division = ((10**9) + 7)
        result = 0
        q = Q.PriorityQueue()
        for bag in B:
            q.put(ordered(bag))

        while A > 0:
            popped = q.get()
            result = (result + popped.val % division) % division
            q.put(ordered(popped.val/2))
            A -= 1
        return result % division