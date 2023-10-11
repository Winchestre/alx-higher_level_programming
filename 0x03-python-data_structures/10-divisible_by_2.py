#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_mul2 = my_list[:]
    for i in range(len(is_mul2)):
        is_mul2[i] = True if is_mul2[i] % 2 == 0 else False
    return is_mul2
