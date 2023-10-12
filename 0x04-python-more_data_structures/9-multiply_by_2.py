#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for d in a_dictionary:
        new_dic[d] = 2 * a_dictionary[d]
    return new_dic
