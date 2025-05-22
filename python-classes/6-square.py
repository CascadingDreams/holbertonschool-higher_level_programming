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
    def __init__(self, size=0, position=(0, 0)):
        '''
            Initialise a new Square

            Args:
                size: size of square
                position (tuple): The position of the square (default: (0, 0))
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square

        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): The position value to set

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''
            Returns: the current square area
        '''
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
