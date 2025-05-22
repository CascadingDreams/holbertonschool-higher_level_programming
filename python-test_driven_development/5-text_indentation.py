#!/usr/bin/python3
"""
This module contains a function that prints text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed with indentation

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end='')

        if char in separators:
            print()
            print()

            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1
