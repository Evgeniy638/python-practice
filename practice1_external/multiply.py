def multiply12(number):
    mul_number_2 = number + number
    mul_number_6 = mul_number_2 + mul_number_2 + mul_number_2
    return mul_number_6 + mul_number_6


def multiply16(number):
    mul_number_2 = number + number
    mul_number_4 = mul_number_2 + mul_number_2
    mul_number_8 = mul_number_4 + mul_number_4
    return mul_number_8 + mul_number_8


def multiply15(number):
    mul_number_2 = number + number
    mul_number_4 = mul_number_2 + mul_number_2
    mul_number_8 = mul_number_4 + mul_number_4
    return mul_number_8 + mul_number_8 - number


def multiply29(number):
    mul_number_2 = number + number
    mul_number_4 = mul_number_2 + mul_number_2
    mul_number_8 = mul_number_4 + mul_number_4
    mul_number_16 = mul_number_8 + mul_number_8
    mul_number_32 = mul_number_16 + mul_number_16
    return mul_number_32 - mul_number_4 + number


if __name__ == '__main__':
    print(multiply12(10))
    print(multiply15(10))
    print(multiply16(10))
    print(multiply29(10))
