#!/usr/bin/python3

'''
Module for dividing elements of a matrix
divides all elements of a matrix.
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix.

    Args:
        matrix: list of lists of ints or floats.
        div: number (int or float) Cannot equal zero.

    Returns:
        new matrix: all elements divided by div

    Raises:
        TypeError: if matrix not a list of lists of ints or floats
        TypeError: if each row of matrix not the same size
        TypeError: if div is not int or float
        ZeroDivisionError:  if div is equal to zero
    '''
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, (list)):
            raise TypeError(err_msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)
    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
