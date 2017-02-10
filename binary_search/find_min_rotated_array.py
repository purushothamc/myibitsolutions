def findMin(A):
    if A[0] < A[-1]:
        return A[0]
    ln = len(A)
    start = 0
    end = ln - 1
    while start <= end:
        mid = start + (end - start) / 2
        if A[(mid - 1) % ln] >= A[mid] <= A[(mid + 1) % ln]:
            break
        elif A[mid] <= A[end]:
            end = mid - 1
        elif A[mid] >= A[start]:
            start = mid + 1
    return A[mid], mid

A = [3,4,5,6,0,1,2]
A = [5137, 5525, 9511, 13269, 16255, 16700, 19870, 23034, 29247, 29934, 34583, 41585, 42598,\
     44113, 46035, 50147, 50737, 57084, 65916, 76905, 84098, 85912, 92081, 92257, 95449 ]
print findMin(A)