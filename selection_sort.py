#!/bin/env/python

"""---- Selection sort is an inplace sorting algorithm that sorts
#---- a list based on placing minimum element of current sub list
#---- in front of list to make total list sorted.
"""

sample_list = [5, 2, 6, 9, 3, 1, 8, 4, 7, 0]


def selection_sort(sl, ln):
    for i in xrange(ln-1):
        i_min = i
        for j in xrange(i+1, ln):
            if sl[i_min] > sl[j]:
                i_min = j
        sl[i_min], sl[i] = sl[i], sl[i_min]

selection_sort(sample_list, len(sample_list))
print sample_list
