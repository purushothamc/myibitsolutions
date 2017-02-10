def findMin(A):
    ln = len(A)
    low, high = 0, ln - 1
    while low <= high:
        mid = low + (high - low) / 2
        if A[(mid-1) % ln] > A[mid] and A[(mid+1) % ln] >A[mid]:
            break
        elif A[low] <= A[mid]:
            low = mid + 1
        elif A[high] >= A[mid]:
            high = mid - 1
    return mid

def binarySearch(A, B, start, end):
    low, high = start, end
    result = -1
    while low <= high:
        mid = low + (high - low) / 2
        if A[mid] == B:
            return mid
        elif B > A[mid]:
            low = mid + 1
        elif B < A[mid]:
            high = mid - 1
    return result

def searchRotate(A, B):
    if not A:
        return -1
    result = -1
    minIndex = findMin(A)
    result = binarySearch(A, B, 0, minIndex)
    if result == -1:
        result = binarySearch(A, B, minIndex, len(A)-1)
    return result

A = [4,5,6,7,0,1,2]
print searchRotate(A, 4)