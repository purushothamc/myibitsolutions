def fourSum(A, B):
    # 2 - pointer approach
    if len(A) <= 3:
        return [[]]
    result = list()
    A = sorted(A)
    print A
    for first in xrange(len(A) - 3):
        for second in xrange(first + 1, len(A) - 2):
            start, end = second + 1, len(A) - 1
            while start < end:
                leftSum = A[first] + A[second]
                rigtSum = A[start] + A[end]
                if leftSum + rigtSum == B:
                    if [A[first], A[second], A[start], A[end]] not in result:
                        result.append([A[first], A[second], A[start], A[end]])
                    start += 1
                    end -= 1
                if leftSum + rigtSum < B:
                    start += 1
                if leftSum + rigtSum > B:
                    end -= 1
    return result

A, B = [-2, -1, 0, 0, 1, 2], 0
A, B = [-13, 11, 30, 12, 20, 21, -13, 6, -4, 7, 5, -2, 19, -10, 4, 8, 1], 79
print fourSum(A, B)


"""
pair_sum_indices = dict()
result = list()
for outer in xrange(len(A) - 1):
    curSum = 0
    for inner in xrange(outer+1, len(A)):
        curSum = A[outer] + A[inner]
        if pair_sum_indices.has_key(curSum):
            pair_sum_indices[curSum].append([outer, inner])
        else:
            pair_sum_indices[curSum] = [[outer, inner]]
for pair_sum in pair_sum_indices:
    if (B - pair_sum) in pair_sum_indices:
        print pair_sum_indices[pair_sum], pair_sum, B - pair_sum
        for value in pair_sum_indices[B - pair_sum]:
            pass
            #if pair_sum_indices[pair_sum][0] < value[0]:
            #    result.append([pair_sum_indices[pair_sum[0]], pair_sum_indices[pair_sum[1]], value[0], value[1]])
print result
"""