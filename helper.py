def form(f):
    def g(*args, **kwargs):
        return format(f(*args, **kwargs), '.2e')

    return g
