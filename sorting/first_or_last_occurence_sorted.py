# Problem 1:
# find first or last occurrence of a given number in a sorted
# list of numbers which might contain duplicates.

# Problem 2
# A variation of above problem.
# We've to count the number of duplicates of given number in
# sorted array of integers.
# If we can find first and last occurrence of given input number,
# we can subtract the indices and to find the required number.

sample_list = [1,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,7,8,9]


def find_first_occurrence(sl, start, end, to_find):
    result = -1
    while start <= end:
        mid = start + (end - start) / 2
        if to_find == sl[mid]:
            result = mid
            end = mid - 1
        elif to_find < sl[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


def find_last_occurrence(sl, start, end, to_find):
    result = -1
    while start <= end:
        mid = start + (end - start) / 2
        if to_find == sl[mid]:
            result = mid
            start = mid + 1
        elif to_find < sl[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


def find_first_or_last_occurrence(sl, start, end, to_find, search_first):
    result = -1
    while start <= end:
        mid = start + (end - start) / 2
        if to_find == sl[mid]:
            result = mid
            if search_first:
                end = mid -1
            else:
                start = mid + 1
        elif to_find < sl[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


def count_number_of_duplicates(sl, start, end, to_find):
    first = find_first_or_last_occurrence(sl, start, end, to_find, True)
    last = find_first_or_last_occurrence(sl, start, end, to_find, False)
    num_duplicates = -1
    if (first != -1) and (last != -1):
        num_duplicates = last - first + 1
    return num_duplicates



#print find_first_occurrence(sample_list, 0, len(sample_list)-1, 4)
#print find_last_occurrence(sample_list, 0, len(sample_list)-1, 3)
print count_number_of_duplicates(sample_list, 0, len(sample_list)-1, 8  )