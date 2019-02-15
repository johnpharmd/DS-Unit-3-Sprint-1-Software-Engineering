#!/usr/bin/env python
'''
This is an exercise in writing OOP Python code for a LSDS01 Sprint Challenge
'''
import random


class Product():
    '''
    This is a product class for fictional company Acme Corporation
    '''
    def __init__(self, name='', price=10, weight=20, flammability=0.5, identifier=random.randrange(int(1e7))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        This method calculates the quotient of product price and weight
        and returns a string regarding the 'stealability' of the product
        '''
        pass

    def explode(self):
        '''
        This method calculates product flammability times weight and
        returns a string that describes explosion
        '''
        pass


