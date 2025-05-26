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
