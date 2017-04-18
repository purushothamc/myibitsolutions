def prevSmaller(arr):
    stk = list()
    res = list()
    for num in arr:
        if not stk:
            res.append(-1)
        else:
            print stk, num
            while stk and stk[-1] > num:
                stk.pop()
            print stk, num
            if not stk:
                res.append(-1)
            else:
                res.append(stk[-1])
        stk.append(num)
    return res

A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
B = 1 #-1 34 -1 27 -1 5 28 5 20
print prevSmaller(A)

