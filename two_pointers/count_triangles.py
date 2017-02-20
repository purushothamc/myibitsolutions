def nTriang(lst):
    count = 0
    lst_len = len(lst)
    lst = sorted(lst)
    for outer in xrange(lst_len - 2):
        in_end = outer + 2
        for in_start in xrange(outer + 1, lst_len-1):
            while in_end < lst_len and (lst[outer] + lst[in_start] > lst[in_end]):
                in_end += 1
            count += (in_end - in_start) - 1
    return count

A = [ 4, 6, 13, 16, 20, 3, 1, 12 ]
#A = [1,1,1,2,2]
print nTriang(A)