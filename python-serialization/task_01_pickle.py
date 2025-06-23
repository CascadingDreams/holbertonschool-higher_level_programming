#!/usr/bin/python3

'''custom object serialisation with pickle'''


import pickle


class CustomObject:
    '''Custom object class'''
    def __init__(self, name, age, is_student):
        '''initialises custome object'''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''prints object attributes'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''
        Uses pickle method to serialise current
        instance and save to filename
        '''
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        '''Uses pickle to load and return instnace of custom object'''
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
