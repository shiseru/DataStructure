'''
    balance factor: height of left subtree - height of right sub tree
    AVL invariant: balance factor is between -1 and 1
    AVL tree is a binary search tree with AVL-balanced
'''

def insert(D, key, value):
    D.height = max(D.left.height, D.right.height) + 1
    D.balance_factor = D.right.height - D.left.height

    if D.balance_factor < -1 or D.balance_factor > 1:
        fix_imbalance(D)


def fix_imbalance(D):
    if D.balance_factor == -2:
        if D.left.left.height == D.right.height + 1:
            right_rotation(D)
        else:
            left_rotation(D.left)
            right_rotation(D)
    elif D.balance_factor == 2:
        if D.right.rightheight == D.left.height + 1:
            left_rotation(D)
        else:
            right_rotation(D.right)
            left_rotation(D)


def right_rotation(D):
    y = D.root
    x = D.left.root
    A = D.left.left
    B = D.right.right
    C = D.right

    D.root = x
    D.left = A

    D.right = AVLTree(y, B, C)
