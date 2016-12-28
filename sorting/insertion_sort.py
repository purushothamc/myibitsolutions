#!/bin/env/python

sample_list = [5, 2, 6, 9, 3, 1, 8, 4, 7, 0]


def insertion_sort(sl, ln):
    """
    In insertion sort, we run a loop over list and in each iteration, we pick
    current element and place it in its correct position in elements before it.
    example: [3, 1, 4, 5, 2]
    1st iteration: 3 picked, we can place 3 at index 0 only since there are no elements before 3.
    2nd iteration: 1 is picked, we can place 1 in 3's place ( 1 < 3 ), we swap 1, 3
    3rd iteration: 4 is picked, we can place 4 at current 4's place only since there is no less element before it.
    4th iteration: 5 is picked, same above, current state - > [1,3,4,5,2]
    5th iteration: 2 picked, we can find that 2 can be place at 3's position and all elements after 3 have to
                   move by a index 1.
    :param sl: list on which sorting has to perform
    :param ln: length of the list
    :return: n/a
    """
    for i in xrange(1, ln):
        elem = sl[i]
        j = i
        while j > 0 and (sl[j-1] > elem ):
            sl[j] = sl[j-1]
            j -= 1
        sl[j] = elem

insertion_sort(sample_list, len(sample_list))
print sample_list