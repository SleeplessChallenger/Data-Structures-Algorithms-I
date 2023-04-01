# Binary search
from math import floor


def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        elif arr[mid] > target:
            hi = mid - 1
        else:
            return mid

    return -1


# not best variant
def binary_search_another_example(arr, target):
    left = 0
    right = len(arr) - 1
    middle = floor((left + right) / 2)  # or (left + right) // 2
    while left <= right and arr[middle] != target:
        if target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = floor((left + right) / 2)
    if arr[middle] == target:
        return middle
    return -1
