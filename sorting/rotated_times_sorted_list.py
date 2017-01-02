# Problem 1
# A sorted list is rotated by an unknown number of times,
# find how many times it is rotated.

# Problem 2
# Search for an element in a circularly sorted list.

sample_list = [4,5,6,7,8,1,2,3]


def number_of_rotation(sl, start, end):
    if sl[start] <= sl[end]:
        return start
    ln = len(sl)

    while start <= end:
        mid = start + (end - start) / 2
        prev, next = sl[(mid-1)%ln], sl[(mid+1)%ln]
        if sl[mid] <= prev and sl[mid] <= next:
            return mid
        elif sl[mid] <= sl[end]:
            end = mid - 1
        elif sl[mid] >= sl[start]:
            start = mid + 1
    return -1


def binary_search_iterative(sl, start, end, to_find):
    while start <= end:
        mid = start + (end - start) / 2
        if to_find == sl[mid]:
            return mid
        elif to_find < sl[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def search_in_circular_list_v1(sl, start, end, to_find):
    min_index = number_of_rotation(sl, start, end)
    result = binary_search_iterative(sl, start, min_index-1, to_find)
    if result == -1:
        result = binary_search_iterative(sl, min_index, end, to_find)
    return result


def search_in_circular_list_v2(sl, start, end, to_find):
    while start <= end:
        mid = start + (end - start) / 2
        if to_find == sl[mid]:
            return mid
        if sl[mid] <= sl[end]:
            if sl[mid] < to_find <= sl[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if sl[start] <= to_find < sl[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1



#print number_of_rotation(sample_list, 0, len(sample_list)-1)
print search_in_circular_list_v2(sample_list, 0, len(sample_list)-1, 3)

