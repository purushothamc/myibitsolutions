def swapPermutation(left, right, result, A, mapper):
    if left == right:
        temp = [y for y in A]
        if not mapper.has_key(tuple(temp)):
            result.append(temp)
        mapper[tuple(temp)] = True

        return

    for index in xrange(left, right+1):
        A[left], A[index] = A[index], A[left]
        swapPermutation(left+1, right, result, A, mapper)
        A[left], A[index] = A[index], A[left]

def permutations(A):
    if not A:
        return []
    result, temp, _mapper = [], [], {}
    swapPermutation(0, len(A)-1, result, A, _mapper)
    return result

A = [ 0, 0, 1, 9 ]
A = [1,2,3]
print permutations(A)