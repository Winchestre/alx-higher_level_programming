#!/usr/bin/python3
"""
Module print_square
"""


def print_square(size):
    """
<<<<<<< HEAD
    Prints a square with the character #.
=======
        Prints a square with the character #.
>>>>>>> a707dffc2cd8e9554d9d7ed7451b99286e0733f9
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
