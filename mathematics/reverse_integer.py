class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        maxint = 2147483647
        negative = False
        if A < 0:
            negative = True
            A = -1*A
        reverse = 0
        while A > 0:
            digit = A % 10
            #print reverse, maxint
            if (reverse > maxint/10) or (reverse == maxint and digit > maxint % 10):
                return 0
            reverse = reverse * 10 + digit
            A /= 10
        if negative:
            reverse = -1*reverse
        return reverse

P = Solution()
print P.reverse(123456)