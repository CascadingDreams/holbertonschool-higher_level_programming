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
    def __init__(self, size=0):
        '''
            Initialise a new Square

            Args:
                size: size of square

            Raises:
                TypeError: size must be integer
                ValueError: size must be >= 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not (size >= 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
            Returns: the current square area
        '''
        return self.__size ** 2
