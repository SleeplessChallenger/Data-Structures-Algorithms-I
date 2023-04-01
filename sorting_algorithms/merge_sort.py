from math import floor, trunc


# Merge sort
def merge(a, b):
    lst = list()
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if b[j] > a[i]:
            lst.append(a[i])
            i += 1
        else:
            lst.append(b[j])
            j += 1

    while i < len(a):
        lst.append(a[i])
        i += 1

    while j < len(b):
        lst.append(b[j])
        j += 1

    return lst


def sort(arr):
    if len(arr) == 1:
        return arr
    arr1 = sort(arr[:floor(len(arr) / 2)])
    arr2 = sort(arr[trunc(len(arr) / 2):])
    return merge(arr1, arr2)


print(sort([5, 1, 89, 32, 0, 76, 12]))
