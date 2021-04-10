import math

# def error_assign_to_literal():
#     "language" = "English"

#
# def error_invalid_syntax():
#     try:
#         print (""
#     except BaseException as e:
#         print(e)


def error_name_is_not_defined():
    number = 1
    print(num)


def error_unsupported_operand_type():
    num = "sadasd" - 1.22


# def error_indented_block():
#     def value(one, two):
#     if one < two:
#     return two
#     else:
#     return one


def error_division_by_zero():
    return 1 / 0


def error_math_domain_error():
    return math.log(0)


def error_math_range():
    val = '9' * 200
    print(math.pow(int(val), math.e))


if __name__ == '__main__':
    print()
    # error_name_is_not_defined()
    # error_unsupported_operand_type()
    # error_division_by_zero()
    # error_math_domain_error()
    # error_math_range()






