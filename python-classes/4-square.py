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
        self.size = size

    @property
    def size(self):
        '''
        Get the size of square

        Returns:
            int: size of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Set the size of the square

        Args:
            value (int): size value to set

        Raises:
            TypeError: If size not int
            ValueError: if size is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if not (value >= 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
            Returns: the current square area
        '''
        return self.__size ** 2
