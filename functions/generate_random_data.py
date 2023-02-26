'''
This code will generate a list of items where the items are represented by lists of their component parts
'''
#import string
import random

def generate_components():
    ## Generates 325 unique names
    ## Can be extended with additional for loops to increase exponentially
    letters = "abcdefghijklmnopqrstuvwxyz" #string.ascii_lowercase
    components = []
    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            component = letters[i] + letters[j]
            components.append(component)
    return components

def generate_items(components, n_item, n_comp):
    ## components are the component names that will be combined to make the items
    ## n_item is the number of items you want to create
    ## n_comp is how many components go into an item

    items = []
    for i in range(0,n_item):
        item = random.sample(components, n_comp)
        if item in items:
            print(item)
        if item not in items:
            items.append(item)
    return items

def generate_random_data(n_item,n_comp):
    components = generate_components()
    items = generate_items(components,n_item,n_comp)
    return items
