def maxProfit(A):
    import sys
    if len(A) < 2:
        return 0
    minPrice, maxProfit = A[0], 0
    for index in xrange(1, len(A)):
        stock_price = A[index]
        if A[index - 1] <= stock_price:
            continue
        else:
            maxProfit += A[index - 1] - minPrice
            minPrice = stock_price
    maxProfit += A[-1] - minPrice
    return maxProfit

A = [2,4,3,5,4,3]
print maxProfit(A)