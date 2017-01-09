class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if not A and not B: return 0
        if A is 1 or B is 1: return 1
        while B:
            if A < B:
                A, B = B, A
            c = B
            B = A % B
            A = c
            #print A, B, c
        return A

P = Solution()
print P.gcd(3,6)