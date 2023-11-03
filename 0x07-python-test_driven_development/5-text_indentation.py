#!/usr/bin/python3
"""
<<<<<<< HEAD
Module text_indentation
Adds two new lines after a set of characters.
=======
    Module text_indentation
    Adds two new lines after a set of characters.
>>>>>>> a707dffc2cd8e9554d9d7ed7451b99286e0733f9
"""


def text_indentation(text):
<<<<<<< HEAD
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.

=======
    """
        Prints text with added two newline
        after each of these characters {'.', '?', ':'}.
>>>>>>> a707dffc2cd8e9554d9d7ed7451b99286e0733f9
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
<<<<<<< HEAD
        text = (delim + "\n\n").join([line.strip(" ")
            for line in text.split(delim)])
=======
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
>>>>>>> a707dffc2cd8e9554d9d7ed7451b99286e0733f9

        print("{}".format(text), end="")
