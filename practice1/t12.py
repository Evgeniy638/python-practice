import math
from helper import form


def t12(x):
    if x < -23:
        return math.pow(x, 3) + math.pow(x, 2) - 90
    elif -23 <= x < 9:
        return abs(math.log10(x) + math.pow(x, 6)/28) + math.pow(x, 4)
    elif 9 <= x < 101:
        return math.pow(math.sin(x) + math.tan(x) - 12, 3)/33 - 56 * x
    elif x >= 101:
        return math.sin(math.pow(x, 3) - math.pow(x, 4)) + 77*x - 20


f12 = form(t12)

if __name__ == '__main__':
    print(f12(66))
    print(f12(11))
