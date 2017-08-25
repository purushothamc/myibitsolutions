def maxProfit(A):
    import sys
    if len(A) < 2:
        return 0
    minPrice, maxProfit = sys.maxint, 0
    for stock_price in A:
        if stock_price < minPrice:
            minPrice = stock_price
        elif maxProfit < stock_price - minPrice:
            maxProfit = stock_price - minPrice
    return maxProfit

A = [2,4,3,5,4,3]
print maxProfit(A)