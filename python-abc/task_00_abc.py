#!/usr/bin/env python3

'''Module to create abstract method'''


from abc import ABC, abstractmethod


class Animal(ABC):
    '''Creates Animal class'''
    @abstractmethod
    def sound(self) -> str:
        '''Creates abstract method sound'''
        pass


class Dog(Animal):
    '''Creates Dog class'''
    def sound(self):
        '''
        Creates dog sound method
        Returns str
        '''
        return "Bark"


class Cat(Animal):
    '''Creates Cat class'''
    def sound(self):
        '''
        Creates cat sound method
        Returns str
        '''
        return "Meow"
