import math


def form(f):
    def g(*args, **kwargs):
        return format(f(*args, **kwargs), '.2e')

    return g


def t14(n):
    if n == 0:
        return 9
    elif n == 1:
        return 4
    else:
        return math.tan(t14(n-2)) - math.pow(t14(n-1), 2)/91


def f14(n):
    return "{:.2e}".format(t14(n))


# if __name__ == '__main__':
#     print(f14(8))
#     print(f14(13))
