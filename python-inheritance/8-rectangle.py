#!/usr/bin/python3

'''
Module that writes and empty class BaseGeometry
'''


class BaseGeometry:
    '''Creates BaseGeometry class'''
    def area(self):
        '''Raises exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates value
        Args:
            name: always str
            value: int
        Raises:
            TypeError: if value is not int
            ValueError: if value is less or equal to 0
        '''
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    '''
    Creates a Rectangle class.

    Attributes:
        __width: private instance attribute width
        __height: private instance attribute height
    '''
    def __init__(self, width, height):
        '''
        Initialises a new rectangle

        Args:
            width: with of the rectangle
            height: height of rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
