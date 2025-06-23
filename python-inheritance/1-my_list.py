#!/usr/bin/python3

'''Module that creates a MyList class from list'''


class MyList(list):
    '''
    MyList class that inherits from list with print_sort method
    '''
    def print_sorted(self):
        '''
        Prints the list in asecending order
        Assumes all elements are ints
        Does not modify original list
        '''
        print(sorted(self))
