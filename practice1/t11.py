import math
from helper import form


def t11(x, y):
    return 18*x - math.cos(y) - 60 + abs(math.log10(x) + math.pow(x, 6)/28) + math.pow(x, 4) - math.sqrt(math.pow(y, 2)/3 - math.cos(x))


f11 = form(t11)


if __name__ == '__main__':
    print(f11(23, 27))
    print(f11(23, -84))
