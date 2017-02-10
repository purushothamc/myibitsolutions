def findCount(A, B):
    if not A: return 0
    firstIdx = find_occurence(A, B, True)
    if firstIdx == -1:
        return 0
    lastIdx = find_occurence(A, B, False)
    return lastIdx - firstIdx + 1


def find_occurence(A, B, searchFirst):
    start = 0
    end = len(A) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) / 2
        if A[mid] == B:
            result = mid
            if searchFirst:
                end = mid - 1
            else:
                start = mid + 1
        elif B < A[mid]:
            end = mid - 1
        else:
            start = mid + 1
        print start, end, mid
    return result

A = [6,7,8,8,10]
B = 4
print findCount(A, B)