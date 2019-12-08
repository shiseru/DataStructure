def build_heap(items):
    length = len(items)

    while length > 0:
        bubble_down(items, i)
        i = i - 1


def bubble_down(heap, i):
    while i < heap.size:
        current_priority = heap[i].priority
        left_priority = heap[i * 2].priority
        right_priority = heap[i * 2 + 1].priority

        if current_priority >= left_priority and current_priority >= right_priority:
            break

        elif left_priority > current_priority:
            heap[i], heap[i * 2] = heap[i * 2], heap[i]
            i = i * 2

        else:
            heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
            i = i * 2 + 1
