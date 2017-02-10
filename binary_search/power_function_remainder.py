def pow(x, n, d):
    if x == 0:
        return 0
    if x < 0:
        x = x + d
    if n == 0:
        return 1
    elif n == 1:
        return x % d
    temp = (pow(x % d, n / 2, d)) % d
    if n % 2 == 0:
        return ((temp % d) * (temp % d) % d)
    else:
        return ((temp % d) * (temp % d) * (x % d)) % d

A = 71045970
B = 41535484
C = 64735492
print pow(A, B, C)