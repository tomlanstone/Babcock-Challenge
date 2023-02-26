def list_pairs(items):
    ## Reads in a list of items and creates a list of all combinations of two items from the list
    ## Creates an empty list
    pairs = []
    for i in range(len(items)-1):
        for j in range(i+1, len(items)):
            pair = [items[i], items[j]]
            pairs.append(pair)
    return pairs
'''
def count_items(dict, pairs):
    ## Takes in a dictionary to reference and the list of pairs to count items in
    ## Iterates over the pairs, if the item is not in the dictionary it will add it, if the item is in the dictionary it will add one to its total
    for pair in pairs:
        if pair not in dict:
            dict[pair] = 0
        dict[pair] += 1
'''
def count_items(dict, pairs):
    ## Takes in a dictionary to reference and the list of pairs to count items in
    ## Iterates over the pairs, if the item is not in the dictionary it will add it, if the item is in the dictionary it will add one to its total
    for pair in pairs:
        pair_tuple = tuple(pair)  # Convert list to tuple
        if pair_tuple not in dict:
            dict[pair_tuple] = 0
        dict[pair_tuple] += 1


def count_list_combinations(words):
    ## Takes in a list of words which it will then loop over each of and count the occurrences of combinations of two letters in the same word
    ## Constructs a dictionary in which to store
    combinations = {}
    for word in words:
        pairs = list_pairs(word)
        count_items(combinations, pairs)
    return combinations

def find_unused_combos(a, b):
    c = []
    for pair in a:
        if pair not in b:
            c.append(pair)
    return c

'''
def letter_pairs(word):
    ## Reads in a word which it will then iterate over, adding all combinations of two letters to a list
    ## Creates an empty list
    pairs = []
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            pair = word[i] + word[j]
            pairs.append(pair)
    return pairs

def count_items(dict, list):
    ## Takes in a dictionary to reference and the list to count items in
    ## Iterates  over the list, if the item is not in the dictionary it will add it, if the item is in the dictionary it will add one to it's total
    for item in list:
        if item not in dict: dict[item] = 0
        if item in dict: dict[item] += 1

def count_letter_combinations(words):
    ## Takes in a list of words which it will then loop over each of and count the occurences of combinations of two letters in the same word
    ## Constructs a dictionary in which to store
    combinations = {}
    for word in words:
        pairs = letter_pairs(word)
        count_items(combinations, pairs)
    return combinations

def find_unused_combos(a,b):
    c = []
    for i in a:
        if i not in b:
            c.append((i))
    return c
'''