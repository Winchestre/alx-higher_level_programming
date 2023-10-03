#!/usr/bin/python3
def islower(char):
    return ord(char) >= ord('a') and ord(char) <= ord('z')

def uppercase(str):
    for ch in str:
        print("{:c}".format(ord(ch) - 32 if islower(ch) else ord(ch)), end='')
    print()
