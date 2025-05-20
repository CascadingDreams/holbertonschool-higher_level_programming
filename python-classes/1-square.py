#!/usr/bin/python3

'''
Module initialise square size.
defines a square by private instance attribute size
'''


class Square:
    '''
    class Square that defines a square.

    Attributes:
        __size: private value of square size

    '''
    def __init__(self, size):
        '''
            Initialise a new Square.

            Args:
                size: size of square
        '''
        self.__size = size
