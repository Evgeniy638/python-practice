def deriv(func):
    def g(x):
        h = 0.00001
        return (func(x + h) - func(x)) / h
    return g


if __name__ == '__main__':
    print(deriv(lambda x: x ** 3)(5))
