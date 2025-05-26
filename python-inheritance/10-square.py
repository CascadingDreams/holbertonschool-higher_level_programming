#!/usr/bin/python3

'''
Module that writes new subclass
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle, BaseGeometry):
    '''Creates a square class'''
    def __init__(self, size):
        '''
        Initialises square with size
        Args:
            size: + int for width and height
        '''
        self.integer_validator("size", size)

        super().__init__(size, size)  # calls parent rect for width and height

        self.__size = size

    def are(self):
        '''Calculates are of square'''
        return self.size * self.size
