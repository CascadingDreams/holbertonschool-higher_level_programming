#!/usr/bin/python3

'''Module for true/false instance of exact class'''


def is_same_class(obj, a_class):
    '''
    Determines if instnace is of the exact class specified

    Args:
        obj: object
        a_class: specified class

    Returns:
        True/False
    '''
    return type(obj) is a_class
