class Solution:
    def __init__(self):
        pass

    def findDigitsInBinary(self, A):
        result = []
        if A is 0: return "0"
        elif A is 1: return  "1"
        while(A):
            result.append(A%2)
            A /= 2
        result.reverse()
        return "".join([str(i) for i in result])

P = Solution()
print P.decToBin(6)
