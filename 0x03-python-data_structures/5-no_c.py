#!/usr/bin/python3
def no_c(string):
    string = ""
    for char in string:
        if char != 'c' and char != 'C':
            string = string + char
    return string
