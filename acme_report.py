#!/usr/bin/env python
'''
This module uses acme.py to generate random products then print a summary
'''
from acme import Product
import random

# Please note: the specs for this part of the SC appear to be best met
# using functional programming

prod_list = []
adject_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
int_rand = random.randrange(5, 101)  # use for both price and weight
flamm_rand = random.randrange(0.0, 2.51)


def generate_products(num_prods=30):
    '''
    This function generates a list of a specified number of products
    '''
    for _ in range(num_prods):
        prod_list.append([random.choice(adject_list),
                         random.choice(noun_list), int_rand, int_rand,
                         flamm_rand])
    return prod_list


def inventory_report():
    '''
    This function calculates and prints number of unique product names
    in the product list; and mean price, weight, and flammability of
    listed products
    '''
    pass


if __name__ == '__main__':
    inventory_report(generate_products())

