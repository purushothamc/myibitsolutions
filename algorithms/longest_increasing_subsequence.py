# given a list of integers, find a sub-sequence in which all elements
# are in sorted order
# example: [3, 4, -1, 0, 6, 2, 5, 3] and the sub-sequence is: [-1, 0, 2, 3]

# We use dynamic programming solution for this problem
# and it uses O(N) space and time, O(N^2)

def longest_increasing_subsequence(subsequence):
    ln = len(subsequence)
    if ln == 1:
        return 1 # there is only 1 element and sub-sequence length is 1.
    temp_space = [1 for i in xrange(ln)]

    i, j = 1, 0
    while i < ln:
        for j in xrange(0, i):
            if subsequence[i] > subsequence[j] and temp_space[i] < temp_space[j] + 1:
                temp_space[i] = temp_space[j] + 1
        i += 1
    return max(temp_space)

A = [3, 4, -1, 0, 6, 2, 3]
print longest_increasing_subsequence(A)