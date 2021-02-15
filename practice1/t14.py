import math
from helper import form


def t14(n):
    if n == 0:
        return 9
    elif n == 1:
        return 4
    else:
        return math.tan(t14(n-2)) - math.pow(t14(n-1), 2)/91


f14 = form(t14)

if __name__ == '__main__':
    print(f14(8))
    print(f14(13))
