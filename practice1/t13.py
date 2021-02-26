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

# [([36, 40], 34466190.4151475), ([47, 15], 22592315.135527577), ([54, 70], 145911719.88595784), ([43, 37], 46909873.19145881), ([74, 56], 225854227.35636732), ([14, 40], 3529038.4947795765), ([39, 69], 71503219.60226274), ([95, 48], 325320393.2914341)]

