def longestConsecutive(A):
    import sys
    if not A:
        return 0
    mapper = dict()
    for each in A:
        mapper[each] = 1

    max_count, prev_max_value, count = -1*sys.maxint, -1*sys.maxint, 0
    for each_value in mapper:
        current_val = each_value
        while mapper.has_key(current_val - 1):
            if mapper[current_val - 1] > 1:
                mapper[each_value] += mapper[current_val - 1]
                break
            else:
                mapper[each_value] += 1
                current_val -= 1
        print mapper
        max_count = max(max_count, mapper[each_value])
    print mapper

    #print max_count


A = [4,3,2,1]
#A = [100, 4, 200, 1, 3, 2, 5]
"""A = [ 19, 109, 52, 4, 16, 11, 87, 112, 70, 105, -4, 68, 48, 101, 47, 119, 7, 25, 42, 33, 34,
          2, 30, 37, -5, 75, 82, 59, 114, 73, 91, 57, 1, 103, 92, 26, 81, 38, 17, 83, -1, 46,
          118, 27, 89, 13, 117, 20, -2, 23, 54, 88, 111, 29, 53, 69, 84, 22, 15, 58, 85, 79,
          35, 96, 45, 9, 74, 12, 80, 108 ]
"""
longestConsecutive(A)