# Range A-B
# -10000 <= A, B <= 10000
# Return all square numbers in range [A-B]

def solution(A, B):
    # negative numbers can't be square numbers.
    if A <= 0 and B <= 0:
        return 0
    if A < 0 and B > 0:
        A = 0
    if B < 0 and A > 0:
        B = 0
    # maximum positive range is 10000, so I'm using the fact of sum of odd numbers is square to solve this
    start = 1
    sqSum = 1
    step = 2
    result = []
    while sqSum <= 10000:
        if A <= sqSum <= B:
            result.append(sqSum)
        start += step
        sqSum += start
    print result

solution(4, 17)