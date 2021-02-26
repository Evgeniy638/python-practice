import math


def f11(x, y):
    res = 18*x - math.cos(y) - 60 + abs(math.log(x) + math.pow(x, 6)/28) + math.pow(x, 4) - math.sqrt(math.pow(y, 2)/3 - math.cos(x))
    return "{:.2e}".format(res)

