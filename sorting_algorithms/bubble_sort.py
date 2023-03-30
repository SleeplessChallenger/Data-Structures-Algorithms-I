# Bubble sort
def bubble_sort(arr):
    i = len(arr) - 1
    j = 0
    while i > 0:
        while i > j:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            else:
                j += 1
        j = 0
        i -= 1
    return arr


print(bubble_sort([2, 14, 6, 23, 1, 10]))


def bubble_optimized(arr):
    i = len(arr) - 1
    j = 0
    while i > 0:
        no_swap = True
        while j < i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
                no_swap = False
            else:
                j += 1
        if no_swap:
            return arr
        i -= 1
        j = 0
    return arr


print(bubble_sort([5, 1, 76, 2, 43, 23, 84, 4, 0, 59, 12]))


# reverse bubble
def bubble2(arr):
    i = 0
    j = len(arr) - 1
    no_swap = True
    while i < len(arr):
        while j > i:
            if arr[j] > arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
                no_swap = False
            else:
                j -= 1
                no_swap = True
        if no_swap:
            return arr
        i += 1
        j = len(arr) - i

    return arr
