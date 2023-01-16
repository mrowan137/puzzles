from random import shuffle

# Insertsort
def insert_sort(arr):
    # O(N Log(N))
    for i in range(1, len(arr)):
        # Scoot val[i] back to correct location
        # j points to object to be copied;
        # after exit, j points to something we do not copy,
        # and j+1 was already copied, so overwrite j+1
        j, val = i - 1, arr[i]
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1

        # Put original arr[i] to the right place
        arr[j + 1] = val


# Mergesort
def merge(a, b):
    # Input is two sorted arrays a and b
    res = []
    while a and b:
        if a[0] < b[0]:
            res.append(a.pop(0))
        elif a[0] > b[0]:
            res.append(b.pop(0))
        else:
            res.append(a.pop(0))
            res.append(b.pop(0))

    if a:
        res += a
    elif b:
        res += b

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)


# Quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = low  # points to potential swap element
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Put pivot in the right place
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):
    if low >= high:
        return
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    x = [_ for _ in range(20)]

    # Insert sort
    shuffle(x)
    print("{:10}: {}\n".format("x", x))
    insert_sort(x)  # in-place
    print("{:10}: {}\n".format("Insert sort", x))

    # Merge sort
    shuffle(x)
    print("{:10}: {}\n".format("x", x))
    print("{:10}: {}\n".format("Merge sort", merge_sort(x)))

    # Quick sort
    shuffle(x)
    print("{:10}: {}\n".format("x", x))
    insert_sort(x)  # in-place
    print("{:10}: {}\n".format("Quick sort", x))
