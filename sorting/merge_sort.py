#!/bin/env/python

sample_list = [5, 2, 6, 9, 3, 1, 8, 4, 7, 0]


def merge(a, sl1, sl2):
    ln1, ln2 = len(sl1), len(sl2)
    print a, sl1, sl2
    i, j, k = 0, 0, 0
    while i < ln1 and j < ln2:
        if sl1[i] <= sl2[j]:
            a[k] = sl1[i]
            i += 1
        else:
            a[k] = sl2[j]
            j += 1
        k += 1
    while i < ln1:
        a[k] = sl1[i]
        i += 1
        k += 1
    while j < ln2:
        a[k] = sl2[j]
        j += 1
        k += 1


def merge_sort(sl, n):
    if n < 2:
        return
    mid = n / 2
    left = sl[:mid]
    right = sl[mid:]
    merge_sort(left, mid)
    merge_sort(right, n-mid)
    merge(sl, left, right)


merge_sort(sample_list, len(sample_list))
print sample_list
