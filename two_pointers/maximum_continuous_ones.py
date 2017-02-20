def maxContinuous1(A, B):
    lenA = len(A)
    if B < 0:
        return range(lenA)
    result = [(0,0)]
    i, j, cnt, count = 0, 0, B, 0
    while i < lenA and j < lenA:
        if A[i] == 1 and cnt >= 0:
            if (i - j) > result[0][1] - result[0][0]:
                result[0] = (j, i)
            i += 1
        elif A[i] == 0:
            cnt -= 1
            if cnt >= 0:
                if (i - j) > result[0][1] - result[0][0]:
                    result[0] = (j, i)
            elif cnt < 0:
                while j < lenA and A[j] != 0:
                    j += 1
                j += 1
                cnt += 1
            i += 1
    return range(result[0][0], result[0][1]+1)

A = [0,1,1,1,0,0]
B = 0
print maxContinuous1(A, B)