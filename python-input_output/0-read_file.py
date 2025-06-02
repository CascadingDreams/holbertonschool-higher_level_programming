#!/usr/bin/python3

'''Module to read a file and print to stdout'''


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): The name of the file to read
    """
    with open(filename, 'r') as file:
        print(file.read(), end='')
