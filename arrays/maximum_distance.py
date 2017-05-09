def maximumGap(self, A):
    if not A: return -1
    """ Solution 1
    lastMin, lastMax, maxDiff = 0, 0, 0
    for idx in xrange(len(A)-1):
        if not lastMin or A[idx] < A[lastMin]:
            lastMin = idx
            for j in xrange(lastMax, len(A)):
                if A[idx] <= A[j] and (j-idx) > maxDiff:
                    maxDiff = j-idx
                    lastMax = j
    return maxDiff
    """
    ##### Solution 2
    temp = []
    from operator import itemgetter
    import sys
    for i in xrange(len(A)):
        temp.append((A[i], i))
    temp = sorted(temp, key=itemgetter(0))
    indexMax = [0 for i in xrange(len(A))]
    maxIndex = -1 * sys.maxint
    for i in xrange(len(A) - 1, -1, -1):
        maxIndex = max(maxIndex, temp[i][1])
        indexMax[i] = maxIndex
    maxIndex = -1
    for i in xrange(len(temp)):
        maxIndex = max(indexMax[i] - temp[i][1], maxIndex)
    return maxIndex