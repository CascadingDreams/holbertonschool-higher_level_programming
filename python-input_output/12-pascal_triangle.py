#!/usr/bin/python3

'''Module to build pascals triangle'''


def pascal_triangle(n):
    '''Returns a pascal triangle'''
    if n <= 0:
        return []

    triangle = []
    triangle.append([1])

    if n >= 2:
        triangle.append([1, 1])

    for i in range(2, n):
        previous_row = triangle[i-1]
        new_row = [1]

        for j in range(len(previous_row) - 1):
            new_row.append(previous_row[j] + previous_row[j + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
