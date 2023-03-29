# Binary search
from math import floor


def binary_search(arr, target):
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
