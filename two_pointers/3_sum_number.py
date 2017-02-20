def threeSumClosest(list_of_ints, number):
    import sys
    result = sys.maxint
    prev_difference = sys.maxint
    list_of_ints = sorted(list_of_ints)
    list_len = len(list_of_ints)
    if list_of_ints <= 3:
        return sum(list_of_ints)
    for outer_index in xrange(list_len):
        inner_idx_start = outer_index + 1
        inner_idx_end = list_len - 1
        while inner_idx_start < inner_idx_end:
            sum_of_ints = list_of_ints[outer_index] + \
                          list_of_ints[inner_idx_start] + \
                          list_of_ints[inner_idx_end]
            print outer_index, inner_idx_start, inner_idx_end
            if abs(sum_of_ints - number) < prev_difference:
                prev_difference = abs(sum_of_ints - number)
                result = sum_of_ints
            if sum_of_ints == number:
                result = number
                break
            elif sum_of_ints < number:
                inner_idx_start += 1
            elif sum_of_ints > number:
                inner_idx_end -= 1
    return result

A = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, \
      -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
A = [7,-6,2,10]
B = 3
print threeSumClosest(A, B)