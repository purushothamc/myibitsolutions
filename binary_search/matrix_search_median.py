def findLastInsertLocation(A, B):
    ln = len(A)
    start, end = 0, ln - 1
    while start <= end:
        mid = start + (end - start) / 2
        if B >= A[mid]:
            start = mid + 1
        elif B < A[mid]:
            end = mid - 1
    return start

def findFirstInsertLocation(A, B):
    ln = len(A)
    start, end = 0, ln - 1
    while start <= end:
        mid = start + (end - start) / 2
        if B > A[mid]:
            start = mid + 1
        elif B <= A[mid]:
            end = mid - 1
    return start


def findMedian(A):
    rows, cols = len(A), len(A[0])
    mid = ((rows * cols) / 2)
    for i in xrange(rows):
        for j in xrange(cols):
            firstCount, lastCount = 0, 0
            for k in xrange(rows):
                last = findLastInsertLocation(A[k], A[i][j])
                first = findFirstInsertLocation(A[k], A[i][j])
                firstCount += first
                lastCount += last
            if firstCount <= mid and lastCount > mid:
                return A[i][j]
            print A[i][j], firstCount, lastCount, mid


A = [[1,3,5],[2,6,9],[3,6,9]]
A = [[1, 1, 3, 3, 3, 3, 3]]
A = [[5],[4],[3],[1],[3],[1],[4],[2],[5],[3],[3]]
A = [[1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]]
A = [[1],[4],[3],[1],[2],[4],[4],[4],[2],[2],[1]]
print findMedian(A)