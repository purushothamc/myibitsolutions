#!/bin/env/python

"""
In Bubble sort, adjacent pairs are compared and ordered.
A loop runs through all nC2 pairs and perform comparisons to order them.
"""

sample_list = [5, 2, 6, 9, 3, 1, 8, 4, 7, 0]


def bubble_sort(sl, ln):
    n = ln + 1
    for iPass in xrange(1, n): # number of passes
        flag = True # To not pass over redundant passes.
        for j in xrange(n-iPass-1): # to bubble elements only in unsorted sublist
            if sl[j] > sl[j+1]:
                sl[j], sl[j+1] = sl[j+1], sl[j]
                flag = False
        if flag:
            break

bubble_sort(sample_list, len(sample_list))
print sample_list
