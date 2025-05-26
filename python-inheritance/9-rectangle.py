#!/usr/bin/python3

'''
Module that writes new subclass
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
            width: width of the rectangle
            height: height of rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
        Returns:
            current rectangle area
        '''
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Return string representation of Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
