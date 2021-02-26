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

# [([8], -1.4774170536831417), ([13], -2.5911989377055114), ([7], -1.2501984800722192), ([14], -6.7083015348709), ([4], -0.7408907357148689), ([10], -10.77912925042954), ([16], -0.45287914274658514), ([3], 1.1534854619908086)]


def f14(n):
    return "{:.2e}".format(t14(n))


# if __name__ == '__main__':
#     print(f14(8))
#     print(f14(13))
