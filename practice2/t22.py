def create_num(count):
    res = 0

    for i in range(count):
        res = (res << 1) | 1

    return res


def f22(origin_num):
    settings = [
        {
            'start': 15,
            'end': 20
        },
        {
            'start': 27,
            'end': 28
        },
        {
            'start': 9,
            'end': 14
        },
        {
            'start': 21,
            'end': 26
        },
        {
            'start': 0,
            'end': 8
        },
        {
            'start': 29,
            'end': 31
        }
    ]

    res_num = 0

    for i in range(len(settings)):
        number_bit = settings[i]['end'] - settings[i]['start'] + 1
        cur_num = origin_num >> settings[i]['start']
        res_num = (res_num << number_bit) | (cur_num & create_num(number_bit))

    return hex(res_num)

