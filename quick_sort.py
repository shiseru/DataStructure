# best case running time - O(nlogn). case which median is always pivot
# worst case running time - O(n^2). case which the maximum is always pivot


def quick_sort(array):
    if len(array) < 2:
        return

    else:
        pivot = array[0]
        smaller, bigger = partition(array, pivot)

        smaller = quick_sort(smaller)
        bigger = quick_sort(bigger)

        return smaller + pivot + bigger


def partition(array, pivot):
    smaller = []
    bigger = []

    for item in array:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)
    return smaller, bigger
