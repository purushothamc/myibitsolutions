def longest_increaing_subsequence_helper(A):
    if not A:
        return 0
    temp1 = [1 for i in xrange(len(A))]
    temp2 = [1 for i in xrange(len(A))]
    result = 1
    for i in range(1, len(A)):
        j = 0
        while j < i:
            if A[j] < A[i] and temp1[i] < temp1[j] + 1:
                temp1[i] = temp1[j] + 1
            j += 1

    A = A[::-1]
    result = 1
    for i in range(1, len(A)):
        j = 0
        while j < i:
            if A[j] < A[i] and temp2[j] + 1 > temp2[i]:
                temp2[i] = temp2[j] + 1
            j += 1
    temp2 = temp2[::-1]
    print temp1
    print temp2
    result = 1
    for i in range(len(A)):
        result = max(result, temp1[i] + temp2[i])
    return result - 1

def longestSubsequenceLength(A):
    result = longest_increaing_subsequence_helper(A)
    return result

A = [15, 27, 14, 38, 26, 55, 46, 65, 85]
A = [1, 11, 2, 10, 4, 5, 2, 1]
A = [7, 6, 8, 10, 2, 5, 12, 30, 31, 20, 22, 18]
#A = [7, 6, 8, 2, 3, 4]
longestSubsequenceLength(A)
#print longestSubsequenceLength(A[::-1])