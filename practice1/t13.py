import math


def f13(n, m):
    res_loop1 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            res_loop1 += 18*i - math.cos(j) - 60
    res_loop1 *= 84

    res_loop2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            res_loop2 += abs(i) + math.tan(j)
    res_loop2 *= 91

    return "{:.2e}".format(res_loop1 + res_loop2)

