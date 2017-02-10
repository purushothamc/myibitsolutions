def sqrt(A):
    if A <= 1:
        return A
    start = 0
    end = A
    ans = 0
    while start <= end:
        mid = (start + end) / 2
        square = mid * mid
        #print start, end, mid, square
        if square == A:
            return mid
        if square < A:
            start = mid + 1
            ans = mid
        else:
            end = mid -1
    return ans


print sqrt(5)
print sqrt(19)
print sqrt(930675566)
for i in xrange(20):
    print i, sqrt(i)