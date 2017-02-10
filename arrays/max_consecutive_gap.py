def maximumGap(A):
    ln = len(A)
    if not A or ln == 1:
        return 0
    minimum, maximum = A[0], A[0]
    for elem in A:
        if elem > maximum:
            maximum = elem
        if elem < minimum:
            minimum = elem
    difference = (maximum-minimum) / (ln - 1)
    bucket = [0 for i in xrange(difference)]
    for elem in A:
        bucket[elem - minimum] += 1

    maxDiff = 0
    previous = 0
    print bucket
    for b in xrange(1, difference):
        if not bucket[b]:
            continue
        else:
            diff = abs(b - previous)
            previous = b
            if diff > maxDiff:
                maxDiff = diff
    return maxDiff

A = [1,10,5]
#A = [5, 3, 1, 8, 9, 2, 4]
print maximumGap(A)