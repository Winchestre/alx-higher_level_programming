#!/usr/bin/python3
def new_in_list(listArr, index, el):
    new_el = listArr[:]
    if index < 0 or index >= len(listArr):
        pass
    else:
        new_el[index] = el
    return new_el
