#!/usr/bin/python3

'''
Module to print a square
prints a square with the character #
'''


def print_square(size):
    '''
    Prints a square with the character #

    Args:
        size: the number of rows and columns in the square (x * x)

    Returns:
        A square of # with size * size

    Raises:

    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
