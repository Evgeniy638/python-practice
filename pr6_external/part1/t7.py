fact = (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n < 2 else f(f, n-1) * n)

if __name__ == '__main__':
    print(fact(10))
