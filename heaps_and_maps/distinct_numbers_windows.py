from collections import OrderedDict, deque

class Solution:
    def __init__(self):
        pass

    def solve(self, A, k):
        if k > len(A):
            return list()

        result = list()
        mapper = OrderedDict()
        d = deque()

        count = 0
        for i in xrange(k):
            d.append(A[i])
            if not mapper.get(A[i], 0):
                count += 1
            mapper[A[i]] = mapper.get(A[i], 0) + 1

        result.append(count)

        for i in xrange(k, len(A)):
            popped = d.popleft()

            if mapper[popped] == 1:
                mapper.pop(popped)
                count -= 1
            elif mapper[popped] > 1:
                mapper[popped] -= 1
            d.append(A[i])
            if not mapper.get(A[i], 0):
                count += 1
            mapper[A[i]] = mapper.get(A[i], 0) + 1
            result.append(count)

        return result

A = [1, 2, 1, 3, 4, 3]
C = Solution()
print C.solve(A, 3)