def threeSum(list_of_ints):
    result = set()
    list_of_ints = sorted(list_of_ints)
    list_len = len(list_of_ints)
    for outer_index in xrange(list_len):
        inner_idx_start = outer_index + 1
        inner_idx_end = list_len - 1
        while inner_idx_start < inner_idx_end:
            sum_of_ints = list_of_ints[outer_index] + \
                          list_of_ints[inner_idx_start] + \
                          list_of_ints[inner_idx_end]
            if sum_of_ints == 0:
                result.add((list_of_ints[outer_index], \
                    list_of_ints[inner_idx_start], list_of_ints[inner_idx_end]))
                inner_idx_end -= 1
                inner_idx_start += 1
            elif sum_of_ints < 0:
                inner_idx_start += 1
            elif sum_of_ints > 0:
                inner_idx_end -= 1
    return list(result)

A = [-1, 0, 1, 2, -1, -4]
print threeSum(A)