"""
    hash function - takes a key and compares with its array slot which key is paired

    direct addressing - have list A and stores values into the spot
    * only work for the case, small number of items will be stored
"""


def search(hash_table, key):
    hash = h(key)
    return hash_table[hash]


def insert(hash_table, key, value):
    hash = h(key)
    hash_table[hash] = value


def delete(hash_table, key):
    hash = h(key)
    hash_table[hash] = None
