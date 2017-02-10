def searchInsert(A, B):
    if not A:
        return -1
    ln = len(A)
    start, end = 0, ln - 1
    while start <= end:
        mid = start + (end - start) / 2
        if B >= A[mid]:
            start = mid + 1
        elif B < A[mid]:
            end = mid - 1
    return start

A = [1,3,5,6]
print searchInsert(A, 2)