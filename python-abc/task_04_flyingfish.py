#!/usr/bin/env python3

'''Module for FlyingFish class'''


class Fish:
    """
    Base Fish class with swimming and habitat behaviours.
    """
    def swim(self):
        """Fish swimming behaviour."""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat description."""
        print("The fish lives in water")


class Bird:
    """
    Base Bird class with flying and habitat behaviors.
    """
    def fly(self):
        """Bird flying behaviour."""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat description."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''FlyingFish class'''
    def swim(self):
        '''FlyingFish swim behaviour'''
        print("The flying fish is swimming!")

    def fly(self):
        '''FlyingFish flying behaviour'''
        print("The flying fish is soaring!")

    def habitat(self):
        '''FlyingFish habitat description'''
        print("The flying fish lives both in water and the sky!")
