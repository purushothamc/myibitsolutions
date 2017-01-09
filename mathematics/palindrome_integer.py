class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        import math
        if A < 0: return 0
        if 0 <= A <= 9: return 1
        numDigits = int(math.log10(A))
        while A:
            front = A/(10**numDigits)
            last = A%10
            if front is not last:
                return 0
            A = A % (10**numDigits)
            A = A/10
            numDigits -= 2
        return True

P = Solution()
print P.isPalindrome(12221)