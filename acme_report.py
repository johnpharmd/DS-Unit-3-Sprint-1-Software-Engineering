#!/usr/bin/env python
'''
This module uses acme.py to generate random products, then prints a summary
'''
from acme import Product
import random
from statistics import mean

# Please note: the specs for this part of the SC appear to be best met
# using functional programming

prod_list = []
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
price_list = [_ for _ in range(5, 101)]
weight_list = [_ for _ in range(5, 101)]
flamm_rand = random.uniform(0.0, 2.51)


def get_flamm_rand():
    return flamm_rand


def generate_products(num_prods=30):
    '''
    This function generates a list of a specified number of products
    '''
    product_list = []
    for _ in range(num_prods):
        gen_list = []
        gen_list = [random.choice(ADJECTIVES) + ' ' +
                    random.choice(NOUNS), random.choice(price_list),
                    random.choice(weight_list)]
        gen_list.append(get_flamm_rand())
        product_list.append(gen_list)
    return product_list


def inventory_report(product_list):
    '''
    This function calculates and prints number of unique product names
    in the product list; and mean price, weight, and flammability of
    listed products
    '''
    # product_set = set(product_list)
    # product_list = []
    mean_price = []
    mean_weight = []
    mean_flam = []

    report_text = '''
    ACME CORPORATION OFFICIAL INVENTORY REPORT
    Unique product names: {}
    Average price: {}
    Average weight: {}
    Average flammability: {}
    '''
    # print(report_text.format(len(product_list), mean_price,
    #                           mean_weight, mean_flam))
    print('product_list is:', product_list)

if __name__ == '__main__':
    inventory_report(generate_products())

