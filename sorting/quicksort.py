#!/bin/env/python

sample_list = [5, 2, 0, 9, 3, 1, 8, 4, 7, 6]


def partition(A, start, end):
    pivot = A[end]
    p_index = start
    for i in xrange(start, end):
        if A[i] <= pivot:
            A[i], A[p_index] = A[p_index], A[i]
            p_index += 1
    A[p_index], A[end] = A[end], A[p_index]
    return p_index


def quick_sort(A, start, end):
    if start < end:
        p_idx = partition(A, start, end)
        quick_sort(A, start, p_idx-1)
        quick_sort(A, p_idx+1, end)


quick_sort(sample_list, 0, len(sample_list)-1)
print sample_list
