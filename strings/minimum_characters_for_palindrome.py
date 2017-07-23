class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        lenA = len(A)

        A = A + "$" + A[::-1]
        j, i = 0, 1
        temp = [0 for x in range(len(A))]
        while i < len(A):
            if A[j] == A[i]:
                temp[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = temp[j - 1]
                else:
                    temp[i] = 0
                    i += 1
        return lenA - temp[-1]