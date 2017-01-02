# pre requisite -- list should be sorted.


sample_list = [1,2,3,4,5,6,7,8,9]


def binary_search_recursive(sl, start, end, to_find):
    if start > end:
        return -1
    mid = start + ((end - start) / 2)
    if to_find == sl[mid]:
        return mid
    elif to_find < sl[mid]:
        return binary_search_recursive(sl, start, mid-1, to_find)
    else:
        return binary_search_recursive(sl, mid+1, end, to_find)


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


print binary_search_recursive(sample_list, 0, len(sample_list)-1, 9)
print binary_search_iterative(sample_list, 0, len(sample_list)-1, 9)