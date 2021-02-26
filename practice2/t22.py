def f22(origin_num):
    a = (origin_num & 0x000001ff) << 3
    b = (origin_num & 0x00007e00) << 9
    c = (origin_num & 0x001f8000) << 11
    d = (origin_num & 0x07e00000) >> 9
    e = (origin_num & 0x18000000) >> 3
    f = (origin_num & 0xe0000000) >> 29

    return a + b + c + d + e + f
