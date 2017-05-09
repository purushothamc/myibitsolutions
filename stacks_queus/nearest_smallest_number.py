def prevSmaller(self, arr):
    stk = list()
    res = list()
    for num in arr:
        if not stk:
            res.append(-1)
        else:
            while stk and stk[-1] >= num:
                stk.pop()
            if not stk:
                res.append(-1)
            else:
                res.append(stk[-1])
        stk.append(num)
    return res