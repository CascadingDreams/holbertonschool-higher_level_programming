#!/usr/bin/python3

'''
Module for a rectangle:
    creates a rectangle class
'''


class Rectangle:
    '''
    Creates an empty Rectangle class.

    Attributes:
        __width: private instance attribute width
        __height: private instance attribute height
        number_of_instances: class attribute tracking number of instances
        print_symbol: prints #
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Initialises a new rectangle and increments instance counter

        Args:
            width: with of the rectangle
            height: height of rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        '''
        Rectangle.number_of_instances += 1

        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Gets the width of rectangle

        Returns:
            int: width of rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Sets the width of the rectangle

        Args:
            Value (int): width value to set

        Raises:
            TypeError: If width not int
            ValueError: if width is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not (value >= 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Gets the height of the rectangle

        Returns:
            int: height of rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets the height of the rectangle

        Args:
            Value (int): height value to set

        Raises:
            TypeError: If height not int
            ValueError: if height is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not (value >= 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
            Returns:
                current rectangle area
        '''
        area = self.__width * self.__height
        return area

    def perimeter(self):
        '''
            Returns:
                current rectangle perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        '''
        String representation of the rectangle using # characters

        Returns:
            str: Rectangle drawn with # characters
        '''
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for row in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if row < self.__height - 1:
                rectangle_str += "\n"

        return rectangle_str

    def __repr__(self):
        '''
        Developer string representation that can recreate object
        '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''
        prints "bye rectangle" when rectangle is deleted
        decrements instnace counter
        '''
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Static method that returns the biggest rectangle based on area

        Args:
            rect_1: First rectangle to compare
            rect_2: Second rectangle to compare

        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1 if equal

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
