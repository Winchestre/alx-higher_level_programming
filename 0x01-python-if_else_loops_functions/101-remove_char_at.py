#!/usr/bin/python3
def remove_char_at(str, i):
    if i >= len(str) or i < 0:
        copy_string = str
    else:
        copy_string = str[:i] + str[i + 1:]
    return copy_string
