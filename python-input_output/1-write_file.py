#!/usr/bin/python3

'''Module to write a string to file and return num of chars'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file (UTF8) and returns the
    number of characters written.
    Args:
        filename (str): The name of the file to write to
        text (str): The text content to write to the file
    Returns:
        int: The number of characters written to the file
    '''
    with open(filename, 'w') as f:
        return f.write(text)
