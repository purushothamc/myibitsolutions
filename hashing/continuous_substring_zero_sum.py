def lszero(A):
    if not A:
        return list()
    result, sum, maxLen, mapper, curLen = list(), 0, 0, dict(), 0
    for index, value in enumerate(A):
        sum += value
        if sum == 0:
            curLen = index + 1
            if curLen > maxLen:
                maxLen = curLen
                result = A[0: index + 1]
        if not mapper.has_key(sum):
            mapper[sum] = index
        elif mapper.has_key(sum):
            curLen = index - mapper[sum]
            if curLen > maxLen:
                maxLen = curLen
                result = A[mapper[sum] + 1: mapper[sum] + maxLen + 1]
    return result

A = [1, 2, -2, 4, -4, 5, -5, 0, 0, 0]
#A = [1, 2, -3, 3]
#A =[-1, 1, 1, -1, -1, 1, 1, -1]
#A = [-1, -1, -1, 1, 1, 1]
#A = [1, 2, -1, 1, 3, -1, 1, 4]
#A = [10, -3, -9, -10, 9, -26, 7, -2, -20, -19, -9, 7, 13, -5, -8, -24, -11, 28, 28, 24]
#A = [ -8, 8, -1, -16, -28, -27, 15, -14, 14, -27, -5, -6,
#      -25, -11, 28, 29, -3, -25, 17, -25, 4, -20, 2, 1, -17, -10, -25 ]
print lszero(A)