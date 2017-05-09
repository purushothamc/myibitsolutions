def maxSubArray(A):
    import sys
    if not A: return -1000000000
    maxSum, maxSoFar = A[0], A[0]
    for x in A[1:]:
        maxSum = max(x, maxSum + x)
        maxSoFar = max(maxSum, maxSoFar)
    return maxSoFar
