#!/usr/bin/python3

'''Module to write class '''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        '''
        Initialise student with:
            first name
            last name
            age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictonary rep of Student instance"""
        return self.__dict__
