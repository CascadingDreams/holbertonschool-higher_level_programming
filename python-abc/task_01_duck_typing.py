#!/usr/bin/env python3

'''Module for creating Shape class'''


from abc import ABC, abstractmethod
import math


class Shape:
    '''Creates shape class'''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    '''Creates circle class'''    
    def __init__(self, radius):
        '''
        Initialises circle
        Args:
            radius
        '''
        self.radius = radius

    def area(self):
        '''Returns area of circle'''
        return math.pi * self.radius ** 2

    def perimeter(self):
        '''Returns perimeter of circle'''
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    '''Creates rectangle class'''
    def __init__(self, width, height):
        '''
        Initialises rectangle
        Args:
            width
            height
        '''
        self.width = width
        self.height = height

    def area(self):
        '''Returns area of rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Returns perimeter of rectangle'''
        return 2 * (self.width + self.height)

def shape_info(shape):
    '''
    Prints area and perimeter of shapes
    Args:
        Shape passed through
    '''
    print(f"{shape.area}")
    print(f"{shape.perimeter}")
