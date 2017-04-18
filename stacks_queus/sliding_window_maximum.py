def slidingMaximum(A, B):
    from collections import deque
    window = deque()
    result = list()
    if not A or B <= 1:
        return A
    for i in xrange(B):
        while window and A[window[-1]] <= A[i]:
            window.pop()
        window.append(i)
    for j in xrange(i+1, len(A)):
        print window, j
        result.append(A[window[0]])
        while window and window[0] <= (j - B):
            window.popleft()
        while window and A[window[-1]] <= A[j]:
            window.pop()
        window.append(j)
    result.append(window[0])
    return result

A = [1, 3, -1, -3, 5, 3, 6, 7]
A = [10, 9, 8, 7, 6, 5, 4]
B = 2
print slidingMaximum(A, B)