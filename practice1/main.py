
def f11(x, y):
    return 18*x - math.cos(y) - 60 + abs(math.log(x) + x ** 6/28) + x ** 4 - math.sqrt(y ** 2/3 - math.cos(x))


def f12(x):
    if x < -23:
        return x ** 3 + x ** 2 - 90
    elif -23 <= x < 9:
        return abs(math.log(x) + x ** 6/28) + x ** 4
    elif 9 <= x < 101:
        return (math.sin(x) + math.tan(x) - 12) ** 3/33 - 56 * x
    elif x >= 101:
        return x ** 3 - x ** 4 + 77*x - 20


def f13(n, m):
    res_loop1 = 0
    res_loop2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            res_loop1 += 18*i - math.cos(j) - 60
            res_loop2 += abs(i) + math.tan(j)

    return 84*res_loop1 + 91*res_loop2


def f14(n):
    if n == 0:
        return 9
    elif n == 1:
        return 4
    else:
        return math.tan(f14(n-2)) - f14(n-1) ** 2/91
