def make_perf(dict_perf):
    def func_perf(f):
        def g(*args, **kwargs):
            if f.__name__ in dict_perf:
                dict_perf[f.__name__] += 1
            else:
                dict_perf[f.__name__] = 1
            return f(*args, **kwargs)

        return g

    return func_perf


PERF = {}


@make_perf(PERF)
def fact(n):
    if n < 2:
        return 1

    return fact(n-1) * n


@make_perf(PERF)
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fact(10), fib(27))
    print(PERF)
