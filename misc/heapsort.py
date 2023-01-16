"""By-hand heap sort implementation"""
import random


def heapSort(arr):
    # Build max heap
    start = end = len(arr) - 1
    while start >= 0:
        heapify(arr, start, end)
        start -= 1

    # Pick out elements 1 by 1:
    while end >= 0:
        arr[0], arr[end] = arr[end], arr[0]
        end -= 1

        # Re-heapify
        heapify(arr, 0, end)

    return arr


def heapify(arr, start, end):
    largest, l, r = start, 2 * start + 1, 2 * start + 2
    if l <= end and arr[largest] < arr[l]:
        largest = l

    if r <= end and arr[largest] < arr[r]:
        largest = r

    if largest != start:
        arr[largest], arr[start] = arr[start], arr[largest]
        heapify(arr, largest, end)


if __name__ == "__main__":
    arr = [random.randrange(1, 100, 1) for i in range(10)]

    print("arr is: ", arr)
    print("sorting...")
    heapSort(arr)
    print("arr is: ", arr)
