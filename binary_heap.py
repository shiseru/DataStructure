""""
    heap:
    - a binary satisfying the heap property and is complete.

    heap property:
    1. the value of the node is greater than or equal to all of its descendants

    complete binary tree (CBT):
    - binary tree is complete if and only if
    1. every leaf must be in one of the two bottommost levels.
    2. every leaf is af far to the left as possible.

    CBT property:
    1. with n nodes, it has log n height
"""


class BinaryHeap:
    def __init__(self, PQ):
        self.PQ = PQ

    # The root of the binary heap always has the highest priority
    # O(1)
    def find_max(self):
        return self.PQ[1]

    # O(log n)
    def extract_max(self):
        max_node = self.PQ[1]

        # replace the root with the last leaf in the heap
        self.PQ[1] = self.PQ[len(self.PQ) - 1]
        self.PQ.size -= 1

        i = 1
        while i < self.PQ.size:
            current_priority = self.PQ[i].priority
            left_priority = self.PQ[2 * i].priority
            right_priority = self.PQ[2 * i + 1].priority

            # heap property is satisfied
            if current_priority >= left_priority and current_priority >= right_priority:
                break

            elif left_priority > current_priority:
                # swap the root with left node.
                self.PQ[i], self.PQ[i * 2] = self.PQ[i * 2], self.PQ[i]
                i = i * 2

            else:
                self.PQ[i], self.PQ[i * 2 + 1] = self.PQ[i * 2 + 1], self.PQ[i]
                i = i * 2 + 1

        return max_node

