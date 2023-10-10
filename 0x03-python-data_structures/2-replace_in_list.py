#!/usr/bin/python3
def replace_in_list(listArr, index, el):
    if index < 0 or index >= len(listArr):
        return listArr
    listArr[index] = el
    return listArr
