import turtle

turtle.speed('fastest')
screen = turtle.Screen()

store = []
canceled_store = []


def check_store(s):
    def f(func):
        def g(*args, **kwargs):
            if len(s) > 0:
                func(*args, **kwargs)

        return g
    return f


def save_xy(func):
    global store

    def g(x, y):
        print(x, y)
        func(x, y)
        store.append({'x': x, 'y': y})
        print(canceled_store, store)

    return g


def save_canceled_xy(func):
    global store
    global canceled_store

    def g():
        if len(store) > 0:
            canceled_store.append(store.pop())
        print(canceled_store, store)
        func()

    return g


def print_by_coords(coordinates):
    for coord in coordinates:
        turtle.goto(coord['x'], coord['y'])


@save_xy
def line_func(x, y):
    turtle.goto(x, y)


@check_store(store)
@save_canceled_xy
def undo_func():
    turtle.goto(0, 0)
    turtle.clear()
    print_by_coords(store)


@check_store(canceled_store)
def redo_func():
    global canceled_store
    coord = canceled_store.pop()
    line_func(coord['x'], coord['y'])


screen.onclick(line_func)
screen.onkey(undo_func, "u")
screen.onkey(redo_func, "r")
screen.listen()
screen.mainloop()

if __name__ == '__main__':
    print('start')
