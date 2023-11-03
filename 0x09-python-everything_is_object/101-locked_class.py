#!/usr/bin/python3
''' Locked class module'''


class LockedClass:
    '''Object that prevents dynamic attributes'''

    __slots__ = ['first_name']
