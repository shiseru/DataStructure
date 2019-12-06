"""
    Priority Queue Operations
        1. insert(PQ, x, priority): Add x to PQ with given priority
        2. find_max(PQ): Return the item with highest priority
        3. extract_max(PQ): Remove and return the item with highest priority
"""


def insert(PQ, x, priority):
    n = Node(x, priority)
    PQ.last.next = n
    n.next = None


def find_max(PQ):
    n = PQ.head()
    max_node = n

    while n is not None:
        if n.priority > max_node.priority:
            max_node = n
        n = n.next

    return max_node


def extract_max(PQ):
    extracted_node = find_max(PQ)
    extracted_node.prev = extracted_node.next

