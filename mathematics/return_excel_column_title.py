class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        result = []
        while A:
            result.append(chr(65 + (A-1) % 26))
            A = (A-1)/26
        result.reverse()
        out = "".join(result)
        return out

P = Solution()
print P.convertToTitle(28)