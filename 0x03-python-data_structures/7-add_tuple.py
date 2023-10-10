#!/usr/bin/python3
def handle_tuple(_tuple=()):
    if len(_tuple) == 0:
        return (0, 0)
    elif len(_tuple) == 1:
        return (_tuple[0], 0)

    return (_tuple[0], _tuple[1])

def add_tuple(tuple_a=(), tuple_b=()):
    a = handle_tuple(tuple_a)
    b = handle_tuple(tuple_b)
    return (a[0] + b[0], a[1] + b[1])
