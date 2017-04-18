def kthSmallet(A, B):
    """
    this solution uses extra O(B) space
    """
    if B == 0:
        return min(A)
    temp = [A[i] for i in xrange(B)]
    temp = sorted(temp)
    for j in xrange(i, len(A)):
        bI = B - 1
        while bI >= 0 and temp[bI] > A[j]:
            if bI > 0:
                temp[bI] = temp[bI - 1]
            bI -= 1
        if bI < B - 1:
            temp[bI + 1] = A[j]
    return temp[B - 1]

def kthSmallestHeap(A, B):
    if B == 0:
        return min(A)
    elif B == len(A):
        return max(A)
    import heapq
    temp = []
    for idx in xrange(B):
        heapq.heappush(temp, -1 * A[idx])
    for x in xrange(idx + 1, len(A)):
        max_value = heapq.heappop(temp)
        if max_value < -1 * A[x]:
            heapq.heappush(temp, -1 * A[x])
        else:
            heapq.heappush(temp, max_value)
    return -1 * heapq.heappop(temp)

A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, \
      42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, \
      39, 62, 20, 17, 46, 26, 81, 92 ]
#A = [1,4,3,5,2,4,3,5,6,7]
A = [ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ]
B = 2
print kthSmallestHeap(A, B)