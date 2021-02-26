def delete_empty_column(table):
    res_table = table

    for i in range(len(res_table)):
        for j in range(len(res_table[i]) - 1, -1, -1):
            if res_table[i][j] == "":
                del res_table[i][j]

    return res_table


def delete_copy_row(table):
    res_table = table

    for i in range(len(res_table) - 1, -1, -1):
        for j in range(i-1, -1, -1):
            if res_table[i] == res_table[j]:
                del res_table[i]
                break

    return res_table


def transform(table):
    for i in range(len(table)):
        table[i][0] = 1 if table[i][0] == "Да" else 0

        table[i][1] = table[i][1].split("/")[2]

        table[i][2] = table[i][2].split("[at]")[0]

        table[i][3] = table[i][3].replace("+7", "").replace(" ", "").replace("-", "")

    return table


def sort(table):
    return sorted(table, key=lambda row: row[2])


def transpose(table):
    res_table = list(range(len(table[0])))

    for i in range(len(res_table)):
        res_table[i] = list(range(len(table)))

    for i in range(len(table)):
        for j in range(len(table[i])):
            res_table[j][i] = table[i][j]

    return res_table


def f23(*args):
    res_table = delete_empty_column(list(args))
    res_table = delete_copy_row(res_table)
    res_table = transform(res_table)
    res_table = sort(res_table)
    res_table = transpose(res_table)

    return tuple(res_table)
