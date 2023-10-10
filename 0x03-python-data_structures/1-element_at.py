#!/usr/bin/python3
def element_at(listArr, index):
    if index < 0 or index >= len(listArr):
        return None
    return listArr[index]
