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
        steal_quotient = self.price / self.weight
        if steal_quotient < 0.5:
            return "Not so stealable..."
        elif 0.5 <= steal_quotient < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"
        

    def explode(self):
        '''
        This method calculates product flammability times weight and
        returns a string that describes explosion
        '''
        explode_product = int(self.flammability * self.weight)
        if explode_product < 10:
            return "...fizzle."
        elif 10 <= explode_product < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    '''
    This class is for a fictional boxing glove product based on Product
    '''
    def __init__(self, weight=10):
        super(BoxingGlove, self).__init__()
        self.weight = weight

    def explode(self):
        '''
        Overrides superclass explode method
        '''
        return "...it's a glove."

    def punch(self):
        '''
        This method returns an expressive string that reflects potential
        pain-delivering ability of glove based on glove weight
        '''
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"


