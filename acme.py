#!/usr/bin/env python
import random


class Product():
    def __init__(self, name='', price=10, weight=20, flammability=0.5, identifier=random.randrange(int(1e7), int(1e8))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
