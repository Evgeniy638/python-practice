import random
import random_bot
import main


def wall_walk(check, x, y):
    if (check('wall', x - 1, y) or check('wall', x - 1, y - 1)) and not check('wall', x, y - 1):
        return 'up'

    if (check('wall', x + 1, y) or check('wall', x + 1, y + 1)) and not check('wall', x, y + 1):
        return 'down'

    if (check('wall', x, y + 1) or check('wall', x - 1, y + 1)) and not check('wall', x - 1, y):
        return 'left'

    if (check('wall', x, y - 1) or check('wall', x + 1, y - 1)) and not check('wall', x + 1, y):
        return 'right'


def script(check, x, y):
    if check('gold', x, y):
        return 'take'

    if check("level") == 1:
        if not check('wall', x + 2, y):
            return 'right'

        return 'down'

    elif check("level") == 2:
        if check('gold', x, y+1):
            return 'down'

        if check('gold', x, y-1):
            return 'up'

        if check('gold', x+1, y):
            return 'right'

        if check('wall', x+2, y):
            return 'up'

        return 'right'

    elif check("level") == 3:
        return wall_walk(check, x, y)

    elif check("level") == 4:
        if x == 4 and y == 14:
            return 'right'

        if x == 5 and y == 13:
            return 'up'

        if x == 5 and y == 12:
            return 'up'

        return wall_walk(check, x, y)

    return "pass"
