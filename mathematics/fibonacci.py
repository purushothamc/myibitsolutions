# to compute nth fibonocci number
fib_cache = {}

def iterative_fibo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in xrange(2, n+1):
        a, b = b, a+b
    return b


def recursive_memoized_fibo(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = n if n < 2 else \
            recursive_memoized_fibo(n-1) + recursive_memoized_fibo(n-2)
        return fib_cache[n]


print iterative_fibo(5)
print recursive_memoized_fibo(5)
