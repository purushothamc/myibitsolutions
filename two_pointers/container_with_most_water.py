def maxArea(A):
    lenA = len(A)
    if not A or lenA == 1:
        return 0
    i, j = 0, lenA - 1
    area, maxA = 0, 0
    while i < j:
        area = min(A[i], A[j]) * abs(j-i)
        if area > maxA:
            maxA = area
        if A[i] <= A[j]:
            i += 1
        else:
            j -= 1
    print maxA

A = [6,2,5,4,5,1,6]
maxArea(A)