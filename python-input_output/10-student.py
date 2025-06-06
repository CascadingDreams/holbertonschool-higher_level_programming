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

    def to_json(self, attrs=None):
        """returns dictonary rep of Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attribute_name in attrs:
                if attribute_name in self.__dict__:
                    new_dict[attribute_name] = self.__dict__[attribute_name]
            return new_dict
