def largestRectangleArea(self, A):
    right = list()
    left = list()
    height = [1 for i in xrange(len(A))]
    width = [1 for i in xrange(len(A))]
    for i in xrange(len(A)):
        while left and A[left[-1]] >= A[i]:
            left.pop()
        if not left:
            width[i] += i
        else:
            width[i] += i - left[-1] - 1
        left.append(i)
    tp = len(A) - 1
    for i in xrange(len(A) - 1, -1, -1):
        while right and A[right[-1]] >= A[i]:
            right.pop()
        if not right:
            width[i] += len(A) - 1 - i
        else:
            width[i] += right[-1] - i - 1
        right.append(i)
    result = -1
    for i in xrange(len(A)):
        result = max(result, (width[i]) * A[i])
    return result