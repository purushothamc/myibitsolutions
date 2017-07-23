#!/bin/env/python

sample_list = [5, 2, 6, 9, 3, 1, 8, 4, 7, 0]


def merge(a, sl1, sl2):
    ln1, ln2 = len(sl1), len(sl2)
    i, j, k = 0, 0, 0
    cnt = 0
    while i < ln1 and j < ln2:
        if sl1[i] <= sl2[j]:
            a[k] = sl1[i]
            i += 1
        else:
            a[k] = sl2[j]
            j += 1
            cnt += ln1 - i
        k += 1
    while i < ln1:
        a[k] = sl1[i]
        i += 1
        k += 1
    while j < ln2:
        a[k] = sl2[j]
        j += 1
        k += 1
    return cnt

def merge_sort(sl, n):
    if n < 2:
        return 0
    mid = n / 2
    left = sl[:mid]
    right = sl[mid:]
    cnt = 0
    cnt += merge_sort(left, mid)
    cnt += merge_sort(right, n-mid)
    cnt += merge(sl, left, right)
    return cnt


A = [7,6,2,4,1,3,5]
A = [ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60,
      47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]
cnt = merge_sort(A, len(A))
print cnt
