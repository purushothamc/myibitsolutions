class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        n = A
        rows, cols = n, n
        top, bottom = 0, n-1
        left, right = 0, n-1
        direction = 0
        result = [[0 for j in xrange(n)] for i in xrange(n)]
        count = 1
        while top <= bottom and left <= right:
            if direction is 0:
                for i in xrange(left, right+1):
                    result[top][i] = count
                    count += 1
                top += 1
                direction = 1
            elif direction is 1:
                for i in xrange(top, bottom+1):
                    result[i][right] = count
                    count += 1
                right -= 1
                direction = 2
            elif direction is 2:
                for i in xrange(right, left-1, -1):
                    result[bottom][i] = count
                    count += 1
                bottom -= 1
                direction = 3
            elif direction is 3:
                for i in xrange(bottom, top-1, -1):
                    result[i][left] = count
                    count += 1
                left += 1
                direction = 4
            direction %= 4
        return result

P = Solution()
print P.generateMatrix(4)