#!/usr/bin/python3

'''
Module to check if an object is an instance of,
or if an object is an instance of a class that
inherited from, the specified class
'''


def is_kind_of_class(obj, a_class):
    '''
    Determines if instance of, or instance of class inherited from
    Args:
        obj: object
        a_class: specified class

    Returns:
        True/False
    '''
    return isinstance(obj, a_class)
