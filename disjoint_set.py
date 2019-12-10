"""
Disjoint set ADT
    make_set(DS, v):
    find(DS, v):
    Union(DS, x, y):
"""


def make_set(DS, v):
    node = new node with value v
    DS.add(node)
    return node

def find(DS, x):
    curr = x

    while crur.next is not null:
        curr = curr.next
    return curr

def union(DS, x, y):
    end1 = find(DS, x)
    end2 = find(DS, y)

    end1.next = end2


"""
    Union by rank
    
    rank: 
        1. the rank of a leaf is 0
        2. The rank of an internal node is one plus the maximum rank of its child
"""

def union_by_rank(DS, x, y):
    root1 = find(DS, x)
    root2 = find(DS, y)

    if root1.rank > root2.rank:
        root2.parent = root1
    elif root1.rank < root2.rank:
        root1.parent = root2
    else:
        root1.parent = root2
        root2.rank = root2.rank
