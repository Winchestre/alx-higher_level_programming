#!/usr/bin/python3
def print_reversed_list_integer(listArr=[]):
    if listArr:
        for i in range(len(listArr) - 1, -1, -1):
            print("{:d}".format(listArr[i]))
