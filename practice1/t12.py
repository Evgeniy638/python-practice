import math


def f12(x):
    if x < -23:
        return format(math.pow(x, 3) + math.pow(x, 2) - 90, '.2e')
    elif -23 <= x < 9:
        return format(abs(math.log(x) + math.pow(x, 6)/28) + math.pow(x, 4), '.2e')
    elif 9 <= x < 101:
        return format(math.pow(math.sin(x) + math.tan(x) - 12, 3)/33 - 56 * x, '.2e')
    elif x >= 101:
        return format(math.sin(math.pow(x, 3) - math.pow(x, 4)) + 77*x - 20, '.2e')


if __name__ == '__main__':
    print(f12(66))
    print(f12(11))
