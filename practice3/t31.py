import struct
        

def get_list_links_list_items(length, link_list, size_link, original_binary, format_unpack):
    list_links = []
    
    for i in range(length):
        [item_link] = struct.unpack(format_unpack, original_binary[link_list + i * size_link: link_list + (i + 1) * size_link])
        list_links.append(item_link)

    return list_links


def unpuck_string(length, binary, link_str):
    return struct.unpack('<' + str(length) + 's', binary[link_str: link_str + length])[0].decode('ascii')


def struct_a(offset, binary):
    length = struct.unpack('< H', binary[offset: offset + 2])[0]
    link_list = struct.unpack('< H', binary[offset + 2: offset + 4])[0]
    list_links = get_list_links_list_items(length, link_list, 4, binary, '< L')
    a1 = []
    for i in range(length):
        a1.append(struct_b(list_links[i], binary))
    offset += 4

    [a2] = struct.unpack('< b', binary[offset: offset + 1])
    offset += 1

    [a3] = struct.unpack('< B', binary[offset: offset + 1])
    offset += 1

    res_c = struct_c(offset, binary)
    a4 = res_c['structC']
    offset = res_c['offset']

    [a5] = struct.unpack('< f', binary[offset: offset + 4])

    return {
        'A1': a1,
        'A2': a2,
        'A3': a3,
        'A4': a4,
        'A5': a5
    }


def struct_b(offset, binary):
    [b1] = struct.unpack('< H', binary[offset: offset + 2])

    length = struct.unpack('< L', binary[offset + 2: offset + 6])[0]
    link_str = struct.unpack('< H', binary[offset + 6: offset + 8])[0]
    b2 = unpuck_string(length, binary, link_str)
    return {
        'B1': b1,
        'B2': b2,
    }


def struct_c(offset, binary):
    length_c1 = struct.unpack('< H', binary[offset: offset + 2])[0]
    link_arr_c1 = struct.unpack('< H', binary[offset + 2: offset + 4])[0]
    c1 = list(struct.unpack('<' + (length_c1 * 'B'), binary[link_arr_c1: link_arr_c1 + 1 * length_c1]))
    offset += 4

    [c2] = struct.unpack('< B', binary[offset: offset + 1])
    offset += 1

    [link_c3] = struct.unpack('< I', binary[offset: offset + 4])
    c3 = struct_d(link_c3, binary)
    offset += 4

    [c4] = struct.unpack('< f', binary[offset: offset + 4])
    offset += 4

    length_c5 = struct.unpack('< H', binary[offset: offset + 2])[0]
    link_arr_c5 = struct.unpack('< H', binary[offset + 2: offset + 4])[0]
    c5 = list(struct.unpack('<' + (length_c5 * 'f'), binary[link_arr_c5: link_arr_c5 + 4 * length_c5]))
    offset += 4

    [c6] = struct.unpack('< h', binary[offset: offset + 2])
    offset += 2

    return {
        'structC': {
            'C1': c1,
            'C2': c2,
            'C3': c3,
            'C4': c4,
            'C5': c5,
            'C6': c6
        },
        'offset': offset
    }


def struct_d(offset, binary):
    d1 = list(struct.unpack('< BBB', binary[offset: offset + 1 * 3]))
    offset += 3

    [d2] = struct.unpack('< h', binary[offset: offset + 2])
    offset += 2

    [d3] = struct.unpack('< Q', binary[offset: offset + 8])

    return {
        'D1': d1,
        'D2': d2,
        'D3': d3
    }


def f31(binary):
    begin_offset = 3
    return struct_a(begin_offset, binary)
