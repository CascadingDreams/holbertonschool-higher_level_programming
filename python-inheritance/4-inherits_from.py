#!/usr/bin/python3

'''
Module checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
'''


def inherits_from(obj, a_class):
    '''
    Checks if object is of class that inhertited
    directly or indirectly from the specified class

     Args:
        obj: object
        a_class: specified class

    Returns:
        True/False
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
