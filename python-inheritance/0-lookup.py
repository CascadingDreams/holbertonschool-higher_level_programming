#!/usr/bin/python3

'''Module returns the list of available attributes and methods'''


def lookup(obj):
    '''
    Returns the list of available attributes and methods

    Args:
        obj: object

    Returns:
        list object with attributes and methods
    '''
    print(list(dir(obj)))
