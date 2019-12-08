"""
    hash function - takes a key and compares with its array slot which key is paired

    direct addressing - have list A and stores values into the spot
    * only work for the case, small number of items will be stored

    perfect hash functions: when there is enough slots and collision for hash key never happens
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


"""
    Closed Addressing ("Chaining")
    When collision happens, it stored into linked list.
"""


# O(N)
def serach(hash_table, key):
    hash = h(key)
    linked_list = hash_table[hash]

    for node in linked_list:
        if node.key == key:
            return node[key]

    return None


def insert(hash_table, value, key):
    hash = h(key)
    linked_list = hash_table[hash]
    for node in linked_list:
        if node.next is not None:
            continue

        linked_list.next = node(key, value)


def delete(hash_table, key):
    hash = h(key)
    linked_list = hash_table[hash]

    for node in linked_list:
        if node.key == key:
            node.prev.next = node.next
