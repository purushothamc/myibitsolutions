def my_power_func(n, a):
    if a == 0: return 1
    y = my_power_func(n, a/2)
    if a % 2 == 0:
        return y*y
    else:
        return n*my_power_func(n, a-1)


print my_power_func(3, 6)
