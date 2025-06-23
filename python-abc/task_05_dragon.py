#!/usr/bin/env python3

'''Module mixin classes'''


class SwimMixin:
    '''Creates SwimMixin class'''
    def swim(self):
        '''Swimming behaviour'''
        print("The creature swims!")


class FlyMixin:
    '''Creates Flymixin class'''
    def fly(self):
        '''Flying behaviour'''
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''Creates Dragon class'''
    def roar(self):
        print("The dragon roars!")
